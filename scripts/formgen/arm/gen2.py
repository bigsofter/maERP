#!/usr/bin/env python3
"""Форма рабочего места производства, редакция 2 (замечания владельца 2026-09-15): без колонки комментария, панель
фильтров справа как у списков документов, кнопки ввода на основании над таблицами, статусы в «Продукции»."""
import sys
import gen
from gen import (IDS, ml, ext_tooltip, context_menu, common_vis, handlers, field, button, popup, pages, page,
                 attr_simple, attr_vt, form_command, NUM, STR, DATE, T, DOC_TYPES)

T.update({
    'Менеджер': ('Менеджер', 'Manager', 'Manager', 'Gerente'),
    'Фильтры': ('Фильтры', 'Filtres', 'Filters', 'Filtros'),
    'Заказы на производство': ('Заказы', 'Commandes', 'Orders', 'Pedidos'),
    'Показывать заказы': ('Заказы', 'Commandes', 'Orders', 'Pedidos'),
})
TT = lambda k: T[k]


def group(name, children, ind, group_kind='Vertical', representation='None', visible=True, extra='', behavior=True):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ''.join(c(i2) for c in children)
    s += common_vis(i2, visible)
    s += extra
    s += ext_tooltip(name, i2)
    s += f'{i2}<type>UsualGroup</type>\n{i2}<extInfo xsi:type="form:UsualGroupExtInfo">\n{i2}  <group>{group_kind}</group>\n'
    if behavior:
        s += f'{i2}  <behavior>Usual</behavior>\n'
    s += (f'{i2}  <representation>{representation}</representation>\n{i2}  <showLeftMargin>false</showLeftMargin>\n'
          f'{i2}  <united>true</united>\n{i2}  <showTitle>false</showTitle>\n{i2}  <throughAlign>Auto</throughAlign>\n'
          f'{i2}  <currentRowUse>Auto</currentRowUse>\n{i2}</extInfo>\n{ind}</items>\n')
    return s


def command_bar(name, children, ind, visible=False):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ''.join(c(i2) for c in children)
    s += common_vis(i2, visible)
    s += ext_tooltip(name, i2)
    s += (f'{i2}<type>CommandBar</type>\n{i2}<extInfo xsi:type="form:CommandBarExtInfo">\n'
          f'{i2}  <horizontalAlign>Left</horizontalAlign>\n{i2}</extInfo>\n{ind}</items>\n')
    return s


def picture_button(name, command, picture, ind):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:Button">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += common_vis(i2)
    s += ext_tooltip(name, i2)
    s += (f'{i2}<commandName>{command}</commandName>\n{i2}<representation>Picture</representation>\n'
          f'{i2}<autoMaxWidth>true</autoMaxWidth>\n{i2}<autoMaxHeight>true</autoMaxHeight>\n'
          f'{i2}<placementArea>UserCmds</placementArea>\n{i2}<picture xsi:type="core:PictureRef">\n'
          f'{i2}  <picture>CommonPicture.{picture}</picture>\n{i2}</picture>\n'
          f'{i2}<representationInContextMenu>Auto</representationInContextMenu>\n{ind}</items>\n')
    return s


def info_pages_group(name, children, ind):
    """Страницы панели сведений: скрыты, пока панель свёрнута; растягиваются, чтобы кнопка свернуть была внизу."""
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ''.join(c(i2) for c in children)
    s += common_vis(i2, False)
    s += f'{i2}<verticalStretch>true</verticalStretch>\n'
    s += ext_tooltip(name, i2)
    s += (f'{i2}<type>Pages</type>\n{i2}<extInfo xsi:type="form:PagesGroupExtInfo">\n'
          f'{i2}  <pagesRepresentation>TabsOnTop</pagesRepresentation>\n{i2}</extInfo>\n{ind}</items>\n')
    return s


def top_field(name, path, ind, title, hs):
    """Поле фильтра панели: заголовок сверху, как ОтборКонтрагент списка реализаций."""
    return field(name, path, ind, title=title, kind='InputField', hs=hs, title_loc='Top')


