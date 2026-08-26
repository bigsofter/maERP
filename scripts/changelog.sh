#!/usr/bin/env bash
# Выгружает секцию описания изменений одной версии в JSON для хаба tinycio.
# Источник - общий макет ОписаниеИзменений (тот же, что показывает окно
# «Что нового»), формат секций описан в самом макете.
#
# Использование:
#   scripts/changelog.sh [версия] [файл-макета]
#   версия      - по умолчанию берётся из Configuration.mdo
#   файл-макета - по умолчанию макет EDT-проекта, при его отсутствии - макет
#                 XML-выгрузки (build/xml)
#
# Результат: build/changelog-<версия>.json
#
#   {
#     "product": "maERP",          # идентификатор продукта в хабе
#     "version": "2.0.12.4",       # версия релиза
#     "changes": {                 # пункты секции по языкам, в порядке макета
#       "ru": ["пункт", ...],
#       "fr": [...], "en": [...], "es": [...]
#     }
#   }
#
# Отправка в хаб (HMAC-вебхук Product Hub) - этап 12 плана MERGE-DRISSOTEX,
# здесь фиксируется только формат.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$ROOT/build"

CONFIG_MDO="$ROOT/src/cf/src/Configuration/Configuration.mdo"
TEMPLATE_SRC="$ROOT/src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt"
TEMPLATE_DUMP="$BUILD/xml/CommonTemplates/ОписаниеИзменений/Ext/Template.txt"

VERSION="${1:-}"
if [ -z "$VERSION" ]; then
	VERSION="$(sed -n 's:.*<version>\(.*\)</version>.*:\1:p' "$CONFIG_MDO" | head -1)"
fi
[ -n "$VERSION" ] || { echo "Не удалось определить версию: задай её аргументом" >&2; exit 1; }

TEMPLATE="${2:-}"
if [ -z "$TEMPLATE" ]; then
	if [ -f "$TEMPLATE_SRC" ]; then
		TEMPLATE="$TEMPLATE_SRC"
	else
		TEMPLATE="$TEMPLATE_DUMP"
	fi
fi
[ -f "$TEMPLATE" ] || { echo "Не найден макет описания изменений: $TEMPLATE" >&2; exit 1; }

mkdir -p "$BUILD"
OUT="$BUILD/changelog-$VERSION.json"

python3 - "$VERSION" "$TEMPLATE" "$OUT" <<'PY'
import io, json, sys

version, template, out = sys.argv[1], sys.argv[2], sys.argv[3]

DEFAULT_LANGUAGE = 'ru'

changes, in_section, language = {}, False, DEFAULT_LANGUAGE
for line in io.open(template, encoding='utf-8'):
	line = line.strip()
	if line.startswith('## '):
		in_section = line[3:].strip() == version
		language = DEFAULT_LANGUAGE
	elif in_section and line.startswith('### '):
		language = line[4:].strip().lower()
	elif in_section and line.startswith('- '):
		changes.setdefault(language, []).append(line[2:].strip())

total = sum(len(items) for items in changes.values())
if not total:
	sys.exit('В макете нет секции версии %s или она пуста: %s' % (version, template))

payload = {'product': 'maERP', 'version': version, 'changes': changes}
io.open(out, 'w', encoding='utf-8').write(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print('Языков: %d, пунктов изменений: %d' % (len(changes), total))
PY

echo "Описание изменений: $OUT"
