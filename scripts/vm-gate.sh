#!/usr/bin/env bash
# Гейт базы в виртуальной машине (Tart, ВМ maerp-vm): окна 1С на экране владельца не открываются (решение владельца
# 2026-11-25 - прогоны с окнами только в ВМ). Выгрузка EDT - на хосте (EDT в ВМ нет); проект копируется в ЛОКАЛЬНУЮ
# папку ВМ (rsync по ssh) и исполняется там: загрузка в базу, CheckConfig, смок, тесты документов и интерфейса.
# Журналы, отчёты и штамп возвращаются в build/ хоста - их видят хук коммита и отправка в хаб.
#
# Общую папку Tart (virtiofs) для кода не используем: ВМ видела правку хоста с опозданием и однажды исполнила скрипт,
# прочитанный наполовину (2026-11-25).
#
# Использование: scripts/vm-gate.sh            гейт целиком
#                scripts/vm-gate.sh -- <cmd>    любая команда в корне проекта ВМ в окружении 1С (прогоны под ролями:
#                                               scripts/vm-gate.sh -- bash scripts/roles-run.sh <журнал> "<наборы>")
# Подготовка ВМ (один раз): docs/TESTING.md, раздел «Прогоны в ВМ».
set -u
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
set +e
VM="${MAERP_VM:-maerp-vm}"
VM_ROOT="${MAERP_VM_ROOT:-/Users/admin/maerp}"
# Команды в ВМ - по ssh: в образе Cirrus входу по ssh выданы разрешения macOS (управление System Events, нажатия
# клавиш) - сторож диалога лицензии под ролью без них не работает; агенту tart exec они не выданы.
SSH_KEY="${MAERP_VM_KEY:-$HOME/.ssh/maerp_vm_ed25519}"
SSH_OPTS=(-i "$SSH_KEY" -o BatchMode=yes -o StrictHostKeyChecking=accept-new -o UserKnownHostsFile="$BUILD/vm/known_hosts")
command -v tart >/dev/null || { echo "Нет tart (ВМ не подготовлена)" >&2; exit 1; }
[ -n "${SMOKE_USER:-}" ] && [ -n "${SMOKE_PWD:-}" ] || { echo "SMOKE_USER/SMOKE_PWD не заданы" >&2; exit 1; }
mkdir -p "$BUILD/vm"

if ! tart exec "$VM" true 2>/dev/null; then
	echo "== Запуск ВМ $VM без окна =="
	(nohup tart run "$VM" --no-graphics > "$BUILD/vm/tart-run.log" 2>&1 &)
	for i in $(seq 1 60); do tart exec "$VM" true 2>/dev/null && break; sleep 5; done
	tart exec "$VM" true 2>/dev/null || { echo "ВМ не отвечает - $BUILD/vm/tart-run.log" >&2; exit 1; }
fi
HOST="admin@$(tart ip "$VM")"
vmssh() { ssh "${SSH_OPTS[@]}" "$HOST" "$(printf '%q ' "$@")"; }
RSYNC_SSH="ssh $(printf '%q ' "${SSH_OPTS[@]}")"
to_vm() { rsync -a --delete -e "$RSYNC_SSH" "$@"; }

# Проект (с .git - отпечаток дерева src/cf считает git) без build/; из build/ - только нужное прогону.
vmssh mkdir -p "$VM_ROOT/build/gate" "$VM_ROOT/build/vm" "$VM_ROOT/build/uitest"
to_vm --exclude=/build/ "$ROOT/" "$HOST:$VM_ROOT/" || { echo "Копирование проекта в ВМ не прошло" >&2; exit 1; }
to_vm "$BUILD/uitest/" "$HOST:$VM_ROOT/build/uitest/"
[ -f "$BUILD/gate/role-users.env" ] && to_vm "$BUILD/gate/role-users.env" "$HOST:$VM_ROOT/build/gate/"
[ -f "$BUILD/gate-stamps.txt" ] && to_vm "$BUILD/gate-stamps.txt" "$HOST:$VM_ROOT/build/"
# Пароли - файлом с правами 600, не в командной строке ВМ.
( umask 077; printf 'SMOKE_USER=%q\nSMOKE_PWD=%q\n' "$SMOKE_USER" "$SMOKE_PWD" > "$BUILD/vm/secrets.env" )
to_vm "$BUILD/vm/secrets.env" "$HOST:$VM_ROOT/build/vm/"

# Результаты прогона - обратно на хост: журналы гейта, отчёты интерфейса, штампы.
from_vm() {
	rsync -a -e "$RSYNC_SSH" "$HOST:$VM_ROOT/build/gate/" "$BUILD/gate/" --exclude=role-users.env
	rsync -a -e "$RSYNC_SSH" "$HOST:$VM_ROOT/build/vm/" "$BUILD/vm/" --exclude=secrets.env
	for f in uitest-report.txt doctests-report.txt smoke-report.txt gate-stamps.txt; do
		rsync -a -e "$RSYNC_SSH" "$HOST:$VM_ROOT/build/$f" "$BUILD/$f" 2>/dev/null
	done
}

if [ "${1:-}" = "--" ]; then
	shift
	vmssh /bin/bash "$VM_ROOT/scripts/vm-run.sh" "$VM_ROOT/build/vm/cmd.log" "$@"
	RC=$?
	from_vm
	cat "$BUILD/vm/cmd.log"
	exit $RC
fi

echo "== Выгрузка EDT на хосте =="
for attempt in 1 2; do
	bash "$ROOT/scripts/edt-export.sh" > "$BUILD/vm/export-$attempt.log" 2>&1 && EXPORT_OK=1 && break
done
[ "${EXPORT_OK:-}" = 1 ] || { echo "Выгрузка EDT не прошла - $BUILD/vm/export-2.log" >&2; exit 1; }
"$ROOT/scripts/srchash.sh" > "$XML_OUT/.srchash"
bash "$ROOT/scripts/xmlsum.sh" > "$XML_OUT/.xmlsum"
to_vm "$XML_OUT/" "$HOST:$VM_ROOT/build/xml/" || { echo "Копирование выгрузки в ВМ не прошло" >&2; exit 1; }

echo "== Гейт в ВМ (база $VM_ROOT/build/ib-gate) =="
vmssh /bin/bash "$VM_ROOT/scripts/vm-run.sh" "$VM_ROOT/build/vm/gate.log" env IB_SYNC_XML_READY=1 bash "$VM_ROOT/scripts/gate.sh"
RC=$?
from_vm
grep -h "^==\|^ИТОГ\|^ПРОВАЛ" "$BUILD/vm/gate.log" | tail -15
tail -1 "$BUILD/gate-stamps.txt"
exit $RC
