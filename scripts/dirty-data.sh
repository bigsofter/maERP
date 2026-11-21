#!/usr/bin/env bash
# «Грязные» данные базы гейта: непроведённые и помеченные на удаление документы каждого вида, длинные названия
# со спецсимволами (tests/data/dirty-data.bsl). Демо-набор «чистый» - ошибки на таких состояниях доходили до
# владельца. Повторный запуск ничего не добавляет. Только на базе гейта (build/ib-gate), не на базах клиентов.
# Использование: scripts/dirty-data.sh [каталог-базы]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
set +e
IB="${1:-$BUILD/ib-gate}"
case "$IB" in *ib-gate*) ;; *) echo "Только база гейта (build/ib-gate), дано: $IB" >&2; exit 1 ;; esac
[ -n "${SMOKE_USER:-}" ] && [ -n "${SMOKE_PWD:-}" ] || { echo "SMOKE_USER/SMOKE_PWD не заданы" >&2; exit 1; }
W="$BUILD/gate/dirty"; REP="$W/report.txt"
mkdir -p "$W"; : > "$REP"
python3 "$ROOT/scripts/print-preview/build_epf.py" ГрязныеДанные "$ROOT/tests/data/dirty-data.bsl" "$W/src" || exit 1
"$V8" DESIGNER /F "$IB" /N "$SMOKE_USER" /P "$SMOKE_PWD" /LoadExternalDataProcessorOrReportFromFiles \
	"$W/src/ГрязныеДанные.xml" "$W/ГрязныеДанные.epf" "${V8_BATCH[@]}" /Out "$W/build.log" || true
i=0; while pgrep -f "1cv8.*LoadExternalDataProcessor" >/dev/null && [ "$i" -lt 120 ]; do sleep 2; i=$((i + 2)); done
"$V8_DIR/1cv8c" ENTERPRISE /F "$IB" /N "$SMOKE_USER" /P "$SMOKE_PWD" /Execute "$W/ГрязныеДанные.epf" \
	/C "$REP|" "${V8_BATCH[@]}" /Out "$W/client.log" &
PID=$!
i=0; while ! grep -q 'ИТОГ;' "$REP" && [ "$i" -lt 600 ]; do sleep 2; i=$((i + 2)); done
kill "$PID" 2>/dev/null
grep -a 'ГРЯЗНЫЕДАННЫЕ\|ОТКАЗ\|ПРОПУСК\|ИТОГ' "$REP" | cut -c1-300
grep -q 'ИТОГ;ОК' "$REP" || { echo "Грязные данные не созданы (журнал $W/client.log)"; exit 1; }
