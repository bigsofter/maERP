#!/usr/bin/env python3
"""Очередь «К оформлению» в формах списков ордеров (план warehouse-orders, фаза 4, §4.1): произвольный запрос списка с
колонкой неоформленного остатка, флажок «Только к оформлению» в панели фильтров, команда «Оформить» в командной
панели списка. Запуск после gen_forms.py: python3 scripts/formgen/warehouse-orders/queue.py
"""
import copy
import os
import re

from lxml import etree

SRC = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src', 'cf', 'src')
XSI = 'http://www.w3.org/2001/XMLSchema-instance'

ЗАПРОС = '''ВЫБРАТЬ
	Док.Ссылка КАК Ссылка,
	Док.Номер КАК Номер,
	Док.Дата КАК Дата,
	Док.Проведен КАК Проведен,
	Док.ПометкаУдаления КАК ПометкаУдаления,
	Док.Организация КАК Организация,
	Док.Контрагент КАК Контрагент,
	Док.МестоХранения КАК МестоХранения,
	Док.Основание КАК Основание,
	Док.Ответственный КАК Ответственный,
	Док.Комментарий КАК Комментарий,
	ЕСТЬNULL(Остатки.КОформлению, 0) КАК КОформлению
ИЗ
	Документ.{имя} КАК Док
		ЛЕВОЕ СОЕДИНЕНИЕ (ВЫБРАТЬ
			Неоформленные.Ордер КАК Ордер,
			СУММА(Неоформленные.КоличествоОстаток) КАК КОформлению
		ИЗ
			РегистрНакопления.ТоварыКОформлению.Остатки(, Составляющая = ЗНАЧЕНИЕ(Справочник.Номенклатура.ПустаяСсылка)) КАК Неоформленные
		СГРУППИРОВАТЬ ПО
			Неоформленные.Ордер) КАК Остатки
		ПО Док.Ссылка = Остатки.Ордер'''

КОМАНДЫ = {
    'ПриходныйОрдер': ('Оформить поступлением', 'Régulariser par une réception', 'Document with a receipt',
                       'Formalizar con una recepción'),
    'РасходныйОрдер': ('Оформить реализацией', 'Régulariser par une vente', 'Document with a sale',
                       'Formalizar con una venta'),
}


def прочитать(путь):
    return etree.parse(os.path.join(SRC, путь), etree.XMLParser(remove_blank_text=True)).getroot()


def элемент(корень, имя):
    for e in корень.iter('items'):
        if e.findtext('name') == имя:
            return e
    raise KeyError(имя)


def локализ(тег, значения):
    res = []
    for k, v in zip(('ru', 'fr', 'en', 'es'), значения):
        t = etree.Element(тег)
        etree.SubElement(t, 'key').text = k
        etree.SubElement(t, 'value').text = v
        res.append(t)
    return res


