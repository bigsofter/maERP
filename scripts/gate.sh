#!/usr/bin/env bash
# Гейт базы одной командой: src/cf -> отдельная база гейта -> CheckConfig, смок, тесты документов -> штамп.
# Использование: scripts/gate.sh            полный прогон
#                scripts/gate.sh --check    только ответить, есть ли штамп PASS на текущее дерево src/cf
#
# Зачем (разбор качества 2026-11-21): из 204 финальных проверок 185 шли без тестов на базе - build/ib
# обновляет из EDT владелец, и она занята IDE. Сборки уходили на тест со статикой и вердиктом
# «ALL GATES PASSED». У гейта своя база build/ib-gate: её не открывает никто, кроме этого скрипта,
# поэтому прогон не зависит ни от владельца, ни от EDT.
#
# База гейта создаётся копией GATE_IB_SOURCE (по умолчанию build/ib-kp, иначе build/ib) при первом запуске.
# Порог смока и тестов - scripts/smoke-floor.txt: меньше проверок, чем записано, или пропущенный сценарий -
# провал, а не «пройдено» (20.11 смок дал 0 клиентских проверок при 100 пропусках и остался зелёным).
#
# Итог - строка в build/gate-stamps.txt: результат, отпечаток src/cf (scripts/srchash.sh), версия, время.
# Время: выгрузка ~4 мин, загрузка ~2 мин, CheckConfig ~4 мин, смок до 20 мин, тесты документов ~20 мин.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"
set +e
SCRIPTS="$(dirname "${BASH_SOURCE[0]}")"
GATE_IB="${GATE_IB:-$BUILD/ib-gate}"
STAMPS="$BUILD/gate-stamps.txt"
LOG_DIR="$BUILD/gate"
mkdir -p "$LOG_DIR"

version() { sed -n 's:.*<version>\(.*\)</version>.*:\1:p' "$SRC_CF/src/Configuration/Configuration.mdo" | head -1; }

if [ "${1:-}" = "--check" ]; then
	TREE="$("$SCRIPTS/srchash.sh")"
	if grep -q "^PASS $TREE " "$STAMPS" 2>/dev/null; then
		grep "^PASS $TREE " "$STAMPS" | tail -1
		exit 0
	fi
	echo "Штампа гейта базы на текущее дерево src/cf нет ($TREE) - нужен scripts/gate.sh"
	exit 1
fi

if [ -z "${SMOKE_USER:-}" ] || [ -z "${SMOKE_PWD:-}" ]; then
	echo "SMOKE_USER/SMOKE_PWD не заданы - база не пустит" >&2
	exit 1
fi

if [ ! -f "$GATE_IB/1Cv8.1CD" ]; then
	SRC_IB="${GATE_IB_SOURCE:-}"
	if [ -z "$SRC_IB" ]; then
		if [ -f "$BUILD/ib-kp/1Cv8.1CD" ]; then SRC_IB="$BUILD/ib-kp"; else SRC_IB="$IB_BUILD"; fi
	fi
	echo "== База гейта не найдена - создаю копией $SRC_IB =="
	mkdir -p "$GATE_IB"
	cp "$SRC_IB/1Cv8.1CD" "$GATE_IB/1Cv8.1CD" || { echo "Не удалось скопировать базу" >&2; exit 1; }
fi

TREE_BEFORE="$("$SCRIPTS/srchash.sh")"
VERSION="$(version)"
echo "== Гейт базы: версия $VERSION, дерево $TREE_BEFORE, база $GATE_IB =="

RESULT=PASS
NOTE=""
fail() { RESULT=FAIL; NOTE="${NOTE:+$NOTE; }$1"; echo "ПРОВАЛ: $1"; }

# Выгрузка EDT иногда падает на гонке (память edt-export-race) - один повтор.
SYNC_OK=0
for attempt in 1 2; do
	echo "== Синхронизация базы, попытка $attempt =="
	if bash "$SCRIPTS/ib-sync.sh" "$GATE_IB" > "$LOG_DIR/sync-$attempt.log" 2>&1; then SYNC_OK=1; break; fi
	tail -15 "$LOG_DIR/sync-$attempt.log"
done
[ "$SYNC_OK" -eq 1 ] || fail "база не синхронизирована с src/cf (журнал $LOG_DIR/sync-*.log)"

if [ "$RESULT" = PASS ]; then
	export SMOKE_START_TIMEOUT="${SMOKE_START_TIMEOUT:-600}"
	echo "== Смок =="
	# Код 141 без строк в журнале - SIGPIPE на старте клиента, не результат: один повтор.
	for attempt in 1 2; do
		SMOKE_FLOOR=1 bash "$SCRIPTS/smoke.sh" "$GATE_IB" > "$LOG_DIR/smoke.log" 2>&1; RC=$?
		[ "$RC" -ne 141 ] && break
	done
	tail -25 "$LOG_DIR/smoke.log"
	[ "$RC" -eq 0 ] || fail "смок (журнал $LOG_DIR/smoke.log)"

	echo "== Тесты документов =="
	for attempt in 1 2; do
		SMOKE_FLOOR=1 bash "$SCRIPTS/doctests.sh" "$GATE_IB" > "$LOG_DIR/doctests.log" 2>&1; RC=$?
		[ "$RC" -ne 141 ] && break
	done
	grep -a 'ИТОГ;\|ОШИБКА;\|ПРОПУСК;\|ТЕСТЫ\|ПОРОГ' "$LOG_DIR/doctests.log" | tail -30
	[ "$RC" -eq 0 ] || fail "тесты документов (журнал $LOG_DIR/doctests.log)"
fi

TREE_AFTER="$("$SCRIPTS/srchash.sh")"
if [ "$TREE_AFTER" != "$TREE_BEFORE" ]; then
	fail "src/cf менялся во время прогона ($TREE_BEFORE -> $TREE_AFTER): проверена смесь, прогон повторить"
fi

echo "$RESULT $TREE_BEFORE $VERSION $(date '+%Y-%m-%dT%H:%M:%S')${NOTE:+ $NOTE}" >> "$STAMPS"
if [ "$RESULT" = PASS ]; then
	echo "ГЕЙТ БАЗЫ ПРОЙДЕН: версия $VERSION, дерево $TREE_BEFORE"
	exit 0
fi
echo "ГЕЙТ БАЗЫ НЕ ПРОЙДЕН: $NOTE"
exit 1
