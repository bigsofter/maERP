#!/usr/bin/env python3
"""Форма списка товаров (Catalogs/Номенклатура/Forms/ФормаСписка/Form.form), этап 1 плана docs/plans/nomenclature-ui.md.

Исходная форма (до этапа 1) берётся из git (коммит БАЗА), панель «Сведения» - из формы списка реализаций (FORMS-STYLE,
правило 6; урок tiny1C workflow-005: новую конструкцию брать по работающему образцу), флажок - из рабочего места закупок.
Таблица списка сохраняет колонки (лишние скрываются, «Продажи» удаляется), запрос динсписка - текст
Справочники.Номенклатура.ТекстЗапросаСписка() из модуля менеджера (форма ставит его же при создании).

    python3 list.py > ../../../src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
"""
import copy
import os
import re
import subprocess
import sys

from lxml import etree

ЗДЕСЬ = os.path.dirname(os.path.abspath(__file__))
КОРЕНЬ = os.path.normpath(os.path.join(ЗДЕСЬ, '..', '..', '..'))
БАЗА = '0da61db'
ФОРМА = 'src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form'
ОБРАЗЕЦ = os.path.join(КОРЕНЬ, 'src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Form.form')
ОБРАЗЕЦ_ФЛАЖКА = os.path.join(КОРЕНЬ, 'src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Form.form')
МЕНЕДЖЕР = os.path.join(КОРЕНЬ, 'src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl')
XSI = 'http://www.w3.org/2001/XMLSchema-instance'
ЯЗЫКИ = ('ru', 'fr', 'en', 'es')

парсер = etree.XMLParser(remove_blank_text=True)
исходник = subprocess.run(['git', '-C', КОРЕНЬ, 'show', f'{БАЗА}:{ФОРМА}'], capture_output=True, check=True).stdout
форма = etree.fromstring(исходник, парсер)
образец = etree.parse(ОБРАЗЕЦ, парсер).getroot()
образец_флажка = etree.parse(ОБРАЗЕЦ_ФЛАЖКА, парсер).getroot()


def найти(корень, имя, тег='items'):
    for e in корень.iter(тег):
        if e.findtext('name') == имя:
            return e
    raise KeyError(имя)


def копия(корень, имя, без_детей=False):
    e = copy.deepcopy(найти(корень, имя))
    if без_детей:
        for c in e.findall('items'):
            e.remove(c)
    return e


def удалить(корень, имя):
    e = найти(корень, имя)
    e.getparent().remove(e)


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


def путь(e, значение):
    e.find('dataPath/segments').text = значение


def обработчик(e, событие, имя, перед):
    h = etree.Element('handlers')
    etree.SubElement(h, 'event').text = событие
    etree.SubElement(h, 'name').text = имя
    e.insert(list(e).index(e.find(перед)), h)


def вставить_после(якорь, новые):
    родитель = якорь.getparent()
    позиция = list(родитель).index(якорь)
    for i, n in enumerate(новые, 1):
        родитель.insert(позиция + i, n)


# --- таблица списка ----------------------------------------------------------------------------------------------------

таблица = найти(форма, 'Список')
ВИДИМЫЕ = ('ЕстьФайлы', 'Наименование', 'Артикул', 'Единица', 'КоличествоОстаток', 'РозничнаяЦена')
удалить(таблица, 'Продажи')
единица = копия(таблица, 'Бренд')
переименовать(единица, 'Бренд', 'Единица')
путь(единица, 'Список.Единица')
локализация(единица, 'title', ('Ед.', 'Unité', 'Unit', 'Unidad'), после='id')
вставить_после(найти(таблица, 'Артикул'), [единица])
# Колонки вне основных - скрыты пользовательской видимостью (userVisible), а не visible: их можно включить через
# «Ещё → Изменить форму» (ревью кода Codex 2.0.16.60, P2).
for колонка in таблица.findall('items'):
    видимость = колонка.find('visible')
    значение = 'true'
    колонка.find('userVisible/common').text = 'true' if колонка.findtext('name') in ВИДИМЫЕ else 'false'
    if видимость is None:
        видимость = etree.Element('visible')
        # Порядок тегов EDT: title, titleFont, visible.
        якорь = колонка.find('titleFont')
        if якорь is None:
            якорь = (колонка.findall('title') or [колонка.find('id')])[-1]
        колонка.insert(list(колонка).index(якорь) + 1, видимость)
    видимость.text = значение
