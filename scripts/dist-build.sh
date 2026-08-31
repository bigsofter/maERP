#!/usr/bin/env bash
# Собирает файлы поставки тиражного решения: CF и, при наличии предыдущих
# релизов, файл обновления CFU.
# Использование: scripts/dist-build.sh <версия> [предыдущий1.cf предыдущий2.cf ...]
# Без списка предыдущих версий CFU строится от всех maERP-*.cf, лежащих в каталоге
# поставок (опубликованные релизы и сборки, переданные на тест): клиент с любой из них
# обновится одним файлом.
# База берётся из DIST_IB, по умолчанию build/ib. Когда база занята конфигуратором или
# агентом EDT, собираем от копии: cp build/ib/1Cv8.1CD build/ib-dist/ и DIST_IB=build/ib-dist.
# База с пользователями: логин и пароль - через переменные окружения DIST_USER и DIST_PWD
# (по умолчанию берутся SMOKE_USER / SMOKE_PWD), в файлы и логи они не попадают.
source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

VERSION="${1:?Укажи версию поставки, например 1.0.2}"
shift || true

IB="${DIST_IB:-$IB_BUILD}"
LOG="$BUILD/dist-build.log"
mkdir -p "$DIST"

AUTH=()
USER="${DIST_USER:-${SMOKE_USER:-}}"
PWD_="${DIST_PWD:-${SMOKE_PWD:-}}"
[ -n "$USER" ] && AUTH+=(/N "$USER")
[ -n "$PWD_" ] && AUTH+=(/P "$PWD_")

CF_OUT="$DIST/maERP-${VERSION}.cf"
ARGS=(/CreateDistributionFiles -cffile "$CF_OUT")

# Источники обновления: заданные аргументами, иначе все сборки из каталога поставок.
# Забыть предыдущий релиз нельзя - клиент на нём остался бы без файла обновления.
PREV=("$@")
if [ "${#PREV[@]}" -eq 0 ]; then
  while IFS= read -r cf; do
    [ "$cf" = "$CF_OUT" ] || PREV+=("$cf")
  done < <(ls -1 "$DIST"/maERP-*.cf 2>/dev/null | sort -V)
  [ "${#PREV[@]}" -gt 0 ] && echo "Источники обновления (все сборки из $DIST): ${PREV[*]##*/}"
fi

if [ "${#PREV[@]}" -gt 0 ]; then
  ARGS+=(-cfufile "$DIST/maERP-${VERSION}.cfu")
  for prev in "${PREV[@]}"; do
    [ -f "$prev" ] || { echo "Нет файла предыдущего релиза: $prev" >&2; exit 1; }
    ARGS+=(-f "$prev")
  done
fi

"$V8" DESIGNER /F "$IB" ${AUTH[@]+"${AUTH[@]}"} "${ARGS[@]}" "${V8_BATCH[@]}" /Out "$LOG"
cat "$LOG"
ls -la "$DIST"
