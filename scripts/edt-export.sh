#!/usr/bin/env bash
# Экспортирует EDT-проект в XML-формат конфигуратора через 1cedtcli.
# Первое звено сборки: src/cf (EDT) -> build/xml -> база -> CF.
# Использование: scripts/edt-export.sh [проект] [каталог-выгрузки]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

PROJECT="${1:-$SRC_CF}"
OUT="${2:-$XML_OUT}"

if [ -z "$EDT_CLI" ] || [ ! -x "$EDT_CLI" ]; then
  echo "Не задан путь к 1cedtcli. Установи EDT и пропиши EDT_CLI в scripts/env.sh." >&2
  echo "См. docs/EDT-SETUP.md" >&2
  exit 1
fi

rm -rf "$OUT"; mkdir -p "$OUT" "$EDT_WS"
"$EDT_CLI" -data "$EDT_WS" -command export \
  --project "$PROJECT" \
  --configuration-files "$OUT"
echo "EDT-проект выгружен в XML: $OUT"
