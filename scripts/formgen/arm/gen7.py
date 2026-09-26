#!/usr/bin/env python3
"""Форма рабочего места производства, редакция 7 (E12.4, косметика по замечаниям владельца 2026-09-16):
кнопки ввода на основании - в командных панелях своих нижних закладок, явные ширины колонок строк документов,
колонки «Продукция» и «Материалы» с подвалом на закладке «Документы». Количества в заголовках закладок, цвета
движения, узкий «Статус» и подсказка индикатора - в модуле формы.

ВНИМАНИЕ: форма правилась вручную ПОСЛЕ этой редакции и генератор от неё отстал.
2.0.15.39 - колонка «Способ изготовления» на закладке «Материалы»; 2.0.15.40 - закладка «Материалы»
стала деревом (реквизит Материалы типа ValueTree, колонка «Уровень», representation Tree у таблицы,
колонка «Материал» перед «Продукцией»). Источник правды - Form.form в src/cf, как и сказано в README.
Следующая редакция генератора обязана начаться с переноса этих двух правок сюда, иначе она их молча
откатит. Проверка: python3 gen7.py | diff - ../../../src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form

Прежние редакции: 6 (E12.3b - «Переработка»), 5 (E12.3a - «Выпуск» и «Отгрузки»), 4 (E12.2 - закупки),
3 (замечания владельца к 2.0.15.30), 2 (gen2.py)."""
import sys
import gen
import gen6
from gen import (IDS, handlers, button, popup, pages, page, attr_simple, attr_vt, form_command,
                 NUM, STR, DATE, T, DOC_TYPES)
from gen2 import picture_button, info_pages_group, top_field
from gen6 import group, table_command, QUERY, PURCHASE_STATUS, PURCHASE_CMDS

T.update({
    'Материалы движение': ('Материалы', 'Matières', 'Materials', 'Materiales'),
    'Продукция движение': ('Продукция', 'Produits', 'Products', 'Productos'),
})
TT = lambda k: T[k]

# Ширины колонок строк документов в знаках: без них платформа тянет колонку по типу, а не по данным, и
# «Поступления» не помещаются в ширину экрана (замечание владельца 2026-09-16, пункты 4 и 6).
W = {
    'Статус': 12,
    'Поставщик': 22,
    'Позиция': 22,
    'Характеристика': 14,
    'Количество': 8,
    'Упаковка': 8,
    'Цена': 8,
    'Сумма': 10,
    'НомерВходящего': 10,
    'ДатаВходящего': 9,
    'Основание': 16,
    'Документ': 16,
    'Склад': 14,
    'Через': 14,
    'Автовыпуск': 14,
    'Дата': 9,
}
# Закладка «Документы»: вид и контрагент длиннее, движение - две узкие колонки со знаком.
WD = {'Вид': 20, 'Номер': 10, 'Дата': 14, 'Контрагент': 22, 'Статус': 14, 'Через': 18, 'Сумма': 10, 'Движение': 12}

# Команда ввода на основании и закладка, в чьей командной панели теперь живёт её кнопка (пункт 3 владельца).
CREATE_ON_TABLE = [
    ('ЗаказыПоставщику', 'СоздатьЗаказПоставщику'),
    ('Поступления', 'СоздатьПоступление'),
    ('Выпуски', 'СоздатьВыпуск'),
    ('Отгрузки', 'СоздатьОтгрузку'),
    ('Переработки', 'СоздатьПередачу'),
]
# Команды ввода на основании: по одной на действие, кнопка - в панели своей нижней закладки (E12.4, пункт 3).
CREATE_CMDS = [
    ('СоздатьЗаказПоставщику', ('Заказ поставщику', 'Commande fournisseur', 'Supplier order', 'Pedido a proveedor'),
     ('Заказ поставщику на основании отмеченного заказа на производство', 'Commande fournisseur à partir de la commande en production cochée', 'Supplier order based on the ticked production order', 'Pedido a proveedor a partir del pedido para producción marcado')),
    ('СоздатьПоступление', ('Поступление', 'Réception', 'Receipt', 'Recepción'),
     ('Поступление на основании отмеченного заказа на производство', 'Réception à partir de la commande en production cochée', 'Receipt based on the ticked production order', 'Recepción a partir del pedido para producción marcado')),
    ('СоздатьВыпуск', ('Выпуск по заказу', 'Production par commande', 'Output by order', 'Producción por pedido'),
     ('Выпуск продукции, которую осталось выпустить по отмеченному заказу', 'Production des produits restant à produire pour la commande cochée', 'Output of the products still to be produced for the ticked order', 'Producción de los productos que faltan por producir del pedido marcado')),
    ('СоздатьОтгрузку', ('Отгрузка', 'Expédition', 'Shipment', 'Envío'),
     ('Реализация на основании отмеченного заказа на производство', 'Vente à partir de la commande en production cochée', 'Sale based on the ticked production order', 'Venta a partir del pedido para producción marcado')),
    ('СоздатьПередачу', ('Передача в переработку', 'Envoi en sous-traitance', 'Send to subcontractor', 'Envío a subcontratista'),
     ('Передача в переработку на основании отмеченного заказа на производство', 'Envoi en sous-traitance à partir de la commande en production cochée', 'Subcontracting transfer based on the ticked production order', 'Envío a subcontratista a partir del pedido para producción marcado')),
]

