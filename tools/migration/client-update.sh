#!/usr/bin/env bash
# Переход файловой базы старой ветки Commerce на maERP одним прогоном (docs/plans/retail-client-update.md, раздел 7).
# Использование: tools/migration/client-update.sh <база-источник> <рабочий-каталог-базы> <каталог-XML-maERP> <выгрузка.json> [ПРОБА] [расширение-к-удалению]
#   ПРОБА - источник копируется в рабочий каталог, выгрузка без монопольного режима и выключения заданий;
#   без ПРОБА - рабочий каталог и есть боевая база (источник = рабочий каталог), окно простоя - на всё время скрипта.
# Шаги: копия -> выгрузка «до» (условия, отпечаток, сверка) -> удаление расширения -> загрузка XML maERP ->
# реструктуризация -> вход с обновлением и загрузкой «после» -> .dt. Остановка на любом шаге - код возврата 1.
# Окружение (необязательно): PROFILE - профиль переноса (tools/migration/profiles/*.json: пороги условий выгрузки «до»);
# MIGRATION_LOGS - каталог журналов (по умолчанию build/migration-logs; свой на каждую базу - прогоны параллельно);
# HOOK_BEFORE_LOAD - команда после загрузки CF maERP до шага 5 (параметр - каталог базы: пересоздание документов клиента
# с другим uuid, чтобы отпечаток сошёлся); DUMP - путь .dt (по умолчанию <база>.dt), «нет» - без выгрузки .dt;
# RECONCILE=внешняя - расхождения сверки загрузки «после» не останавливают скрипт (только с DUMP=нет): сверку принимает
# tools/migration/reconcile.py (округление сумм с тремя знаками, ожидаемые дельты шагов по базе).
set -euo pipefail
D=$(cd "$(dirname "$0")" && pwd)
source "$D/../../scripts/env.sh"
SRC=$1; IB=$2; XML=$3; JSON=$4; MODE=${5:-}; EXT=${6:-}
LOGS="${MIGRATION_LOGS:-$BUILD/migration-logs}"; mkdir -p "$LOGS"
export MIGRATION_EPF="${MIGRATION_EPF:-$LOGS/epf}"
PROFILE=${PROFILE:-}; [ -z "$PROFILE" ] || PROFILE=$(cd "$(dirname "$PROFILE")" && pwd -P)/$(basename "$PROFILE")
step() { echo "== $1   [$(date '+%Y-%m-%d %H:%M:%S')]"; }
AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")
designer() { "$V8" DESIGNER /F "$IB" ${AUTH[@]+"${AUTH[@]}"} "$@" "${V8_BATCH[@]}"; }

