#!/usr/bin/env python3
"""Форма рабочего места производства, редакция 4 (E12.2: закладки «Заказы поставщику» и «Поступления»); редакция 3 (замечания владельца к 2.0.15.30): без колонок процентов (проценты - в
подсказке индикатора), статус и ввод на основании - командами таблиц в панели выделенных строк 8.5.1, нижняя цепочка -
в сворачиваемой группе с разделителем, фильтры клиента и продукции - по вхождению текста, в «Продукции» статус впереди,
заказ - последней колонкой. Остальное - как в редакции 2 (gen2.py)."""
import sys
import gen
import gen2
from gen import (IDS, ext_tooltip, common_vis, handlers, field, button, popup, pages, page,
                 attr_simple, attr_vt, form_command, NUM, STR, DATE, T, DOC_TYPES)
from gen2 import command_bar, picture_button, info_pages_group, top_field, table as table2

T.update({
    'Поставщик': ('Поставщик', 'Fournisseur', 'Supplier', 'Proveedor'),
    'Номер вх.': ('Номер накладной', 'N° du bon', 'Invoice No.', 'N.º de albarán'),
    'Дата вх.': ('Дата накладной', 'Date du bon', 'Invoice date', 'Fecha de albarán'),
    'Заказ поставщику': ('Заказ поставщику', 'Commande fournisseur', 'Supplier order', 'Pedido a proveedor'),
    'Дата поставки': ('Дата поставки', 'Date de livraison', 'Delivery date', 'Fecha de entrega'),
    'Заказы поставщику': ('Заказы поставщику', 'Commandes fournisseur', 'Supplier orders', 'Pedidos a proveedor'),
    'Поступления': ('Поступления', 'Réceptions', 'Receipts', 'Recepciones'),
})
TT = lambda k: T[k]
PURCHASE_STATUS = ['СтатусВРаботу', 'СтатусВЧерновик', 'СтатусОтменить']
PURCHASE_CMDS = {
    'СтатусВРаботу': ('ЗакупкиПровести', ('Провести', 'Valider', 'Post', 'Contabilizar'),
                      ('Провести документы отмеченных строк', 'Valider les documents des lignes cochées',
                       'Post the documents of the ticked lines', 'Contabilizar los documentos de las líneas marcadas')),
    'СтатусВЧерновик': ('ЗакупкиВЧерновик', ('В черновик', 'En brouillon', 'To draft', 'A borrador'),
                        ('Отменить проведение документов отмеченных строк',
                         'Annuler la validation des documents des lignes cochées',
                         'Undo posting of the documents of the ticked lines',
                         'Anular la contabilización de los documentos de las líneas marcadas')),
    'СтатусОтменить': ('ЗакупкиОтменить', ('Отменить', 'Annuler', 'Cancel', 'Cancelar'),
                       ('Пометить документы отмеченных строк на удаление',
                        'Marquer les documents des lignes cochées pour suppression',
                        'Mark the documents of the ticked lines for deletion',
                        'Marcar los documentos de las líneas marcadas para eliminar')),
}


def group(name, children, ind, group_kind='Vertical', representation='None', visible=True, behavior=True,
          collapsible=False):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ''.join(c(i2) for c in children)
    s += common_vis(i2, visible)
    s += ext_tooltip(name, i2)
    s += f'{i2}<type>UsualGroup</type>\n{i2}<extInfo xsi:type="form:UsualGroupExtInfo">\n{i2}  <group>{group_kind}</group>\n'
    if collapsible:
        s += f'{i2}  <behavior>Collapsible</behavior>\n{i2}  <controlRepresentation>ButtonInParentElement</controlRepresentation>\n'
    elif behavior:
        s += f'{i2}  <behavior>Usual</behavior>\n'
    s += (f'{i2}  <representation>{representation}</representation>\n{i2}  <showLeftMargin>false</showLeftMargin>\n'
          f'{i2}  <united>true</united>\n{i2}  <showTitle>false</showTitle>\n{i2}  <throughAlign>Auto</throughAlign>\n'
          f'{i2}  <currentRowUse>Auto</currentRowUse>\n{i2}</extInfo>\n{ind}</items>\n')
    return s


def table(name, path, columns, ind, bar_items=(), **kw):
    """Таблица редакции 2 с кнопками в автокомандной панели: в 8.5.1 команды таблицы с использованием выделенных строк
    показываются в панели, которая появляется при отметке строк."""
    s = table2(name, path, columns, ind, **kw)
    if not bar_items:
        return s
    i2 = ind + '  '
    marker = f'{i2}  <name>{name}КоманднаяПанель</name>\n'
    head, tail = s.split(marker, 1)
    id_line, rest = tail.split('\n', 1)
    return head + marker + id_line + '\n' + ''.join(c(i2 + '  ') for c in bar_items) + rest


