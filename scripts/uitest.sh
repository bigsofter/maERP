#!/usr/bin/env bash
# Тесты интерфейса (уровень 4): обход форм на клиенте через тест-клиент, под администратором и под ролями.
# Использование: scripts/uitest.sh [каталог-базы]        (по умолчанию build/ib-gate)
#                UITEST_ROLES="Администратор Кладовщик" scripts/uitest.sh    часть ролей (отладка, без порога)
#                UITEST_FORMS=<файл> - свой список форм вместо tests/ui/forms.txt (отладка)
#
# Тест-менеджер (администратор, /TESTMANAGER) выполняет tests/ui/core.bsl внешней обработкой и управляет
# тест-клиентом (/TESTCLIENT), запущенным под пользователем роли. Роли не нужны права ни на тесты, ни на
# внешние обработки - в поставку конфигурации ничего не добавляется. Пользователей «Тест <Роль>» заводит
# tests/ui/role-users.bsl, пароль - build/gate/role-users.env (в git не попадает).
# Формы - tests/ui/forms.txt; под ролью обходятся те, на объект которых у роли есть «Просмотр».
# Итог - build/uitest-report.txt; порог ФормОбойдено и КомандНажато - scripts/smoke-floor.txt (SMOKE_FLOOR=1).
# План, факты пробы и критерии: docs/plans/ui-tests.md.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
set +e
SCRIPTS="$(dirname "${BASH_SOURCE[0]}")"
IB="${1:-$BUILD/ib-gate}"
WORK="$BUILD/uitest"
REPORT="$BUILD/uitest-report.txt"
PORT="${UITEST_PORT:-1548}"
TIMEOUT="${UITEST_TIMEOUT:-900}"
ALL_ROLES="Администратор ОператорПроизводства Кладовщик МенеджерПоПродажам МенеджерПоЗакупкам Казначей Оператор"
ROLES="${UITEST_ROLES:-$ALL_ROLES}"
ENVF="$BUILD/gate/role-users.env"
V8C="$V8_DIR/1cv8c"
mkdir -p "$WORK" "$BUILD/gate"

[ -n "${SMOKE_USER:-}" ] && [ -n "${SMOKE_PWD:-}" ] || { echo "SMOKE_USER/SMOKE_PWD не заданы" >&2; exit 1; }
[ -f "$ENVF" ] || ( umask 077; echo "UITEST_PWD=$(python3 -c 'import secrets;print(secrets.token_urlsafe(12))')" > "$ENVF" )
source "$ENVF"

wait_mark() {  # wait_mark <файл> <секунд>
	local i=0
	while [ "$i" -lt "$2" ]; do
		[ -f "$1" ] && grep -q 'ИТОГ;' "$1" && return 0
		sleep 2; i=$((i + 2))
	done
	return 1
}
stop_clients() {
	pkill -f "TESTCLIENT -TPort $PORT" 2>/dev/null
	pkill -f "TESTMANAGER.*$WORK" 2>/dev/null
	# Под пользователем роли запускалка порождает дочерний клиент (MNG_ENTERPRISE) без ключа TESTCLIENT в строке
	# запуска: он переживал остановку и держал порт следующей роли.
	pkill -f "MNG_ENTERPRISE /F$IB" 2>/dev/null
	sleep 2
}
build_epf() {  # build_epf <имя> <сборщик> <модуль>
	local stamp="$WORK/$1.built"
	python3 "$2" "$1" "$3" "$WORK/src-$1" || return 1
	"$V8" DESIGNER /F "$IB" /N "$SMOKE_USER" /P "$SMOKE_PWD" /LoadExternalDataProcessorOrReportFromFiles \
		"$WORK/src-$1/$1.xml" "$WORK/$1.epf" "${V8_BATCH[@]}" /Out "$WORK/build-$1.log" || true
	local i=0
	while pgrep -f "1cv8.*LoadExternalDataProcessor" >/dev/null && [ "$i" -lt 120 ]; do sleep 2; i=$((i + 2)); done
	[ "$WORK/$1.epf" -nt "$3" ] || { echo "Обработка $1 не собралась:"; cat "$WORK/build-$1.log"; return 1; }
}

echo "== Тесты интерфейса: база $IB =="
build_epf ПользователиРолей "$ROOT/scripts/print-preview/build_epf.py" "$ROOT/tests/ui/role-users.bsl" || exit 1
build_epf ТестыИнтерфейса "$ROOT/tests/ui/build_epf.py" "$ROOT/tests/ui/core.bsl" || exit 1

ROLE_LIST="$(echo "$ALL_ROLES" | tr ' ' '\n' | grep -v '^Администратор$' | paste -sd, -)"
USERS_REP="$WORK/users-report.txt"
: > "$USERS_REP"
"$V8C" ENTERPRISE /F "$IB" /N "$SMOKE_USER" /P "$SMOKE_PWD" /Execute "$WORK/ПользователиРолей.epf" \
	/C "$USERS_REP|$UITEST_PWD|$ROLE_LIST" "${V8_BATCH[@]}" /Out "$WORK/users-client.log" &
if ! wait_mark "$USERS_REP" 300 || ! grep -q 'ИТОГ;ОК' "$USERS_REP"; then
	echo "Пользователи ролей не заведены:"; cat "$USERS_REP"
	echo "ТЕСТЫ НЕ ПРОЙДЕНЫ"; exit 1
fi
sleep 3

