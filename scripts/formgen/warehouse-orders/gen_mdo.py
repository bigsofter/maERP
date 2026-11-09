#!/usr/bin/env python3
"""Метаданные ордеров склада (ПриходныйОрдер, РасходныйОрдер) по образцу ПеремещениеТоваров, план
docs/plans/warehouse-orders.md, фаза 2 (2.0.16.77).

Образец - документ без цен с той же ТЧ товаров (КодСтроки, Номенклатура, Характеристика, Упаковка, Серия,
КоличествоУпаковок, Количество). Все uuid, typeId и valueTypeId генерируются заново (tiny1C mdo-009), блок «Контрагент»
берётся из ПоступлениеТоваровУслуг.

    python3 gen_mdo.py   # пишет src/cf/src/Documents/{ПриходныйОрдер,РасходныйОрдер}/*.mdo
"""
import copy
import os
import uuid

from lxml import etree

ЗДЕСЬ = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(ЗДЕСЬ, '..', '..', '..', 'src', 'cf', 'src'))
NS = {'mdclass': 'http://g5.1c.ru/v8/dt/metadata/mdclass', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
      'core': 'http://g5.1c.ru/v8/dt/mcore'}


def прочитать(путь):
    return etree.parse(os.path.join(SRC, путь), etree.XMLParser(remove_blank_text=True)).getroot()


def узел(корень, тег, имя):
    for e in корень.findall(тег):
        if e.findtext('name') == имя:
            return e
    raise KeyError((тег, имя))


def синоним(e, ru, fr, en, es):
    for s in e.findall('synonym'):
        e.remove(s)
    позиция = list(e).index(e.find('name')) + 1
    for i, (k, v) in enumerate((('ru', ru), ('fr', fr), ('en', en), ('es', es))):
        s = etree.Element('synonym')
        etree.SubElement(s, 'key').text = k
        etree.SubElement(s, 'value').text = v
        e.insert(позиция + i, s)


def новые_uuid(корень):
    for e in корень.iter():
        for атр in ('uuid', 'typeId', 'valueTypeId'):
            if атр in e.attrib:
                e.attrib[атр] = str(uuid.uuid4())


def переименовать_ссылки(корень, старое, новое):
    for e in корень.iter():
        if e.text and старое in e.text:
            e.text = e.text.replace(старое, новое)