обработчик(таблица, 'OnActivateRow', 'СписокПриАктивизацииСтроки', перед='commandBarLocation')
высота = etree.Element('heightInTableRows')
высота.text = '20'
таблица.insert(list(таблица).index(таблица.find('autoMaxRowsCount')), высота)

# --- панель сведений ---------------------------------------------------------------------------------------------------

панель = копия(образец, 'ГруппаПанельСведений')
for имя in ('ОтборКонтрагент', 'ОтборОрганизация', 'ОтборОтветственный', 'ГруппаОтборСумма', 'ГруппаОтборДолг'):
    удалить(панель, имя)

ТУМБЛЕРЫ = {
    'ФильтрТип': (('Тип', 'Type', 'Type', 'Tipo'), 4, [
        ('Все', 'Tous', 'All', 'Todos'), ('Товар', 'Marchandise', 'Goods', 'Mercancía'),
        ('Услуга', 'Service', 'Service', 'Servicio'), ('Продукция', 'Produit fini', 'Product', 'Producto'),
        ('Полуфабрикат', 'Semi-fini', 'Semi-finished', 'Semielaborado'),
        ('Сырьё', 'Matière première', 'Raw material', 'Materia prima'), ('Комплект', 'Kit', 'Kit', 'Kit')]),
    'ФильтрПополнение': (('Пополнение', 'Réapprovisionnement', 'Replenishment', 'Reposición'), 4, [
        ('Все', 'Tous', 'All', 'Todos'), ('Закупка', 'Achat', 'Purchase', 'Compra'),
        ('Производство', 'Production', 'Production', 'Producción'), ('Оба', 'Les deux', 'Both', 'Ambos')]),
    'ФильтрНаличие': (('Наличие', 'Disponibilité', 'Availability', 'Disponibilidad'), 2, [
        ('Все', 'Tous', 'All', 'Todos'), ('В наличии', 'En stock', 'In stock', 'En stock'),
        ('Нет в наличии', 'En rupture', 'Out of stock', 'Agotado'),
        ('Ниже минимума', 'Sous le minimum', 'Below minimum', 'Bajo mínimo')]),
}
образец_тумблера = найти(панель, 'ФильтрОперации')
тумблеры = []
for имя, (заголовок, колонок, позиции) in ТУМБЛЕРЫ.items():
    e = copy.deepcopy(образец_тумблера)
    переименовать(e, 'ФильтрОперации', имя)
    путь(e, имя)
    локализация(e, 'title', заголовок, после='id')
    e.find('handlers/name').text = 'ФильтрПанелиПриИзменении'
    ext = e.find('extInfo')
    for c in ext.findall('choiceList'):
        ext.remove(c)
    if ext.find('columnsCount') is None:
        cc = etree.Element('columnsCount')
        ext.insert(list(ext).index(ext.find('radioButtonsType')) + 1, cc)
    ext.find('columnsCount').text = str(колонок)
    for номер, подписи in enumerate(позиции):
        cl = etree.SubElement(ext, 'choiceList')
        for язык, текст in zip(ЯЗЫКИ, подписи):
            p = etree.SubElement(cl, 'presentation')
            etree.SubElement(p, 'key').text = язык
            etree.SubElement(p, 'value').text = текст
        v = etree.SubElement(cl, 'value')
        v.set('{%s}type' % XSI, 'core:NumberValue')
        etree.SubElement(v, 'value').text = str(номер)
    тумблеры.append(e)

