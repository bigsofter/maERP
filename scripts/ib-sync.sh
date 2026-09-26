#!/usr/bin/env bash
# Обновляет базу сборки из EDT-проекта одной командой: src/cf -> XML -> база (с применением).
# Использование: scripts/ib-sync.sh [каталог-базы]
#
# Зачем: до 2026-09-20 обновить build/ib мог только владелец через IDE, и каждая правка кода
# стоила круга «попроси обновить базу». Цепочка headless работает при двух условиях:
#  1. x86_64-JDK 17+ для 1cedtcli (EDT_JAVA_HOME, см. env.sh) — arm64 не подходит;
#  2. IDE закрыта либо открыта на ДРУГОЙ рабочей области: Eclipse держит свою эксклюзивно,
#     а конфигуратор не может захватить базу, открытую в Designer.
#
# Время: экспорт ~4 мин, загрузка с применением ~2 мин.
set -u
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

IB="${1:-$IB_BUILD}"

echo "== 1/2. Выгрузка EDT-проекта в XML =="
"$(dirname "${BASH_SOURCE[0]}")/edt-export.sh" || exit 1

echo "== 2/2. Загрузка XML в базу и применение к данным =="
"$(dirname "${BASH_SOURCE[0]}")/xml-load.sh" "$XML_OUT" "$IB" || exit 1

echo "База синхронизирована с src/cf: $IB"
echo "Дальше — scripts/smoke.sh и scripts/doctests.sh."
