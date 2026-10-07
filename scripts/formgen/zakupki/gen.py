#!/usr/bin/env python3
"""Форма рабочего места закупок (DataProcessors/АРМЗакупки/Forms/Форма/Form.form), сборка 2.0.16.28.

Форма собирается из проверенных узлов формы рабочего места производства (урок tiny1C workflow-005: новую XML-конструкцию
брать по работающему образцу): оболочки групп, таблица значений «Документы заказа» как образец таблицы и колонки,
поле фильтра, пагинатор, панель фильтров, команды. Узлы переименовываются, id перенумеровываются в трёх независимых
пространствах - элементы, реквизиты, команды (tiny1C forms-001, forms-018).

    python3 gen.py > ../../../src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Form.form

План - docs/plans/arm-purchasing.md.
"""
import copy
import os
import sys

from lxml import etree

ЗДЕСЬ = os.path.dirname(os.path.abspath(__file__))
КОРЕНЬ = os.path.normpath(os.path.join(ЗДЕСЬ, '..', '..', '..'))
ОБРАЗЕЦ = os.path.join(КОРЕНЬ, 'src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form')
XSI = 'http://www.w3.org/2001/XMLSchema-instance'
ЯЗЫКИ = ('ru', 'fr', 'en', 'es')

образец = etree.parse(ОБРАЗЕЦ, etree.XMLParser(remove_blank_text=True)).getroot()


def найти(имя):
    for e in образец.iter('items'):
        if e.findtext('name') == имя:
            return e
    raise KeyError(имя)


def копия(имя, без_детей=False):
    e = copy.deepcopy(найти(имя))
    if без_детей:
        for c in e.findall('items'):
            e.remove(c)
    return e


def переименовать(e, старое, новое):
    """Имя узла и имена его служебных частей (подсказка, контекстное меню, командная панель)."""
    for n in e.iter('name'):
        if n.text and n.text.startswith(старое) and n.getparent().tag in ('items', 'extendedTooltip', 'contextMenu',
                                                                           'autoCommandBar'):
            n.text = новое + n.text[len(старое):]


def задать_локализацию(e, тег, значения, после=None):
    for t in e.findall(тег):
        e.remove(t)
    if значения is None:
        return
    якорь = e.find(после) if после else None
    позиция = list(e).index(якорь) + 1 if якорь is not None else 2
    for i, (язык, текст) in enumerate(zip(ЯЗЫКИ, значения)):
        t = etree.Element(тег)
        etree.SubElement(t, 'key').text = язык
        etree.SubElement(t, 'value').text = текст
        e.insert(позиция + i, t)


def путь_данных(e, путь):
    e.find('dataPath/segments').text = путь


def обработчики(e, пары):
    """Обработчики - на своё место в порядке тегов образца: у таблицы после командной панели, у поля перед подсказкой."""
    for h in e.findall('handlers'):
        e.remove(h)
    панель = e.find('autoCommandBar')
    позиция = list(e).index(панель) + 1 if панель is not None else list(e).index(e.find('extendedTooltip'))
    for i, (событие, имя) in enumerate(пары):
        h = etree.Element('handlers')
        etree.SubElement(h, 'event').text = событие
        etree.SubElement(h, 'name').text = имя
        e.insert(позиция + i, h)


# --- колонки и таблицы -----------------------------------------------------------------------------------------------

ОБРАЗЕЦ_КОЛОНКИ = 'ДокументыЗаказаВид'


def колонка(таблица, поле, заголовки, ширина=None):
    e = копия(ОБРАЗЕЦ_КОЛОНКИ)
    переименовать(e, ОБРАЗЕЦ_КОЛОНКИ, таблица + поле)
    задать_локализацию(e, 'title', заголовки, после='id')
    путь_данных(e, f'{таблица}.{поле}')
    ext = e.find('extInfo')
    w = ext.find('width')
    if ширина is None:
        ext.remove(w)
        ext.find('autoMaxWidth').text = 'true'
    else:
        w.text = str(ширина)
    return e


def таблица(имя, колонки, высота, обработчики_таблицы):
    e = копия('ДокументыЗаказа', без_детей=True)
    переименовать(e, 'ДокументыЗаказа', имя)
    путь_данных(e, имя)
    обработчики(e, обработчики_таблицы)
    e.find('heightInTableRows').text = str(высота)
    позиция = list(e).index(e.find('changeRowSet'))
    for i, (поле, заголовки, ширина) in enumerate(колонки):
        e.insert(позиция + i, колонка(имя, поле, заголовки, ширина))
    return e