def привести(имя):
    путь = 'Documents/{}/Forms/ФормаСписка/Form.form'.format(имя)
    ф = прочитать(путь)
    ids = [int(i.text) for i in ф.iter('id') if re.fullmatch(r'\d+', i.text or '')]
    счетчик = iter(range(max(ids) + 1, 10 ** 6))

    # 1. Произвольный запрос списка.
    список = [a for a in ф.findall('attributes') if a.findtext('name') == 'Список'][0]
    ext = список.find('extInfo')
    if ext.find('queryText') is None:
        q = etree.Element('queryText')
        q.text = ЗАПРОС.replace('{имя}', имя)
        ext.insert(0, q)
        cq = etree.Element('customQuery')
        cq.text = 'true'
        ext.find('autoFillAvailableFields').addnext(cq)

    # 2. Колонка «К оформлению».
    таблица = элемент(ф, 'Список')
    образец = элемент(таблица, 'Комментарий')
    колонка = copy.deepcopy(образец)
    for n in колонка.iter('name'):
        n.text = n.text.replace('Комментарий', 'КОформлению')
    for i in колонка.iter('id'):
        i.text = str(next(счетчик))
    колонка.find('visible').text = 'true'
    колонка.find('dataPath/segments').text = 'Список.КОформлению'
    позиция = list(колонка).index(колонка.find('titleFont'))
    for t in reversed(локализ('title', ('К оформлению', 'À régulariser', 'To document', 'Por formalizar'))):
        колонка.insert(позиция, t)
    элемент(таблица, 'МестоХранения').addnext(колонка)

    # 3. Флажок «Только к оформлению» в панели фильтров.
    реквизит = copy.deepcopy([a for a in ф.findall('attributes') if a.findtext('name') == 'ОтборСклад'][0])
    реквизит.find('name').text = 'ОтборКОформлению'
    реквизит.find('id').text = str(max(int(a.findtext('id')) for a in ф.findall('attributes')) + 1)
    реквизит.find('valueType/types').text = 'Boolean'
    последний = ф.findall('attributes')[-1]
    последний.addnext(реквизит)
    поле = copy.deepcopy(элемент(ф, 'ОтборСклад'))
    for n in поле.iter('name'):
        if n.text and n.text.startswith('ОтборСклад'):
            n.text = n.text.replace('ОтборСклад', 'ОтборКОформлению')
    for i in поле.iter('id'):
        i.text = str(next(счетчик))
    for t in поле.findall('title'):
        поле.remove(t)
    позиция = list(поле).index(поле.find('visible'))
    for t in reversed(локализ('title', ('Только к оформлению', 'À régulariser seulement', 'To document only',
                                        'Solo por formalizar'))):
        поле.insert(позиция, t)
    поле.find('dataPath/segments').text = 'ОтборКОформлению'
    поле.find('titleLocation').text = 'Right'
    поле.find('type').text = 'CheckBoxField'
    поле.remove(поле.find('editMode'))
    ext_поля = поле.find('extInfo')
    поле.remove(ext_поля)
    etree.SubElement(поле, 'extInfo').set('{%s}type' % XSI, 'form:CheckBoxFieldExtInfo')
    элемент(ф, 'ОтборОтветственный').addnext(поле)

    # 4. Команда «Оформить».
    образец_команды = [c for c in ф.findall('formCommands') if c.findtext('name') == 'СтраницаВперед'][0]
    команда = copy.deepcopy(образец_команды)
    команда.find('name').text = 'Оформить'
    команда.find('id').text = str(max(int(c.findtext('id')) for c in ф.findall('formCommands')) + 1)
    for t in команда.findall('title') + команда.findall('toolTip'):
        команда.remove(t)
    позиция = list(команда).index(команда.find('id'))
    for t in reversed(локализ('title', КОМАНДЫ[имя])):
        команда.insert(позиция, t)
    for t in reversed(локализ('toolTip', КОМАНДЫ[имя])):
        команда.insert(позиция + 5, t)
    команда.find('action/handler/name').text = 'Оформить'
    ф.findall('formCommands')[-1].addnext(команда)
    кнопка = copy.deepcopy(элемент(ф, 'КнопкаСтраницаВперед'))
    for n in кнопка.iter('name'):
        n.text = n.text.replace('КнопкаСтраницаВперед', 'КнопкаОформить')
    for i in кнопка.iter('id'):
        i.text = str(next(счетчик))
    кнопка.find('commandName').text = 'Form.Command.Оформить'
    панель = таблица.find('autoCommandBar')
    кнопка.find('representation').text = 'PictureAndText'
    позиция = list(панель).index(панель.find('id')) + 1
    панель.insert(позиция, кнопка)

    текст = etree.tostring(ф, encoding='unicode', pretty_print=True)
    with open(os.path.join(SRC, путь), 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + текст)
    print('ok', имя)


for имя in ('ПриходныйОрдер', 'РасходныйОрдер'):
    привести(имя)
