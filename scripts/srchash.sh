#!/usr/bin/env bash
# Отпечаток состояния src/cf: хэш git-дерева каталога.
# Использование: scripts/srchash.sh            рабочее дерево (с незакоммиченными и новыми файлами)
#                scripts/srchash.sh --staged   то, что уйдёт в коммит (индекс)
#
# Зачем: гейт базы (scripts/gate.sh) записывает отпечаток проверенного дерева в build/gate-stamps.txt,
# а хук коммита сборки и отправка в хаб сверяют с ним то, что сдаётся. Правка src/cf после прогона
# меняет отпечаток - штамп перестаёт подходить, и сборка без повторного гейта не уходит.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
if [ "${1:-}" = "--staged" ]; then
	git write-tree --prefix=src/cf/
	exit 0
fi
TMP_INDEX="$(mktemp)"
trap 'rm -f "$TMP_INDEX"' EXIT
cp "$(git rev-parse --git-dir)/index" "$TMP_INDEX"
GIT_INDEX_FILE="$TMP_INDEX" git add -A src/cf >/dev/null
GIT_INDEX_FILE="$TMP_INDEX" git write-tree --prefix=src/cf/
