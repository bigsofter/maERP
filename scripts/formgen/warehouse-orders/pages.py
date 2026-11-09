#!/usr/bin/env python3
"""Формы документов ордеров - на закладках «Основное» и «Товары» (docs/FORMS-STYLE.md, правило 4; ревью кода фазы 2
ордерных складов, P2). Разметка групп страниц - по форме реализации. Запуск после gen_forms.py:
  python3 scripts/formgen/warehouse-orders/pages.py
"""
import copy
import os
import re

from lxml import etree

SRC = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src', 'cf', 'src')
XSI = '{http://www.w3.org/2001/XMLSchema-instance}type'
ОБРАЗЕЦ = 'Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form'


def прочитать(путь):
    return etree.parse(os.path.join(SRC, путь), etree.XMLParser(remove_blank_text=True)).getroot()


def элемент(корень, имя):
    for e in корень.iter('items'):
        if e.findtext('name') == имя:
            return e
    raise KeyError(имя)


def без_детей(e):
    к = copy.deepcopy(e)
    for ch in list(к):
        if ch.tag == 'items':
            к.remove(ch)
    return к


def перенумеровать(e, счетчик, старое, новое):
    for n in e.iter('name'):
        if n.text and n.text.startswith(старое):
            n.text = новое + n.text[len(старое):]
    for i in e.iter('id'):
        i.text = str(next(счетчик))


def заголовки(e, тег, ru, fr, en, es):
    for t in e.findall(тег):
        e.remove(t)
    позиция = list(e).index(e.find('userVisible')) + 1
    for k, v in reversed((('ru', ru), ('fr', fr), ('en', en), ('es', es))):
        t = etree.Element(тег)
        etree.SubElement(t, 'key').text = k
        etree.SubElement(t, 'value').text = v
        e.insert(позиция, t)


ПОРЯДОК_EXT = ('group', 'verticalSpacing', 'behavior', 'representation', 'showLeftMargin', 'united', 'showTitle',
               'throughAlign', 'currentRowUse')


def группа(e, **знач):
    ext = e.find('extInfo')
    for тег, значение in знач.items():
        узел = ext.find(тег)
        if узел is None:
            узел = etree.Element(тег)
            # на место по порядку схемы: после ближайшего предыдущего тега
            предыдущие = [ext.find(t) for t in ПОРЯДОК_EXT[:ПОРЯДОК_EXT.index(тег)]]
            предыдущие = [p for p in предыдущие if p is not None]
            if предыдущие:
                предыдущие[-1].addnext(узел)
            else:
                ext.insert(0, узел)
        узел.text = значение


def добавить(родитель, ребенок):
    # дочерние элементы группы - после id, картинки и уже добавленных детей, как в разметке EDT
    позиция = 0
    for i, ch in enumerate(родитель):
        if ch.tag in ('name', 'id', 'picture', 'items', 'titleLocation'):
            позиция = i + 1
    родитель.insert(позиция, ребенок)


def привести(имя_документа):
    путь = 'Documents/{}/Forms/ФормаДокумента/Form.form'.format(имя_документа)
    ф = прочитать(путь)
    образец = прочитать(ОБРАЗЕЦ)
    счетчик = iter(range(max(int(i.text) for i in ф.iter('id') if re.fullmatch(r'\d+', i.text or '')) + 1, 10 ** 6))

    страницы = без_детей(элемент(образец, 'ГруппаСтраницы'))
    перенумеровать(страницы, счетчик, 'ГруппаСтраницы', 'ГруппаСтраницы')
    товары = без_детей(элемент(образец, 'СтраницаТовары'))
    перенумеровать(товары, счетчик, 'СтраницаТовары', 'СтраницаТовары')
    заголовки(товары, 'toolTip', 'Товары', 'Articles', 'Products', 'Mercancía')
    основное = без_детей(элемент(образец, 'СтраницаТовары'))
    перенумеровать(основное, счетчик, 'СтраницаТовары', 'СтраницаОсновное')
    заголовки(основное, 'title', 'Основное', 'Principal', 'Main', 'Principal')
    заголовки(основное, 'toolTip', 'Основное', 'Principal', 'Main', 'Principal')
    for p in основное.findall('picture') + основное.findall('extInfo/picture') + основное.findall('extInfo/titleDataPath'):
        p.getparent().remove(p)

    номер_дата = элемент(ф, 'ГруппаНомерДата')
    шапка = элемент(ф, 'ГруппаШапка')
    комментарий = элемент(ф, 'ГруппаКомментарий')
    тч = элемент(ф, 'ТЧТовары')
    первый = list(ф).index(номер_дата)
    for e in (номер_дата, шапка, комментарий, тч):
        ф.remove(e)
    группа(шапка, group='AutoScreenTypeSensitive', verticalSpacing='Half', representation='None', showTitle='false')
    for колонка in ('ГруппаШапкаЛевая', 'ГруппаШапкаПравая'):
        группа(элемент(шапка, колонка), group='Vertical', verticalSpacing='Half', representation='None',
               showTitle='false')
    группа(комментарий, representation='None', showTitle='false')
    # Колонки как у реализации: слева контрагент и основание, справа склад и организация; ответственный - над
    # комментарием, в блоке автора (ревью кода фазы 2, P2).
    левая, правая = элемент(шапка, 'ГруппаШапкаЛевая'), элемент(шапка, 'ГруппаШапкаПравая')
    организация, ответственный = элемент(шапка, 'Организация'), элемент(шапка, 'Ответственный')
    основание = элемент(шапка, 'Основание')
    for e in (организация, ответственный, основание):
        e.getparent().remove(e)
    элемент(левая, 'Контрагент').addnext(основание)
    элемент(правая, 'МестоХранения').addnext(организация)
    элемент(комментарий, 'Комментарий').addprevious(ответственный)
    # Заголовок поля шапки - слева (правило 5).
    for поле in list(шапка.iter('items')) + [ответственный]:
        if поле.get(XSI) == 'form:FormField' and поле.find('titleLocation') is None:
            t = etree.Element('titleLocation')
            t.text = 'Left'
            поле.find('id').addnext(t)
    for e in (номер_дата, шапка, комментарий):
        добавить(основное, e)
    добавить(товары, тч)
    добавить(страницы, основное)
    добавить(страницы, товары)
    ф.insert(первый, страницы)

    текст = etree.tostring(ф, encoding='unicode', pretty_print=True)
    with open(os.path.join(SRC, путь), 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + текст)


for имя in ('ПриходныйОрдер', 'РасходныйОрдер'):
    привести(имя)
