#!/usr/bin/env bash
# Собирает файлы поставки тиражного решения: CF и, при наличии предыдущих
# релизов, файл обновления CFU.
# Использование: scripts/dist-build.sh <версия> [предыдущий1.cf предыдущий2.cf ...]
# База берётся из DIST_IB, по умолчанию build/ib. Когда база занята конфигуратором или
# агентом EDT, собираем от копии: cp build/ib/1Cv8.1CD build/ib-dist/ и DIST_IB=build/ib-dist.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

VERSION="${1:?Укажи версию поставки, например 1.0.2}"
shift || true

IB="${DIST_IB:-$IB_BUILD}"
LOG="$BUILD/dist-build.log"
mkdir -p "$DIST"

CF_OUT="$DIST/maERP-${VERSION}.cf"
ARGS=(/CreateDistributionFiles -cffile "$CF_OUT")

if [ "$#" -gt 0 ]; then
  ARGS+=(-cfufile "$DIST/maERP-${VERSION}.cfu")
  for prev in "$@"; do
    [ -f "$prev" ] || { echo "Нет файла предыдущего релиза: $prev" >&2; exit 1; }
    ARGS+=(-f "$prev")
  done
fi

"$V8" DESIGNER /F "$IB" "${ARGS[@]}" "${V8_BATCH[@]}" /Out "$LOG"
cat "$LOG"
ls -la "$DIST"
