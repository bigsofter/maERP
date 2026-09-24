#!/usr/bin/env bash
# Открывает одну форму в живом клиенте и снимает экран.
# Использование: scripts/openform.sh <полное имя формы> [каталог-базы] [файл-снимка]
#   scripts/openform.sh Документ.ПоступлениеТоваровУслуг.Форма.ФормаСписка
#
# Зачем: смок открывает формы через ПолучитьФорму - это только серверная часть. Ошибки,
# которые видны лишь при запросе данных (динамические списки, условное оформление),
# проходят мимо него, и владелец ловит их руками. Здесь клиент поднимается по-настоящему,
# форма открывается параметром /C "ОткрытьФорму;<имя>" (АвтотестыКлиент.ОбработатьЗапускТеста),
# через OPENFORM_WAIT секунд снимается экран, клиент снимается.
#
# Снимок - в build/openform.png (в git не попадает). Ошибка формы видна на нём диалогом.
# Доступ к базе с пользователями - переменные SMOKE_USER и SMOKE_PWD, как в scripts/smoke.sh.
set -u
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

FORM="${1:-}"
[ -n "$FORM" ] || { echo "Не указано имя формы: scripts/openform.sh <полное имя формы>" >&2; exit 1; }
IB="${2:-$IB_BUILD}"
SHOT="${3:-$BUILD/openform.png}"
WAIT="${OPENFORM_WAIT:-30}"
V8C="${V8_DIR}/1cv8c"

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

rm -f "$SHOT"
echo "== Клиент открывает форму: $FORM =="
"$V8C" ENTERPRISE /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /C "ОткрытьФорму;$FORM" \
	"${V8_BATCH[@]}" &
CLIENT_PID=$!

sleep "$WAIT"

# Клиент стартует в фоне и окно не поднимает: без этого снимок покажет чужое окно,
# а не форму. Поднимаем именно процесс клиента (1cv8c), конфигуратор рядом не трогаем.
osascript -e 'tell application "System Events" to set frontmost of (first process whose name is "1cv8c") to true' 2>/dev/null || true
sleep 2
screencapture -x "$SHOT"

# Снимается именно свой процесс клиента: шаблон по подстроке цепляет чужие 1С (урок workflow-008).
kill "$CLIENT_PID" 2>/dev/null || true
wait "$CLIENT_PID" 2>/dev/null || true

[ -f "$SHOT" ] && echo "Снимок: $SHOT" || { echo "Снимок не сделан" >&2; exit 1; }