def table(name, path, columns, ind, hs=(), dynamic=False, read_only=False, height=10, change_rows=False, multi=True,
          stretch=True, command_bar_none=False):
    """Таблица со свойствами эталонного списка реализаций: без них EDT пишет в платформу выключенные полосы прокрутки,
    нулевой подвал и начальный вид «с начала»."""
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:Table">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += common_vis(i2)
    s += f'{i2}<dataPath xsi:type="form:DataPath">\n{i2}  <segments>{path}</segments>\n{i2}</dataPath>\n'
    s += f'{i2}<titleLocation>None</titleLocation>\n'
    if read_only:
        s += f'{i2}<readOnly>true</readOnly>\n'
    s += ext_tooltip(name, i2)
    s += context_menu(name, i2)
    if command_bar_none:
        s += f'{i2}<commandBarLocation>None</commandBarLocation>\n'
    s += (f'{i2}<autoCommandBar>\n{i2}  <name>{name}КоманднаяПанель</name>\n{i2}  <id>{IDS.next()}</id>\n'
          f'{i2}  <horizontalAlign>Left</horizontalAlign>\n{i2}  <autoFill>{"true" if change_rows else "false"}</autoFill>\n'
          f'{i2}</autoCommandBar>\n')
    s += handlers(hs, i2)
    s += ''.join(c(i2) for c in columns)
    s += f'{i2}<changeRowSet>{"true" if change_rows else "false"}</changeRowSet>\n{i2}<changeRowOrder>false</changeRowOrder>\n'
    s += (f'{i2}<autoMaxWidth>true</autoMaxWidth>\n{i2}<autoMaxHeight>true</autoMaxHeight>\n'
          f'{i2}<heightInTableRows>{height}</heightInTableRows>\n{i2}<autoMaxRowsCount>true</autoMaxRowsCount>\n')
    s += f'{i2}<selectionMode>{"MultiRow" if multi else "SingleRow"}</selectionMode>\n'
    s += (f'{i2}<header>true</header>\n{i2}<headerHeight>1</headerHeight>\n{i2}<footerHeight>1</footerHeight>\n'
          f'{i2}<horizontalScrollBar>AutoUse</horizontalScrollBar>\n{i2}<verticalScrollBar>AutoUse</verticalScrollBar>\n'
          f'{i2}<horizontalLines>true</horizontalLines>\n{i2}<verticalLines>true</verticalLines>\n'
          f'{i2}<searchOnInput>Auto</searchOnInput>\n{i2}<initialListView>Auto</initialListView>\n')
    s += f'{i2}<horizontalStretch>true</horizontalStretch>\n{i2}<verticalStretch>{"true" if stretch else "false"}</verticalStretch>\n'
    s += (f'{i2}<borderColor xsi:type="core:ColorRef">\n{i2}  <color>Style.FormBackColor</color>\n{i2}</borderColor>\n'
          f'{i2}<autoMaxCardHeight>true</autoMaxCardHeight>\n')
    if dynamic:
        s += (f'{i2}<extInfo xsi:type="form:DynamicListTableExtInfo">\n{i2}  <autoRefreshPeriod>60</autoRefreshPeriod>\n'
              f'{i2}  <period>\n{i2}    <startDate>0001-01-01T00:00:00</startDate>\n{i2}    <endDate>0001-01-01T00:00:00</endDate>\n'
              f'{i2}  </period>\n{i2}  <topLevelParent xsi:type="core:UndefinedValue"/>\n{i2}  <showRoot>true</showRoot>\n'
              f'{i2}  <allowGettingCurrentRowURL>true</allowGettingCurrentRowURL>\n{i2}</extInfo>\n')
    s += f'{ind}</items>\n'
    return s


QUERY = gen.QUERY.replace('''	ДокументЗаказПокупателя.Комментарий КАК Комментарий,
''', '').replace('''ГДЕ
	(&amp;ВсеЗаказы
			ИЛИ ДокументЗаказПокупателя.ВидОперации = ЗНАЧЕНИЕ(Перечисление.ВидыОперацийЗаказаПокупателя.Производство))''',
'''ГДЕ
	(&amp;ВсеЗаказы
			ИЛИ ДокументЗаказПокупателя.ВидОперации = ЗНАЧЕНИЕ(Перечисление.ВидыОперацийЗаказаПокупателя.Производство))
	И (&amp;ЛюбаяПродукция
			ИЛИ ДокументЗаказПокупателя.Ссылка В
				(ВЫБРАТЬ
					ТоварыЗаказа.Ссылка
				ИЗ
					Документ.ЗаказПокупателя.ТЧТовары КАК ТоварыЗаказа
				ГДЕ
					ТоварыЗаказа.Номенклатура = &amp;Продукция))''')
assert 'ЛюбаяПродукция' in QUERY and 'Комментарий' not in QUERY

