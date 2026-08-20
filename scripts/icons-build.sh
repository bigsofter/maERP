#!/usr/bin/env bash
# Растеризует исходники иконок из design/icons в общие картинки конфигурации.
# Требует rsvg-convert (brew install librsvg).
# Использование: scripts/icons-build.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CP="$ROOT/src/cf/src/CommonPictures"

command -v rsvg-convert >/dev/null || { echo "Нет rsvg-convert: brew install librsvg" >&2; exit 1; }

# исходник : имя общей картинки
MAP=(
	"ECommerce:Leads48"
	"Закупки:Закупки128"
	"Продажи:Продажи128"
	"Склад:Склад128"
	"Казначейство:Казначейство128"
	"Сервис:Сервис128"
	"Бухгалтерия:Бухгалтерия128"
	"ЗарплатаИКадры:ЗарплатаИКадры128"
)

for pair in "${MAP[@]}"; do
	src="$ROOT/design/icons/${pair%%:*}.svg"
	dst="$CP/${pair##*:}/Picture.png"
	[ -f "$src" ] || { echo "Нет исходника: $src" >&2; exit 1; }
	[ -d "$(dirname "$dst")" ] || { echo "Нет общей картинки: ${pair##*:}" >&2; exit 1; }
	rsvg-convert -w 128 -h 128 -o "$dst" "$src"
	echo "${pair%%:*} -> ${pair##*:}"
done

echo "Готово. В EDT нужен Refresh (F5)."