def страница(имя, заголовки, дети):
    e = копия('СтраницаДокументы', без_детей=True)
    переименовать(e, 'СтраницаДокументы', имя)
    задать_локализацию(e, 'title', заголовки, после='id')
    позиция = list(e).index(e.find('type'))
    for i, ребёнок in enumerate(дети):
        e.insert(позиция + i, ребёнок)
    return e


def вложить(родитель, дети):
    позиция = list(родитель).index(родитель.find('type'))
    for i, ребёнок in enumerate(дети):
        родитель.insert(позиция + i, ребёнок)
    return родитель


def фильтр(образец_поля, имя, заголовки):
    e = копия(образец_поля)
    переименовать(e, образец_поля, имя)
    задать_локализацию(e, 'title', заголовки, после='id')
    путь_данных(e, имя)
    return e


def надпись(имя, образец_надписи='НадписьЛегенда'):
    e = копия(образец_надписи)
    переименовать(e, образец_надписи, имя)
    return e


# --- элементы --------------------------------------------------------------------------------------------------------

Т = {
    'Номер': ('Номер', 'Numéro', 'Number', 'Número'),
    'Дата': ('Дата', 'Date', 'Date', 'Fecha'),
    'Поставщик': ('Поставщик', 'Fournisseur', 'Supplier', 'Proveedor'),
    'Статус': ('Статус', 'Statut', 'Status', 'Estado'),
    'Индикатор': ('Поставка · оплата', 'Livraison · paiement', 'Delivery · payment', 'Entrega · pago'),
    'ДатаПоставки': ('Дата поставки', 'Date de livraison', 'Delivery date', 'Fecha de entrega'),
    'Сумма': ('Сумма', 'Montant', 'Amount', 'Importe'),
    'Валюта': ('Валюта', 'Devise', 'Currency', 'Moneda'),
    'ЗаказКлиента': ('Заказ клиента', 'Commande client', 'Customer order', 'Pedido del cliente'),
    'Ответственный': ('Ответственный', 'Responsable', 'Responsible', 'Responsable'),
    'Номенклатура': ('Товар', 'Article', 'Item', 'Artículo'),
    'Характеристика': ('Характеристика', 'Caractéristique', 'Variant', 'Característica'),
    'Заказано': ('Заказано', 'Commandé', 'Ordered', 'Pedido'),
    'Пришло': ('Пришло', 'Reçu', 'Received', 'Recibido'),
    'Осталось': ('Осталось', 'Reste', 'Remaining', 'Pendiente'),
    'Цена': ('Цена', 'Prix', 'Price', 'Precio'),
    'Продукция': ('Продукция', 'Produit', 'Product', 'Producto'),
    'Документ': ('Документ', 'Document', 'Document', 'Documento'),
    'НомерНакладной': ('№ накладной', 'N° de facture', 'Invoice No.', 'N.º de factura'),
    'ДатаНакладной': ('Дата накладной', 'Date de facture', 'Invoice date', 'Fecha de factura'),
    'Количество': ('Количество', 'Quantité', 'Quantity', 'Cantidad'),
    'Основание': ('По документу', 'Pour le document', 'For document', 'Por documento'),
    'Вид': ('Вид', 'Type', 'Type', 'Tipo'),
    'ВидЗаказа': ('Вид заказа', 'Type de commande', 'Order type', 'Tipo de pedido'),
}


def кол(поле, ширина=None):
    return (поле, Т[поле], ширина)


заказы = таблица('Заказы', [кол('Номер', 9), кол('Дата', 12), кол('Поставщик', 20), кол('Статус', 12),
                            кол('Индикатор', 6), кол('ДатаПоставки', 8), кол('Сумма', 9), кол('Валюта', 5),
                            кол('ЗаказКлиента', 14), кол('Ответственный', 11)], 10,
                 [('Selection', 'ЗаказыВыбор'), ('OnActivateRow', 'ЗаказыПриАктивизацииСтроки')])
пагинация = копия('ГруппаПагинация')
стр_заказы = страница('СтраницаЗаказы', ('Заказы поставщикам', 'Commandes fournisseurs', 'Supplier orders',
                                         'Pedidos a proveedores'), [заказы, пагинация])
верх = вложить(копия('ГруппаВерх', без_детей=True), [стр_заказы])
обработчики_верх = верх.findall('handlers')
for h in обработчики_верх:
    верх.remove(h)