: > "$REPORT"
FAILED=0
for ROLE in $ROLES; do
	FORMS="$WORK/forms-$ROLE.txt"
	ROLE_REP="$WORK/report-$ROLE.txt"
	python3 - "$ROOT" "$ROLE" > "$FORMS" <<'PY'
import os, re, sys, unicodedata
root, role = sys.argv[1], sys.argv[2]
rights = None
if role != 'Администратор':
    base = os.path.join(root, 'src/cf/src/Roles')
    folder = [d for d in os.listdir(base) if unicodedata.normalize('NFC', d) == role]
    if not folder:
        sys.exit('нет роли ' + role)
    rights = open(os.path.join(base, folder[0], 'Rights.rights'), encoding='utf-8').read()
for line in open(os.environ.get('UITEST_FORMS') or os.path.join(root, 'tests/ui/forms.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    parts = line.split(';')
    obj, link, name = parts[:3]
    if rights is not None:
        m = re.search(r'<object>\s*<name>' + re.escape(obj) + r'</name>(.*?)</object>', rights, re.S)
        if not (m and re.search(r'<name>View</name>\s*<value>true</value>', m.group(1))):
            continue
    separate = len(parts) > 3 and parts[3].strip() == 'отдельно'
    print(('S' if separate else 'M') + ';' + link + ';' + name)
PY
	EXPECT=$(grep -c . "$FORMS")
	if [ "$EXPECT" -eq 0 ]; then
		echo "ОШИБКА;$ROLE;прогон;у роли нет ни одной формы из tests/ui/forms.txt" >> "$REPORT"
		FAILED=1; continue
	fi
	if [ "$ROLE" = "Администратор" ]; then CU="$SMOKE_USER"; CP="$SMOKE_PWD"; else CU="Тест $ROLE"; CP="$UITEST_PWD"; fi
	echo "-- $ROLE: форм к обходу $EXPECT"
	# Сеансы клиента: общий - формы без пометки, и по одному на каждую форму с пометкой «отдельно».
	grep '^M;' "$FORMS" | cut -d';' -f2- > "$FORMS.0"
	N=0
	grep '^S;' "$FORMS" | cut -d';' -f2- | while IFS= read -r line; do N=$((N + 1)); echo "$line" > "$FORMS.$N"; done
	DONE=0
	for SESSION in "$FORMS".[0-9]*; do
		[ -s "$SESSION" ] || continue
		stop_clients
		ROLE_REP="$WORK/report-$ROLE-$(basename "$SESSION" | sed 's/.*\.//')-$(date +%H%M%S).txt"
		"$V8C" ENTERPRISE /F "$IB" /N "$CU" /P "$CP" /TESTCLIENT -TPort "$PORT" /Out "$WORK/tc-$ROLE.log" &
		sleep 20
		"$V8C" ENTERPRISE /F "$IB" /N "$SMOKE_USER" /P "$SMOKE_PWD" /TESTMANAGER /Execute "$WORK/ТестыИнтерфейса.epf" \
			/C "$ROLE_REP|$PORT|$ROLE|$SESSION" /Out "$WORK/tm-$ROLE.log" &
		if wait_mark "$ROLE_REP" "$TIMEOUT"; then
			sed -e 's/^\xEF\xBB\xBF//' "$ROLE_REP" | grep -v '^СТАРТ;' >> "$REPORT"; echo >> "$REPORT"
			GOT=$(grep -a 'ИТОГ;' "$ROLE_REP" | sed -n 's/.*ФормОбойдено=\([0-9]*\).*/\1/p')
			DONE=$((DONE + ${GOT:-0}))
			grep -a 'ИТОГ;' "$ROLE_REP"
		else
			echo "ОШИБКА;$ROLE;прогон;нет итога за ${TIMEOUT}с (журналы $WORK/tm-$ROLE.log, $WORK/tc-$ROLE.log)" >> "$REPORT"
		fi
		sleep 3
	done
	rm -f "$FORMS".[0-9]*
	if [ "$DONE" -ne "$EXPECT" ]; then
		echo "ОШИБКА;$ROLE;прогон;обойдено форм $DONE из $EXPECT" >> "$REPORT"
	fi
done
stop_clients

SUM() { grep -a '^ИТОГ;Роль=' "$REPORT" | sed -n "s/.*$1=\([0-9]*\).*/\1/p" | paste -sd+ - | bc; }
ERRORS=$(grep -ac '^ОШИБКА;' "$REPORT")
echo "ИТОГ;Ролей=$(grep -a '^ИТОГ;Роль=' "$REPORT" | cut -d';' -f2 | LC_ALL=C sort -u | grep -c .);ФормОбойдено=$(SUM ФормОбойдено);КомандНажато=$(SUM КомандНажато);ОшибокИнтерфейса=$ERRORS" >> "$REPORT"
tail -1 "$REPORT"
if [ "$ERRORS" -ne 0 ]; then
	echo "--- Ошибки интерфейса ($REPORT):"
	grep -a '^ОШИБКА;' "$REPORT" | cut -c1-600
	FAILED=1
fi
if [ "${SMOKE_FLOOR:-0}" = 1 ] && [ -z "${UITEST_ROLES:-}" ]; then
	python3 "$SCRIPTS/floorcheck.py" "$REPORT" Ролей,ФормОбойдено,КомандНажато || FAILED=1
fi
if [ "$FAILED" -ne 0 ]; then echo "ТЕСТЫ НЕ ПРОЙДЕНЫ"; exit 1; fi
echo "ТЕСТЫ ПРОЙДЕНЫ"
