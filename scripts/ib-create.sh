#!/usr/bin/env bash
# Создаёт чистую файловую базу и загружает в неё CF.
# Использование: scripts/ib-create.sh <путь-к.cf> [каталог-базы]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

CF="${1:?Укажи путь к .cf}"
IB="${2:-$IB_BUILD}"
LOG="$BUILD/ib-create.log"

[ -f "$CF" ] || { echo "Нет файла: $CF" >&2; exit 1; }
rm -rf "$IB"; mkdir -p "$IB"

"$V8" CREATEINFOBASE "File=\"$IB\";" /UseTemplate "$CF" "${V8_BATCH[@]}" /Out "$LOG"
cat "$LOG"
echo "База создана: $IB"
