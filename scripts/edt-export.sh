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

# Архитектура JVM обязана совпадать с архитектурой 1cedtcli (см. комментарий в env.sh):
# иначе лаунчер молча падает с rc=254, а причина остаётся только в логе рабочей области.
if [ -z "$EDT_JAVA_HOME" ] || [ ! -x "$EDT_JAVA_HOME/bin/java" ]; then
  echo "Не найдена x86_64-JDK 17+ для 1cedtcli. Поставь её или задай EDT_JAVA_HOME." >&2
  echo "См. docs/EDT-SETUP.md" >&2
  exit 1
fi
if ! file "$EDT_CLI" | grep -q "$(file "$EDT_JAVA_HOME/bin/java" | grep -o 'x86_64\|arm64')"; then
  echo "Архитектуры не совпадают: 1cedtcli и JDK из EDT_JAVA_HOME собраны под разные платформы." >&2
  file "$EDT_CLI" "$EDT_JAVA_HOME/bin/java" >&2
  exit 1
fi

LOG="$BUILD/edt-export.log"
rm -rf "$OUT"; mkdir -p "$OUT" "$EDT_WS" "$BUILD"
# Рабочая область CLI — своя, не та, что открыта в IDE: Eclipse держит её эксклюзивно.
# Проект, которого в ней нет, команда export импортирует сама.
JAVA_HOME="$EDT_JAVA_HOME" PATH="$EDT_JAVA_HOME/bin:$PATH" \
"$EDT_CLI" -data "$EDT_WS" -nl ru_RU -command export \
  --project "$PROJECT" \
  --configuration-files "$OUT" > "$LOG" 2>&1
RC=$?
# Чистый экспорт пишет пустой лог: grep без совпадений вернул бы 1 и под pipefail (env.sh) оборвал скрипт
# молча, хотя выгрузка удалась. Итог решает проверка RC и каталога ниже.
grep -v "^WARNING" "$LOG" | grep -v '^$' | tail -20 || true
if [ $RC -ne 0 ] || [ ! -d "$OUT/Documents" ]; then
  echo "Экспорт EDT не удался (rc=$RC). Лог: $LOG; журнал EDT: $EDT_WS/.metadata/1cedtcli.log" >&2
  exit 1
fi
echo "EDT-проект выгружен в XML: $OUT"