склад = найти(панель, 'ОтборСклад')
склад.find('handlers/name').text = 'ФильтрПанелиПриИзменении'
ПОЛЯ = {
    'ОтборТоварнаяГруппа': ('Товарная группа', 'Groupe de marchandises', 'Product group', 'Grupo de mercancías'),
    'ОтборБренд': ('Бренд', 'Marque', 'Brand', 'Marca'),
    'ОтборПоставщик': ('Основной поставщик', 'Fournisseur principal', 'Main supplier', 'Proveedor principal'),
    'ОтборКачество': ('Качество', 'Qualité', 'Quality', 'Calidad'),
}
поля = []
for имя, заголовок in ПОЛЯ.items():
    e = copy.deepcopy(склад)
    переименовать(e, 'ОтборСклад', имя)
    путь(e, имя)
    локализация(e, 'title', заголовок, после='id')
    поля.append(e)
флажок = копия(образец_флажка, 'ТолькоДефицит')
переименовать(флажок, 'ТолькоДефицит', 'ПоказыватьПомеченные')
путь(флажок, 'ПоказыватьПомеченные')
локализация(флажок, 'title', ('Показывать помеченные на удаление', 'Afficher les éléments marqués pour suppression',
                              'Show items marked for deletion', 'Mostrar marcados para eliminar'), после='id')
флажок.find('handlers/name').text = 'ФильтрПанелиПриИзменении'
вставить_после(образец_тумблера, тумблеры)
удалить(панель, 'ФильтрОперации')
вставить_после(склад, поля + [флажок])

# Закладки «Товар» и «Движение» - из «Клиент» и «Детали» образца.
стр_товар = найти(панель, 'СтраницаКлиент')
переименовать(стр_товар, 'СтраницаКлиент', 'СтраницаТовар')
локализация(стр_товар, 'title', ('Товар', 'Article', 'Item', 'Artículo'), после='id')
текст_товара = найти(стр_товар, 'КлиентТекст')
переименовать(текст_товара, 'КлиентТекст', 'ТоварТекст')
путь(текст_товара, 'ТоварТекст')
стр_движение = найти(панель, 'СтраницаИнфо')
переименовать(стр_движение, 'СтраницаИнфо', 'СтраницаДвижение')
локализация(стр_движение, 'title', ('Движение', 'Mouvements', 'Movement', 'Movimientos'), после='id')
текст_движения = найти(стр_движение, 'ИнфоТекст')
переименовать(текст_движения, 'ИнфоТекст', 'ДвижениеТекст')
путь(текст_движения, 'ДвижениеТекст')
остатки = найти(стр_движение, 'ТаблицаСостав')
переименовать(остатки, 'ТаблицаСостав', 'ОстаткиПоСкладам')
путь(остатки, 'ОстаткиПоСкладам')
for старое, новое, заголовок in (
        ('Номенклатура', 'Склад', ('Склад', 'Entrepôt', 'Warehouse', 'Almacén')),
        ('Количество', 'Остаток', ('Остаток', 'Stock', 'Stock', 'Existencias')),
        ('Сумма', 'Свободно', ('Свободно', 'Libre', 'Free', 'Libre'))):
    кол = найти(остатки, 'ОстаткиПоСкладам' + старое)
    переименовать(кол, 'ОстаткиПоСкладам' + старое, 'ОстаткиПоСкладам' + новое)
    путь(кол, 'ОстаткиПоСкладам.' + новое)
    локализация(кол, 'title', заголовок, после='id')
# Таблица остатков - над текстом движения: склад читается первым.
стр_движение.remove(остатки)
стр_движение.insert(list(стр_движение).index(текст_движения), остатки)

for старое, новое, команда in (('КнопкаПоказатьКлиента', 'КнопкаПоказатьТовар', 'ПоказатьТовар'),
                                ('КнопкаПоказатьДетали', 'КнопкаПоказатьДвижение', 'ПоказатьДвижение')):
    кнопка = найти(панель, старое)
    переименовать(кнопка, старое, новое)
    кнопка.find('commandName').text = 'Form.Command.' + команда