выбор = [('Selection', 'ДокументСтрокиВыбор')]
товары = таблица('Товары', [кол('Номенклатура', 30), кол('Характеристика', 15), кол('Заказано', 9), кол('Пришло', 9),
                            кол('Осталось', 9), кол('Цена', 10), кол('Сумма', 11), кол('Продукция', 20)], 5, [])
поступления = таблица('Поступления', [кол('Дата', 14), кол('Документ', 22), кол('НомерНакладной', 12),
                                      кол('ДатаНакладной', 11), кол('Номенклатура', 25), кол('Характеристика', 12),
                                      кол('Количество', 9), кол('Сумма', 11), кол('Статус', 14)], 5, выбор)
оплаты = таблица('Оплаты', [кол('Дата', 14), кол('Документ', 30), кол('Основание', 30), кол('Сумма', 12)], 5, выбор)
документы = таблица('Документы', [кол('Вид', 22), кол('Номер', 12), кол('Дата', 14), кол('Сумма', 12),
                                  кол('Статус', 16)], 5, выбор)
for т in (поступления, оплаты, документы):
    т.find('handlers/name').text = т.findtext('name') + 'Выбор'
сальдо = надпись('НадписьСальдо')
низ = вложить(копия('ГруппаНиз', без_детей=True), [
    страница('СтраницаТовары', ('Товары', 'Articles', 'Items', 'Artículos'), [товары]),
    страница('СтраницаПоступления', ('Поступления', 'Réceptions', 'Receipts', 'Recepciones'), [поступления]),
    страница('СтраницаОплаты', ('Оплаты', 'Paiements', 'Payments', 'Pagos'), [сальдо, оплаты]),
    страница('СтраницаДокументы', ('Документы', 'Documents', 'Documents', 'Documentos'), [документы]),
])
цепочка = вложить(копия('ГруппаЦепочка', без_детей=True), [низ])
левая = вложить(копия('ГруппаЛевая', без_детей=True), [верх, цепочка])

панель = копия('ГруппаПанельСведений')
фильтры = None
for e in панель.iter('items'):
    if e.findtext('name') == 'СтраницаФильтры':
        фильтры = e
for c in фильтры.findall('items'):
    фильтры.remove(c)
вложить(фильтры, [
    фильтр('ОтборКлиент', 'ОтборПоставщик', Т['Поставщик']),
    фильтр('ОтборПродукция', 'ОтборТовар', Т['Номенклатура']),
    фильтр('ОтборСтадия', 'ОтборСтатус', Т['Статус']),
    фильтр('ОтборПериодОтгрузки', 'ОтборПериодПоставки', Т['ДатаПоставки']),
    фильтр('ОтборКлиент', 'ОтборОтветственный', Т['Ответственный']),
    фильтр('ОтборСтадия', 'ОтборВидЗаказа', Т['ВидЗаказа']),
])
главная = вложить(копия('ГруппаГлавная', без_детей=True), [левая, панель])

# --- реквизиты -------------------------------------------------------------------------------------------------------


def тип(e, типы):
    vt = etree.SubElement(e, 'valueType')
    for t in типы:
        if isinstance(t, tuple):
            etree.SubElement(vt, 'types').text = t[0]
            vt.append(etree.fromstring(t[1]))
        else:
            etree.SubElement(vt, 'types').text = t


def права(e):
    for тег in ('view', 'edit'):
        etree.SubElement(etree.SubElement(e, тег), 'common').text = 'true'


def локализация(e, тег, значения):
    for язык, текст in zip(ЯЗЫКИ, значения):
        t = etree.SubElement(e, тег)
        etree.SubElement(t, 'key').text = язык
        etree.SubElement(t, 'value').text = текст


СТРОКА = ('String', '<stringQualifiers><length>150</length></stringQualifiers>')
ЧИСЛО = ('Number', '<numberQualifiers><precision>15</precision><scale>3</scale></numberQualifiers>')
ДЕНЬГИ = ('Number', '<numberQualifiers><precision>15</precision><scale>2</scale></numberQualifiers>')
ДАТА = ('Date', '<dateQualifiers><dateFractions>DateTime</dateFractions></dateQualifiers>')
ДЕНЬ = ('Date', '<dateQualifiers><dateFractions>Date</dateFractions></dateQualifiers>')
СТРАНИЦА = ('Number', '<numberQualifiers><precision>10</precision><scale>0</scale><nonNegative>true</nonNegative>'
                      '</numberQualifiers>')