CREATE = ['СоздатьЗаказПоставщику', 'СоздатьПоступление', 'СоздатьПередачу', 'СоздатьОтгрузку', 'ОткрытьПотребности']
SHARES = [('ПроцентОбеспечения', 'Обеспечение, %'), ('ПроцентПоступления', 'Поступление, %'), ('ПроцентВыпуска', 'Выпуск, %'),
          ('ПроцентОтгрузки', 'Отгрузка, %'), ('ПроцентОплаты', 'Оплата, %')]


def build():
    L = lambda n, p, t=None, **k: (lambda ind: field(n, p, ind, title=t, **k))
    F = lambda n, p, t=None, **k: (lambda ind: field(n, p, ind, title=t, kind='InputField', **k))

    orders_cols = [
        L('ЗаказыНомер', 'Заказы.Номер', TT('Номер')),
        L('ЗаказыДата', 'Заказы.Дата', TT('Дата')),
        L('ЗаказыКонтрагент', 'Заказы.Контрагент', TT('Клиент')),
        L('ЗаказыСтатус', 'Заказы.Статус', TT('Стадия')),
        L('ЗаказыИндикатор', 'Заказы.Индикатор', TT('Индикатор')),
    ] + [L('Заказы' + c, 'Заказы.' + c, TT(t)) for c, t in SHARES] + [
        L('ЗаказыДатаОтгрузки', 'Заказы.ДатаОтгрузки', TT('Дата отгрузки')),
        L('ЗаказыСумма', 'Заказы.Сумма', TT('Сумма')),
        L('ЗаказыМенеджер', 'Заказы.Менеджер', TT('Менеджер')),
    ]
    prod_cols = [
        F('ПродукцияЗаказПредставление', 'Продукция.ЗаказПредставление', TT('Заказ на производство'), choice_button=True,
          text_edit=False, hs=[('StartChoice', 'ПродукцияЗаказПредставлениеНачалоВыбора')]),
        F('ПродукцияКлиент', 'Продукция.Клиент', TT('Клиент'), hs=[('OnChange', 'ПродукцияКлиентПриИзменении')]),
        F('ПродукцияНоменклатура', 'Продукция.Номенклатура', TT('Продукция'),
          hs=[('OnChange', 'ПродукцияНоменклатураПриИзменении')]),
        F('ПродукцияХарактеристика', 'Продукция.Характеристика', TT('Характеристика')),
        F('ПродукцияКоличествоУпаковок', 'Продукция.КоличествоУпаковок', TT('Количество')),
        F('ПродукцияУпаковка', 'Продукция.Упаковка', TT('Упаковка')),
        F('ПродукцияЦена', 'Продукция.Цена', TT('Цена'), hs=[('OnChange', 'ПродукцияЦенаПриИзменении')]),
        L('ПродукцияСумма', 'Продукция.Сумма', TT('Сумма'), read_only=True),
        L('ПродукцияСтадия', 'Продукция.Стадия', TT('Стадия'), read_only=True),
        L('ПродукцияИндикатор', 'Продукция.Индикатор', TT('Индикатор'), read_only=True),
    ] + [L('Продукция' + c, 'Продукция.' + c, TT(t), read_only=True) for c, t in SHARES] + [
        L('ПродукцияДатаОтгрузки', 'Продукция.ДатаОтгрузки', TT('Дата отгрузки'), read_only=True),
        L('ПродукцияМенеджер', 'Продукция.Менеджер', TT('Менеджер'), read_only=True),
        L('ПродукцияСтатусДокумента', 'Продукция.СтатусДокумента', TT('Статус'), read_only=True),
    ]
    mat_cols = [L('Материалы' + c, 'Материалы.' + c, TT(t)) for c, t in [
        ('Продукция', 'Продукция'), ('Материал', 'Материал'), ('Характеристика', 'Характеристика'),
        ('ПоСоставу', 'По составу'), ('Потребность', 'Потребность'), ('Заказано', 'Заказано'), ('Пришло', 'Пришло'),
        ('ИзОстатка', 'Из остатка'), ('Дефицит', 'Дефицит'), ('КПоступлению', 'К поступлению')]]
    doc_cols = [L('ДокументыЗаказа' + c, 'ДокументыЗаказа.' + c, TT(t)) for c, t in [
        ('Вид', 'Вид'), ('Номер', 'Номер'), ('Дата', 'Дата'), ('Контрагент', 'Контрагент'), ('Статус', 'Статус'),
        ('Через', 'Через'), ('Сумма', 'Сумма')]]

    def actions(prefix):
        return lambda ind: command_bar('ГруппаДействия' + prefix,
                                       [(lambda n: (lambda i: button(prefix + n, 'Form.Command.' + n, i)))(n) for n in CREATE],
                                       ind)

    top = lambda ind: pages('ГруппаВерх', [
        lambda i: page('СтраницаЗаказы', TT('Заказы'), [
            actions('Заказы'),
            lambda j: table('Заказы', 'Заказы', orders_cols, j, dynamic=True, height=8, command_bar_none=True,
                            hs=[('Selection', 'ЗаказыВыбор'), ('OnActivateRow', 'ЗаказыПриАктивизацииСтроки')])], i),
        lambda i: page('СтраницаПродукция', TT('Продукция'), [
            actions('Продукция'),
            lambda j: table('Продукция', 'Продукция', prod_cols, j, height=8, change_rows=True,
                            hs=[('OnActivateRow', 'ПродукцияПриАктивизацииСтроки'),
                                ('OnStartEdit', 'ПродукцияПриНачалеРедактирования'),
                                ('BeforeAddRow', 'ПродукцияПередНачаломДобавления'),
                                ('BeforeRowChange', 'ПродукцияПередНачаломИзменения'),
                                ('BeforeDeleteRow', 'ПродукцияПередУдалением'),
                                ('OnEditEnd', 'ПродукцияПриОкончанииРедактирования')])], i),
    ], ind, hs=[('OnCurrentPageChange', 'ГруппаВерхПриСменеСтраницы')])

    bottom = lambda ind: pages('ГруппаНиз', [
        lambda i: page('СтраницаМатериалы', TT('Материалы'), [
            lambda j: table('Материалы', 'Материалы', mat_cols, j, read_only=True, height=5, multi=False,
                            stretch=False)], i),
        lambda i: page('СтраницаДокументы', TT('Документы'), [
            lambda j: table('ДокументыЗаказа', 'ДокументыЗаказа', doc_cols, j, read_only=True, height=5, multi=False,
                            stretch=False, hs=[('Selection', 'ДокументыЗаказаВыбор')])], i),
    ], ind)

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
        lambda i: group('ГруппаЛевая', [top, bottom], i),
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
    bar += popup('ПодменюСтатус', TT('Статус'),
                 [(lambda n: (lambda ind: button('Форма' + n, 'Form.Command.' + n, ind)))(n)
                  for n in ('СтатусВРаботу', 'СтатусВЧерновик', 'СтатусОтменить')], '    ')
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
    PERCENT = '<types>Number</types>' + NUM(5, 0)
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
    ] + [(c, PERCENT, TT(t)) for c, t in SHARES] + [
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
    attrs += attr_simple('ТекущийЗаказ', 7, REF('DocumentRef.ЗаказПокупателя'))
    booleans = ['ПоказыватьСуммы', 'МожноМенятьЗаказы', 'МожноПроводитьЗаказы', 'МожноПомечатьЗаказы',
                'МожноЗаказПоставщику', 'МожноПоступление', 'МожноПередачу', 'МожноОтгрузку', 'МожноНаОсновании']
    for i, n in enumerate(booleans, 8):
        attrs += attr_simple(n, i, REF('Boolean'))
    next_id = 8 + len(booleans)
    attrs += attr_simple('ПанельРазвернута', next_id, REF('Boolean'), saved=True)
    attrs += attr_simple('ОтборКлиент', next_id + 1, REF('CatalogRef.Контрагенты'), title=TT('Клиент'))
    attrs += attr_simple('ОтборПродукция', next_id + 2, REF('CatalogRef.Номенклатура'), title=TT('Продукция'))

    fcmds = ''.join(form_command(n, i, t, tt, n) for i, (n, t, tt) in enumerate(cmds, 1))

    out = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<form:Form xmlns:form="http://g5.1c.ru/v8/dt/form" xmlns:core="http://g5.1c.ru/v8/dt/mcore" '
           'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n')
    out += items + bar + form_handlers + props + attrs + fcmds
    out += '  <commandInterface>\n    <navigationPanel/>\n    <commandBar/>\n  </commandInterface>\n'
    out += '  <extInfo xsi:type="form:ObjectFormExtInfo"/>\n</form:Form>\n'
    return out


if __name__ == '__main__':
    sys.stdout.write(build())
