#!/usr/bin/env python3
"""Карточка товара (Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form), этап 3 плана docs/plans/nomenclature-ui.md.

Перегруппировка по важности без потери элементов: элементы переносятся узлами XML (имена не меняются - на них
ссылается модуль), новые узлы - копии соседних элементов этой же формы (tiny1C workflow-005). Исходная форма - из git
(коммит БАЗА), id элементов и реквизитов перенумеровываются (forms-001, forms-018).

    python3 card.py > /tmp/card.form && cp /tmp/card.form ../../../src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form

Закладки: Основное | Цены | Склад | Производство | Комплект | Свойства | Описание и печать | Служебное.
"""
import copy
import os
import subprocess
import sys

from lxml import etree

ЗДЕСЬ = os.path.dirname(os.path.abspath(__file__))
КОРЕНЬ = os.path.normpath(os.path.join(ЗДЕСЬ, '..', '..', '..'))
БАЗА = 'b87bc9b'
ФОРМА = 'src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form'
XSI = 'http://www.w3.org/2001/XMLSchema-instance'
ЯЗЫКИ = ('ru', 'fr', 'en', 'es')

парсер = etree.XMLParser(remove_blank_text=True)
исходник = subprocess.run(['git', '-C', КОРЕНЬ, 'show', f'{БАЗА}:{ФОРМА}'], capture_output=True, check=True).stdout
форма = etree.fromstring(исходник, парсер)


def найти(имя, корень=None):
    for e in (форма if корень is None else корень).iter('items'):
        if e.findtext('name') == имя:
            return e
    raise KeyError(имя)


def извлечь(имя):
    e = найти(имя)
    e.getparent().remove(e)
    return e


def переименовать(e, старое, новое):
    for n in e.iter('name'):
        if n.text and n.text.startswith(старое) and n.getparent().tag in ('items', 'extendedTooltip', 'contextMenu',
                                                                           'autoCommandBar'):
            n.text = новое + n.text[len(старое):]


def локализация(e, тег, значения, после):
    for t in e.findall(тег):
        e.remove(t)
    if значения is None:
        return
    позиция = list(e).index(e.find(после)) + 1
    for i, (язык, текст) in enumerate(zip(ЯЗЫКИ, значения)):
        t = etree.Element(тег)
        etree.SubElement(t, 'key').text = язык
        etree.SubElement(t, 'value').text = текст
        e.insert(позиция + i, t)


def видимый(e):
    """Элемент без <visible> скрыт (tiny1C forms-012): скрытые блоки возвращаются на свои закладки."""
    v = e.find('visible')
    if v is None:
        v = etree.Element('visible')
        якорь = e.find('enabled')
        e.insert(list(e).index(якорь), v)
    v.text = 'true'
    return e


def дети(группа, элементы, перед=None):
    """Дочерние элементы - перед указанным ребёнком или в конец (перед служебными тегами группы)."""
    if перед is not None:
        позиция = list(группа).index(перед)
    else:
        позиция = list(группа).index(группа.find('type'))
    for i, e in enumerate(элементы):
        группа.insert(позиция + i, e)
    return группа


def обработчик(e, событие, имя, перед):
    h = etree.Element('handlers')
    etree.SubElement(h, 'event').text = событие
    etree.SubElement(h, 'name').text = имя
    e.insert(list(e).index(e.find(перед)), h)


def страница(имя, заголовок):
    e = copy.deepcopy(найти('СтраницаОписание'))
    for c in e.findall('items'):
        e.remove(c)
    переименовать(e, 'СтраницаОписание', имя)
    локализация(e, 'title', заголовок, после='userVisible')
    локализация(e, 'toolTip', None, после='userVisible')
    ext = e.find('extInfo')
    if ext.find('picture') is not None:
        ext.remove(ext.find('picture'))
    return e