# --- раскладка: главная группа (список слева, панель справа) -------------------------------------------------------------

главная = копия(образец, 'ГруппаГлавная', без_детей=True)
левая = копия(образец, 'ГруппаЛевая', без_детей=True)
группа_списка = найти(форма, 'ГруппаСписок')
if группа_списка.find('visible') is None:
    v = etree.Element('visible')
    v.text = 'true'
    группа_списка.insert(list(группа_списка).index(группа_списка.find('enabled')), v)
форма.remove(группа_списка)
левая.insert(list(левая).index(левая.find('type')), группа_списка)
главная.insert(list(главная).index(главная.find('type')), левая)
главная.insert(list(главная).index(главная.find('type')), панель)
форма.insert(0, главная)

# --- этап 2: навигатор иерархии слева и отбор «свойство = значение» в панели (2.0.16.61) -------------------------------

def значение_узла_тип(vt):
    """Тип значения узла и отбора по свойству: классификаторы режимов и типы значений дополнительных реквизитов."""
    for тип in ('EnumRef.ТипыНоменклатуры', 'EnumRef.СпособыПополненияЗапасов', 'CatalogRef.ТоварныеГруппы',
                'CatalogRef.Бренды', 'CatalogRef.Контрагенты', 'CatalogRef.КачествоТоваров',
                'CatalogRef.ЗначенияДополнительныхРеквизитов', 'CatalogRef.Номенклатура', 'String', 'Date', 'Boolean',
                'Number'):
        etree.SubElement(vt, 'types').text = тип
    q = etree.SubElement(vt, 'numberQualifiers')
    etree.SubElement(q, 'precision').text = '15'
    etree.SubElement(q, 'scale').text = '3'
    q = etree.SubElement(vt, 'stringQualifiers')
    etree.SubElement(q, 'length').text = '200'
    q = etree.SubElement(vt, 'dateQualifiers')
    etree.SubElement(q, 'dateFractions').text = 'Date'


иерархия = копия(образец, 'ГруппаЛевая', без_детей=True)
переименовать(иерархия, 'ГруппаЛевая', 'ГруппаИерархия')
строка_режима = копия(образец, 'ГруппаЛевая', без_детей=True)
переименовать(строка_режима, 'ГруппаЛевая', 'ГруппаРежимИерархии')
строка_режима.find('extInfo/group').text = 'AlwaysHorizontal'

режим = copy.deepcopy(найти(панель, 'ОтборСклад'))
переименовать(режим, 'ОтборСклад', 'РежимИерархии')
путь(режим, 'РежимИерархии')
локализация(режим, 'title', ('Иерархия', 'Hiérarchie', 'Hierarchy', 'Jerarquía'), после='id')
режим.find('titleLocation').text = 'None'
режим.find('handlers/name').text = 'РежимИерархииПриИзменении'
ext = режим.find('extInfo')
lcm = etree.Element('listChoiceMode')
lcm.text = 'true'
ext.insert(list(ext).index(ext.find('textEdit')), lcm)
ext.find('textEdit').text = 'false'

избранное = copy.deepcopy(найти(панель, 'КнопкаСвернутьПанель'))
переименовать(избранное, 'КнопкаСвернутьПанель', 'КнопкаИзбранныйРежим')
избранное.find('commandName').text = 'Form.Command.ИзбранныйРежим'
избранное.find('representation').text = 'Text'
избранное.remove(избранное.find('picture'))
обновить = copy.deepcopy(избранное)
переименовать(обновить, 'КнопкаИзбранныйРежим', 'КнопкаОбновитьИерархию')
обновить.find('commandName').text = 'Form.Command.ОбновитьИерархию'
for c in (режим, избранное, обновить):
    строка_режима.insert(list(строка_режима).index(строка_режима.find('type')), c)