# В панели выделенных строк верхних таблиц остаются статус и отчёт по заказу: отчёт - не ввод на основании.
TOP_EXTRA = ['ОткрытьПотребности']
STATUS = ['СтатусВРаботу', 'СтатусВЧерновик', 'СтатусОтменить']


def field(name, path, ind, **kw):
    """Поле редакции 7: заданная ширина держится, только если снять автоматическую максимальную ширину (forms-007)."""
    s = gen.field(name, path, ind, **kw)
    if not kw.get('width'):
        return s
    old = '<autoMaxWidth>true</autoMaxWidth>'
    assert s.count(old) == 2, name  # первое вхождение - расширенная подсказка поля, второе - само поле
    head, tail = s.rsplit(old, 1)
    return head + '<autoMaxWidth>false</autoMaxWidth>' + tail


def table(name, path, columns, ind, footer=False, **kw):
    """Таблица редакции 6 с необязательным подвалом: итоги движения закладки «Документы»."""
    s = gen6.table(name, path, columns, ind, **kw)
    if not footer:
        return s
    i2 = ind + '  '
    old = f'{i2}<headerHeight>1</headerHeight>\n{i2}<footerHeight>1</footerHeight>\n'
    assert s.count(old) == 1, name
    return s.replace(old, f'{i2}<headerHeight>1</headerHeight>\n{i2}<footer>true</footer>\n{i2}<footerHeight>1</footerHeight>\n')


