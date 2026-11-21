#!/usr/bin/env bash
# Сверка неслитых веток: в какой ветке лежат правки конфигурации, которых нет в проверяемом состоянии.
# Использование: scripts/branchcheck.sh [ревизия]     (по умолчанию HEAD)
#
# Зачем: сборки 2.0.17.30 и 2.0.17.31 были переданы на тест из отдельных веток, тикет закрыт, записи ушли в
# историю релизов - а в develop их не слили, и релиз 2.0.17.48 вышел без них (найдено 2026-11-21).
# Запускать перед каждой передачей на тест и перед тегом релиза (docs/RELEASING.md).
#
# Что считается расхождением: локальная или удалённая ветка, у которой есть коммиты с правками src/cf,
# не входящие в проверяемую ревизию. Коммит, перенесённый без изменений (cherry-pick), не считается.
# Перенос с правками git не распознаёт: такую ветку удаляют после слияния либо записывают в
# scripts/branchcheck-known.txt строкой «<ветка> <хеш вершины> <причина>». Сдвинулась вершина - запись
# перестаёт действовать, ветка всплывает снова.
# Перед сверкой удалённые ветки не обновляются: при работе с нескольких машин сначала git fetch --all.
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/.."

TARGET="${1:-HEAD}"
KNOWN="scripts/branchcheck-known.txt"
git rev-parse --verify -q "$TARGET^{commit}" >/dev/null || { echo "Нет такой ревизии: $TARGET" >&2; exit 2; }

FOUND=0
CHECKED=0
while IFS= read -r REF; do
	NAME="${REF#refs/heads/}"
	NAME="${NAME#refs/remotes/}"
	case "$NAME" in */HEAD) continue ;; esac
	CHECKED=$((CHECKED + 1))
	TIP="$(git rev-parse --short "$REF")"
	# Вершина принята осознанно.
	if [ -f "$KNOWN" ] && grep -qE "^${NAME}[[:space:]]+${TIP}([[:space:]]|$)" "$KNOWN"; then
		continue
	fi
	# Коммиты ветки с правками конфигурации, чей патч не входит в проверяемую ревизию.
	LIST=""
	while IFS= read -r SHA; do
		[ -n "$SHA" ] || continue
		if [ -n "$(git diff-tree --no-commit-id --name-only -r "$SHA" -- src/cf | head -1)" ]; then
			LIST+="    $(git log -1 --format='%h %ad %s' --date=short "$SHA" | cut -c1-150)"$'\n'
		fi
	done < <(git cherry "$TARGET" "$REF" 2>/dev/null | sed -n 's/^+ //p')
	if [ -n "$LIST" ]; then
		FOUND=$((FOUND + 1))
		echo "НЕ СЛИТО: $NAME ($TIP)"
		printf '%s' "$LIST"
	fi
done < <(git for-each-ref --format='%(refname)' refs/heads refs/remotes)

if [ "$FOUND" -gt 0 ]; then
	echo "Сверка веток: в $TARGET не входят правки конфигурации из веток - $FOUND (проверено веток: $CHECKED)."
	echo "Слить, удалить ветку или записать вершину в $KNOWN с причиной."
	exit 1
fi
echo "Сверка веток: неслитых правок конфигурации нет (проверено веток: $CHECKED)"
