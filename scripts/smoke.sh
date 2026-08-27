#!/usr/bin/env bash
# Автотесты на базе: проверка конфигурации (DESIGNER /CheckConfig) и дымовой
# прогон «открыть все формы» (обработка СмокТест, запуск через /C).
# Использование: scripts/smoke.sh [каталог-базы]        (по умолчанию build/ib)
# Шаг 2 не запускается, если CheckConfig нашёл ошибку компиляции: клиент с несобирающимся
# модулем всё равно не поднимется, а прогон только съест таймаут.
# Доступ к базе с пользователями: переменные окружения SMOKE_USER и SMOKE_PWD —
# пароль передаётся только так, в файлы и логи не попадает.
# Регламент и разбор ошибок: docs/TESTING.md.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

IB="${1:-$IB_BUILD}"
CHECK_LOG="$BUILD/check-config.log"
REPORT="$BUILD/smoke-report.txt"
CLIENT_LOG="$BUILD/smoke-client.log"
TIMEOUT="${SMOKE_TIMEOUT:-900}"   # секунд на каждый шаг
START_TIMEOUT="${SMOKE_START_TIMEOUT:-120}"   # секунд на старт клиента (до строки СТАРТ в отчёте)

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

FAILED=0

# Ожидание клиента и отчёта - в scripts/run-lib.sh (общее с scripts/fixtures.sh).
source "$(dirname "${BASH_SOURCE[0]}")/run-lib.sh"

echo "== Шаг 1. Проверка конфигурации (CheckConfig) =="
rm -f "$CHECK_LOG"
"$V8" DESIGNER /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /CheckConfig \
	-ConfigLogIntegrity -IncorrectReferences -ThinClient -Server \
	"${V8_BATCH[@]}" /Out "$CHECK_LOG" || true
wait_process_end "CheckConfig" || { echo "CheckConfig не завершился за ${TIMEOUT}с — процесс снят"; FAILED=1; }
# Платформа пишет в лог строку «ошибок не обнаружено» на своём языке интерфейса —
# для скрипта это чистый результат, а не замечание.
CHECK_CLEAN_LINE='Ошибок не обнаружено|Errores no encontrados|No errors found|Aucune erreur'
COMPILE_ERROR=0
if [ -s "$CHECK_LOG" ] && grep -qvE "^[[:space:]]*$|$CHECK_CLEAN_LINE" "$CHECK_LOG"; then
	echo "--- Замечания CheckConfig ($CHECK_LOG):"
	cat "$CHECK_LOG"
	FAILED=1
	# Признак ошибки компиляции модуля: платформа печатает позицию вида
	# {ОбщийМодуль.Имя.Модуль(859,37)} или {Документ.Имя.Форма.Имя.Форма(12,3)}.
	# Сообщения локализованы, а такая позиция — нет, поэтому ловим именно её.
	if grep -qE '\{[^}]*Модуль[^}]*\([0-9]+,[0-9]+\)\}|\{[^}]*Форма[^}]*\([0-9]+,[0-9]+\)\}' "$CHECK_LOG"; then
		COMPILE_ERROR=1
	fi
else
	echo "CheckConfig: ошибок нет"
fi

if [ "$COMPILE_ERROR" -ne 0 ]; then
	echo "Есть ошибки компиляции модулей — шаг 2 пропущен: клиент с ними не запустится."
	echo "ТЕСТЫ НЕ ПРОЙДЕНЫ"
	exit 1
fi

echo "== Шаг 2. Смок-тест «открыть все формы» =="
# Тонкий клиент обязателен: толстый компилирует общие модули «Сервер + Вызов
# сервера» дважды и падает на старте («функция уже определена»).
V8C="${V8_DIR}/1cv8c"
rm -f "$REPORT" "$CLIENT_LOG"
"$V8C" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /C "СмокТест;$REPORT" \
	"${V8_BATCH[@]}" /Out "$CLIENT_LOG" || true
if ! wait_client_start "СмокТест;$REPORT" "$REPORT"; then
	echo "Клиент не стартовал за ${START_TIMEOUT}с (нет строки СТАРТ в $REPORT) — процесс снят."
	echo "Клиентский лог: $CLIENT_LOG"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	echo "ТЕСТЫ НЕ ПРОЙДЕНЫ"
	exit 1
fi

if wait_report_mark "СмокТест;$REPORT" "$REPORT" "ИТОГ;"; then
	grep 'ИТОГ;' "$REPORT"
	SKIPPED=$(grep -c 'ПРОПУСК;' "$REPORT" || true)
	EMPTY=$(grep -c 'ПУСТО;' "$REPORT" || true)
	SUSPECT=$(grep -c 'ПОДОЗРЕНИЕ;' "$REPORT" || true)
	echo "Пропущено проверок: ${SKIPPED:-0}; пустых печатных форм: ${EMPTY:-0} (подробности в $REPORT)"
	if [ "${SUSPECT:-0}" -ne 0 ]; then
		# Не ошибка прогона: печатная форма сформировалась, но номера документа в ней нет.
		echo "--- Печатные формы под подозрением (смотреть глазами):"
		grep 'ПОДОЗРЕНИЕ;' "$REPORT"
	fi
	if grep -q 'ОШИБКА;' "$REPORT"; then
		echo "--- Ошибки прогона ($REPORT):"
		grep 'ОШИБКА;' "$REPORT"
		FAILED=1
	fi
else
	echo "Смок-тест не отработал: нет строки ИТОГ в $REPORT (клиентский лог: $CLIENT_LOG)"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	FAILED=1
fi

if [ "$FAILED" -ne 0 ]; then
	echo "ТЕСТЫ НЕ ПРОЙДЕНЫ"
	exit 1
fi
echo "ТЕСТЫ ПРОЙДЕНЫ"