QUERY = '\n'.join(line for line in gen2.QUERY.split('\n') if 'Процент' not in line).replace(
    '\tИстория.Индикатор КАК Индикатор,\n', '\tИстория.Индикатор КАК Индикатор\n').replace(
'''	И (&amp;ЛюбаяПродукция''',
'''	И (&amp;ЛюбойКлиент
			ИЛИ ДокументЗаказПокупателя.Контрагент В
				(ВЫБРАТЬ
					КлиентыОтбора.Ссылка
				ИЗ
					Справочник.Контрагенты КАК КлиентыОтбора
				ГДЕ
					КлиентыОтбора.Наименование ПОДОБНО &amp;Клиент СПЕЦСИМВОЛ "~"))
	И (&amp;ЛюбаяПродукция''').replace(
'''ТоварыЗаказа.Номенклатура = &amp;Продукция))''',
'''ТоварыЗаказа.Номенклатура В
						(ВЫБРАТЬ
							ПродукцияОтбора.Ссылка
						ИЗ
							Справочник.Номенклатура КАК ПродукцияОтбора
						ГДЕ
							ПродукцияОтбора.Наименование ПОДОБНО &amp;Продукция СПЕЦСИМВОЛ "~")))''')
assert 'Процент' not in QUERY and 'ЛюбойКлиент' in QUERY and 'Наименование ПОДОБНО &amp;Продукция' in QUERY and 'Контрагент.Наименование' not in QUERY

CREATE = gen2.CREATE
STATUS = ['СтатусВРаботу', 'СтатусВЧерновик', 'СтатусОтменить']


