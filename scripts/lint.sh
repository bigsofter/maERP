#!/usr/bin/env bash
# Статический анализ модулей BSL Language Server по правилам из .bslls.json.
# Использование: scripts/lint.sh [каталог-с-исходниками]
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

SRC="${1:-$SRC_CF}"
REPORT="$BUILD/bsl-report.json"

JAVA="${JAVA:-/Applications/1C/1CE/components/axiom-jdk-full-17.0.16+12-x86_64/bin/java}"
BSL_LS_JAR="${BSL_LS_JAR:-$HOME/.local/share/bsl-language-server/bsl-language-server.jar}"

[ -x "$JAVA" ] || { echo "Не найдена Java: $JAVA" >&2; exit 1; }
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