def группа(имя, заголовок=None, вид='Vertical'):
    """Обычная группа без рамки (FORMS-STYLE, правила 1-3); заголовок - у разделов внутри закладки."""
    e = copy.deepcopy(найти('ГруппаНаименование'))
    for c in e.findall('items'):
        e.remove(c)
    переименовать(e, 'ГруппаНаименование', имя)
    локализация(e, 'title', заголовок, после='userVisible')
    локализация(e, 'toolTip', None, после='userVisible')
    ext = e.find('extInfo')
    ext.find('group').text = вид
    показ = ext.find('showTitle')
    if показ is None:
        показ = etree.Element('showTitle')
        ext.insert(list(ext).index(ext.find('throughAlign')), показ)
    показ.text = 'true' if заголовок else 'false'
    return e


def в_группу(страница_):
    """Бывшая закладка - раздел внутри новой закладки: имя то же (на него ссылается модуль), заголовок виден."""
    страница_.find('type').text = 'UsualGroup'
    ext = страница_.find('extInfo')
    новый = etree.Element('extInfo')
    новый.set('{%s}type' % XSI, 'form:UsualGroupExtInfo')
    for тег, значение in (('group', 'Vertical'), ('behavior', 'Auto'), ('representation', 'None'),
                          ('showLeftMargin', 'true'), ('united', 'true'), ('showTitle', 'true'),
                          ('throughAlign', 'Auto'), ('currentRowUse', 'Auto')):
        etree.SubElement(новый, тег).text = значение
    страница_.replace(ext, новый)
    return страница_


def поле(образец, имя, путь_, заголовок=None):
    e = copy.deepcopy(найти(образец))
    переименовать(e, образец, имя)
    e.find('dataPath/segments').text = путь_
    локализация(e, 'title', заголовок, после='id')
    return e


страницы = найти('ГруппаСтраницы')

# --- шапка: наименование и артикул, тип, папка, живые показатели ---------------------------------------------------------

шапка = найти('ГруппаНаименование')
код = извлечь('Код')
тип = извлечь('ТипНоменклатуры')
папка = извлечь('Родитель')
показатели = поле('ПлановаяСебестоимостьТехкарты', 'ПоказателиШапки', 'ПоказателиШапки')
строка_типа = группа('ГруппаШапкаТип', вид='HorizontalIfPossible')
дети(строка_типа, [тип])
строка_папки = группа('ГруппаШапкаПапка', вид='HorizontalIfPossible')
дети(строка_папки, [папка, показатели])
право = найти('ГруппаПраво')
дети(право, [строка_типа, строка_папки], перед=страницы)

# --- Основное (бывшая «Реквизиты») ------------------------------------------------------------------------------------

основное = найти('СтраницаРеквизиты')
локализация(основное, 'title', ('Основное', 'Principal', 'Main', 'Principal'), после='userVisible')
полное = извлечь('НаименованиеПолное')
код_старый = извлечь('КодСтарый')
упаковки = извлечь('ГруппаУпаковки')
видимый(найти('ТоварнаяГруппа'))
видимый(найти('Производитель'))
видимый(найти('Импортер'))
# Классификация первой: группа сегментов - в начало закладки.
сегменты = извлечь('ГруппаСегменты')
основное.insert(list(основное).index(основное.find('items')), сегменты)

# --- Склад (бывшая «Хранение»): минимумы, ячейки, упаковки, ограничения хранения ---------------------------------------

склад = найти('СтраницаХранение')
локализация(склад, 'title', ('Склад', 'Stock', 'Stock', 'Almacén'), после='userVisible')
видимый(найти('ГруппаОграничения'))
видимый(найти('ВыводитьНаПечатьДатуУпаковки'))
# Порядок: минимумы и ячейки, упаковки, условия хранения.
правая = извлечь('ГруппаХранениеПравая')
дети(склад, [видимый(упаковки), правая])

# --- Производство: техкарта и станки разделами одной закладки ------------------------------------------------------------

производство = страница('СтраницаПроизводство', ('Производство', 'Production', 'Production', 'Producción'))
техкарта = в_группу(извлечь('СтраницаТехкарта'))
станки = в_группу(извлечь('СтраницаСтанки'))
дети(производство, [техкарта, станки])