def собрать(имя, синонимы, основания, движения, основание_типы, расходный):
    образец = прочитать('Documents/ПеремещениеТоваров/ПеремещениеТоваров.mdo')
    doc = copy.deepcopy(образец)
    doc.find('name').text = имя
    синоним(doc, *синонимы)
    переименовать_ссылки(doc, 'Document.ПеремещениеТоваров', 'Document.' + имя)
    # Основания ввода
    for e in doc.findall('basedOn'):
        doc.remove(e)
    позиция = list(doc).index(doc.find('createOnInput'))
    for i, осн in enumerate(основания):
        b = etree.Element('basedOn')
        b.text = осн
        doc.insert(позиция + i, b)
    # Движения
    for e in doc.findall('registerRecords'):
        doc.remove(e)
    позиция = list(doc).index(doc.find('postInPrivilegedMode'))
    for i, рег in enumerate(движения):
        r = etree.Element('registerRecords')
        r.text = рег
        doc.insert(позиция + i, r)
    # Удаление движений - автоматически (документ-образец реализации так же)
    rd = etree.Element('registerRecordsDeletion')
    rd.text = 'AutoDelete'
    doc.insert(list(doc).index(doc.find('realTimePosting')) + 1, rd)
    # Реквизиты шапки
    for лишний in ('МестоХраненияОприходование', 'ХозяйственнаяОперация'):
        doc.remove(узел(doc, 'attributes', лишний))
    контрагент = copy.deepcopy(узел(прочитать('Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo'),
                                    'attributes', 'Контрагент'))
    if расходный:
        синоним(контрагент, 'Покупатель', 'Client', 'Customer', 'Cliente')
        контрагент.find('choiceParameters/name').text = 'Отбор.Покупатель'
    else:
        синоним(контрагент, 'Поставщик', 'Fournisseur', 'Supplier', 'Proveedor')
    # Контрагент необязателен: ордер без основания (внутренний приход/расход) его может не иметь.
    fc = контрагент.find('fillChecking')
    if fc is not None:
        контрагент.remove(fc)
    doc.insert(list(doc).index(узел(doc, 'attributes', 'МестоХранения')), контрагент)
    основание = узел(doc, 'attributes', 'Основание')
    тип = основание.find('type')
    for t in тип.findall('types'):
        тип.remove(t)
    for т in основание_типы:
        etree.SubElement(тип, 'types').text = т
    # Формы: документа и списка
    doc.remove(узел(doc, 'forms', 'ФормаСпискаИнтерфейсКассира'))
    # Макеты и команды перемещения не переносятся (печать - фирменным адаптером)
    for тег in ('templates', 'commands'):
        for e in doc.findall(тег):
            doc.remove(e)
    # ТЧ товаров: КодСтрокиЗаказа после Количество
    тч = узел(doc, 'tabularSections', 'ТЧТовары')
    код = узел(тч, 'attributes', 'КодСтроки')
    код_заказа = copy.deepcopy(код)
    код_заказа.find('name').text = 'КодСтрокиЗаказа'
    синоним(код_заказа, 'Код строки заказа', 'Code de ligne de commande', 'Order line code', 'Código de línea del pedido')
    тч.append(код_заказа)
    if расходный:
        состав = copy.deepcopy(тч)
        состав.find('name').text = 'ТЧФизическийСостав'
        синоним(состав, 'Физический состав', 'Composition physique', 'Physical composition', 'Composición física')
        for e in list(состав.findall('attributes')):
            if e.findtext('name') not in ('КодСтроки', 'Номенклатура', 'Количество'):
                состав.remove(e)
        количество = узел(состав, 'attributes', 'Количество')
        количество.find('name').text = 'КоличествоНаЕдиницу'
        синоним(количество, 'Количество на единицу', 'Quantité par unité', 'Quantity per unit', 'Cantidad por unidad')
        номенклатура = узел(состав, 'attributes', 'Номенклатура')
        синоним(номенклатура, 'Составляющая', 'Composant', 'Component', 'Componente')
        for e in номенклатура.findall('choiceParameterLinks') + номенклатура.findall('choiceParameters'):
            номенклатура.remove(e)
        # Снимок состава пишет проведение (ПередЗаписью) - проверка заполнения его не требует.
        for e in list(состав.iter('fillChecking')):
            e.getparent().remove(e)
        doc.append(состав)
    новые_uuid(doc)
    каталог = os.path.join(SRC, 'Documents', имя)
    os.makedirs(каталог, exist_ok=True)
    текст = etree.tostring(doc, encoding='unicode', pretty_print=True)
    with open(os.path.join(каталог, имя + '.mdo'), 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + текст)


собрать('ПриходныйОрдер',
        ('Приходный ордер на товары', 'Bon de réception', 'Goods receipt order', 'Orden de entrada de mercancías'),
        ['Document.ЗаказПоставщику', 'Document.ЗаказПокупателя', 'Document.РеализацияТоваровУслуг'],
        ['AccumulationRegister.ТоварыНаСкладах', 'AccumulationRegister.ТоварыКОформлению',
         'AccumulationRegister.ЗаказыПоставщикам', 'AccumulationRegister.ПотребностиПроизводства'],
        ['DocumentRef.ЗаказПоставщику', 'DocumentRef.ЗаказПокупателя', 'DocumentRef.РеализацияТоваровУслуг'],
        False)
собрать('РасходныйОрдер',
        ('Расходный ордер на товары', 'Bon de sortie', 'Goods issue order', 'Orden de salida de mercancías'),
        ['Document.ЗаказПокупателя', 'Document.ПоступлениеТоваровУслуг'],
        ['AccumulationRegister.ТоварыНаСкладах', 'AccumulationRegister.ТоварыКОформлению'],
        ['DocumentRef.ЗаказПокупателя', 'DocumentRef.ПоступлениеТоваровУслуг'],
        True)
