#!/usr/bin/env bash
# Загружает XML-выгрузку конфигурации в базу. Звено сборочной цепочки EDT -> CF.
# Использование: scripts/xml-load.sh [каталог-выгрузки] [каталог-базы]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

IN="${1:-$XML_OUT}"
IB="${2:-$IB_BUILD}"
LOG="$BUILD/xml-load.log"

[ -d "$IN" ] || { echo "Нет каталога выгрузки: $IN" >&2; exit 1; }
"$V8" DESIGNER /F "$IB" /LoadConfigFromFiles "$IN" -Format Hierarchical "${V8_BATCH[@]}" /Out "$LOG"
cat "$LOG"
echo "XML загружен в базу: $IB"
