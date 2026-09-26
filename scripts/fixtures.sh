#!/usr/bin/env bash
# Заполнение тестовой базы образцами объектов печати (обработка ТестовыеДанные).
# Использование: scripts/fixtures.sh [--demo] [каталог-базы]      (по умолчанию build/ib)
#
# ВНИМАНИЕ: скрипт ЗАПИСЫВАЕТ данные — документы остаются в базе. Запускать только
# на тестовой базе, не на базе клиента.
#
# Второй проход смока проверяет печатную форму только там, где в базе есть хотя бы один
# объект. Скрипт заводит по одному образцу для каждого объекта, у которого образца нет,
# после чего scripts/smoke.sh закрывает печать целиком.
#
# С ключом --demo вместо образцов заводится демо-набор производственного контура и
# торговли: заказы на производство на каждой стадии, статусы продаж, КП, лидов, договоров
# и заявок (Обработки.ТестовыеДанные.СоздатьДемоНабор). Одной транзакцией в текущем
# дне; повторный запуск набор не дублирует; в первые 15 минут дня запуск отказывает.
# Состав — docs/TESTING.md, раздел «Демо-набор».
#
# Доступ к базе с пользователями: переменные окружения SMOKE_USER и SMOKE_PWD.
# Регламент: docs/TESTING.md.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
source "$(dirname "${BASH_SOURCE[0]}")/run-lib.sh"

MODE_PARAM=""
TITLE="== Заполнение образцов объектов печати =="
if [ "${1:-}" = "--demo" ]; then
	shift
	MODE_PARAM=";Демо"
	TITLE="== Заполнение демо-набора производственного контура и торговли =="
fi
IB="${1:-$IB_BUILD}"
REPORT="$BUILD/fixtures-report.txt"
CLIENT_LOG="$BUILD/fixtures-client.log"
TIMEOUT="${SMOKE_TIMEOUT:-900}"
START_TIMEOUT="${SMOKE_START_TIMEOUT:-120}"

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

echo "$TITLE"
echo "База: $IB"

# Тонкий клиент обязателен: толстый компилирует общие модули «Сервер + Вызов сервера»
# дважды и падает на старте.
V8C="${V8_DIR}/1cv8c"
rm -f "$REPORT" "$CLIENT_LOG"
"$V8C" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /C "ТестовыеДанные;$REPORT$MODE_PARAM" \
	"${V8_BATCH[@]}" /Out "$CLIENT_LOG" || true

if ! wait_client_start "ТестовыеДанные;$REPORT$MODE_PARAM" "$REPORT"; then
	echo "Клиент не стартовал за ${START_TIMEOUT}с (нет строки СТАРТ в $REPORT) — процесс снят."
	echo "Клиентский лог: $CLIENT_LOG"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	exit 1
fi

if ! wait_report_mark "ТестовыеДанные;$REPORT$MODE_PARAM" "$REPORT" "ИТОГ;"; then
	echo "Заполнение не отработало: нет строки ИТОГ в $REPORT (клиентский лог: $CLIENT_LOG)"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	exit 1
fi

grep 'ИТОГ;' "$REPORT"
# Без якоря ^: отчёт 1С пишет с BOM, первая строка иначе не находится (tiny1C workflow-002).
if grep -qE '(ЕСТЬ|НАСТРОЙКА);' "$REPORT"; then
	grep -E '(ЕСТЬ|НАСТРОЙКА);' "$REPORT"
fi
if grep -q 'СОЗДАН;' "$REPORT"; then
	echo "--- Заведено:"
	grep 'СОЗДАН;' "$REPORT"
fi
if grep -q 'ОШИБКА;' "$REPORT"; then
	echo "--- Не удалось завести ($REPORT):"
	grep 'ОШИБКА;' "$REPORT"
	echo "ЗАПОЛНЕНИЕ НЕ ЗАВЕРШЕНО"
	exit 1
fi
echo "ЗАПОЛНЕНИЕ ВЫПОЛНЕНО"
