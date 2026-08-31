#!/usr/bin/env bash
# Ожидание клиента и отчёта при headless-запуске 1С. Общая часть scripts/smoke.sh
# и scripts/fixtures.sh.
#
# 1cv8 на macOS: процесс-обёртка может упасть сразу (134/139), работу делает
# дочерний процесс. Поэтому код возврата 1cv8 не используется: ждём завершения
# процессов по паттерну командной строки и читаем файлы результатов.
#
# Вызывающий скрипт задаёт TIMEOUT (секунд на шаг) и START_TIMEOUT (секунд на старт клиента).

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

wait_client_start() { # $1 — паттерн процесса, $2 — файл отчёта
	# Обработка пишет строку «СТАРТ;» до начала работы. Нет её за START_TIMEOUT —
	# значит клиент не поднялся (ошибка компиляции, диалог на старте, не та база).
	# Живость процесса тут не проверяем: обёртка 1cv8c на macOS отдаёт работу дочернему
	# процессу с другой командной строкой, и pgrep по паттерну запуска его не находит.
	# Строку ИТОГ ищем на случай, если короткий прогон успел переписать отчёт целиком.
	local elapsed=0
	while [ "$elapsed" -lt "$START_TIMEOUT" ]; do
		# Без якоря ^: 1С пишет отчёт с BOM, и он стоит перед первой строкой.
		if [ -f "$2" ] && grep -qE 'СТАРТ;|ИТОГ;' "$2"; then
			return 0
		fi
		sleep 3; elapsed=$((elapsed + 3))
	done
	pkill -f "$1" 2>/dev/null || true
	return 1
}

# Отчёт 1С пишется с BOM, и он стоит перед первой строкой: якорь ^ в шаблонах grep
# по отчёту не используется, иначе первая строка отчёта теряется.
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
