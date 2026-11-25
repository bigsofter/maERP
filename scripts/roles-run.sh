#!/usr/bin/env bash
# Прогон тестов интерфейса под наборами ролей на свежей копии базы гейта (сценарии под ролью пишут в базу - сама база
# гейта остаётся чистой). Идёт в ВМ: scripts/vm-gate.sh -- bash scripts/roles-run.sh <журнал> "<наборы>" [сценарии].
# Стартовый диалог лицензии разработчика у тест-клиента под ролью закрывается Enter - один раз на процесс (окно отказа
# программы с тем же заголовком появляется позже, его читает сценарий).
#
# Использование: scripts/roles-run.sh <журнал> "<Набор1> <Набор2>..." [файл сценариев под ролью]
#   ROLES_IB   - копия базы (по умолчанию <база гейта>/../ib-roles), ROLES_KEEP=1 - не обновлять копию.
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
LOG="$1"; SETS="$2"; SCEN="${3:-}"
GATE_IB="${GATE_IB:-$ROOT/build/ib-gate}"
IBR="${ROLES_IB:-$(dirname "$GATE_IB")/ib-roles}"
[ -n "$SCEN" ] && export UITEST_ROLE_SCENARIOS="$SCEN"
# Тест-клиент под ролью изредка не подключается («нет соединения с тест-клиентом») - сбой запуска, а не программы:
# такой прогон повторяется целиком на свежей копии базы, один раз.
for ATTEMPT in 1 2; do
if [ -z "${ROLES_KEEP:-}" ]; then mkdir -p "$IBR"; cp "$GATE_IB/1Cv8.1CD" "$IBR/1Cv8.1CD" || exit 1; fi
UITEST_ALL_ROLES="Администратор $SETS" UITEST_ROLES="$SETS" bash scripts/uitest.sh "$IBR" > "$LOG" 2>&1 &
MAIN=$!
PRESSED=""
while kill -0 $MAIN 2>/dev/null; do
	sleep 6
	for pid in $(pgrep -f "1cv8c.*TESTCLIENT" || true); do
		case " $PRESSED " in *" $pid "*) continue;; esac
		WIN=$(build/uitest/wins 2>/dev/null | awk -v p="$pid" '$2==p && $6==1' | grep "1C:Enterprise$" | awk 'NR==1{print $1}')
		if [ -n "$WIN" ]; then
			PRESSED="$PRESSED $pid"
			# Нажатие изредка теряется (баннер уведомления macOS перехватывает фокус) - диалог остаётся, главное окно
			# не появляется. Повтор - только пока на экране то же окно диалога (номер окна): у окон отказа программы
			# тот же заголовок, их Enter нажимать нельзя.
			for TRY in 1 2 3; do
				osascript -e "tell application \"System Events\" to set frontmost of (first process whose unix id is $pid) to true" 2>/dev/null
				sleep 1
				osascript -e 'tell application "System Events" to key code 36' 2>/dev/null
				echo "$(date +%H:%M:%S) Enter на диалоге лицензии, pid $pid, попытка $TRY" >> "$LOG.enter"
				sleep 8
				build/uitest/wins 2>/dev/null | awk -v p="$pid" -v w="$WIN" '$1==w && $2==p' | grep -q "1C:Enterprise$" || break
			done
		fi
	done
done
wait $MAIN
RC=$?
echo "rc=$RC" >> "$LOG"
grep -q "нет соединения с тест-клиентом" build/uitest-report.txt || break
[ "$ATTEMPT" = 1 ] && echo "$(date +%H:%M:%S) тест-клиент не подключился - повтор прогона" >> "$LOG.enter"
done
grep "^ОШИБКА\|^ИТОГ" build/uitest-report.txt | cut -c1-400
exit $RC
