#!/usr/bin/env python3
"""Формы ордеров склада (ФормаДокумента, ФормаСписка) по образцу форм ПеремещениеТоваров, план
docs/plans/warehouse-orders.md, фаза 2 (2.0.16.77). Урок tiny1C workflow-005: XML-конструкции - из работающей формы
этой же конфигурации; новые узлы получают id в пространстве элементов формы после максимального.

    python3 gen_forms.py   # пишет Form.form обеих форм обоих ордеров; модули форм ведутся руками
"""
import copy
import os

from lxml import etree

ЗДЕСЬ = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(ЗДЕСЬ, '..', '..', '..', 'src', 'cf', 'src'))
XSI = 'http://www.w3.org/2001/XMLSchema-instance'
ОБРАЗЕЦ = 'Documents/ПеремещениеТоваров/Forms/{}/Form.form'


def прочитать(путь):
    return etree.parse(os.path.join(SRC, путь), etree.XMLParser(remove_blank_text=True)).getroot()


def найти(корень, имя):
    for e in корень.iter('items'):
        if e.findtext('name') == имя:
            return e
    raise KeyError(имя)


def удалить(корень, имя):
    e = найти(корень, имя)
    e.getparent().remove(e)


class Счетчик:
    def __init__(self, корень):
        self.n = max(int(e.text) for e in корень.iter('id') if e.text and e.text.isdigit())

    def __call__(self):
        self.n += 1
        return str(self.n)


def переименовать(e, старое, новое):
    for n in e.iter('name'):
        if n.text and n.text.startswith(старое) and n.getparent().tag in ('items', 'extendedTooltip', 'contextMenu',
                                                                           'autoCommandBar'):
            n.text = новое + n.text[len(старое):]


def заголовок(e, ru, fr, en, es):
    for t in e.findall('title'):
        e.remove(t)
    позиция = list(e).index(e.find('id')) + 1
    for i, (k, v) in enumerate((('ru', ru), ('fr', fr), ('en', en), ('es', es))):
        t = etree.Element('title')
        etree.SubElement(t, 'key').text = k
        etree.SubElement(t, 'value').text = v
        e.insert(позиция + i, t)


def клон(корень, образец, новое_имя, путь, счетчик):
    e = copy.deepcopy(найти(корень, образец))
    переименовать(e, образец, новое_имя)
    for i in e.iter('id'):
        i.text = счетчик()
    e.find('dataPath/segments').text = путь
    for h in e.findall('handlers'):
        e.remove(h)
    return e


def записать(корень, путь):
    текст = etree.tostring(корень, encoding='unicode', pretty_print=True)
    полный = os.path.join(SRC, путь)
    os.makedirs(os.path.dirname(полный), exist_ok=True)
    with open(полный, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + текст)


ЗАГОЛОВКИ_КОНТРАГЕНТА = {
    'ПриходныйОрдер': ('Поставщик', 'Fournisseur', 'Supplier', 'Proveedor'),
    'РасходныйОрдер': ('Покупатель', 'Client', 'Customer', 'Cliente'),
}


def форма_документа(имя):
    ф = прочитать(ОБРАЗЕЦ.format('ФормаДокумента'))
    счетчик = Счетчик(ф)
    for лишний in ('ХозяйственнаяОперация', 'МестоХраненияОприходование', 'ТЧТоварыРазмещениеСписание',
                   'ТЧТоварыРазмещениеОприходование'):
        удалить(ф, лишний)
    склад = найти(ф, 'МестоХраненияСписание')
    переименовать(склад, 'МестоХраненияСписание', 'МестоХранения')
    заголовок(склад, 'Склад', 'Entrepôt', 'Warehouse', 'Almacén')
    склад.find('handlers/name').text = 'МестоХраненияПриИзменении'
    организация = найти(ф, 'Организация')
    контрагент = клон(ф, 'Организация', 'Контрагент', 'Объект.Контрагент', счетчик)
    заголовок(контрагент, *ЗАГОЛОВКИ_КОНТРАГЕНТА[имя])
    организация.addnext(контрагент)
    основание = клон(ф, 'Организация', 'Основание', 'Объект.Основание', счетчик)
    склад.addnext(основание)
    # Команда «Заполнить» образца без обработчика в модуле ордера (ревью кода фазы 2, P2).
    for к in ф.findall('formCommands'):
        if к.findtext('name') == 'Заполнить':
            ф.remove(к)
    for a in ф.findall('attributes'):
        if a.findtext('name') == 'Объект':
            a.find('valueType/types').text = 'DocumentObject.' + имя
    записать(ф, 'Documents/{}/Forms/ФормаДокумента/Form.form'.format(имя))


def форма_списка(имя):
    ф = прочитать(ОБРАЗЕЦ.format('ФормаСписка'))
    счетчик = Счетчик(ф)
    for лишний in ('МестоХраненияОприходование', 'ХозяйственнаяОперация'):
        удалить(ф, лишний)
    склад = найти(ф, 'МестоХраненияСписание')
    переименовать(склад, 'МестоХраненияСписание', 'МестоХранения')
    контрагент = клон(ф, 'Организация', 'Контрагент', 'Список.Контрагент', счетчик)
    найти(ф, 'Организация').addnext(контрагент)
    for e in ф.iter():
        if e.text and 'Document.ПеремещениеТоваров' in e.text:
            e.text = e.text.replace('Document.ПеремещениеТоваров', 'Document.' + имя)
    записать(ф, 'Documents/{}/Forms/ФормаСписка/Form.form'.format(имя))


for имя in ('ПриходныйОрдер', 'РасходныйОрдер'):
    форма_документа(имя)
    форма_списка(имя)