def table_command(name, cid, title, tooltip, action, table_name):
    """Команда таблицы для панели выделенных строк: связана с таблицей и использует выделенные строки."""
    s = form_command(name, cid, title, tooltip, action)
    old = '    <currentRowUse>Auto</currentRowUse>\n    <selectedRowsUse>Auto</selectedRowsUse>\n'
    assert old in s
    return s.replace(old, '    <currentRowUse>Auto</currentRowUse>\n    <associatedTableElementId xsi:type="core:StringValue">\n'
                          f'      <value>{table_name}</value>\n    </associatedTableElementId>\n'
                          '    <selectedRowsUse>Use</selectedRowsUse>\n')


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
        L('ПродукцияСтатусДокумента', 'Продукция.СтатусДокумента', TT('Статус'), read_only=True),
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
    doc_cols = [L('ДокументыЗаказа' + c, 'ДокументыЗаказа.' + c, TT(t)) for c, t in [
        ('Вид', 'Вид'), ('Номер', 'Номер'), ('Дата', 'Дата'), ('Контрагент', 'Контрагент'), ('Статус', 'Статус'),
        ('Через', 'Через'), ('Сумма', 'Сумма')]]

    def bar_items(prefix):
        cmd_button = lambda n: (lambda i: button(prefix + n, 'Form.Command.' + prefix + n, i))
        status = lambda ind: popup(prefix + 'ПодменюСтатус', TT('Статус'), [cmd_button(n) for n in STATUS], ind)
        return [status] + [cmd_button(n) for n in CREATE]

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

    def purchase_bar(prefix):
        cmd_button = lambda n: (lambda i: button(prefix + n, 'Form.Command.' + prefix + n, i))
        return [lambda ind: popup(prefix + 'ПодменюСтатус', TT('Статус'), [cmd_button(n) for n in PURCHASE_STATUS], ind)]

    def purchase_handlers(prefix):
        return [('BeforeAddRow', prefix + 'ПередНачаломДобавления'), ('BeforeRowChange', prefix + 'ПередНачаломИзменения'),
                ('BeforeDeleteRow', prefix + 'ПередУдалением'), ('OnEditEnd', prefix + 'ПриОкончанииРедактирования'),
                ('Selection', prefix + 'Выбор')]

    def purchase_cols(prefix, receipts):
        P = prefix
        cols = [
            L(P + 'Статус', P + '.Статус', TT('Статус'), read_only=True),
            F(P + 'Поставщик', P + '.Поставщик', TT('Поставщик'), hs=[('OnChange', 'ЗакупкиПоставщикПриИзменении')]),
        ]
        if receipts:
            cols += [
                F(P + 'НомерВходящегоДокумента', P + '.НомерВходящегоДокумента', TT('Номер вх.'),
                  hs=[('OnChange', 'ПоступленияНомерВходящегоДокументаПриИзменении')]),
                F(P + 'ДатаВходящегоДокумента', P + '.ДатаВходящегоДокумента', TT('Дата вх.')),
            ]
        cols += [
            F(P + 'Материал', P + '.Материал', TT('Материал'), hs=[('OnChange', 'ЗакупкиМатериалПриИзменении')]),
            F(P + 'Характеристика', P + '.Характеристика', TT('Характеристика'),
              hs=[('OnChange', 'ЗакупкиХарактеристикаПриИзменении')]),
            F(P + 'КоличествоУпаковок', P + '.КоличествоУпаковок', TT('Количество')),
            F(P + 'Упаковка', P + '.Упаковка', TT('Упаковка')),
            F(P + 'Цена', P + '.Цена', TT('Цена'), hs=[('OnChange', 'ЗакупкиЦенаПриИзменении')]),
            L(P + 'Сумма', P + '.Сумма', TT('Сумма'), read_only=True),
        ]
        if receipts:
            cols += [F(P + 'СтрокаОснованияПредставление', P + '.СтрокаОснованияПредставление', TT('Заказ поставщику'),
                       choice_button=True, text_edit=False,
                       hs=[('StartChoice', 'ПоступленияСтрокаОснованияПредставлениеНачалоВыбора')])]
        else:
            cols += [L(P + 'Продукция', P + '.Продукция', TT('Продукция'), read_only=True),
                     L(P + 'ДатаПоставки', P + '.ДатаПоставки', TT('Дата поставки'), read_only=True)]
        cols += [F(P + 'ДокументПредставление', P + '.ДокументПредставление', TT('Документ'), choice_button=True,
                   text_edit=False, hs=[('StartChoice', 'ЗакупкиДокументПредставлениеНачалоВыбора')])]
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
        lambda i: page('СтраницаДокументы', TT('Документы'), [
            lambda j: table('ДокументыЗаказа', 'ДокументыЗаказа', doc_cols, j, read_only=True, height=5, multi=False,
                            hs=[('Selection', 'ДокументыЗаказаВыбор')])], i),
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
        ('СоздатьЗаказПоставщику', ('Заказ поставщику', 'Commande fournisseur', 'Supplier order', 'Pedido a proveedor'),
         ('Заказ поставщику на основании заказа на производство', 'Commande fournisseur à partir de la commande en production', 'Supplier order based on the production order', 'Pedido a proveedor a partir del pedido para producción')),
        ('СоздатьПоступление', ('Поступление', 'Réception', 'Receipt', 'Recepción'),
         ('Поступление на основании заказа на производство', 'Réception à partir de la commande en production', 'Receipt based on the production order', 'Recepción a partir del pedido para producción')),
        ('СоздатьПередачу', ('Передача в переработку', 'Envoi en sous-traitance', 'Send to subcontractor', 'Envío a subcontratista'),
         ('Передача в переработку на основании заказа на производство', 'Envoi en sous-traitance à partir de la commande en production', 'Subcontracting transfer based on the production order', 'Envío a subcontratista a partir del pedido para producción')),
        ('СоздатьОтгрузку', ('Отгрузка', 'Expédition', 'Shipment', 'Envío'),
         ('Реализация на основании заказа на производство', 'Vente à partir de la commande en production', 'Sale based on the production order', 'Venta a partir del pedido para producción')),
        ('ОткрытьПотребности', ('Потребности', 'Besoins', 'Requirements', 'Necesidades'),
         ('Отчёт «Потребности производства» по заказу', 'Rapport « Besoins de production » pour la commande', 'Production requirements report for the order', 'Informe de necesidades de producción del pedido')),
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
    attrs += attr_simple('МожноВводитьЗаказыПоставщику', 32, BOOL)
    attrs += attr_simple('МожноВводитьПоступления', 33, BOOL)
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
    for prefix in ('Заказы', 'Продукция'):
        for n, t, tt in cmds:
            if n in STATUS or n in CREATE:
                cid += 1
                fcmds += table_command(prefix + n, cid, t, tt, n, prefix)
    for prefix in ('ЗаказыПоставщику', 'Поступления'):
        for n in PURCHASE_STATUS:
            action, title, tooltip = PURCHASE_CMDS[n]
            cid += 1
            fcmds += table_command(prefix + n, cid, title, tooltip, action, prefix)
    for n, t, tt in cmds:
        if n not in STATUS and n not in CREATE:
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
