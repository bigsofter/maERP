#!/usr/bin/env bash
# Разворачивает базу из выгрузки .dt (конфигурация вместе с данными).
# Использование: scripts/ib-restore.sh <файл.dt> [каталог-базы]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

DT="${1:?Укажи путь к .dt}"
IB="${2:-$IB_BUILD}"
LOCALE="${IB_LOCALE:-ru}"

[ -f "$DT" ] || { echo "Нет файла: $DT" >&2; exit 1; }
rm -rf "$IB"; mkdir -p "$IB"

"$V8" CREATEINFOBASE "File=\"$IB\";Locale=\"$LOCALE\";" "${V8_BATCH[@]}" /Out "$BUILD/ib-create.log"
cat "$BUILD/ib-create.log"

"$V8" DESIGNER /F "$IB" /RestoreIB "$DT" "${V8_BATCH[@]}" /Out "$BUILD/ib-restore.log" -NoTruncate
cat "$BUILD/ib-restore.log"
echo "База развёрнута из $DT: $IB"