# --- Описание и печать: описание и данные стикера -----------------------------------------------------------------------

описание = найти('СтраницаОписание')
локализация(описание, 'title', ('Описание и печать', 'Description et impression', 'Description and printing',
                                'Descripción e impresión'), после='userVisible')
стикер = извлечь('СтраницаСтикер')
раздел_стикера = группа('ГруппаСтикер', ('Стикер', 'Étiquette', 'Sticker', 'Etiqueta'))
дети(раздел_стикера, [c for c in стикер.findall('items')])
дети(описание, [раздел_стикера])

# --- Свойства (бывшая «Дополнительно») ----------------------------------------------------------------------------------

свойства = найти('СтраницаДополнительно')
локализация(свойства, 'title', ('Свойства', 'Propriétés', 'Properties', 'Propiedades'), после='userVisible')

# --- Служебное ----------------------------------------------------------------------------------------------------------

низ = извлечь('ГруппаНиз')
служебное = страница('СтраницаСлужебное', ('Служебное', 'Service', 'Service', 'Servicio'))
ответственный = поле('Бренд', 'Ответственный', 'Объект.Ответственный')
# Заголовок поля - слева (FORMS-STYLE, правило 5; ревью кода Codex 2.0.16.62, P3).
слева = etree.Element('titleLocation')
слева.text = 'Left'
ответственный.insert(list(ответственный).index(ответственный.find('dataPath')) + 1, слева)
ecommerce = поле('ВыводитьНаПечатьОписание', 'ECommerce', 'Объект.ECommerce')
лкп = поле('ВыводитьНаПечатьОписание', 'ОтражатьвЛКП', 'Объект.ОтражатьвЛКП')
дети(служебное, [видимый(код), код_старый, видимый(полное), ответственный, ecommerce, лкп]
     + [c for c in низ.findall('items')])

# --- порядок закладок ---------------------------------------------------------------------------------------------------

цены = извлечь('ГруппаЦены')
комплект = извлечь('СтраницаКомплект')
старые_свойства = извлечь('ГруппаСвойства')
for имя in ('СтраницаРеквизиты', 'СтраницаХранение', 'СтраницаДополнительно', 'СтраницаОписание'):
    извлечь(имя)
for c in страницы.findall('items'):
    raise SystemExit('неразобранная закладка: ' + c.findtext('name'))
дети(страницы, [основное, цены, склад, производство, комплект, свойства, старые_свойства, описание, служебное])
обработчик(страницы, 'OnCurrentPageChange', 'ГруппаСтраницыПриСменеСтраницы', перед='extendedTooltip')

# --- реквизиты ----------------------------------------------------------------------------------------------------------


def реквизит(имя, тип_):
    a = etree.Element('attributes')
    etree.SubElement(a, 'name').text = имя
    etree.SubElement(a, 'id').text = '0'
    vt = etree.SubElement(a, 'valueType')
    etree.SubElement(vt, 'types').text = тип_
    if тип_ == 'String':
        etree.SubElement(vt, 'stringQualifiers')
    for тег in ('view', 'edit'):
        etree.SubElement(etree.SubElement(a, тег), 'common').text = 'true'
    return a


последний = форма.findall('attributes')[-1]
позиция = list(форма).index(последний)
for i, (имя, тип_) in enumerate((('ПоказателиШапки', 'String'), ('ЦеныЗагружены', 'Boolean'),
                                 ('ТехкартаЗагружена', 'Boolean'), ('ИспользоватьУпаковку', 'Boolean'),
                                 ('ИспользоватьИмпорт', 'Boolean'), ('ИспользоватьКомплектацию', 'Boolean'),
                                 ('ЭтоКассир', 'Boolean')), 1):
    форма.insert(позиция + i, реквизит(имя, тип_))
for номер, a in enumerate(форма.findall('attributes'), 1):
    a.find('id').text = str(номер)

# id элементов: сквозной счётчик по дереву элементов.
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
