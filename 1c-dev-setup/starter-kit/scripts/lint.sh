#!/usr/bin/env bash
# Прогон BSL Language Server по исходникам (Mac/Linux).
# Требует Java 17+ и скачанный bsl-language-server-*-exec.jar.
set -euo pipefail

JAR="${BSL_LS_JAR:-$HOME/tools/bsl-language-server-exec.jar}"
SRC="${1:-./src}"
OUT="${2:-./reports}"

mkdir -p "$OUT"
java -jar "$JAR" --analyze \
  --src "$SRC" \
  --reporter json \
  --outputDir "$OUT" \
  --configuration ./.bslls.json

echo "Отчёт линтера: $OUT"