узлы = копия(образец, 'ТаблицаСостав')
переименовать(узлы, 'ТаблицаСостав', 'УзлыИерархии')
путь(узлы, 'УзлыИерархии')
удалить(узлы, 'УзлыИерархииСумма')
for старое, новое, заголовок in (
        ('Номенклатура', 'Представление', ('Значение', 'Valeur', 'Value', 'Valor')),
        ('Количество', 'Количество', ('Товаров', 'Articles', 'Items', 'Artículos'))):
    кол = найти(узлы, 'УзлыИерархии' + старое)
    переименовать(кол, 'УзлыИерархии' + старое, 'УзлыИерархии' + новое)
    путь(кол, 'УзлыИерархии.' + новое)
    локализация(кол, 'title', заголовок, после='id')
обработчик(узлы, 'OnActivateRow', 'УзлыИерархииПриАктивизацииСтроки', перед='extendedTooltip')
for c in (строка_режима, узлы):
    иерархия.insert(list(иерархия).index(иерархия.find('type')), c)
главная.insert(0, иерархия)

# Отбор «свойство = значение» в панели фильтров - после качества.
свойство = copy.deepcopy(найти(панель, 'ОтборКачество'))
переименовать(свойство, 'ОтборКачество', 'ОтборСвойство')
путь(свойство, 'ОтборСвойство')
локализация(свойство, 'title', ('Свойство', 'Propriété', 'Property', 'Propiedad'), после='id')
свойство.find('handlers/name').text = 'ОтборСвойствоПриИзменении'
значение = copy.deepcopy(найти(панель, 'ОтборКачество'))
переименовать(значение, 'ОтборКачество', 'ОтборЗначенияСвойства')
путь(значение, 'ОтборЗначенияСвойства')
локализация(значение, 'title', ('Значение свойства', 'Valeur de la propriété', 'Property value', 'Valor de la propiedad'),
            после='id')
вставить_после(найти(панель, 'ОтборКачество'), [свойство, значение])


# --- запрос динсписка: текст из модуля менеджера, параметры ------------------------------------------------------------

модуль = open(МЕНЕДЖЕР, encoding='utf-8').read()
m = re.search(r'Функция ТекстЗапросаСписка\(.*?Текст =\s*"(.*?)";', модуль, re.S)
текст = '\n'.join(re.sub(r'^\s*\|', '', с) for с in m.group(1).split('\n')).replace('""', '"')
список = найти(форма, 'Список', 'attributes')
ext = список.find('extInfo')
ext.find('queryText').text = текст
for f in ext.findall('fields'):
    if f.findtext('dataPath') == 'Продажи':
        ext.remove(f)
for p in ext.findall('parameters'):
    if p.findtext('name') in ('ТипыНоменклатуры', 'ТипыНоменклатурыУстановлены', 'ТоварныеГруппы',
                              'ТоварныеГруппыУстановлены', 'Период', 'НачалоПериода', 'КонецПериода'):
        ext.remove(p)
установлен = copy.deepcopy([p for p in ext.findall('parameters') if p.findtext('name') == 'ИсключаемыеТипыУстановлены'][0])
установлен.find('name').text = 'СкладУстановлен'
for c, т in zip(установлен.find('title/localValue').findall('content'),
                ('Склад установлен', 'Entrepôt défini', 'Warehouse set', 'Almacén establecido')):
    c.find('value').text = т
ext.append(установлен)

# --- реквизиты и команды ------------------------------------------------------------------------------------------------

def реквизит(имя, тип, сохранять=False, квалификаторы=None):
    a = etree.Element('attributes')
    etree.SubElement(a, 'name').text = имя
    etree.SubElement(a, 'id').text = '0'
    vt = etree.SubElement(a, 'valueType')
    etree.SubElement(vt, 'types').text = тип
    if квалификаторы is not None:
        vt.append(квалификаторы)
    for тег in ('view', 'edit'):
        etree.SubElement(etree.SubElement(a, тег), 'common').text = 'true'
    if сохранять:
        etree.SubElement(a, 'savedData').text = 'true'
    return a


