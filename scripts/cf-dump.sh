#!/usr/bin/env bash
# Выгружает конфигурацию из базы в файл CF.
# Использование: scripts/cf-dump.sh [каталог-базы] [выходной.cf]
# База с пользователями — логин из SMOKE_USER/SMOKE_PWD (как у остальных скриптов).
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

IB="${1:-$IB_BUILD}"
OUT="${2:-$DIST/maERP.cf}"
LOG="$BUILD/cf-dump.log"

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

mkdir -p "$(dirname "$OUT")"
"$V8" DESIGNER /F "$IB" ${AUTH[@]+"${AUTH[@]}"} /DumpCfg "$OUT" "${V8_BATCH[@]}" /Out "$LOG"
cat "$LOG"
echo "CF выгружен: $OUT"
