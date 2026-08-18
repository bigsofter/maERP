#!/usr/bin/env bash
# Загружает CF в базу и обновляет конфигурацию базы данных.
# Использование: scripts/cf-load.sh <файл.cf> [каталог-базы]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

CF="${1:?Укажи путь к .cf}"
IB="${2:-$IB_BUILD}"
LOG="$BUILD/cf-load.log"

"$V8" DESIGNER /F "$IB" /LoadCfg "$CF" /UpdateDBCfg "${V8_BATCH[@]}" /Out "$LOG"
cat "$LOG"
echo "CF загружен в базу: $IB"