def число(точность, дробь=0):
    q = etree.Element('numberQualifiers')
    etree.SubElement(q, 'precision').text = str(точность)
    if дробь:
        etree.SubElement(q, 'scale').text = str(дробь)
    return q


РЕКВИЗИТЫ = [
    реквизит('ФильтрТип', 'Number', True, число(1)),
    реквизит('ФильтрПополнение', 'Number', True, число(1)),
    реквизит('ФильтрНаличие', 'Number', True, число(1)),
    реквизит('ОтборСклад', 'CatalogRef.МестаХранения', True),
    реквизит('ОтборТоварнаяГруппа', 'CatalogRef.ТоварныеГруппы', True),
    реквизит('ОтборБренд', 'CatalogRef.Бренды', True),
    реквизит('ОтборПоставщик', 'CatalogRef.Контрагенты', True),
    реквизит('ОтборКачество', 'CatalogRef.КачествоТоваров', True),
    реквизит('ПоказыватьПомеченные', 'Boolean', True),
    реквизит('ПанельСвернута', 'Boolean', True),
    реквизит('ТоварТекст', 'String', квалификаторы=etree.Element('stringQualifiers')),
    реквизит('ДвижениеТекст', 'String', квалификаторы=etree.Element('stringQualifiers')),
]
таблица_остатков = реквизит('ОстаткиПоСкладам', 'ValueTable')
for номер, (имя, тип, кв) in enumerate((('Склад', 'CatalogRef.МестаХранения', None),
                                        ('Остаток', 'Number', число(15, 3)), ('Свободно', 'Number', число(15, 3))), 1):
    c = etree.SubElement(таблица_остатков, 'columns')
    etree.SubElement(c, 'name').text = имя
    etree.SubElement(c, 'id').text = str(номер)
    vt = etree.SubElement(c, 'valueType')
    etree.SubElement(vt, 'types').text = тип
    if кв is not None:
        vt.append(кв)
    for тег in ('view', 'edit'):
        etree.SubElement(etree.SubElement(c, тег), 'common').text = 'true'
РЕКВИЗИТЫ.append(таблица_остатков)
РЕКВИЗИТЫ_2 = []
тип_значения = etree.Element('valueType')
значение_узла_тип(тип_значения)
for имя, тип, сохранять, кв in (('РежимИерархии', 'String', True, None), ('ИзбранныеРежимы', 'String', True, None),
                                ('ВидУзла', 'Number', True, число(1)),
                                ('ОтборСвойство', 'ChartOfCharacteristicTypesRef.ДополнительныеРеквизиты', True, None)):
    a = реквизит(имя, тип, сохранять, кв if кв is not None else (etree.Element('stringQualifiers') if тип == 'String'
                                                                   else None))
    РЕКВИЗИТЫ_2.append(a)
for имя in ('ЗначениеУзла', 'ОтборЗначенияСвойства'):
    a = реквизит(имя, 'String', True)
    a.replace(a.find('valueType'), copy.deepcopy(тип_значения))
    РЕКВИЗИТЫ_2.append(a)
таблица_узлов = реквизит('УзлыИерархии', 'ValueTable')
for номер, (имя, тип, кв) in enumerate((('Значение', None, None), ('Представление', 'String', etree.Element('stringQualifiers')),
                                        ('Количество', 'Number', число(10)), ('Вид', 'Number', число(1))), 1):
    c = etree.SubElement(таблица_узлов, 'columns')
    etree.SubElement(c, 'name').text = имя
    etree.SubElement(c, 'id').text = str(номер)
    if тип is None:
        c.append(copy.deepcopy(тип_значения))
    else:
        vt = etree.SubElement(c, 'valueType')
        etree.SubElement(vt, 'types').text = тип
        vt.append(кв)
    for тег in ('view', 'edit'):
        etree.SubElement(etree.SubElement(c, тег), 'common').text = 'true'
РЕКВИЗИТЫ_2.append(таблица_узлов)
РЕКВИЗИТЫ.extend(РЕКВИЗИТЫ_2)
последний = форма.findall('attributes')[-1]
вставить_после(последний, РЕКВИЗИТЫ)
for номер, a in enumerate(форма.findall('attributes'), 1):
    a.find('id').text = str(номер)