def build():
    L = lambda n, p, t=None, **k: (lambda ind: field(n, p, ind, title=t, **k))
    F = lambda n, p, t=None, **k: (lambda ind: field(n, p, ind, title=t, kind='InputField', **k))

    orders_cols = [
        L('ЗаказыНомер', 'Заказы.Номер', TT('Номер')),
        L('ЗаказыДата', 'Заказы.Дата', TT('Дата')),
        L('ЗаказыКонтрагент', 'Заказы.Контрагент', TT('Клиент')),
        L('ЗаказыСтатус', 'Заказы.Статус', TT('Стадия')),
        L('ЗаказыИндикатор', 'Заказы.Индикатор', TT('Индикатор')),
        L('ЗаказыДатаОтгрузки', 'Заказы.ДатаОтгрузки', TT('Дата отгрузки')),
        L('ЗаказыСумма', 'Заказы.Сумма', TT('Сумма')),
        L('ЗаказыМенеджер', 'Заказы.Менеджер', TT('Менеджер')),
    ]
    prod_cols = [
        L('ПродукцияСтатусДокумента', 'Продукция.СтатусДокумента', TT('Статус'), read_only=True, width=W['Статус']),
        L('ПродукцияСтадия', 'Продукция.Стадия', TT('Стадия'), read_only=True),
        L('ПродукцияИндикатор', 'Продукция.Индикатор', TT('Индикатор'), read_only=True),
        F('ПродукцияКлиент', 'Продукция.Клиент', TT('Клиент'), hs=[('OnChange', 'ПродукцияКлиентПриИзменении')]),
        F('ПродукцияНоменклатура', 'Продукция.Номенклатура', TT('Продукция'),
          hs=[('OnChange', 'ПродукцияНоменклатураПриИзменении')]),
        F('ПродукцияХарактеристика', 'Продукция.Характеристика', TT('Характеристика')),
        F('ПродукцияКоличествоУпаковок', 'Продукция.КоличествоУпаковок', TT('Количество')),
        F('ПродукцияУпаковка', 'Продукция.Упаковка', TT('Упаковка')),
        F('ПродукцияЦена', 'Продукция.Цена', TT('Цена'), hs=[('OnChange', 'ПродукцияЦенаПриИзменении')]),
        L('ПродукцияСумма', 'Продукция.Сумма', TT('Сумма'), read_only=True),
        L('ПродукцияДатаОтгрузки', 'Продукция.ДатаОтгрузки', TT('Дата отгрузки'), read_only=True),
        L('ПродукцияМенеджер', 'Продукция.Менеджер', TT('Менеджер'), read_only=True),
        F('ПродукцияЗаказПредставление', 'Продукция.ЗаказПредставление', TT('Заказ на производство'), choice_button=True,
          text_edit=False, hs=[('StartChoice', 'ПродукцияЗаказПредставлениеНачалоВыбора')]),
    ]
    mat_cols = [L('Материалы' + c, 'Материалы.' + c, TT(t)) for c, t in [
        ('Продукция', 'Продукция'), ('Материал', 'Материал'), ('Характеристика', 'Характеристика'),
        ('ПоСоставу', 'По составу'), ('Потребность', 'Потребность'), ('Заказано', 'Заказано'), ('Пришло', 'Пришло'),
        ('ИзОстатка', 'Из остатка'), ('Дефицит', 'Дефицит'), ('КПоступлению', 'К поступлению')]]
    doc_cols = [L('ДокументыЗаказа' + c, 'ДокументыЗаказа.' + c, TT(t), width=WD[c]) for c, t in [
        ('Вид', 'Вид'), ('Номер', 'Номер'), ('Дата', 'Дата'), ('Контрагент', 'Контрагент'), ('Статус', 'Статус'),
        ('Через', 'Через'), ('Сумма', 'Сумма')]]
    # Движение по документу: строки со знаком, цвет и итоги подвала - в модуле формы (E12.4, пункт 5 владельца).
    движение = ('Приход и расход по документу целиком: документ может содержать строки других заказов.',
                'Entrées et sorties du document entier : le document peut contenir des lignes d\'autres commandes.',
                'Receipts and write-offs of the whole document: it may contain lines of other orders.',
                'Entradas y salidas del documento completo: puede contener líneas de otros pedidos.')
    doc_cols += [L('ДокументыЗаказаПродукция', 'ДокументыЗаказа.Продукция', TT('Продукция движение'),
                   width=WD['Движение'], tooltip=движение),
                 L('ДокументыЗаказаМатериалы', 'ДокументыЗаказа.Материалы', TT('Материалы движение'),
                   width=WD['Движение'], tooltip=движение)]

    def bar_items(prefix):
        cmd_button = lambda n: (lambda i: button(prefix + n, 'Form.Command.' + prefix + n, i))
        status = lambda ind: popup(prefix + 'ПодменюСтатус', TT('Статус'), [cmd_button(n) for n in STATUS], ind)
        return [status] + [cmd_button(n) for n in TOP_EXTRA]

    top = lambda ind: pages('ГруппаВерх', [
        lambda i: page('СтраницаЗаказы', TT('Заказы'), [
            lambda j: table('Заказы', 'Заказы', orders_cols, j, dynamic=True, height=8, bar_items=bar_items('Заказы'),
                            hs=[('Selection', 'ЗаказыВыбор'), ('OnActivateRow', 'ЗаказыПриАктивизацииСтроки')])], i),
        lambda i: page('СтраницаПродукция', TT('Продукция'), [
            lambda j: table('Продукция', 'Продукция', prod_cols, j, height=8, change_rows=True,
                            bar_items=bar_items('Продукция'),
                            hs=[('OnActivateRow', 'ПродукцияПриАктивизацииСтроки'),
                                ('BeforeAddRow', 'ПродукцияПередНачаломДобавления'),
                                ('BeforeRowChange', 'ПродукцияПередНачаломИзменения'),
                                ('BeforeDeleteRow', 'ПродукцияПередУдалением'),
                                ('OnEditEnd', 'ПродукцияПриОкончанииРедактирования')])], i),
    ], ind, hs=[('OnCurrentPageChange', 'ГруппаВерхПриСменеСтраницы')])

    def purchase_bar(prefix, extra=()):
        """Панель нижней таблицы: статус строк, кнопка ввода на основании своей закладки и её особые команды."""
        table_button = lambda n: (lambda i: button(prefix + n, 'Form.Command.' + prefix + n, i))
        items = [lambda ind: popup(prefix + 'ПодменюСтатус', TT('Статус'), [table_button(n) for n in PURCHASE_STATUS], ind)]
        for имя_таблицы, команда in CREATE_ON_TABLE:
            if имя_таблицы == prefix:
                items.append((lambda n: (lambda i: button(prefix + n, 'Form.Command.' + n, i)))(команда))
        return items + [table_button(n) for n in extra]

    def processing_cols():
        P = 'Переработки'
        return [
            L(P + 'Статус', P + '.Статус', TT('Статус'), read_only=True, width=W['Статус']),
            F(P + 'Поставщик', P + '.Поставщик', TT('Переработчик'), width=W['Поставщик'],
              hs=[('OnChange', 'ЗакупкиПоставщикПриИзменении')]),
            F(P + 'Материал', P + '.Материал', TT('Материал'), width=W['Позиция'],
              hs=[('OnChange', 'ЗакупкиМатериалПриИзменении')]),
            F(P + 'Характеристика', P + '.Характеристика', TT('Характеристика'), width=W['Характеристика']),
            F(P + 'КоличествоУпаковок', P + '.КоличествоУпаковок', TT('Количество'), width=W['Количество']),
            F(P + 'Упаковка', P + '.Упаковка', TT('Упаковка'), width=W['Упаковка']),
            L(P + 'Склад', P + '.Склад', TT('Склад'), read_only=True, width=W['Склад']),
            L(P + 'Поступления', P + '.Поступления', TT('Поступления из переработки'), read_only=True, width=W['Основание']),
            F(P + 'ДокументПредставление', P + '.ДокументПредставление', TT('Документ'), choice_button=True,
              text_edit=False, width=W['Документ'],
              hs=[('StartChoice', 'СтрокиДокументовДокументПредставлениеНачалоВыбора')]),
        ]

    def purchase_handlers(prefix):
        return [('BeforeAddRow', prefix + 'ПередНачаломДобавления'), ('BeforeRowChange', prefix + 'ПередНачаломИзменения'),
                ('BeforeDeleteRow', prefix + 'ПередУдалением'), ('OnEditEnd', prefix + 'ПриОкончанииРедактирования'),
                ('Selection', prefix + 'Выбор')]

    def purchase_cols(prefix, receipts):
        P = prefix
        cols = [
            L(P + 'Статус', P + '.Статус', TT('Статус'), read_only=True, width=W['Статус']),
            F(P + 'Поставщик', P + '.Поставщик', TT('Поставщик'), width=W['Поставщик'],
              hs=[('OnChange', 'ЗакупкиПоставщикПриИзменении')]),
        ]
        if receipts:
            cols += [
                F(P + 'НомерВходящегоДокумента', P + '.НомерВходящегоДокумента', TT('Номер вх.'), width=W['НомерВходящего'],
                  hs=[('OnChange', 'ПоступленияНомерВходящегоДокументаПриИзменении')]),
                F(P + 'ДатаВходящегоДокумента', P + '.ДатаВходящегоДокумента', TT('Дата вх.'), width=W['ДатаВходящего']),
            ]
        cols += [
            F(P + 'Материал', P + '.Материал', TT('Материал'), width=W['Позиция'],
              hs=[('OnChange', 'ЗакупкиМатериалПриИзменении')]),
            F(P + 'Характеристика', P + '.Характеристика', TT('Характеристика'), width=W['Характеристика'],
              hs=[('OnChange', 'ЗакупкиХарактеристикаПриИзменении')]),
            F(P + 'КоличествоУпаковок', P + '.КоличествоУпаковок', TT('Количество'), width=W['Количество']),
            F(P + 'Упаковка', P + '.Упаковка', TT('Упаковка'), width=W['Упаковка']),
            F(P + 'Цена', P + '.Цена', TT('Цена'), width=W['Цена'], hs=[('OnChange', 'СтрокиДокументовЦенаПриИзменении')]),
            L(P + 'Сумма', P + '.Сумма', TT('Сумма'), read_only=True, width=W['Сумма']),
        ]
        if receipts:
            cols += [F(P + 'СтрокаОснованияПредставление', P + '.СтрокаОснованияПредставление', TT('Заказ поставщику'),
                       choice_button=True, text_edit=False, width=W['Основание'],
                       hs=[('StartChoice', 'ПоступленияСтрокаОснованияПредставлениеНачалоВыбора')])]
        else:
            cols += [L(P + 'Продукция', P + '.Продукция', TT('Продукция'), read_only=True, width=W['Позиция']),
                     L(P + 'ДатаПоставки', P + '.ДатаПоставки', TT('Дата поставки'), read_only=True, width=W['Дата'])]
        cols += [F(P + 'ДокументПредставление', P + '.ДокументПредставление', TT('Документ'), choice_button=True,
                   text_edit=False, width=W['Документ'],
                   hs=[('StartChoice', 'СтрокиДокументовДокументПредставлениеНачалоВыбора')])]
        return cols

    def output_cols(prefix, shipments):
        P = prefix
        cols = [
            L(P + 'Статус', P + '.Статус', TT('Статус'), read_only=True, width=W['Статус']),
            F(P + 'Продукция', P + '.Продукция', TT('Продукция'), width=W['Позиция'],
              hs=[('OnChange', 'ВыпускиОтгрузкиПродукцияПриИзменении'),
                  ('StartChoice', 'ВыпускиОтгрузкиПродукцияНачалоВыбора')]),
            F(P + 'Характеристика', P + '.Характеристика', TT('Характеристика'), width=W['Характеристика']),
            F(P + 'КоличествоУпаковок', P + '.КоличествоУпаковок', TT('Количество'), width=W['Количество']),
            F(P + 'Упаковка', P + '.Упаковка', TT('Упаковка'), width=W['Упаковка']),
        ]
        if shipments:
            cols += [
                F(P + 'Цена', P + '.Цена', TT('Цена'), width=W['Цена'],
                  hs=[('OnChange', 'СтрокиДокументовЦенаПриИзменении')]),
                L(P + 'Сумма', P + '.Сумма', TT('Сумма'), read_only=True, width=W['Сумма']),
                L(P + 'Автовыпуск', P + '.Автовыпуск', TT('Автовыпуск'), read_only=True, width=W['Автовыпуск']),
            ]
        else:
            cols += [
                L(P + 'Склад', P + '.Склад', TT('Склад'), read_only=True, width=W['Склад']),
                L(P + 'Через', P + '.Через', TT('Через'), read_only=True, width=W['Через']),
            ]
        cols += [F(P + 'ДокументПредставление', P + '.ДокументПредставление', TT('Документ'), choice_button=True,
                   text_edit=False, width=W['Документ'],
                   hs=[('StartChoice', 'СтрокиДокументовДокументПредставлениеНачалоВыбора')])]
        return cols

    bottom = lambda ind: pages('ГруппаНиз', [
        lambda i: page('СтраницаМатериалы', TT('Материалы'), [
            lambda j: table('Материалы', 'Материалы', mat_cols, j, read_only=True, height=5, multi=False)], i),
        lambda i: page('СтраницаЗаказыПоставщику', TT('Заказы поставщику'), [
            lambda j: table('ЗаказыПоставщику', 'ЗаказыПоставщику', purchase_cols('ЗаказыПоставщику', False), j,
                            height=5, change_rows=True, bar_items=purchase_bar('ЗаказыПоставщику'),
                            hs=purchase_handlers('ЗаказыПоставщику'))], i),
        lambda i: page('СтраницаПоступления', TT('Поступления'), [
            lambda j: table('Поступления', 'Поступления', purchase_cols('Поступления', True), j,
                            height=5, change_rows=True, bar_items=purchase_bar('Поступления'),
                            hs=purchase_handlers('Поступления'))], i),
        lambda i: page('СтраницаВыпуски', TT('Выпуск'), [
            lambda j: table('Выпуски', 'Выпуски', output_cols('Выпуски', False), j,
                            height=5, change_rows=True, bar_items=purchase_bar('Выпуски'),
                            hs=purchase_handlers('Выпуски'))], i),
        lambda i: page('СтраницаОтгрузки', TT('Отгрузки'), [
            lambda j: table('Отгрузки', 'Отгрузки', output_cols('Отгрузки', True), j,
                            height=5, change_rows=True, bar_items=purchase_bar('Отгрузки'),
                            hs=purchase_handlers('Отгрузки'))], i),
        lambda i: page('СтраницаПереработки', TT('Переработка'), [
            lambda j: table('Переработки', 'Переработки', processing_cols(), j,
                            height=5, change_rows=True, bar_items=purchase_bar('Переработки', ['СоздатьПоступление']),
                            hs=purchase_handlers('Переработки'))], i),
        lambda i: page('СтраницаДокументы', TT('Документы'), [
            lambda j: table('ДокументыЗаказа', 'ДокументыЗаказа', doc_cols, j, read_only=True, height=5, multi=False,
                            footer=True, hs=[('Selection', 'ДокументыЗаказаВыбор')])], i),
    ], ind)
    # Цепочка сворачивается кнопкой на разделителе (8.5.1); перетаскиваемого мышью разделителя в формах нет.
    chain = lambda ind: group('ГруппаЦепочка', [bottom], ind, collapsible=True)

    queue = lambda ind: field('РежимОчереди', 'РежимОчереди', ind, title=TT('Показывать заказы'), radio=True,
                              title_loc='Top', hs=[('OnChange', 'ОтборПриИзменении')],
                              choice_list=[(('Производство', 'Production', 'Production', 'Producción'), 0),
                                           (('Все', 'Toutes', 'All', 'Todos'), 1)])
    filters_page = lambda ind: page('СтраницаФильтры', TT('Фильтры'), [
        queue,
        lambda i: top_field('ОтборКлиент', 'ОтборКлиент', i, TT('Клиент'), [('OnChange', 'ОтборПриИзменении')]),
        lambda i: top_field('ОтборПродукция', 'ОтборПродукция', i, TT('Продукция'), [('OnChange', 'ОтборПриИзменении')]),
    ], ind)
    info_pages = lambda ind: info_pages_group('ГруппаСтраницыСведений', [filters_page], ind)
    panel = lambda ind: group('ГруппаПанельСведений', [
        lambda i: group('ГруппаПанельЗначки', [
            lambda j: picture_button('КнопкаРазвернутьПанель', 'Form.Command.РазвернутьПанель', 'ПанельРазвернуть', j),
            lambda j: picture_button('КнопкаПоказатьФильтры', 'Form.Command.ПоказатьФильтры', 'ПанельФильтры', j),
        ], i, behavior=False),
        info_pages,
        lambda i: group('ГруппаПодвалПанели', [
            lambda j: picture_button('КнопкаСвернутьПанель', 'Form.Command.СвернутьПанель', 'ПанельСвернуть', j),
        ], i, visible=False, behavior=False),
    ], ind, representation='WeakSeparation')

    main = lambda ind: group('ГруппаГлавная', [
        lambda i: group('ГруппаЛевая', [top, chain], i),
        panel,
    ], ind, group_kind='AutoScreenTypeSensitive')
    items = main('  ')

    cmds = [
        ('СтатусВРаботу', ('В работу', 'Lancer', 'Start', 'Poner en marcha'),
         ('Провести выделенные заказы', 'Valider les commandes sélectionnées', 'Post the selected orders', 'Contabilizar los pedidos seleccionados')),
        ('СтатусВЧерновик', ('В черновик', 'En brouillon', 'To draft', 'A borrador'),
         ('Отменить проведение выделенных заказов', 'Annuler la validation des commandes sélectionnées', 'Undo posting of the selected orders', 'Anular la contabilización de los pedidos seleccionados')),
        ('СтатусОтменить', ('Отменить', 'Annuler', 'Cancel', 'Cancelar'),
         ('Пометить выделенные заказы на удаление', 'Marquer les commandes sélectionnées pour suppression', 'Mark the selected orders for deletion', 'Marcar los pedidos seleccionados para eliminar')),
        ('ОткрытьПотребности', ('Потребности', 'Besoins', 'Requirements', 'Necesidades'),
         ('Отчёт «Потребности производства» по заказу', 'Rapport « Besoins de production » pour la commande', 'Production requirements report for the order', 'Informe de necesidades de producción del pedido')),
    ]
    create_cmds = CREATE_CMDS
    panel_cmds = [
        ('Обновить', ('Обновить', 'Actualiser', 'Refresh', 'Actualizar'),
         ('Перечитать заказы и строки', 'Relire les commandes et les lignes', 'Reload orders and lines', 'Releer los pedidos y las líneas')),
        ('СвернутьПанель', ('Свернуть панель', 'Réduire le panneau', 'Collapse panel', 'Contraer el panel'),
         ('Свернуть панель фильтров', 'Réduire le panneau des filtres', 'Collapse the filter panel', 'Contraer el panel de filtros')),
        ('РазвернутьПанель', ('Развернуть панель', 'Déployer le panneau', 'Expand panel', 'Expandir el panel'),
         ('Развернуть панель фильтров', 'Déployer le panneau des filtres', 'Expand the filter panel', 'Expandir el panel de filtros')),
        ('ПоказатьФильтры', ('Фильтры', 'Filtres', 'Filters', 'Filtros'),
         ('Открыть фильтры', 'Ouvrir les filtres', 'Open filters', 'Abrir los filtros')),
    ]
    bar = '  <autoCommandBar>\n    <name>ФормаКоманднаяПанель</name>\n    <id>-1</id>\n'
    bar += button('ФормаОбновить', 'Form.Command.Обновить', '    ')
    bar += '    <horizontalAlign>Left</horizontalAlign>\n    <autoFill>true</autoFill>\n  </autoCommandBar>\n'

    form_handlers = handlers([('OnCreateAtServer', 'ПриСозданииНаСервере'), ('OnOpen', 'ПриОткрытии'),
                              ('OnLoadDataFromSettingsAtServer', 'ПриЗагрузкеДанныхИзНастроекНаСервере')], '  ')
    props = ('  <autoSaveDataInSettings>Use</autoSaveDataInSettings>\n  <saveDataInSettings>UseList</saveDataInSettings>\n'
             '  <saveWindowSettings>true</saveWindowSettings>\n  <autoTitle>true</autoTitle>\n  <autoUrl>true</autoUrl>\n'
             '  <group>Vertical</group>\n  <autoFillCheck>true</autoFillCheck>\n  <allowFormCustomize>true</allowFormCustomize>\n'
             '  <enabled>true</enabled>\n  <verticalScroll>UseIfNecessary</verticalScroll>\n  <showTitle>auto</showTitle>\n'
             '  <showCloseButton>true</showCloseButton>\n')

    REF = lambda t: f'<types>{t}</types>'
    doc_ref_types = '\n        '.join(f'<types>DocumentRef.{d}</types>' for d in DOC_TYPES)
    attrs = attr_simple('Объект', 1, REF('DataProcessorObject.АРМПроизводство'), main=True)
    attrs += attr_simple('РежимОчереди', 2, '<types>Number</types>' + NUM(1, 0), title=TT('Показывать заказы'), saved=True)
    attrs += (f'  <attributes>\n    <name>Заказы</name>\n    <id>3</id>\n    <valueType>\n      <types>DynamicList</types>\n    </valueType>\n'
              '    <view>\n      <common>true</common>\n    </view>\n    <edit>\n      <common>true</common>\n    </edit>\n'
              f'    <extInfo xsi:type="form:DynamicListExtInfo">\n      <queryText>{QUERY}</queryText>\n'
              '      <mainTable>Document.ЗаказПокупателя</mainTable>\n      <autoFillAvailableFields>true</autoFillAvailableFields>\n'
              '      <customQuery>true</customQuery>\n      <autoSaveUserSettings>true</autoSaveUserSettings>\n'
              '      <getInvisibleFieldPresentations>true</getInvisibleFieldPresentations>\n    </extInfo>\n  </attributes>\n')
    QTY = '<types>Number</types>' + NUM(15, 3)
    MONEY = '<types>Number</types>' + NUM(15, 2)
    attrs += attr_vt('Продукция', 4, [
        ('Заказ', REF('DocumentRef.ЗаказПокупателя'), None),
        ('ЗаказПредставление', '<types>String</types>' + STR(250), TT('Заказ на производство')),
        ('Клиент', REF('CatalogRef.Контрагенты'), TT('Клиент')),
        ('НомерСтроки', '<types>Number</types>' + NUM(5, 0), None),
        ('ВерсияДанных', '<types>String</types>' + STR(50), None),
        ('Номенклатура', REF('CatalogRef.Номенклатура'), TT('Продукция')),
        ('Характеристика', REF('CatalogRef.ХарактеристикиНоменклатуры'), TT('Характеристика')),
        ('Упаковка', REF('CatalogRef.УпаковкиЕдиницыИзмерения'), TT('Упаковка')),
        ('КоличествоУпаковок', QTY, TT('Количество')),
        ('Цена', MONEY, TT('Цена')),
        ('Сумма', MONEY, TT('Сумма')),
        ('ДатаОтгрузки', '<types>Date</types>' + DATE, TT('Дата отгрузки')),
        ('Стадия', REF('EnumRef.СтатусыЗаказовПокупателя'), TT('Стадия')),
        ('СтатусДокумента', '<types>String</types>' + STR(100), TT('Статус')),
        ('Редактируется', REF('Boolean'), None),
        ('Записана', REF('Boolean'), None),
        ('ЦенаИзменена', REF('Boolean'), None),
        ('Индикатор', '<types>String</types>' + STR(10), TT('Индикатор')),
        ('Менеджер', REF('CatalogRef.ФизическиеЛица'), TT('Менеджер')),
    ])
    attrs += attr_vt('Материалы', 5, [
        ('Продукция', REF('CatalogRef.Номенклатура'), TT('Продукция')),
        ('Материал', REF('CatalogRef.Номенклатура'), TT('Материал')),
        ('Характеристика', REF('CatalogRef.ХарактеристикиНоменклатуры'), TT('Характеристика')),
    ] + [(c, QTY, TT(t)) for c, t in [('ПоСоставу', 'По составу'), ('Потребность', 'Потребность'), ('Заказано', 'Заказано'),
                                       ('Пришло', 'Пришло'), ('ИзОстатка', 'Из остатка'), ('Дефицит', 'Дефицит'),
                                       ('КПоступлению', 'К поступлению')]])
    DT = '<types>Date</types>\n        <dateQualifiers>\n          <dateFractions>DateTime</dateFractions>\n        </dateQualifiers>'
    attrs += attr_vt('ДокументыЗаказа', 6, [
        ('Документ', doc_ref_types, TT('Документ')),
        ('Вид', '<types>String</types>' + STR(150), TT('Вид')),
        ('Номер', '<types>String</types>' + STR(50), TT('Номер')),
        ('Дата', DT, TT('Дата')),
        ('Контрагент', REF('CatalogRef.Контрагенты'), TT('Контрагент')),
        ('Статус', '<types>String</types>' + STR(100), TT('Статус')),
        ('Через', doc_ref_types, TT('Через')),
        ('Сумма', MONEY, TT('Сумма')),
        # Движение документа: видимая строка со знаком и число для оформления и итогов подвала.
        ('Продукция', '<types>String</types>' + STR(20), TT('Продукция движение')),
        ('Материалы', '<types>String</types>' + STR(20), TT('Материалы движение')),
        ('ПродукцияЧисло', QTY, None),
        ('МатериалыЧисло', QTY, None),
    ])
    STR_ = lambda n: '<types>String</types>' + STR(n)
    BOOL = REF('Boolean')
    purchase_common_head = [
        ('ДокументПредставление', STR_(250), TT('Документ')),
        ('НомерСтроки', '<types>Number</types>' + NUM(5, 0), None),
        ('ВерсияДанных', STR_(50), None),
        ('Статус', STR_(500), TT('Статус')),
        ('Поставщик', REF('CatalogRef.Контрагенты'), TT('Поставщик')),
    ]
    purchase_common_tail = [
        ('Материал', REF('CatalogRef.Номенклатура'), TT('Материал')),
        ('Характеристика', REF('CatalogRef.ХарактеристикиНоменклатуры'), TT('Характеристика')),
        ('Упаковка', REF('CatalogRef.УпаковкиЕдиницыИзмерения'), TT('Упаковка')),
        ('КоличествоУпаковок', QTY, TT('Количество')),
        ('Цена', MONEY, TT('Цена')),
        ('Сумма', MONEY, TT('Сумма')),
        ('Проведен', BOOL, None),
        ('Записана', BOOL, None),
        ('ЦенаИзменена', BOOL, None),
        ('ТолькоПросмотр', BOOL, None),
        ('ДокументЗаСегодня', BOOL, None),
    ]
    attrs += attr_vt('ЗаказыПоставщику', 30, [('Документ', REF('DocumentRef.ЗаказПоставщику'), TT('Документ'))]
                     + purchase_common_head + purchase_common_tail + [
        ('Продукция', REF('CatalogRef.Номенклатура'), TT('Продукция')),
        ('ДатаПоставки', '<types>Date</types>' + DATE, TT('Дата поставки')),
    ])
    attrs += attr_vt('Поступления', 31, [('Документ', REF('DocumentRef.ПоступлениеТоваровУслуг'), TT('Документ'))]
                     + purchase_common_head + [
        ('НомерВходящегоДокумента', STR_(30), TT('Номер вх.')),
        ('ДатаВходящегоДокумента', '<types>Date</types>' + DATE, TT('Дата вх.')),
        ('ЗаказПоставщику', REF('DocumentRef.ЗаказПоставщику'), TT('Заказ поставщику')),
        ('КодСтрокиОснования', '<types>Number</types>' + NUM(10, 0), None),
        ('СтрокаОснованияПредставление', STR_(250), TT('Заказ поставщику')),
    ] + purchase_common_tail)
    output_common = [
        ('ДокументПредставление', STR_(250), TT('Документ')),
        ('НомерСтроки', '<types>Number</types>' + NUM(5, 0), None),
        ('ВерсияДанных', STR_(50), None),
        ('Статус', STR_(500), TT('Статус')),
        ('Продукция', REF('CatalogRef.Номенклатура'), TT('Продукция')),
        ('Характеристика', REF('CatalogRef.ХарактеристикиНоменклатуры'), TT('Характеристика')),
        ('Упаковка', REF('CatalogRef.УпаковкиЕдиницыИзмерения'), TT('Упаковка')),
        ('КоличествоУпаковок', QTY, TT('Количество')),
    ]
    output_flags = [
        ('Проведен', BOOL, None),
        ('Записана', BOOL, None),
        ('ЦенаИзменена', BOOL, None),
        ('ТолькоПросмотр', BOOL, None),
        ('ДокументЗаСегодня', BOOL, None),
    ]
    attrs += attr_simple('МожноВводитьЗаказыПоставщику', 32, BOOL)
    attrs += attr_simple('МожноВводитьПоступления', 33, BOOL)
    attrs += attr_vt('Выпуски', 34, [('Документ', REF('DocumentRef.ВыпускПродукции'), TT('Документ'))] + output_common + [
        ('Склад', REF('CatalogRef.МестаХранения'), TT('Склад')),
        ('Через', STR_(100), TT('Через')),
    ] + output_flags)
    attrs += attr_vt('Отгрузки', 35, [('Документ', REF('DocumentRef.РеализацияТоваровУслуг'), TT('Документ'))] + output_common + [
        ('Цена', MONEY, TT('Цена')),
        ('Сумма', MONEY, TT('Сумма')),
        ('Автовыпуск', STR_(100), TT('Автовыпуск')),
    ] + output_flags)
    attrs += attr_simple('МожноВводитьВыпуски', 36, BOOL)
    attrs += attr_simple('МожноВводитьОтгрузки', 37, BOOL)
    attrs += attr_simple('МожноВыпуск', 38, BOOL)
    attrs += attr_vt('Переработки', 39, [('Документ', REF('DocumentRef.ПередачаВПереработку'), TT('Документ'))]
                     + purchase_common_head[:4] + [('Поставщик', REF('CatalogRef.Контрагенты'), TT('Переработчик'))] + [
        ('Материал', REF('CatalogRef.Номенклатура'), TT('Материал')),
        ('Характеристика', REF('CatalogRef.ХарактеристикиНоменклатуры'), TT('Характеристика')),
        ('Упаковка', REF('CatalogRef.УпаковкиЕдиницыИзмерения'), TT('Упаковка')),
        ('КоличествоУпаковок', QTY, TT('Количество')),
        ('Склад', REF('CatalogRef.МестаХранения'), TT('Склад')),
        ('Поступления', STR_(250), TT('Поступления из переработки')),
    ] + output_flags)
    attrs += attr_simple('МожноВводитьПереработку', 40, BOOL)
    attrs += attr_simple('МожноПоступлениеИзПереработки', 41, BOOL)
    attrs += attr_simple('ТекущийЗаказ', 7, REF('DocumentRef.ЗаказПокупателя'))
    booleans = ['ПоказыватьСуммы', 'МожноМенятьЗаказы', 'МожноПроводитьЗаказы', 'МожноПомечатьЗаказы',
                'МожноЗаказПоставщику', 'МожноПоступление', 'МожноПередачу', 'МожноОтгрузку', 'МожноНаОсновании']
    for i, n in enumerate(booleans, 8):
        attrs += attr_simple(n, i, REF('Boolean'))
    next_id = 8 + len(booleans)
    attrs += attr_simple('ПанельРазвернута', next_id, REF('Boolean'), saved=True)
    attrs += attr_simple('ОтборКлиент', next_id + 1, '<types>String</types>' + STR(100), title=TT('Клиент'))
    attrs += attr_simple('ОтборПродукция', next_id + 2, '<types>String</types>' + STR(100), title=TT('Продукция'))

    fcmds = ''
    cid = 0
    # Команды верхних таблиц: статус заказов и отчёт по заказу - в панели выделенных строк.
    for prefix in ('Заказы', 'Продукция'):
        for n, t, tt in cmds:
            cid += 1
            fcmds += table_command(prefix + n, cid, t, tt, n, prefix)
    # Статус строк нижних закладок - команды своих таблиц.
    for prefix in ('ЗаказыПоставщику', 'Поступления', 'Выпуски', 'Отгрузки', 'Переработки'):
        for n in PURCHASE_STATUS:
            action, title, tooltip = PURCHASE_CMDS[n]
            cid += 1
            fcmds += table_command(prefix + n, cid, title, tooltip, action, prefix)
    cid += 1
    fcmds += table_command('ПереработкиСоздатьПоступление', cid,
                           ('Поступление из переработки', 'Réception de sous-traitance', 'Subcontracting receipt',
                            'Recepción de subcontratación'),
                           ('Поступление из переработки на основании передачи отмеченной строки',
                            'Réception de sous-traitance à partir du transfert de la ligne cochée',
                            'Subcontracting receipt based on the transfer of the ticked line',
                            'Recepción de subcontratación a partir del envío de la línea marcada'),
                           'СоздатьПоступлениеИзПереработки', 'Переработки')
    # Ввод на основании и панель - команды формы: заказ берётся из отмеченных строк верхней таблицы.
    for n, t, tt in create_cmds + panel_cmds:
        cid += 1
        fcmds += form_command(n, cid, t, tt, n)

    out = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<form:Form xmlns:form="http://g5.1c.ru/v8/dt/form" xmlns:core="http://g5.1c.ru/v8/dt/mcore" '
           'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')
    out += items + bar + form_handlers + props + attrs + fcmds
    out += '  <commandInterface>\n    <navigationPanel/>\n    <commandBar/>\n  </commandInterface>\n'
    out += '  <extInfo xsi:type="form:ObjectFormExtInfo"/>\n</form:Form>\n'
    return out


if __name__ == '__main__':
    sys.stdout.write(build())
