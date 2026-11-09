#!/usr/bin/env bash
# Конкурентный тест КП из реализации (docs/plans/branded-print.md, 9.10) на копии базы: в ТестыДокументов его не
# проверить — раннер откатывает транзакцию, другие сеансы её не видят.
#   (а) два сеанса 1cv8c одновременно печатают КП новой реализации без КП → авто-КП один;
#   (б) печать одновременно со служебной записью «Выигран» (заказ по авто-КП) → выигранный КП без флага и не
#       перезаписан, активных авто-КП не больше одного; повторная печать → активный ровно один и это не выигранный.
# Созданные документы удаляются, значение опции возвращается.
#
# Использование: scripts/kp-concurrency.sh
# База — KP_IB (по умолчанию build/ib-kp: build/ib держит EDT), доступ — SMOKE_USER/SMOKE_PWD.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

IB="${KP_IB:-$BUILD/ib-kp}"
TIMEOUT="${KP_TIMEOUT:-240}"
WORK="$BUILD/kp-concurrency"
NAME="КонкурентностьКП"
EPF="$WORK/$NAME.epf"
TAG="kp-concurrency $(date +%Y%m%d%H%M%S)"
mkdir -p "$WORK"
OPEN="$WORK/open"; touch "$OPEN"   # барьер последовательных шагов - открыт сразу

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

BODY="$(dirname "${BASH_SOURCE[0]}")/kp-concurrency/run.bsl"
if [ ! -f "$EPF" ] || [ "$BODY" -nt "$EPF" ]; then
	python3 "$(dirname "${BASH_SOURCE[0]}")/print-preview/build_epf.py" "$NAME" "$BODY" "$WORK/src"
	"$V8" DESIGNER /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /LoadExternalDataProcessorOrReportFromFiles \
		"$WORK/src/$NAME.xml" "$EPF" "${V8_BATCH[@]}" /Out "$WORK/build.log" || true
	sleep 3
	while pgrep -f "1cv8.*LoadExternalDataProcessor" >/dev/null; do sleep 2; done
	[ -f "$EPF" ] || { cat "$WORK/build.log"; echo "Обработка теста не собрана" >&2; exit 1; }
fi

# Запуск шага в фоне; отчёт — $WORK/<имя>.txt. Аргументы: имя отчёта, шаг, реализация, барьер, [опция для cleanup].
start_step() {
	local rep="$WORK/$1.txt"
	rm -f "$rep"
	# Окно «Предупреждение безопасности» внешней обработки после обновления конфигурации ждало бы щелчка: защита от
	# опасных действий снимается только для этой копии базы и только на время запуска.
	"$V8_DIR/1cv8c" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /DisableUnsafeActionProtection ".*$(basename "$IB").*" \
		/Execute "$EPF" /C "$rep|$2|$3|$4|$TAG|${5:-}" "${V8_BATCH[@]}" /Out "$WORK/$1.client.log" &
}
wait_report() {
	local rep="$WORK/$1.txt" t=0
	until [ -f "$rep" ] && grep -q 'ИТОГ;' "$rep"; do
		sleep 2; t=$((t + 2))
		if [ "$t" -gt "$TIMEOUT" ]; then
			echo "Таймаут ${TIMEOUT} с: шаг $1 не дописал отчёт (журнал клиента: $WORK/$1.client.log)" >&2
			return 2
		fi
	done
	# 1С пишет отчёт с CRLF: без чистки идентификаторы из полей уносили бы \r в сравнения.
	tr -d '\r' < "$rep" > "$rep.tmp" && mv "$rep.tmp" "$rep"
	grep -q 'ИТОГ;ОК' "$rep" || { echo "Шаг $1 упал:" >&2; cat "$rep" >&2; return 1; }
}
run_step() { start_step "$@"; wait_report "$1"; }
field() { grep "^$2;" "$WORK/$1.txt" | head -1 | cut -d';' -f"$3"; }

FAIL=0
check() { if [ "$1" = "$2" ]; then echo "ОК;$3"; else echo "ОШИБКА;$3 (ожидалось $2, получено $1)"; FAIL=1; fi; }

