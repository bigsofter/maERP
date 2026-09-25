#!/usr/bin/env python3
"""Сверка видимых заголовков конфигурации: что увидит пользователь на четырёх языках.

Ни один прогон maERP такого не ловит: `lint.sh` смотрит модули, `refcheck.py` —
ссылки на объекты, `listcheck.py` и `queryfields.py` — имена полей. Заголовок
поля при этом берётся из синонима реквизита, и одна правка `.mdo` молча меняет
подпись в форме документа, заголовок колонки списка и шапку колонки отчёта.

Скрипт снимает таблицу «где какой заголовок» и сверяет её со снимком:

  scripts/titlecheck.py --снимок            записать scripts/titlecheck-baseline.txt
  scripts/titlecheck.py                     сверить с ним, показать расхождения
  scripts/titlecheck.py --снимок <файл>     записать в свой файл

Строка снимка — `<источник>\t<объект>\t<что>\t<ru>|<fr>|<en>|<es>`. Заголовок,
который наследуется от реквизита, пишется как `=<реквизит>`: именно такие места
и утекают при переименовании синонима.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

КОРЕНЬ = Path(__file__).resolve().parent.parent
ИСХОДНИКИ = КОРЕНЬ / 'src' / 'cf' / 'src'
СНИМОК = КОРЕНЬ / 'scripts' / 'titlecheck-baseline.txt'
ЯЗЫКИ = ('ru', 'fr', 'en', 'es')

ПРОПУСК = ('МобильныйКлиент', 'МобильноеПриложение')

СИНОНИМ = re.compile(r'<synonym>\s*<key>(\w+)</key>\s*<value>([^<]*)</value>\s*</synonym>')
ЗАГОЛОВОК = re.compile(r'<title>\s*<key>(\w+)</key>\s*<value>([^<]*)</value>\s*</title>')
# В схемах компоновки заголовок лежит иначе, чем в формах: v8:LocalStringType с item/lang/content.
ЗАГОЛОВОК_СКД = re.compile(r'<v8:item>\s*<v8:lang>(\w+)</v8:lang>\s*<v8:content>([^<]*)</v8:content>\s*</v8:item>')
ИМЯ = re.compile(r'<name>([^<]*)</name>')


def чисто(значение):
    """Значение в одну строку: перевод строки и табуляция ломают формат снимка."""
    return re.sub(r'\s+', ' ', значение or '').strip()


def языки(пары):
    """Словарь язык→значение в строку снимка, в постоянном порядке языков."""
    как_есть = {к: чисто(з) for к, з in пары}
    return '|'.join(как_есть.get(я, '') for я in ЯЗЫКИ)


def синонимы_узла(узел):
    return [(с.find('key').text, с.find('value').text or '') for с in узел.findall('synonym')]


def синонимы_метаданных(строки):
    """Синонимы реквизитов, табличных частей и их реквизитов — источник заголовков.

    Разбором XML, а не текстом: в `.mdo` теги идут с атрибутами (`<attributes uuid=…>`),
    и поиск по голому тегу не находит ничего. Файл только читается, не переписывается.
    """
    for mdo in sorted(ИСХОДНИКИ.rglob('*.mdo')):
        объект = str(mdo.relative_to(ИСХОДНИКИ)).rsplit('/', 1)[0]
        try:
            корень = ET.parse(mdo).getroot()
        except ET.ParseError as ош:
            print('не разобран %s: %s' % (mdo, ош), file=sys.stderr)
            continue
        for вид in ('attributes', 'standardAttributes', 'dimensions', 'resources', 'commands', 'columns'):
            for узел in корень.findall(вид):
                имя = узел.find('name')
                if имя is not None:
                    строки.append('мдо\t%s\t%s\t%s' % (объект, имя.text, языки(синонимы_узла(узел))))
        for тч in корень.findall('tabularSections'):
            имя_тч = тч.find('name')
            if имя_тч is None:
                continue
            строки.append('мдо\t%s\t%s\t%s' % (объект, имя_тч.text, языки(синонимы_узла(тч))))
            for реквизит in тч.findall('attributes'):
                имя = реквизит.find('name')
                if имя is not None:
                    строки.append('мдо\t%s\t%s.%s\t%s'
                                  % (объект, имя_тч.text, имя.text, языки(синонимы_узла(реквизит))))


def элементы_формы(текст):
    """Поля формы: имя, путь данных, явный заголовок. Поля идут в порядке файла."""
    for м in re.finditer(r'<items xsi:type="form:(FormField|LabelDecoration)">', текст):
        начало = м.start()
        уровень = 0
        конец = начало
        for tok in re.finditer(r'<items\b[^>]*>|</items>', текст[начало:]):
            уровень += 1 if tok.group(0).startswith('<items') else -1
            if уровень == 0:
                конец = начало + tok.end()
                break
        кусок = текст[начало:конец]
        имя = ИМЯ.search(кусок)
        путь = re.search(r'<segments>([^<]*)</segments>', кусок)
        yield (имя.group(1) if имя else '?',
               путь.group(1) if путь else '',
               ЗАГОЛОВОК.findall(кусок))


def заголовки_форм(строки):
    for форма in sorted(ИСХОДНИКИ.rglob('Form.form')):
        путь_формы = str(форма.relative_to(ИСХОДНИКИ)).rsplit('/', 1)[0]
        if any(п in путь_формы for п in ПРОПУСК):
            continue
        текст = форма.read_text(encoding='utf-8')
        for имя, путь, заголовок in элементы_формы(текст):
            if заголовок:
                строки.append('форма\t%s\t%s\t%s' % (путь_формы, имя, языки(заголовок)))
            elif путь:
                строки.append('форма\t%s\t%s\t=%s' % (путь_формы, имя, путь))


def заголовки_скд(строки):
    for схема in sorted(ИСХОДНИКИ.rglob('*.dcs')):
        объект = str(схема.relative_to(ИСХОДНИКИ)).split('/Templates/')[0]
        текст = схема.read_text(encoding='utf-8')
        for кусок in re.findall(r'<field xsi:type="DataSetFieldField">(.*?)</field>\s*(?=<field|</dataSet|</item|$)',
                                текст, re.S):
            путь = re.search(r'<dataPath>([^<]*)</dataPath>', кусок)
            if not путь:
                continue
            начало = кусок.find('<title')
            заголовок = ЗАГОЛОВОК_СКД.findall(кусок[начало:]) if начало >= 0 else []
            if заголовок:
                строки.append('скд\t%s\t%s\t%s' % (объект, путь.group(1), языки(заголовок)))
            else:
                строки.append('скд\t%s\t%s\t=%s' % (объект, путь.group(1), путь.group(1)))


def снять():
    строки = []
    синонимы_метаданных(строки)
    заголовки_форм(строки)
    заголовки_скд(строки)
    return sorted(строки)


def сверить(строки, файл):
    if not файл.exists():
        print('снимка нет: %s — сделайте scripts/titlecheck.py --снимок' % файл, file=sys.stderr)
        return 2
    было = файл.read_text(encoding='utf-8').splitlines()
    было_ключи = {с.rsplit('\t', 1)[0]: с.rsplit('\t', 1)[1] for с in было if '\t' in с}
    стало_ключи = {с.rsplit('\t', 1)[0]: с.rsplit('\t', 1)[1] for с in строки if '\t' in с}
    изменено = [(к, было_ключи[к], стало_ключи[к])
                for к in sorted(set(было_ключи) & set(стало_ключи)) if было_ключи[к] != стало_ключи[к]]
    ушло = sorted(set(было_ключи) - set(стало_ключи))
    пришло = sorted(set(стало_ключи) - set(было_ключи))
    for к, а, б in изменено:
        print('изменён  %s\n    было  %s\n    стало %s' % (к, а, б))
    for к in ушло:
        print('пропал   %s (было %s)' % (к, было_ключи[к]))
    for к in пришло:
        print('новый    %s (%s)' % (к, стало_ключи[к]))
    print('\nитого: изменено %d, пропало %d, новых %d' % (len(изменено), len(ушло), len(пришло)))
    return 1 if (изменено or ушло) else 0


def main(argv):
    строки = снять()
    if '--снимок' in argv:
        поз = argv.index('--снимок')
        файл = Path(argv[поз + 1]) if len(argv) > поз + 1 and not argv[поз + 1].startswith('--') else СНИМОК
        файл.write_text('\n'.join(строки) + '\n', encoding='utf-8')
        print('снимок записан: %s, строк %d' % (файл, len(строки)))
        return 0
    return сверить(строки, СНИМОК)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
