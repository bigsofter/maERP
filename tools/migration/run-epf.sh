#!/usr/bin/env bash
# Собирает внешнюю обработку из BSL-тела (Главная(Части, Лог)) и выполняет её в базе тонким клиентом.
# Использование: tools/migration/run-epf.sh <каталог-базы> <Имя> <тело.bsl> <отчёт> [доп.параметры через |]
# Доступ к базе: SMOKE_USER / SMOKE_PWD (как в scripts/smoke.sh). Ждёт строку «ИТОГ;» в отчёте (TIMEOUT, сек).
set -euo pipefail
D=$(cd "$(dirname "$0")" && pwd)
source "$D/../../scripts/env.sh"
IB=$1; NAME=$2; BODY=$3; REP=$4; EXTRA=${5:-}
WORK="$BUILD/migration-epf/$NAME"; EPF="$WORK.epf"
mkdir -p "$BUILD/migration-epf"; rm -rf "$WORK" "$EPF" "$REP"
python3 "$D/build_epf.py" "$NAME" "$BODY" "$WORK"
AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")
"$V8" DESIGNER /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /LoadExternalDataProcessorOrReportFromFiles "$WORK/$NAME.xml" "$EPF" \
	"${V8_BATCH[@]}" /Out "$WORK.build.log" || true
[ -f "$EPF" ] || { cat "$WORK.build.log"; echo "Внешняя обработка не собрана"; exit 1; }
# Регламентные задания в сеансах переноса не выполняются (файловая база выполняет их в клиенте): перепроведение
# истории до переноса границы последовательности изменило бы перенесённые движения.
"$V8_DIR/1cv8c" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /AllowExecuteScheduledJobs -Off /Execute "$EPF" /C "$REP${EXTRA:+|$EXTRA}" \
	"${V8_BATCH[@]}" /Out "$WORK.client.log" || true
T=0
until [ -f "$REP" ] && grep -q 'ИТОГ;' "$REP"; do
	sleep 5; T=$((T + 5))
	[ $T -gt "${TIMEOUT:-3600}" ] && { echo "Нет итога за ${TIMEOUT:-3600} с: $REP"; exit 1; }
done
cat "$REP"