cleanup() {
	[ -n "$1" ] || return 0
	run_step cleanup cleanup "$1" "" "$2" >/dev/null || { echo "ОШИБКА;очистка реализации $1"; FAIL=1; }
}
# Обрыв на любом шаге не оставляет данных прогона: реализации, ещё не очищенные, удаляются при выходе.
REAL_A=""; REAL_B=""; OPT=""
on_exit() { set +e; cleanup "$REAL_A" "$OPT"; cleanup "$REAL_B" "$OPT"; }
trap on_exit EXIT

# (а) две печати одной реализации без КП
run_step prepA prepare "" "" || exit 1
# Значение опции до прогона - из первого prepare: второй видит уже выключенную.
OPT="$(field prepA ОПЦИЯ 2)"; REAL_A="$(field prepA РЕАЛИЗАЦИЯ 2)"
BARRIER="$WORK/barrier-a"; rm -f "$BARRIER"
# Старт клиентов разнесён: два клиента, открывающие файловую базу в одну секунду, падают на захвате 1Cv8tmp.1CD.
# Одновременность самой работы даёт барьер.
start_step printA1 print "$REAL_A" "$BARRIER"; sleep 5
start_step printA2 print "$REAL_A" "$BARRIER"
sleep "${KP_START_DELAY:-15}"; touch "$BARRIER"
R1=0; wait_report printA1 || R1=$?; R2=0; wait_report printA2 || R2=$?
check "$R1$R2" "00" "(а) обе печати завершились"
run_step checkA check "$REAL_A" "" && check "$(field checkA АВТОКП 2)" "1" "(а) у реализации один авто-КП после двух одновременных печатей"
cp "$WORK/checkA.txt" "$WORK/checkA.keep.txt" 2>/dev/null
cleanup "$REAL_A" "$OPT"; REAL_A=""

# (б) печать одновременно со служебной записью «Выигран»
run_step prepB prepare "" "" || exit 1
REAL_B="$(field prepB РЕАЛИЗАЦИЯ 2)"
run_step printB0 print "$REAL_B" "$OPEN" || exit 1
BARRIER="$WORK/barrier-b"; rm -f "$BARRIER"
start_step orderB order "$REAL_B" "$BARRIER"; sleep 5
start_step printB1 print "$REAL_B" "$BARRIER"
sleep "${KP_START_DELAY:-15}"; touch "$BARRIER"
R1=0; wait_report orderB || R1=$?; R2=0; wait_report printB1 || R2=$?
check "$R1$R2" "00" "(б) заказ и печать завершились"
WON="$(field orderB ВЫИГРАН 2)"
run_step checkB1 check "$REAL_B" ""
ACTIVE="$(field checkB1 АВТОКП 2)"
[ "$ACTIVE" -le 1 ] 2>/dev/null && echo "ОК;(б) активных авто-КП не больше одного ($ACTIVE)" || { echo "ОШИБКА;(б) активных авто-КП $ACTIVE"; FAIL=1; }
WONLINE="$(grep "^КП;$WON;" "$WORK/checkB1.txt" || true)"
check "$(echo "$WONLINE" | cut -d';' -f4)" "0" "(б) выигранный КП передан человеку (флаг снят)"
echo "$WONLINE" | cut -d';' -f3 | grep -q 'Выигран\|Won\|Gagné\|Ganado' && echo "ОК;(б) выигранный КП в статусе «Выигран»" || { echo "ОШИБКА;(б) статус выигранного КП: $WONLINE"; FAIL=1; }
run_step printB2 print "$REAL_B" "$OPEN"
run_step checkB2 check "$REAL_B" ""
check "$(field checkB2 АВТОКП 2)" "1" "(б) после повторной печати активный авто-КП ровно один"
[ "$(field checkB2 АВТОКП 3)" != "$WON" ] && echo "ОК;(б) активный авто-КП - не выигранный" || { echo "ОШИБКА;(б) активный авто-КП - выигранный"; FAIL=1; }
check "$( (grep "^КП;$WON;" "$WORK/checkB2.txt" || true) | cut -d';' -f5)" "$(echo "$WONLINE" | cut -d';' -f5)" "(б) повторная печать не перезаписала выигранный КП"
cleanup "$REAL_B" "$OPT"; REAL_B=""

[ "$FAIL" = 0 ] && echo "ИТОГ;ОК" || { echo "ИТОГ;ОШИБКА"; exit 1; }
