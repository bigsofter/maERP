#!/usr/bin/env bash
# Заполнение тестовой базы образцами объектов печати (обработка ТестовыеДанные).
# Использование: scripts/fixtures.sh [каталог-базы]      (по умолчанию build/ib)
#
# ВНИМАНИЕ: скрипт ЗАПИСЫВАЕТ данные — документы остаются в базе. Запускать только
# на тестовой базе, не на базе клиента.
#
# Второй проход смока проверяет печатную форму только там, где в базе есть хотя бы один
# объект. Скрипт заводит по одному образцу для каждого объекта, у которого образца нет,
# после чего scripts/smoke.sh закрывает печать целиком.
#
# Доступ к базе с пользователями: переменные окружения SMOKE_USER и SMOKE_PWD.
# Регламент: docs/TESTING.md.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
source "$(dirname "${BASH_SOURCE[0]}")/run-lib.sh"

IB="${1:-$IB_BUILD}"
REPORT="$BUILD/fixtures-report.txt"
CLIENT_LOG="$BUILD/fixtures-client.log"
TIMEOUT="${SMOKE_TIMEOUT:-900}"
START_TIMEOUT="${SMOKE_START_TIMEOUT:-120}"

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

echo "== Заполнение образцов объектов печати =="
echo "База: $IB"

# Тонкий клиент обязателен: толстый компилирует общие модули «Сервер + Вызов сервера»
# дважды и падает на старте.
V8C="${V8_DIR}/1cv8c"
rm -f "$REPORT" "$CLIENT_LOG"
"$V8C" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /C "ТестовыеДанные;$REPORT" \
	"${V8_BATCH[@]}" /Out "$CLIENT_LOG" || true

if ! wait_client_start "ТестовыеДанные;$REPORT" "$REPORT"; then
	echo "Клиент не стартовал за ${START_TIMEOUT}с (нет строки СТАРТ в $REPORT) — процесс снят."
	echo "Клиентский лог: $CLIENT_LOG"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	exit 1
fi

if ! wait_report_mark "ТестовыеДанные;$REPORT" "$REPORT" "^ИТОГ;"; then
	echo "Заполнение не отработало: нет строки ИТОГ в $REPORT (клиентский лог: $CLIENT_LOG)"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	exit 1
fi

grep '^ИТОГ;' "$REPORT"
if grep -q '^СОЗДАН;' "$REPORT"; then
	echo "--- Заведены образцы:"
	grep '^СОЗДАН;' "$REPORT"
fi
if grep -q '^ОШИБКА;' "$REPORT"; then
	echo "--- Не удалось завести ($REPORT):"
	grep '^ОШИБКА;' "$REPORT"
	echo "ЗАПОЛНЕНИЕ НЕ ЗАВЕРШЕНО"
	exit 1
fi
echo "ЗАПОЛНЕНИЕ ВЫПОЛНЕНО"
