#!/usr/bin/env bash
# Начальное заполнение базы без интерфейса: организация, пользователи и служебный
# администратор из JSON (обработка НачальноеЗаполнение) - вместо визарда первого запуска.
# Использование: scripts/initial-fill.sh <каталог-базы> <payload.json> [result.json]
#   result.json по умолчанию - build/initial-fill-result.json, отчёт хода -
#   build/initial-fill-report.txt. Формат payload и result - docs/DEPLOY.md,
#   образец payload - scripts/initial-fill.example.json.
#
# ВНИМАНИЕ: скрипт ЗАПИСЫВАЕТ данные. Повторный запуск на заполненной базе ничего не
# создаёт второй раз (организация ищется по наименованию, пользователи - по логину).
#
# Пароли пользователей лежат только в payload-файле: сделай ему права 600 и удали после
# запуска. В аргументы 1cv8, в отчёт, в result-файл и в логи пароли не попадают.
# Доступ к базе, где пользователи уже есть: переменные окружения SMOKE_USER и SMOKE_PWD.
#
# Это dev-обёртка для macOS; серверный initial-fill.sh для раннера хаба пишется по ней
# (контракт скрипта раннера - план хаба, §5.4) и живёт на 1С-сервере вне git.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
source "$(dirname "${BASH_SOURCE[0]}")/run-lib.sh"

IB="${1:?Укажи каталог базы}"
PAYLOAD="${2:?Укажи payload.json}"
RESULT="${3:-$BUILD/initial-fill-result.json}"
REPORT="${INITIAL_FILL_REPORT:-$BUILD/initial-fill-report.txt}"
CLIENT_LOG="$BUILD/initial-fill-client.log"
TIMEOUT="${SMOKE_TIMEOUT:-600}"
START_TIMEOUT="${SMOKE_START_TIMEOUT:-120}"

[ -f "$PAYLOAD" ] || { echo "Нет payload-файла: $PAYLOAD" >&2; exit 1; }
# 1С получает пути как есть, рабочий каталог клиента неизвестен - только абсолютные.
PAYLOAD="$(cd "$(dirname "$PAYLOAD")" && pwd)/$(basename "$PAYLOAD")"
mkdir -p "$(dirname "$RESULT")" "$(dirname "$REPORT")"
RESULT="$(cd "$(dirname "$RESULT")" && pwd)/$(basename "$RESULT")"
REPORT="$(cd "$(dirname "$REPORT")" && pwd)/$(basename "$REPORT")"
case "$PAYLOAD$RESULT$REPORT" in *';'*) echo "Пути не могут содержать «;»: это разделитель параметра запуска" >&2; exit 1;; esac

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

echo "== Начальное заполнение =="
echo "База: $IB"
echo "Payload: $PAYLOAD"

# Тонкий клиент обязателен: толстый компилирует общие модули «Сервер + Вызов сервера»
# дважды и падает на старте (scripts/smoke.sh).
V8C="${V8_DIR}/1cv8c"
PARAM="НачальноеЗаполнение;$PAYLOAD;$RESULT;$REPORT"
rm -f "$RESULT" "$REPORT" "$CLIENT_LOG"
"$V8C" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /C "$PARAM" \
	"${V8_BATCH[@]}" /Out "$CLIENT_LOG" || true

if ! wait_client_start "$PARAM" "$REPORT"; then
	echo "Клиент не стартовал за ${START_TIMEOUT}с (нет строки СТАРТ в $REPORT) — процесс снят."
	echo "Клиентский лог: $CLIENT_LOG"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	exit 1
fi

if ! wait_report_mark "$PARAM" "$REPORT" "ИТОГ;"; then
	echo "Заполнение не отработало: нет строки ИТОГ в $REPORT (клиентский лог: $CLIENT_LOG)"
	[ -f "$CLIENT_LOG" ] && cat "$CLIENT_LOG"
	exit 1
fi

grep 'ИТОГ;' "$REPORT"
if grep -q 'ПРЕДУПРЕЖДЕНИЕ;' "$REPORT"; then
	echo "--- Значения payload, заменённые умолчанием:"
	grep 'ПРЕДУПРЕЖДЕНИЕ;' "$REPORT"
fi
if grep -q 'ОШИБКА;' "$REPORT"; then
	echo "--- Ошибки ($REPORT):"
	grep 'ОШИБКА;' "$REPORT"
fi
if ! grep -q 'ИТОГ;Успех=1' "$REPORT" || [ ! -s "$RESULT" ]; then
	echo "ЗАПОЛНЕНИЕ НЕ ВЫПОЛНЕНО"
	exit 1
fi
echo "Результат: $RESULT"
cat "$RESULT"
echo
echo "ЗАПОЛНЕНИЕ ВЫПОЛНЕНО"
