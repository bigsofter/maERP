#!/usr/bin/env bash
# Тесты документов (уровень 3): жизненный цикл ключевых документов - создание, запись,
# проведение, движения по регистрам. Обработка ТестыДокументов подсистемы «Автотесты».
# Использование: scripts/doctests.sh [каталог-базы]       (по умолчанию build/ib)
#
# Каждый сценарий выполняется в транзакции с откатом: база после прогона не меняется,
# поэтому запуск безопасен и на копии базы клиента.
#
# Доступ к базе с пользователями: переменные окружения SMOKE_USER и SMOKE_PWD.
# Регламент, состав сценариев и разбор ошибок: docs/TESTING.md.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
source "$(dirname "${BASH_SOURCE[0]}")/run-lib.sh"

IB="${1:-$IB_BUILD}"
REPORT="$BUILD/doctests-report.txt"
CLIENT_LOG="$BUILD/doctests-client.log"
TIMEOUT="${SMOKE_TIMEOUT:-900}"
START_TIMEOUT="${SMOKE_START_TIMEOUT:-120}"

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

echo "== Тесты документов (уровень 3) =="
echo "База: $IB"

# Тонкий клиент обязателен: толстый компилирует общие модули «Сервер + Вызов сервера»
# дважды и падает на старте.
V8C="${V8_DIR}/1cv8c"
rm -f "$REPORT" "$CLIENT_LOG"
"$V8C" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /C "ТестыДокументов;$REPORT" \
	"${V8_BATCH[@]}" /Out "$CLIENT_LOG" || true

if ! wait_client_start "ТестыДокументов;$REPORT" "$REPORT"; then
	echo "Клиент не стартовал за ${START_TIMEOUT}с (нет строки СТАРТ в $REPORT) — процесс снят."
	echo "Клиентский лог: $CLIENT_LOG"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	echo "ТЕСТЫ НЕ ПРОЙДЕНЫ"
	exit 1
fi

if ! wait_report_mark "ТестыДокументов;$REPORT" "$REPORT" "ИТОГ;"; then
	echo "Прогон не отработал: нет строки ИТОГ в $REPORT (клиентский лог: $CLIENT_LOG)"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	echo "ТЕСТЫ НЕ ПРОЙДЕНЫ"
	exit 1
fi

# Без якоря ^: отчёт 1С начинается с BOM.
grep 'ИТОГ;' "$REPORT"
grep 'ОК;' "$REPORT" || true
if grep -q 'ПРОПУСК;' "$REPORT"; then
	echo "--- Пропущенные сценарии (в базе нет условий):"
	grep 'ПРОПУСК;' "$REPORT"
fi
if grep -q 'ОШИБКА;' "$REPORT"; then
	echo "--- Ошибки сценариев ($REPORT):"
	grep 'ОШИБКА;' "$REPORT"
	echo "ТЕСТЫ НЕ ПРОЙДЕНЫ"
	exit 1
fi
echo "ТЕСТЫ ПРОЙДЕНЫ"
