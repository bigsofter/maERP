#!/usr/bin/env python3
"""Флажки опций в мастере первого запуска (2.0.16.85): учёт станков и автовыпуск при отгрузке - после «Переработки»,
выбор партии при продаже - после «Правил ценообразования». Флажок и реквизит «Опция<Константа>» - копии соседних,
заголовок реквизита - синоним константы на четырёх языках (как в «Параметрах»). Список имён и применение -
НачальноеЗаполнениеВызовСервера.ФункциональныеОпцииМастера. Запуск: python3 scripts/formgen/wizard/options.py
"""
import copy
import os
import re

from lxml import etree

КОРЕНЬ = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src', 'cf', 'src')
ФОРМА = os.path.join(КОРЕНЬ, 'CommonForms', 'ФормаПервогоЗапуска', 'Form.form')
НОВЫЕ = [('ОпцияИспользоватьПереработку', ['ИспользоватьАвтовыпускПриОтгрузке', 'ИспользоватьУчетСтанков']),
         ('ОпцияИспользоватьПравилаЦенообразования', ['ВыборПартииПриПродаже'])]


def синоним(константа):
    путь = os.path.join(КОРЕНЬ, 'Constants', константа, константа + '.mdo')
    корень = etree.parse(путь).getroot()
    return [(s.findtext('key'), s.findtext('value')) for s in корень.findall('synonym')]


ф = etree.parse(ФОРМА, etree.XMLParser(remove_blank_text=True)).getroot()
элементы = {e.findtext('name'): e for e in ф.iter('items')}
реквизиты = {a.findtext('name'): a for a in ф.findall('attributes')}
# id элементов - одно пространство с подсказками и меню (forms-018), реквизиты - своё (forms-001)
ids = [int(i.text) for e in ф.iter('items', 'extendedTooltip', 'contextMenu', 'autoCommandBar')
       for i in e.findall('id') if re.fullmatch(r'\d+', i.text or '')]
счетчик = iter(range(max(ids) + 1, 10 ** 6))
ids_реквизитов = [int(a.findtext('id')) for a in ф.findall('attributes') if re.fullmatch(r'\d+', a.findtext('id') or '')]
счетчик_реквизитов = iter(range(max(ids_реквизитов) + 1, 10 ** 6))

for после, константы in НОВЫЕ:
    якорь = элементы[после]
    якорь_реквизита = реквизиты[после]
    for константа in константы:
        имя = 'Опция' + константа
        if имя in элементы:
            raise SystemExit('уже есть: ' + имя)
        элемент = copy.deepcopy(элементы[после])
        for e in элемент.iter():
            if e.tag == 'name' and e.text:
                e.text = e.text.replace(после, имя)
            if e.tag == 'segments' and e.text == после:
                e.text = имя
            if e.tag == 'id':
                e.text = str(next(счетчик))
        якорь.addnext(элемент)
        якорь = элемент
        реквизит = copy.deepcopy(реквизиты[после])
        реквизит.find('name').text = имя
        реквизит.find('id').text = str(next(счетчик_реквизитов))
        for t in реквизит.findall('title'):
            реквизит.remove(t)
        позиция = list(реквизит).index(реквизит.find('name')) + 1
        for ключ, значение in синоним(константа):
            t = etree.Element('title')
            etree.SubElement(t, 'key').text = ключ
            etree.SubElement(t, 'value').text = значение
            реквизит.insert(позиция, t)
            позиция += 1
        якорь_реквизита.addnext(реквизит)
        якорь_реквизита = реквизит

текст = etree.tostring(ф, encoding='unicode', pretty_print=True)
with open(ФОРМА, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + текст)
print('ok')
