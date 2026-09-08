#!/usr/bin/env bash
# Собирает общие картинки разделов из исходников design/icons/<Имя>.svg.
# Формат картинки платформы 8.5: Picture.zip с icon.svg (шаблон 24x24, цвет подставляет
# платформа) и manifest.xml. Исходник кладётся в архив как есть - никакой растеризации.
# Использование: scripts/icons-build.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CP="$ROOT/src/cf/src/CommonPictures"

# исходник : имя общей картинки
MAP=(
	"Главное:Главное128"
	"ECommerce:Leads48"
	"Закупки:Закупки128"
	"Продажи:Продажи128"
	"Склад:Склад128"
	"Казначейство:Казначейство128"
	"Сервис:Сервис128"
	"Бухгалтерия:Бухгалтерия128"
	"ЗарплатаИКадры:ЗарплатаИКадры128"
	"Производство:Производство128"
)

for pair in "${MAP[@]}"; do
	src="$ROOT/design/icons/${pair%%:*}.svg"
	dir="$CP/${pair##*:}"
	[ -f "$src" ] || { echo "Нет исходника: $src" >&2; exit 1; }
	[ -d "$dir" ] || { echo "Нет общей картинки: ${pair##*:}" >&2; exit 1; }
	python3 - "$src" "$dir/Picture.zip" <<'PY'
import sys, zipfile
src, dst = sys.argv[1], sys.argv[2]
manifest = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Picture>\n'
            '\t<PictureVariant name="icon.svg" screenDensity="ldpi" interfaceVariant="version8_5" theme="" isTemplate="true"/>\n</Picture>')
with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("icon.svg", open(src, encoding="utf-8").read())
    z.writestr("manifest.xml", manifest)
PY
	echo "${pair%%:*} -> ${pair##*:}/Picture.zip"
done

echo "Готово. В EDT нужен Refresh (F5)."
