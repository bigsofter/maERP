#!/bin/bash
# Run a heavy command (render / snapshot batch) in one of N shared CPU slots.
# Several episodes are produced in parallel on one machine; headless Chrome renders
# saturate all cores, so at most $SLOTS run at once — the others wait here.
# usage: ../tools/render_slot.sh ./render.sh [langs]      (from an episode folder)
#
# Watchdog: a command holding a slot longer than $SLOT_MAX seconds (default 1500 = 25 min;
# a 4-language render takes ~8–10 min) is stopped together with its own children — on
# 2026-10-03 two hung snapshot jobs held both slots for 7 hours and froze every session.
# Only the process tree THIS script started is touched, never anyone else's.
SLOTS=${RENDER_SLOTS:-2}
SLOT_MAX=${SLOT_MAX:-1500}
LOCKDIR=/tmp/matransports-render-slots
mkdir -p "$LOCKDIR"

kill_tree() {   # $1 = pid; children first
  local c
  for c in $(pgrep -P "$1" 2>/dev/null); do kill_tree "$c"; done
  kill -TERM "$1" 2>/dev/null
}

while true; do
  for i in $(seq 1 "$SLOTS"); do
    if mkdir "$LOCKDIR/slot$i" 2>/dev/null; then
      echo "$$ $(date +%s) $(pwd)" > "$LOCKDIR/slot$i/owner"
      trap 'rm -rf "$LOCKDIR/slot'"$i"'"' EXIT INT TERM
      echo "[render_slot] slot $i acquired $(date +%H:%M:%S)"
      "$@" &
      child=$!
      start=$(date +%s)
      while kill -0 "$child" 2>/dev/null; do
        if [ $(( $(date +%s) - start )) -gt "$SLOT_MAX" ]; then
          echo "[render_slot] TIMEOUT after ${SLOT_MAX}s — stopping: $*" >&2
          kill_tree "$child"; sleep 5; kill -KILL "$child" 2>/dev/null
          wait "$child" 2>/dev/null
          exit 124
        fi
        sleep 5
      done
      wait "$child"
      exit $?
    fi
    # stale slot: owner process gone, or older than SLOT_MAX + 5 min (a watchdog that itself died)
    pid= ; since=
    read -r pid since _ < "$LOCKDIR/slot$i/owner" 2>/dev/null
    case "$since" in *[!0-9]*|'') since= ;; esac   # old-format owner line: no timestamp → no age check
    if [ -n "$pid" ]; then
      if ! kill -0 "$pid" 2>/dev/null; then
        rm -rf "$LOCKDIR/slot$i"
      elif [ -n "$since" ] && [ $(( $(date +%s) - since )) -gt $(( SLOT_MAX + 300 )) ]; then
        rm -rf "$LOCKDIR/slot$i"
      fi
    fi
  done
  sleep 10
done
