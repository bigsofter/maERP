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

# В ВМ (scripts/vm-gate.sh) EDT нет: выгрузку делает хост, здесь только сверка, что она от текущего дерева src/cf.
if [ "${IB_SYNC_XML_READY:-}" = 1 ]; then
	echo "== 1/2. Выгрузка EDT сделана на хосте - сверка отпечатка =="
	TREE="$("$(dirname "${BASH_SOURCE[0]}")/srchash.sh")"
	if [ "$(cat "$XML_OUT/.srchash" 2>/dev/null)" != "$TREE" ]; then
		echo "Выгрузка $XML_OUT не от текущего дерева src/cf ($TREE) - запустить scripts/vm-gate.sh заново" >&2
		exit 1
	fi
	if [ "$(cat "$XML_OUT/.xmlsum" 2>/dev/null)" != "$("$(dirname "${BASH_SOURCE[0]}")/xmlsum.sh")" ]; then
		echo "Выгрузка $XML_OUT в ВМ не совпадает с выгрузкой хоста по сумме файлов - кэш общей папки" >&2
		exit 1
	fi
else
	echo "== 1/2. Выгрузка EDT-проекта в XML =="
	"$(dirname "${BASH_SOURCE[0]}")/edt-export.sh" || exit 1
fi

echo "== 2/2. Загрузка XML в базу и применение к данным =="
"$(dirname "${BASH_SOURCE[0]}")/xml-load.sh" "$XML_OUT" "$IB" || exit 1

echo "База синхронизирована с src/cf: $IB"
echo "Дальше — scripts/smoke.sh и scripts/doctests.sh."
