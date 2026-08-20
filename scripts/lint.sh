#!/usr/bin/env bash
# Статический анализ модулей BSL Language Server по правилам из .bslls.json.
# Использование: scripts/lint.sh [каталог-с-исходниками]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

SRC="${1:-$SRC_CF}"
REPORT="$BUILD/bsl-json.json"

# BSL LS требует Java 21, а поставляемая с EDT — 17, поэтому отдельный JDK
# в ~/.local. Раскладка macOS-сборки Temurin — Contents/Home.
if [ -z "${JAVA:-}" ]; then
	for candidate in \
		"$HOME/.local/jdk-21/Contents/Home/bin/java" \
		"$HOME/.local/jdk-21/bin/java"
	do
		[ -x "$candidate" ] && { JAVA="$candidate"; break; }
	done
fi
BSL_LS_JAR="${BSL_LS_JAR:-$HOME/.local/share/bsl-language-server/bsl-language-server.jar}"

if [ -z "${JAVA:-}" ] || [ ! -x "$JAVA" ]; then
	echo "Не найден JDK 21 в ~/.local/jdk-21. Java из комплекта EDT (17) не подходит:" >&2
	echo "BSL LS собран под 21. Поставь JDK 21 туда либо задай JAVA." >&2
	exit 1
fi
if [ ! -f "$BSL_LS_JAR" ]; then
  echo "Не найден BSL Language Server: $BSL_LS_JAR" >&2
  echo "Скачай jar с https://github.com/1c-syntax/bsl-language-server/releases" >&2
  echo "и положи по этому пути либо задай BSL_LS_JAR." >&2
  exit 1
fi

"$JAVA" -jar "$BSL_LS_JAR" \
  --analyze \
  --srcDir "$SRC" \
  --configuration "$ROOT/.bslls.json" \
  --reporter json \
  --outputDir "$BUILD"
echo "Отчёт: $REPORT"
