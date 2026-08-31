#!/usr/bin/env bash
# Собирает описание GitHub Release из общего макета ОписаниеИзменений.
#
# У релиза на GitHub одно тело описания и никакой локализации, поэтому языки
# кладутся в него подряд: английский - основным текстом, остальные - в
# сворачиваемых блоках <details>. Порядок и правило - docs/RELEASING.md.
#
# Использование:
#   scripts/release-notes.sh [версия] [файл-макета]
#   версия      - по умолчанию берётся из Configuration.mdo
#   файл-макета - по умолчанию макет EDT-проекта, при его отсутствии - макет
#                 XML-выгрузки (build/xml)
#
# В описание попадают ВСЕ секции макета: он ведётся от последней публикации CF,
# то есть содержит ровно те сборки, которые входят в этот релиз.
#
# Результат: build/release-notes-<версия>.md, дальше
#   gh release create v<версия> --draft --notes-file build/release-notes-<версия>.md \
#     build/dist/maERP-<версия>.cf build/dist/maERP-<версия>.cfu
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
OUT="$BUILD/release-notes-$VERSION.md"

python3 - "$VERSION" "$TEMPLATE" "$OUT" <<'PY'
import io, sys
from collections import OrderedDict

version, template, out = sys.argv[1], sys.argv[2], sys.argv[3]

DEFAULT_LANGUAGE = 'ru'
# Английский - основной текст описания, остальные языки под ним в <details>.
ORDER = ['en', 'ru', 'fr', 'es']
TITLES = {
	'en': "What's new",
	'ru': 'Что нового (русский)',
	'fr': 'Nouveautés (français)',
	'es': 'Novedades (español)',
}
FILES = {
	'en': ('Distribution files',
		'full configuration', 'update file', 'Installation and update — see the repository README.'),
	'ru': ('Файлы поставки',
		'полная конфигурация', 'файл обновления', 'Установка и обновление — см. README репозитория.'),
	'fr': ('Fichiers de livraison',
		'configuration complète', 'fichier de mise à jour', "Installation et mise à jour — voir le README du dépôt."),
	'es': ('Archivos de entrega',
		'configuración completa', 'archivo de actualización', 'Instalación y actualización: véase el README del repositorio.'),
}

# Секции макета по версиям сборок, внутри - пункты по языкам.
sections, current, language = OrderedDict(), None, DEFAULT_LANGUAGE
for line in io.open(template, encoding='utf-8'):
	line = line.strip()
	if line.startswith('## '):
		current = line[3:].strip()
		sections[current] = OrderedDict()
		language = DEFAULT_LANGUAGE
	elif current and line.startswith('### '):
		language = line[4:].strip().lower()
	elif current and line.startswith('- '):
		sections[current].setdefault(language, []).append(line[2:].strip())

if not sections:
	sys.exit('В макете нет ни одной секции версии: %s' % template)


def block(lang):
	parts = []
	for build, changes in sections.items():
		items = changes.get(lang) or changes.get(DEFAULT_LANGUAGE) or []
		if not items:
			continue
		parts.append('### %s' % build)
		parts.extend('- %s' % item for item in items)
		parts.append('')
	title, full, update, footer = FILES[lang]
	parts.append('### %s' % title)
	parts.append('')
	parts.append('- `maERP-%s.cf` — %s;' % (version, full))
	parts.append('- `maERP-%s.cfu` — %s.' % (version, update))
	parts.append('')
	parts.append(footer)
	return '\n'.join(parts).rstrip('\n')


body = ['# maERP %s' % version, '']
body.append(block('en'))
body.append('')
for lang in ORDER[1:]:
	body.append('<details>')
	body.append('<summary>%s</summary>' % TITLES[lang])
	body.append('')
	body.append(block(lang))
	body.append('')
	body.append('</details>')
	body.append('')

io.open(out, 'w', encoding='utf-8').write('\n'.join(body).rstrip('\n') + '\n')
print('Сборок в описании: %d, языков: %d' % (len(sections), len(ORDER)))
PY

echo "Описание релиза: $OUT"