ПЛАТЁЖКИ = ['DocumentRef.СписаниеБезналичныхДенежныхСредств', 'DocumentRef.РасходныйКассовыйОрдер',
            'DocumentRef.ПоступлениеБезналичныхДенежныхСредств', 'DocumentRef.ПриходныйКассовыйОрдер']
ДОКУМЕНТЫ_ЦЕПОЧКИ = ['DocumentRef.ЗаказПоставщику', 'DocumentRef.ПоступлениеТоваровУслуг',
                     'DocumentRef.ВозвратПоставщику', 'DocumentRef.НалоговаяНакладнаяПокупка'] + ПЛАТЁЖКИ

РЕКВИЗИТЫ = []


def реквизит(имя, типы, заголовки=None, основной=False, сохраняемый=False):
    e = etree.Element('attributes')
    etree.SubElement(e, 'name').text = имя
    if заголовки:
        локализация(e, 'title', заголовки)
    etree.SubElement(e, 'id').text = str(len(РЕКВИЗИТЫ) + 1)
    тип(e, типы)
    права(e)
    if сохраняемый:
        etree.SubElement(e, 'savedData').text = 'true'
    if основной:
        etree.SubElement(e, 'main').text = 'true'
    РЕКВИЗИТЫ.append(e)


def реквизит_тз(имя, колонки):
    e = etree.Element('attributes')
    etree.SubElement(e, 'name').text = имя
    etree.SubElement(e, 'id').text = str(len(РЕКВИЗИТЫ) + 1)
    тип(e, ['ValueTable'])
    права(e)
    for i, (поле, типы) in enumerate(колонки, 1):
        c = etree.SubElement(e, 'columns')
        etree.SubElement(c, 'name').text = поле
        if поле in Т:
            локализация(c, 'title', Т[поле])
        etree.SubElement(c, 'id').text = str(i)
        тип(c, типы)
        права(c)
    РЕКВИЗИТЫ.append(e)


реквизит('Объект', ['DataProcessorObject.АРМЗакупки'], основной=True)
реквизит_тз('Заказы', [('Заказ', ['DocumentRef.ЗаказПоставщику']), ('Номер', [СТРОКА]), ('Дата', [ДАТА]),
                       ('Поставщик', ['CatalogRef.Контрагенты']), ('Статус', ['EnumRef.СтатусыЗаказовПоставщику']),
                       ('Индикатор', [СТРОКА]), ('ДатаПоставки', [ДЕНЬ]), ('Сумма', [ДЕНЬГИ]),
                       ('Валюта', ['CatalogRef.Валюты']), ('ЗаказКлиента', ['DocumentRef.ЗаказПокупателя']),
                       ('Ответственный', ['CatalogRef.Пользователи']),
                       ('ВидЗаказа', ['EnumRef.ВидыЗаказовПоставщику'])])
реквизит_тз('Товары', [('Номенклатура', ['CatalogRef.Номенклатура']),
                       ('Характеристика', ['CatalogRef.ХарактеристикиНоменклатуры']), ('Заказано', [ЧИСЛО]),
                       ('Пришло', [ЧИСЛО]), ('Осталось', [ЧИСЛО]), ('Цена', [ДЕНЬГИ]), ('Сумма', [ДЕНЬГИ]),
                       ('Продукция', ['CatalogRef.Номенклатура'])])
реквизит_тз('Поступления', [('Документ', ['DocumentRef.ПоступлениеТоваровУслуг']), ('Дата', [ДАТА]),
                            ('НомерНакладной', [СТРОКА]), ('ДатаНакладной', [ДЕНЬ]),
                            ('Номенклатура', ['CatalogRef.Номенклатура']),
                            ('Характеристика', ['CatalogRef.ХарактеристикиНоменклатуры']), ('Количество', [ЧИСЛО]),
                            ('Сумма', [ДЕНЬГИ]), ('Статус', [СТРОКА])])
реквизит_тз('Оплаты', [('Документ', ПЛАТЁЖКИ), ('Дата', [ДАТА]),
                       ('Основание', ['DocumentRef.ПоступлениеТоваровУслуг', 'DocumentRef.НалоговаяНакладнаяПокупка']),
                       ('Сумма', [ДЕНЬГИ])])
реквизит_тз('Документы', [('Документ', ДОКУМЕНТЫ_ЦЕПОЧКИ), ('Вид', [СТРОКА]), ('Номер', [СТРОКА]), ('Дата', [ДАТА]),
                          ('Сумма', [ДЕНЬГИ]), ('Статус', [СТРОКА])])
