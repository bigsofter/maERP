#!/usr/bin/env bash
# Автотесты на базе: проверка конфигурации (DESIGNER /CheckConfig) и дымовой
# прогон «открыть все формы» (обработка СмокТест, запуск через /C).
# Использование: scripts/smoke.sh [каталог-базы]        (по умолчанию build/ib)
# Доступ к базе с пользователями: переменные окружения SMOKE_USER и SMOKE_PWD —
# пароль передаётся только так, в файлы и логи не попадает.
# Регламент и разбор ошибок: docs/TESTING.md.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

IB="${1:-$IB_BUILD}"
CHECK_LOG="$BUILD/check-config.log"
REPORT="$BUILD/smoke-report.txt"
CLIENT_LOG="$BUILD/smoke-client.log"
TIMEOUT="${SMOKE_TIMEOUT:-900}"   # секунд на каждый шаг

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

FAILED=0

# 1cv8 на macOS: процесс-обёртка может упасть сразу (134/139), работу делает
# дочерний процесс. Поэтому код возврата 1cv8 не используется: ждём завершения
# процессов по паттерну командной строки и читаем файлы результатов.

wait_process_end() { # $1 — паттерн командной строки процесса
	local elapsed=0
	sleep 2
	while pgrep -f "$1" >/dev/null; do
		if [ "$elapsed" -ge "$TIMEOUT" ]; then
			pkill -f "$1" 2>/dev/null || true
			return 1
		fi
		sleep 5; elapsed=$((elapsed + 5))
	done
	sleep 2
	return 0
}

wait_report_mark() { # $1 — паттерн процесса, $2 — файл отчёта, $3 — строка-признак завершения
	local elapsed=0
	while [ "$elapsed" -lt "$TIMEOUT" ]; do
		if [ -f "$2" ] && grep -q "$3" "$2"; then
			return 0
		fi
		if ! pgrep -f "$1" >/dev/null; then
			sleep 3
			[ -f "$2" ] && grep -q "$3" "$2"
			return $?
		fi
		sleep 5; elapsed=$((elapsed + 5))
	done
	pkill -f "$1" 2>/dev/null || true
	return 1
}

echo "== Шаг 1. Проверка конфигурации (CheckConfig) =="
rm -f "$CHECK_LOG"
"$V8" DESIGNER /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /CheckConfig \
	-ConfigLogIntegrity -IncorrectReferences -ThinClient -Server \
	"${V8_BATCH[@]}" /Out "$CHECK_LOG" || true
wait_process_end "CheckConfig" || { echo "CheckConfig не завершился за ${TIMEOUT}с — процесс снят"; FAILED=1; }
if [ -s "$CHECK_LOG" ] && grep -qvE '^[[:space:]]*$' "$CHECK_LOG"; then
	echo "--- Замечания CheckConfig ($CHECK_LOG):"
	cat "$CHECK_LOG"
	FAILED=1
else
	echo "CheckConfig: ошибок нет"
fi

echo "== Шаг 2. Смок-тест «открыть все формы» =="
# Тонкий клиент обязателен: толстый компилирует общие модули «Сервер + Вызов
# сервера» дважды и падает на старте («функция уже определена»).
V8C="${V8_DIR}/1cv8c"
rm -f "$REPORT" "$CLIENT_LOG"
"$V8C" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /C "СмокТест;$REPORT" \
	"${V8_BATCH[@]}" /Out "$CLIENT_LOG" || true
if wait_report_mark "СмокТест;$REPORT" "$REPORT" "^ИТОГ;"; then
	grep '^ИТОГ;' "$REPORT"
	if grep -q '^ОШИБКА;' "$REPORT"; then
		echo "--- Ошибки открытия форм ($REPORT):"
		grep '^ОШИБКА;' "$REPORT"
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