КОМАНДЫ = []
for имя, новое, заголовок, подсказка in (
        ('СвернутьПанель', None, None, None), ('РазвернутьПанель', None, None, None), ('ПоказатьФильтры', None, None, None),
        ('ПоказатьКлиента', 'ПоказатьТовар', ('Товар', 'Article', 'Item', 'Artículo'),
         ('Сведения о товаре', 'Informations sur l\'article', 'Item details', 'Datos del artículo')),
        ('ПоказатьДетали', 'ПоказатьДвижение', ('Движение', 'Mouvements', 'Movement', 'Movimientos'),
         ('Остатки, заказы и продажи товара', 'Stocks, commandes et ventes de l\'article', 'Item stock, orders and sales',
          'Existencias, pedidos y ventas del artículo'))):
    к = copy.deepcopy(найти(образец, имя, 'formCommands'))
    if новое:
        к.find('name').text = новое
        к.find('action/handler/name').text = новое
        локализация(к, 'title', заголовок, после='name')
        локализация(к, 'toolTip', подсказка, после='id')
    КОМАНДЫ.append(к)
обновить_к = найти(образец, 'ПоказатьФильтры', 'formCommands')
for имя, заголовок, подсказка in (
        ('ИзбранныйРежим', ('Избранный режим', 'Mode favori', 'Favorite mode', 'Modo favorito'),
         ('Закрепить режим иерархии первым в списке', 'Épingler le mode de hiérarchie en tête de liste',
          'Pin the hierarchy mode at the top of the list', 'Fijar el modo de jerarquía al principio de la lista')),
        ('ОбновитьИерархию', ('↻', '↻', '↻', '↻'),
         ('Пересчитать узлы иерархии', 'Recalculer les nœuds de la hiérarchie', 'Recount hierarchy nodes',
          'Recalcular los nodos de la jerarquía'))):
    к = copy.deepcopy(обновить_к)
    к.find('name').text = имя
    к.find('action/handler/name').text = имя
    локализация(к, 'title', заголовок, после='name')
    локализация(к, 'toolTip', подсказка, после='id')
    КОМАНДЫ.append(к)
вставить_после(форма.findall('attributes')[-1], КОМАНДЫ)
for номер, к in enumerate(КОМАНДЫ, 1):
    к.find('id').text = str(номер)

# --- обработчики и свойства формы ----------------------------------------------------------------------------------------

h = etree.Element('handlers')
etree.SubElement(h, 'event').text = 'OnLoadDataFromSettingsAtServer'
etree.SubElement(h, 'name').text = 'ПриЗагрузкеДанныхИзНастроекНаСервере'
вставить_после(форма.findall('handlers')[-1], [h])
сохранять = etree.Element('autoSaveDataInSettings')
сохранять.text = 'Use'
вставить_после(форма.find('windowOpeningMode'), [сохранять])
форма.find('group').text = 'Vertical'
прокрутка = etree.Element('verticalScroll')
прокрутка.text = 'UseIfNecessary'
вставить_после(форма.find('enabled'), [прокрутка])

# id элементов: сквозной счётчик по дереву элементов (без -1 командной панели формы).
счётчик = 0
for узел in [главная, форма.find('autoCommandBar')]:
    for e in узел.iter('id'):
        if e.getparent().tag in ('items', 'extendedTooltip', 'contextMenu', 'autoCommandBar', 'searchStringAddition',
                                 'viewStatusAddition', 'searchControlAddition') and e.text != '-1':
            счётчик += 1
            e.text = str(счётчик)

etree.cleanup_namespaces(форма, keep_ns_prefixes=['form', 'core', 'xsi', 'schema', 'settings'])
etree.indent(форма, space='  ')
sys.stdout.write('<?xml version="1.0" encoding="UTF-8"?>\n' + etree.tostring(форма, encoding='unicode') + '\n')
