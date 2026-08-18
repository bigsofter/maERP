#!/usr/bin/env bash
# Выгружает конфигурацию из базы в файл CF.
# Использование: scripts/cf-dump.sh [каталог-базы] [выходной.cf]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

IB="${1:-$IB_BUILD}"
OUT="${2:-$DIST/maERP.cf}"
LOG="$BUILD/cf-dump.log"

mkdir -p "$(dirname "$OUT")"
"$V8" DESIGNER /F "$IB" /DumpCfg "$OUT" "${V8_BATCH[@]}" /Out "$LOG"
cat "$LOG"
echo "CF выгружен: $OUT"
