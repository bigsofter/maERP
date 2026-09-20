#!/usr/bin/env bash
# Загружает XML-выгрузку конфигурации в базу И ПРИМЕНЯЕТ её к данным (/UpdateDBCfg).
# Звено сборочной цепочки EDT -> CF.
# Использование: scripts/xml-load.sh [каталог-выгрузки] [каталог-базы]
#
# Без /UpdateDBCfg база остаётся со старой структурой данных: конфигурация загружена,
# но не применена, и тесты гоняют прежние таблицы. Раньше этот шаг делал только cf-load.sh,
# поэтому цепочка «EDT -> XML -> база» молча давала базу прошлой сборки.
#
# Доступ к базе с пользователями: SMOKE_USER и SMOKE_PWD, как в smoke.sh. Без них
# конфигуратор отвечает «Пользователь ИБ не опознан» и шаг падает.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

IN="${1:-$XML_OUT}"
IB="${2:-$IB_BUILD}"
LOG="$BUILD/xml-load.log"

AUTH=()
[ -n "${SMOKE_USER:-}" ] && AUTH+=(/N "$SMOKE_USER")
[ -n "${SMOKE_PWD:-}" ] && AUTH+=(/P "$SMOKE_PWD")

[ -d "$IN" ] || { echo "Нет каталога выгрузки: $IN" >&2; exit 1; }

"$V8" DESIGNER /F "$IB" "${AUTH[@]}" \
  /LoadConfigFromFiles "$IN" -Format Hierarchical -UpdateDBCfg \
  "${V8_BATCH[@]}" /Out "$LOG"
RC=$?
cat "$LOG"
if [ $RC -ne 0 ]; then
  echo "Загрузка XML в базу не удалась (rc=$RC): $IB" >&2
  exit 1
fi
echo "XML загружен и применён к базе: $IB"
