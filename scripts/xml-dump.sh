#!/usr/bin/env bash
# Выгружает конфигурацию из базы в XML-файлы формата конфигуратора.
# Нужно, когда правки делались в конфигураторе и их надо втянуть обратно в EDT.
# Использование: scripts/xml-dump.sh [каталог-базы] [каталог-выгрузки]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

IB="${1:-$IB_BUILD}"
OUT="${2:-$XML_OUT}"
LOG="$BUILD/xml-dump.log"

rm -rf "$OUT"; mkdir -p "$OUT"
"$V8" DESIGNER /F "$IB" /DumpConfigToFiles "$OUT" -Format Hierarchical "${V8_BATCH[@]}" /Out "$LOG"
cat "$LOG"
echo "XML-выгрузка: $OUT"
