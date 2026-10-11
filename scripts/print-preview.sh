#!/usr/bin/env bash
# Предпросмотр печатной формы: печатает форму на базе так же, как окно печати
# (ПечатныеФормы.СформироватьПечатныеФормы), пишет PDF и картинки страниц PNG.
# Смок проверяет только, что форма формируется; вид — только глазами (tiny1C tmpl-004).
#
# Использование:
#   scripts/print-preview.sh <ПолноеИмяДокумента> <ИмяМакета> [КодЯзыка] [НомерДокумента] [ПараметрыПечати]
#   scripts/print-preview.sh Документ.КоммерческоеПредложение КоммерческоеПредложение fr
#   scripts/print-preview.sh Документ.КоммерческоеПредложение КоммерческоеПредложение ru 00000000005 "Версия=1"
# НомерДокумента — окончание номера (ПОДОБНО «%номер»); пусто — последний не помеченный документ.
# ПараметрыПечати — «Ключ=Значение;...», числа и Истина приводятся.
# База — PREVIEW_IB (по умолчанию build/ib-kp: build/ib держит EDT), результат — build/print-preview/.
# Доступ — SMOKE_USER/SMOKE_PWD. Первый запуск после обновления конфигурации может остановиться на окне
# «Предупреждение безопасности» внешней обработки — тогда таймаут PREVIEW_TIMEOUT и сообщение, что нужен щелчок «Да».
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

OBJ="${1:?полное имя документа}"
TMPL="${2:?имя макета}"
LANG_CODE="${3:-ru}"
NUM="${4:-}"
PARAMS="${5:-}"
IB="${PREVIEW_IB:-$BUILD/ib-kp}"
TIMEOUT="${PREVIEW_TIMEOUT:-180}"

OUT="$BUILD/print-preview"
WORK="$OUT/work"
NAME="ПредпросмотрПечати"
mkdir -p "$OUT" "$WORK"

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

BASE="$(echo "${OBJ#*.}-$TMPL-$LANG_CODE${NUM:+-$NUM}${PARAMS:+-$PARAMS}" | tr '/;= ' '____')"
PDF="$OUT/$BASE.pdf"
REP="$WORK/$BASE.report.txt"
EPF="$WORK/$NAME.epf"
rm -f "$PDF" "$REP" "$OUT/$BASE"-*.png

if [ ! -f "$EPF" ] || [ "$(dirname "${BASH_SOURCE[0]}")/print-preview/print.bsl" -nt "$EPF" ]; then
	python3 "$(dirname "${BASH_SOURCE[0]}")/print-preview/build_epf.py" "$NAME" \
		"$(dirname "${BASH_SOURCE[0]}")/print-preview/print.bsl" "$WORK/src"
	"$V8" DESIGNER /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /LoadExternalDataProcessorOrReportFromFiles \
		"$WORK/src/$NAME.xml" "$EPF" "${V8_BATCH[@]}" /Out "$WORK/build.log" || true
	sleep 3
	while pgrep -f "1cv8.*LoadExternalDataProcessor" >/dev/null; do sleep 2; done
	[ -f "$EPF" ] || { cat "$WORK/build.log"; echo "Обработка предпросмотра не собрана" >&2; exit 1; }
fi

"$V8_DIR/1cv8c" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /Execute "$EPF" \
	/C "$REP|$OBJ|$TMPL|$LANG_CODE|$NUM|$PDF|$PARAMS" "${V8_BATCH[@]}" /Out "$WORK/client.log" &
CLIENT=$!

T=0
until [ -f "$REP" ] && grep -q 'ИТОГ;' "$REP"; do
	sleep 2; T=$((T + 2))
	if [ "$T" -gt "$TIMEOUT" ]; then
		kill "$CLIENT" 2>/dev/null || true
		echo "Таймаут ${TIMEOUT} с: клиент не дописал отчёт. Если это первый запуск после обновления" \
			"конфигурации — в окне 1С ждёт «Предупреждение безопасности», нужен щелчок «Да»." >&2
		exit 2
	fi
done
wait "$CLIENT" 2>/dev/null || true

cat "$REP"
grep -q 'ИТОГ;ОК' "$REP" || exit 1
pdftoppm -png -r "${PREVIEW_DPI:-110}" "$PDF" "$OUT/$BASE"
ls "$OUT/$BASE"*.png
