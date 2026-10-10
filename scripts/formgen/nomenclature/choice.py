#!/usr/bin/env python3
"""Навигатор иерархии в формах выбора и подбора номенклатуры (этап 5 плана docs/plans/nomenclature-ui.md).

Навигатор (режим, избранное, обновление, таблица узлов), его реквизиты и команды, параметры и запрос динамического
списка копируются из формы списка товаров (её собирает list.py) - один образец на три формы (tiny1C workflow-005).
Исходная форма - из git (коммит БАЗА).

    python3 choice.py ФормаВыбора > /tmp/f.form && cp /tmp/f.form ../../../src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбора/Form.form
"""
import copy
import os
import re
import subprocess
import sys

from lxml import etree

ЗДЕСЬ = os.path.dirname(os.path.abspath(__file__))
КОРЕНЬ = os.path.normpath(os.path.join(ЗДЕСЬ, '..', '..', '..'))
БАЗА = 'f328bab'
ИМЯ = sys.argv[1]
ФОРМА = f'src/cf/src/Catalogs/Номенклатура/Forms/{ИМЯ}/Form.form'
ОБРАЗЕЦ = os.path.join(КОРЕНЬ, 'src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form')

парсер = etree.XMLParser(remove_blank_text=True)
исходник = subprocess.run(['git', '-C', КОРЕНЬ, 'show', f'{БАЗА}:{ФОРМА}'], capture_output=True, check=True).stdout
форма = etree.fromstring(исходник, парсер)
образец = etree.parse(ОБРАЗЕЦ, парсер).getroot()


def найти(корень, имя, тег='items'):
    for e in корень.iter(тег):
        if e.findtext('name') == имя:
            return e
    raise KeyError(имя)


# Навигатор - первым элементом формы (форма горизонтальная: слева от списка).
форма.insert(0, copy.deepcopy(найти(образец, 'ГруппаИерархия')))

# Запрос и параметры списка - как у формы списка: те же поля, режимы и отборы.
список = найти(форма, 'Список', 'attributes').find('extInfo')
список_образца = найти(образец, 'Список', 'attributes').find('extInfo')
# Запрос - ТекстЗапросаВыбора из модуля менеджера (без остатков и цен - права ролей выбора; ревью Codex 2.0.16.64).
модуль = open(os.path.join(КОРЕНЬ, 'src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl'), encoding='utf-8').read()
m = re.search(r'Функция ТекстЗапросаВыбора\(.*?Текст =\s*"(.*?)";', модуль, re.S)
список.find('queryText').text = '\n'.join(re.sub(r'^\s*\|', '', с) for с in m.group(1).split('\n')).replace('""', '"')
for p in список.findall('parameters'):
    список.remove(p)
for p in список_образца.findall('parameters'):
    список.append(copy.deepcopy(p))

# Реквизиты навигатора; дерево сегментов (ДЗСегменты) больше не нужно.
for a in форма.findall('attributes'):
    if a.findtext('name') == 'ДЗСегменты':
        форма.remove(a)
последний = форма.findall('attributes')[-1]
позиция = list(форма).index(последний)
for i, имя in enumerate(('РежимИерархии', 'ИзбранныеРежимы', 'ВидУзла', 'ЗначениеУзла', 'УзлыИерархии'), 1):
    форма.insert(позиция + i, copy.deepcopy(найти(образец, имя, 'attributes')))
for номер, a in enumerate(форма.findall('attributes'), 1):
    a.find('id').text = str(номер)

позиция = list(форма).index(форма.findall('attributes')[-1])
for i, имя in enumerate(('ИзбранныйРежим', 'ОбновитьИерархию'), 1):
    к = copy.deepcopy(найти(образец, имя, 'formCommands'))
    к.find('id').text = str(i)
    форма.insert(позиция + i, к)

h = etree.Element('handlers')
etree.SubElement(h, 'event').text = 'OnLoadDataFromSettingsAtServer'
etree.SubElement(h, 'name').text = 'ПриЗагрузкеДанныхИзНастроекНаСервере'
форма.insert(list(форма).index(форма.findall('handlers')[-1]) + 1, h)
if форма.find('autoSaveDataInSettings') is None:
    с = etree.Element('autoSaveDataInSettings')
    с.text = 'Use'
    форма.insert(list(форма).index(форма.find('windowOpeningMode')) + 1, с)

счётчик = 0
for узел in форма.findall('items') + [форма.find('autoCommandBar')]:
    for e in узел.iter('id'):
        if e.getparent().tag in ('items', 'extendedTooltip', 'contextMenu', 'autoCommandBar', 'searchStringAddition',
                                 'viewStatusAddition', 'searchControlAddition') and e.text != '-1':
            счётчик += 1
            e.text = str(счётчик)

etree.cleanup_namespaces(форма, keep_ns_prefixes=['form', 'core', 'xsi', 'schema', 'settings'])
etree.indent(форма, space='  ')
sys.stdout.write('<?xml version="1.0" encoding="UTF-8"?>\n' + etree.tostring(форма, encoding='unicode') + '\n')
