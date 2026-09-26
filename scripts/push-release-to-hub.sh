#!/usr/bin/env bash
# Публикация релиза maERP в историю релизов TinyCIO
# (страница https://tinycio.<tld>/about/releases/maerp).
#
# Источник — тот же, что у окна «Что нового»: общий макет ОписаниеИзменений.
# Разбирает его scripts/changelog.sh (он уже отдаёт нужную форму
# {"version": …, "changes": {"ru": [...], "fr": [...]}} — хаб принимает
# `changes` как синоним `notes`). Здесь только дата, подпись и отправка.
#
# Использование:
#   scripts/push-release-to-hub.sh --dry-run          # показать, что уедет
#   scripts/push-release-to-hub.sh                    # версия из Configuration.mdo
#   scripts/push-release-to-hub.sh 2.0.14.26          # конкретная версия
#   scripts/push-release-to-hub.sh 2.0.14.26 2026-09-08   # с датой релиза
#
# Переменные окружения:
#   TINYCIO_HUB_SECRET  — HMAC-секрет вебхука maERP в хабе (ОБЯЗАТЕЛЬНО)
#   TINYCIO_HUB_URL     — база хаба, по умолчанию https://my.tinycio.com
#   TINYCIO_HUB_PRODUCT — код продукта в хабе, по умолчанию maerp
#
# ЯЗЫКИ БЕРУТСЯ ИЗ МАКЕТА и не переводятся: у maERP это ru/fr/en/es. Витрина
# печатает язык домена, а при его отсутствии — доступный С ПОМЕТКОЙ языка.
#
# ИДЕМПОТЕНТНО: повтор той же версии обновляет запись (UNIQUE(product, version)
# в хабе), поэтому curl идёт с --retry.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HUB_URL="${TINYCIO_HUB_URL:-https://my.tinycio.com}"
PRODUCT="${TINYCIO_HUB_PRODUCT:-maerp}"

DRY=0
ARGS=()
for a in "$@"; do
	case "$a" in
		--dry-run) DRY=1 ;;
		-*) echo "Неизвестный ключ: $a" >&2; exit 2 ;;
		*) ARGS+=("$a") ;;
	esac
done
VERSION="${ARGS[0]:-}"
RELEASED_AT="${ARGS[1]:-$(date -u +%F)}"

# changelog.sh сам определит версию из Configuration.mdo, если её не задали, и
# положит JSON в build/changelog-<версия>.json.
# MAERP_CHANGELOG_TEMPLATE — путь к макету для проверки на копии (сухой прогон
# на боевом макете невозможен: после публикации CF секция очищается, и в нём
# лежит только следующая, ещё пустая версия).
"$ROOT/scripts/changelog.sh" ${VERSION:+"$VERSION"} ${MAERP_CHANGELOG_TEMPLATE:+"$MAERP_CHANGELOG_TEMPLATE"} >&2
SRC="$(ls -t "$ROOT"/build/changelog-*.json | head -1)"
[ -f "$SRC" ] || { echo "Не найден build/changelog-*.json" >&2; exit 1; }

PAYLOAD="$(mktemp)"
trap 'rm -f "$PAYLOAD"' EXIT

python3 - "$SRC" "$RELEASED_AT" > "$PAYLOAD" <<'PY'
import io, json, sys
src, released_at = sys.argv[1], sys.argv[2]
d = json.load(io.open(src, encoding='utf-8'))
# `product` из changelog.sh — человеческое имя ('maERP'), а код продукта в
# хабе стоит в пути запроса. Наружу его не шлём, чтобы не было двух источников.
out = {'version': d['version'], 'released_at': released_at, 'changes': d['changes']}
json.dump(out, sys.stdout, ensure_ascii=False)
PY

VER="$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["version"])' "$PAYLOAD")"
CNT="$(python3 -c 'import json,sys;d=json.load(open(sys.argv[1]));print(sum(len(v) for v in d["changes"].values()))' "$PAYLOAD")"
LNG="$(python3 -c 'import json,sys;print(",".join(sorted(json.load(open(sys.argv[1]))["changes"])))' "$PAYLOAD")"
echo "[hub] $PRODUCT $VER ($RELEASED_AT) — $CNT пунктов, языки: $LNG" >&2

if [ "$DRY" = "1" ]; then
	python3 -m json.tool "$PAYLOAD"
	exit 0
fi

[ -n "${TINYCIO_HUB_SECRET:-}" ] || { echo "Не задан TINYCIO_HUB_SECRET" >&2; exit 1; }

TS="$(date +%s)"
SIG="$(openssl dgst -sha256 -hmac "$TINYCIO_HUB_SECRET" -r "$PAYLOAD" | cut -d' ' -f1)"

# Подпись — по ТЕМ ЖЕ БАЙТАМ, что уходят телом (--data-binary @файл).
curl -fsS --retry 3 --retry-connrefused --max-time 30 \
	-X POST "$HUB_URL/api/product-hub/$PRODUCT/releases" \
	-H 'Content-Type: application/json' \
	-H "X-Signature: sha256=$SIG" \
	-H "X-Timestamp: $TS" \
	--data-binary "@$PAYLOAD"
echo