if [ "$MODE" = "ПРОБА" ]; then
	SRC_ABS=$(cd "$SRC" && pwd -P)
	mkdir -p "$IB"; IB_ABS=$(cd "$IB" && pwd -P)
	case "$IB_ABS/" in "$SRC_ABS"/*) echo "Рабочий каталог совпадает с источником или лежит в нём: $IB"; exit 1;; esac
	case "$SRC_ABS/" in "$IB_ABS"/*) echo "Источник лежит в рабочем каталоге: $SRC"; exit 1;; esac
	# Удаляется только каталог файловой базы 1С: посторонние файлы - отказ.
	OTHERS=$(find "$IB" -mindepth 1 -maxdepth 1 | while read -r F; do
		case "$(basename "$F")" in
			(1Cv8.1CD|1Cv8.1CL|1Cv8tmp.1CD|1Cv8tmp.1CL|1Cv8snc.1CD|1Cv8snc.1CL|1Cv8Log|1Cv8JobScheduler|1CHelpIndex|1Cv8FTxt) ;;
			(1Cv8.1CD.cfl|1Cv8.1CL.cfl|1Cv8tmp.1CD.cfl|1Cv8tmp.1CL.cfl|1Cv8snc.1CD.cfl|1Cv8snc.1CL.cfl|1Cv8.cgr.cfl) ;;
			(*) echo "$F"; break;;
		esac
	done)
	[ -z "$OTHERS" ] || { echo "В рабочем каталоге есть файлы не базы 1С ($OTHERS) - каталог не удаляется"; exit 1; }
	step "1. Копия базы: $SRC -> $IB"
	rm -rf "$IB"; mkdir -p "$IB"; cp "$SRC_ABS/1Cv8.1CD" "$IB/"
fi

step "2. Выгрузка «до»"
"$D/run-epf.sh" "$IB" Export "$D/ВыгрузкаДляПереноса.bsl" "$LOGS/export.txt" "$JSON|$MODE|$PROFILE" \
	| grep -a "УСЛОВИЕ\|ГОТОВО\|СТОП\|ОШИБКА\|ТИПКОДА"
grep -q "ГОТОВО;" "$LOGS/export.txt" || { echo "Выгрузка остановлена: условия не выполнены (см. $LOGS/export.txt)"; exit 1; }
chmod 600 "$JSON"   # пароли баз партнёров: только владельцу файла, файл удаляется после успешной загрузки

if [ -n "$EXT" ]; then
	step "3. Удаление расширения $EXT"
	designer /DeleteCfg -Extension "$EXT" /Out "$LOGS/delete-ext.log" || { cat "$LOGS/delete-ext.log"; exit 1; }
fi

apply_cfg() {
	designer /LoadConfigFromFiles "$1" -Format Hierarchical /Out "$LOGS/load-$2.log" || { cat "$LOGS/load-$2.log"; exit 1; }
	designer /UpdateDBCfg /Out "$LOGS/apply-$2.log" || { grep -v "ha sido cambiado\|изменен" "$LOGS/apply-$2.log" | tail -20; exit 1; }
	grep -qi "con éxito\|успешно" "$LOGS/apply-$2.log" || { tail -20 "$LOGS/apply-$2.log"; exit 1; }
}

# Тип кода: у части старых веток код справочников Бренды, ВидыЦен, TypesDePayment строковый, у maERP - числовой; прямую
# смену типа реструктуризация не проходит. Сначала вариант CF со строковым кодом, приведение кодов к цифрам, затем CF
# maERP. У ветки с числовым кодом (выгрузка «до» пишет ТИПКОДА) шаги 4а-4в не нужны.
if tr -d '\r' < "$LOGS/export.txt" | grep -q "^ТИПКОДА;.*;String$"; then
step "4а. Вариант конфигурации maERP со строковым кодом трёх справочников"
XML_STR="$LOGS/xml-string-codes"
rm -rf "$XML_STR"; cp -R "$XML" "$XML_STR"
for C in Бренды ВидыЦен TypesDePayment; do
	sed -i '' 's#<CodeType>Number</CodeType>#<CodeType>String</CodeType>#' "$XML_STR/Catalogs/$C.xml"
done
apply_cfg "$XML_STR" string-codes
step "4б. Коды трёх справочников - цифрами"
# Первый вход на CF maERP выполняет обработчики обновления (у базы с годами истории - часы): запас как у загрузки.
TIMEOUT=${TIMEOUT:-14400} "$D/run-epf.sh" "$IB" Codes "$D/codes.bsl" "$LOGS/codes.txt" > /dev/null || { cat "$LOGS/codes.txt"; exit 1; }
grep -q "ИТОГ;ОК" "$LOGS/codes.txt" || { cat "$LOGS/codes.txt"; exit 1; }
grep -a "КОДЫ;" "$LOGS/codes.txt"
# Справочники с предопределёнными элементами меняют тип кода только без автообновления предопределённых: иначе
# реструктуризация обновляет их ещё по старой схеме колонки кода («тип поля Code несовместим с литералом»).
step "4в. Вариант с числовым кодом без автообновления предопределённых"
XML_NUM="$LOGS/xml-number-codes"
rm -rf "$XML_STR" "$XML_NUM"; cp -R "$XML" "$XML_NUM"
for C in ВидыЦен TypesDePayment; do
	sed -i '' 's#<PredefinedDataUpdate>Auto</PredefinedDataUpdate>#<PredefinedDataUpdate>DontAutoUpdate</PredefinedDataUpdate>#' "$XML_NUM/Catalogs/$C.xml"
done
apply_cfg "$XML_NUM" number-codes
rm -rf "$XML_NUM"
else
	echo "Код трёх справочников числовой - шаги 4а-4в не нужны"
fi
step "4г. Конфигурация maERP и реструктуризация"
apply_cfg "$XML" maerp
if [ -n "${HOOK_BEFORE_LOAD:-}" ]; then
	step "4д. Перед загрузкой «после»: $HOOK_BEFORE_LOAD"
	$HOOK_BEFORE_LOAD "$IB" || { echo "Шаг перед загрузкой «после» не выполнен"; exit 1; }
fi

step "5. Вход: обработчики обновления и загрузка «после»"
TIMEOUT=${TIMEOUT:-14400} "$D/run-epf.sh" "$IB" Load "$D/load.bsl" "$LOGS/load-report.txt" "$JSON" > /dev/null \
	|| { cat "$LOGS/load-report.txt" 2>/dev/null; echo "Загрузка «после» не завершилась"; exit 1; }
cat "$LOGS/load-report.txt"
grep -q "ИТОГ;ОК" "$LOGS/load-report.txt" || { echo "Загрузка «после» без маркера ИТОГ;ОК"; exit 1; }
grep -q "ОСТАНОВ\|ИТОГ;ОШИБКА" "$LOGS/load-report.txt" && { echo "Загрузка «после» остановлена"; exit 1; }
if ! tr -d '\r' < "$LOGS/load-report.txt" | grep -q "^СВЕРКА;расхождений 0$"; then
	if [ "${RECONCILE:-}" = "внешняя" ] && [ "${DUMP:-}" = "нет" ]; then
		echo "ВНИМАНИЕ: сверка загрузки с расхождениями - принимает reconcile.py (RECONCILE=внешняя)"
	else
		echo "Сверка «до/после» с расхождениями - .dt не выгружается"; exit 1
	fi
fi
grep -q "пропущено [1-9]" "$LOGS/load-report.txt" && echo "ВНИМАНИЕ: есть пропуски объектов - перечень в отчёте, решение владельца"

rm -f "$JSON"; echo "Файл выгрузки с паролями партнёров удалён: $JSON"

DUMP=${DUMP:-$IB.dt}
[ "$DUMP" = "нет" ] && { step "Готово, .dt не выгружается (DUMP=нет)"; exit 0; }
step "6. Выгрузка .dt"
designer /DumpIB "$DUMP" /Out "$LOGS/dump.log" || { cat "$LOGS/dump.log"; exit 1; }
ls -la "$DUMP"
step "Готово"