реквизит('ТекущийЗаказ', ['DocumentRef.ЗаказПоставщику'])
реквизит('ПанельРазвернута', ['Boolean'], сохраняемый=True)
реквизит('ОтборПоставщик', ['CatalogRef.Контрагенты'], Т['Поставщик'])
реквизит('ОтборТовар', ['CatalogRef.Номенклатура'], Т['Номенклатура'])
реквизит('ОтборСтатус', ['EnumRef.СтатусыЗаказовПоставщику'], Т['Статус'])
реквизит('ОтборПериодПоставки', ['StandardPeriod'], Т['ДатаПоставки'])
реквизит('ОтборОтветственный', ['CatalogRef.Пользователи'], Т['Ответственный'])
реквизит('ОтборВидЗаказа', ['EnumRef.ВидыЗаказовПоставщику'], Т['ВидЗаказа'])
реквизит('НомерСтраницы', [СТРАНИЦА])
реквизит('ВсегоСтраниц', [СТРАНИЦА])

# --- команды ---------------------------------------------------------------------------------------------------------

КОМАНДЫ = []
for имя in ('Обновить', 'СвернутьПанель', 'РазвернутьПанель', 'ПоказатьФильтры', 'СтраницаПервая', 'СтраницаНазад',
            'СтраницаВперед', 'СтраницаПоследняя'):
    for c in образец.findall('formCommands'):
        if c.findtext('name') == имя:
            КОМАНДЫ.append(copy.deepcopy(c))
обновить = КОМАНДЫ[0]
задать_локализацию(обновить, 'toolTip', ('Перечитать заказы поставщикам', 'Relire les commandes fournisseurs',
                                         'Reload supplier orders', 'Releer los pedidos a proveedores'), после='id')
создать = copy.deepcopy(обновить)
создать.find('name').text = 'Создать'
создать.find('action/handler/name').text = 'Создать'
задать_локализацию(создать, 'title', ('Создать', 'Créer', 'Create', 'Crear'), после='name')
задать_локализацию(создать, 'toolTip', ('Новый заказ поставщику', 'Nouvelle commande fournisseur',
                                        'New supplier order', 'Nuevo pedido a proveedor'), после='id')
КОМАНДЫ.insert(0, создать)
for i, c in enumerate(КОМАНДЫ, 1):
    c.find('id').text = str(i)

панель_формы = copy.deepcopy(образец.find('autoCommandBar'))
кнопка_обновить = панель_формы.find('items')
кнопка_создать = copy.deepcopy(кнопка_обновить)
переименовать(кнопка_создать, 'ФормаОбновить', 'ФормаСоздать')
кнопка_создать.find('commandName').text = 'Form.Command.Создать'
панель_формы.insert(list(панель_формы).index(кнопка_обновить), кнопка_создать)

# --- сборка ----------------------------------------------------------------------------------------------------------

корень = etree.Element(образец.tag, nsmap=образец.nsmap)
корень.append(главная)
корень.append(панель_формы)
for событие, имя in (('OnCreateAtServer', 'ПриСозданииНаСервере'),
                     ('OnLoadDataFromSettingsAtServer', 'ПриЗагрузкеДанныхИзНастроекНаСервере')):
    h = etree.SubElement(корень, 'handlers')
    etree.SubElement(h, 'event').text = событие
    etree.SubElement(h, 'name').text = имя
for c in образец:
    if c.tag in ('items', 'autoCommandBar', 'handlers', 'attributes', 'formCommands', 'commandInterface', 'extInfo'):
        continue
    корень.append(copy.deepcopy(c))
for e in РЕКВИЗИТЫ:
    корень.append(e)
for c in КОМАНДЫ:
    корень.append(c)
корень.append(copy.deepcopy(образец.find('commandInterface')))
корень.append(copy.deepcopy(образец.find('extInfo')))

# id элементов: счётчик в порядке документа по всему дереву элементов и командной панели формы (-1 у панели формы).
счётчик = 0
for узел in (главная, панель_формы):
    for e in узел.iter('id'):
        if e.text == '-1':
            continue
        счётчик += 1
        e.text = str(счётчик)

etree.cleanup_namespaces(корень, keep_ns_prefixes=['form', 'core', 'xsi'])
etree.indent(корень, space='  ')
текст = etree.tostring(корень, encoding='unicode')
sys.stdout.write('<?xml version="1.0" encoding="UTF-8"?>\n' + текст + '\n')
