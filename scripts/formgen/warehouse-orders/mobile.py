#!/usr/bin/env python3
"""Колонка «Ордер» в мобильной форме реализации (план warehouse-orders, доработки 2.0.16.80, §5.3): та же колонка, что в
основной форме, - поле надписи по Объект.ТЧТовары.Ордер, после характеристики. Видимость ставит
Документы.РеализацияТоваровУслуг.НастроитьОрдернуюСхемуФормы. Запуск: python3 scripts/formgen/warehouse-orders/mobile.py
"""
import copy
import os
import re

from lxml import etree

SRC = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src', 'cf', 'src', 'Documents', 'РеализацияТоваровУслуг',
                   'Forms')
ОБРАЗЕЦ = os.path.join(SRC, 'ФормаДокумента', 'Form.form')
ЦЕЛЬ = os.path.join(SRC, 'ФормаДокументаМобильныйКлиент', 'Form.form')


def прочитать(путь):
    return etree.parse(путь, etree.XMLParser(remove_blank_text=True)).getroot()


def элемент(корень, имя):
    for e in корень.iter('items'):
        if e.findtext('name') == имя:
            return e
    raise KeyError(имя)


ф = прочитать(ЦЕЛЬ)
if any(e.findtext('name') == 'ТЧТоварыОрдер' for e in ф.iter('items')):
    raise SystemExit('колонка уже есть')
# id элементов - одно пространство на все items формы, включая вложенные подсказки и меню (forms-018)
ids = [int(i.text) for e in ф.iter('items', 'extendedTooltip', 'contextMenu', 'autoCommandBar')
       for i in e.findall('id') if re.fullmatch(r'\d+', i.text or '')]
счетчик = iter(range(max(ids) + 1, 10 ** 6))
колонка = copy.deepcopy(элемент(прочитать(ОБРАЗЕЦ), 'ТЧТоварыОрдер'))
for i in колонка.iter('id'):
    i.text = str(next(счетчик))
элемент(ф, 'ТЧТоварыХарактеристика').addnext(колонка)

текст = etree.tostring(ф, encoding='unicode', pretty_print=True)
with open(ЦЕЛЬ, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + текст)
print('ok')
