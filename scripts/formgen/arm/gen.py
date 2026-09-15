#!/usr/bin/env python3
"""Генератор Form.form рабочего места производства по образцам XML проекта maERP."""
import sys
from xml.sax.saxutils import escape

LANGS = ('ru', 'fr', 'en', 'es')


class Ids:
    def __init__(self):
        self.n = 0

    def next(self):
        self.n += 1
        return self.n


IDS = Ids()


def ml(tag, texts, ind):
    if not texts:
        return ''
    out = []
    for lang, val in zip(LANGS, texts):
        out.append(f'{ind}<{tag}>\n{ind}  <key>{lang}</key>\n{ind}  <value>{escape(val)}</value>\n{ind}</{tag}>')
    return '\n'.join(out) + '\n'


def ext_tooltip(name, ind):
    return (f'{ind}<extendedTooltip>\n{ind}  <name>{name}РасширеннаяПодсказка</name>\n{ind}  <id>{IDS.next()}</id>\n'
            f'{ind}  <type>Label</type>\n{ind}  <autoMaxWidth>true</autoMaxWidth>\n{ind}  <autoMaxHeight>true</autoMaxHeight>\n'
            f'{ind}  <extInfo xsi:type="form:LabelDecorationExtInfo">\n{ind}    <horizontalAlign>Left</horizontalAlign>\n'
            f'{ind}  </extInfo>\n{ind}</extendedTooltip>\n')


def context_menu(name, ind):
    return f'{ind}<contextMenu>\n{ind}  <name>{name}КонтекстноеМеню</name>\n{ind}  <id>{IDS.next()}</id>\n{ind}  <autoFill>true</autoFill>\n{ind}</contextMenu>\n'


def common_vis(ind, visible=True):
    return (f'{ind}<visible>{"true" if visible else "false"}</visible>\n{ind}<enabled>true</enabled>\n'
            f'{ind}<userVisible>\n{ind}  <common>true</common>\n{ind}</userVisible>\n')


def handlers(hs, ind):
    return ''.join(f'{ind}<handlers>\n{ind}  <event>{e}</event>\n{ind}  <name>{n}</name>\n{ind}</handlers>\n' for e, n in hs)


def field(name, path, ind, title=None, kind='LabelField', hs=(), width=None, visible=True, choice_button=False,
          text_edit=True, read_only=False, tooltip=None, choice_list=None, radio=False, title_loc=None):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormField">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ml('title', title, i2)
    s += ml('toolTip', tooltip, i2)
    s += common_vis(i2, visible)
    if read_only:
        s += f'{i2}<readOnly>true</readOnly>\n'
    s += f'{i2}<dataPath xsi:type="form:DataPath">\n{i2}  <segments>{path}</segments>\n{i2}</dataPath>\n'
    if title_loc:
        s += f'{i2}<titleLocation>{title_loc}</titleLocation>\n'
    s += handlers(hs, i2)
    s += ext_tooltip(name, i2)
    s += context_menu(name, i2)
    if radio:
        s += f'{i2}<type>RadioButtonField</type>\n{i2}<editMode>Enter</editMode>\n'
        s += f'{i2}<extInfo xsi:type="form:RadioButtonsFieldExtInfo">\n{i2}  <radioButtonsType>Tumbler</radioButtonsType>\n'
        s += f'{i2}  <equalElementsWidth>false</equalElementsWidth>\n'
        for texts, value in choice_list:
            s += f'{i2}  <choiceList>\n'
            s += ml('presentation', texts, i2 + '    ')
            s += f'{i2}    <value xsi:type="core:NumberValue">\n{i2}      <value>{value}</value>\n{i2}    </value>\n{i2}  </choiceList>\n'
        s += f'{i2}</extInfo>\n'
    elif kind == 'LabelField':
        s += f'{i2}<type>LabelField</type>\n{i2}<editMode>Enter</editMode>\n{i2}<showInHeader>true</showInHeader>\n'
        s += f'{i2}<headerHorizontalAlign>Left</headerHorizontalAlign>\n{i2}<showInFooter>true</showInFooter>\n'
        s += f'{i2}<extInfo xsi:type="form:LabelFieldExtInfo">\n'
        if width:
            s += f'{i2}  <width>{width}</width>\n'
        s += f'{i2}  <autoMaxWidth>true</autoMaxWidth>\n{i2}  <autoMaxHeight>true</autoMaxHeight>\n{i2}</extInfo>\n'
    else:
        s += f'{i2}<type>InputField</type>\n{i2}<editMode>Enter</editMode>\n{i2}<showInHeader>true</showInHeader>\n'
        s += f'{i2}<headerHorizontalAlign>Left</headerHorizontalAlign>\n{i2}<showInFooter>true</showInFooter>\n'
        s += f'{i2}<extInfo xsi:type="form:InputFieldExtInfo">\n'
        if width:
            s += f'{i2}  <width>{width}</width>\n'
        s += f'{i2}  <autoMaxWidth>true</autoMaxWidth>\n{i2}  <autoMaxHeight>true</autoMaxHeight>\n'
        if choice_button:
            s += f'{i2}  <choiceButton>true</choiceButton>\n'
        s += f'{i2}  <textEdit>{"true" if text_edit else "false"}</textEdit>\n{i2}  <textSize>Normal</textSize>\n{i2}</extInfo>\n'
    s += f'{ind}</items>\n'
    return s


def button(name, command, ind, title=None, importance='Normal'):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:Button">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ml('title', title, i2)
    s += common_vis(i2)
    s += ext_tooltip(name, i2)
    s += f'{i2}<commandName>{command}</commandName>\n{i2}<representation>Auto</representation>\n'
    s += f'{i2}<autoMaxWidth>true</autoMaxWidth>\n{i2}<autoMaxHeight>true</autoMaxHeight>\n'
    s += f'{i2}<placementArea>UserCmds</placementArea>\n{i2}<representationInContextMenu>Auto</representationInContextMenu>\n'
    s += f'{i2}<buttonImportance>{importance}</buttonImportance>\n{ind}</items>\n'
    return s


def popup(name, title, children, ind):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ''.join(c(i2) for c in children)
    s += common_vis(i2)
    s += ml('title', title, i2)
    s += ext_tooltip(name, i2)
    s += f'{i2}<type>Popup</type>\n{i2}<extInfo xsi:type="form:PopupGroupExtInfo">\n{i2}  <representation>Auto</representation>\n'
    s += f'{i2}  <importance>Normal</importance>\n{i2}</extInfo>\n{ind}</items>\n'
    return s


def usual_group(name, children, ind, group='Horizontal'):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ''.join(c(i2) for c in children)
    s += common_vis(i2)
    s += ext_tooltip(name, i2)
    s += (f'{i2}<type>UsualGroup</type>\n{i2}<extInfo xsi:type="form:UsualGroupExtInfo">\n{i2}  <group>{group}</group>\n'
          f'{i2}  <behavior>Usual</behavior>\n{i2}  <representation>None</representation>\n{i2}  <showLeftMargin>true</showLeftMargin>\n'
          f'{i2}  <united>true</united>\n{i2}  <showTitle>false</showTitle>\n{i2}  <throughAlign>Auto</throughAlign>\n'
          f'{i2}  <currentRowUse>Auto</currentRowUse>\n{i2}</extInfo>\n{ind}</items>\n')
    return s


def pages(name, children, ind, hs=()):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ''.join(c(i2) for c in children)
    s += common_vis(i2)
    s += handlers(hs, i2)
    s += ext_tooltip(name, i2)
    s += (f'{i2}<type>Pages</type>\n{i2}<extInfo xsi:type="form:PagesGroupExtInfo">\n{i2}  <pagesRepresentation>TabsOnTop</pagesRepresentation>\n'
          f'{i2}  <currentRowUse>Auto</currentRowUse>\n{i2}</extInfo>\n{ind}</items>\n')
    return s


def page(name, title, children, ind, rows_path=None):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += ml('title', title, i2)
    s += common_vis(i2)
    s += ext_tooltip(name, i2)
    s += ''.join(c(i2) for c in children)
    s += f'{i2}<type>Page</type>\n{i2}<extInfo xsi:type="form:PageGroupExtInfo">\n{i2}  <group>Vertical</group>\n{i2}  <showTitle>true</showTitle>\n'
    if rows_path:
        s += f'{i2}  <titleDataPath xsi:type="form:DataPath">\n{i2}    <segments>{rows_path}.RowsCount</segments>\n{i2}  </titleDataPath>\n'
    s += f'{i2}</extInfo>\n{ind}</items>\n'
    return s


def table(name, path, columns, ind, hs=(), dynamic=False, read_only=False, height=10, change_rows=False, multi=True,
          stretch=True):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:Table">\n{i2}<name>{name}</name>\n{i2}<id>{IDS.next()}</id>\n'
    s += common_vis(i2)
    s += f'{i2}<dataPath xsi:type="form:DataPath">\n{i2}  <segments>{path}</segments>\n{i2}</dataPath>\n'
    s += f'{i2}<titleLocation>None</titleLocation>\n'
    if read_only:
        s += f'{i2}<readOnly>true</readOnly>\n'
    s += ext_tooltip(name, i2)
    s += context_menu(name, i2)
    s += (f'{i2}<autoCommandBar>\n{i2}  <name>{name}КоманднаяПанель</name>\n{i2}  <id>{IDS.next()}</id>\n'
          f'{i2}  <horizontalAlign>Left</horizontalAlign>\n{i2}  <autoFill>{"true" if change_rows else "false"}</autoFill>\n{i2}</autoCommandBar>\n')
    s += handlers(hs, i2)
    s += ''.join(c(i2) for c in columns)
    s += f'{i2}<changeRowSet>{"true" if change_rows else "false"}</changeRowSet>\n{i2}<changeRowOrder>false</changeRowOrder>\n'
    s += f'{i2}<autoMaxWidth>true</autoMaxWidth>\n{i2}<heightInTableRows>{height}</heightInTableRows>\n'
    s += f'{i2}<selectionMode>{"MultiRow" if multi else "SingleRow"}</selectionMode>\n'
    s += f'{i2}<header>true</header>\n{i2}<headerHeight>1</headerHeight>\n'
    s += f'{i2}<horizontalStretch>true</horizontalStretch>\n{i2}<verticalStretch>{"true" if stretch else "false"}</verticalStretch>\n'
    if dynamic:
        s += (f'{i2}<extInfo xsi:type="form:DynamicListTableExtInfo">\n{i2}  <autoRefreshPeriod>60</autoRefreshPeriod>\n'
              f'{i2}  <period>\n{i2}    <startDate>0001-01-01T00:00:00</startDate>\n{i2}    <endDate>0001-01-01T00:00:00</endDate>\n'
              f'{i2}  </period>\n{i2}  <topLevelParent xsi:type="core:UndefinedValue"/>\n{i2}  <showRoot>true</showRoot>\n'
              f'{i2}  <allowGettingCurrentRowURL>true</allowGettingCurrentRowURL>\n{i2}</extInfo>\n')
    s += f'{ind}</items>\n'
    return s


def vt(tn, qual=None):
    """Тип значения колонки/реквизита."""
    s = f'<types>{tn}</types>'
    if qual:
        s += qual
    return s


NUM = lambda p, sc: f'\n        <numberQualifiers>\n          <precision>{p}</precision>\n          <scale>{sc}</scale>\n        </numberQualifiers>'
STR = lambda n: f'\n        <stringQualifiers>\n          <length>{n}</length>\n        </stringQualifiers>'
DATE = '\n        <dateQualifiers>\n          <dateFractions>Date</dateFractions>\n        </dateQualifiers>'


def attr_simple(name, aid, types, title=None, saved=False, main=False, extra=''):
    s = f'  <attributes>\n    <name>{name}</name>\n'
    s += ml('title', title, '    ')
    s += f'    <id>{aid}</id>\n    <valueType>\n      {types}\n    </valueType>\n'
    s += '    <view>\n      <common>true</common>\n    </view>\n    <edit>\n      <common>true</common>\n    </edit>\n'
    if main:
        s += '    <main>true</main>\n'
    if saved:
        s += '    <savedData>true</savedData>\n'
    s += extra
    s += '  </attributes>\n'
    return s


def attr_vt(name, aid, cols):
    s = f'  <attributes>\n    <name>{name}</name>\n    <id>{aid}</id>\n    <valueType>\n      <types>ValueTable</types>\n    </valueType>\n'
    s += '    <view>\n      <common>true</common>\n    </view>\n    <edit>\n      <common>true</common>\n    </edit>\n'
    for i, (cn, types, title) in enumerate(cols, 1):
        s += f'    <columns>\n      <name>{cn}</name>\n'
        s += ml('title', title, '      ')
        s += f'      <id>{i}</id>\n      <valueType>\n        {types}\n      </valueType>\n'
        s += '      <view>\n        <common>true</common>\n      </view>\n      <edit>\n        <common>true</common>\n      </edit>\n    </columns>\n'
    s += '  </attributes>\n'
    return s


def form_command(name, cid, title, tooltip, action):
    s = f'  <formCommands>\n    <name>{name}</name>\n'
    s += ml('title', title, '    ')
    s += f'    <id>{cid}</id>\n'
    s += ml('toolTip', tooltip, '    ')
    s += ('    <use>\n      <common>true</common>\n    </use>\n    <action xsi:type="form:FormCommandHandlerContainer">\n'
          f'      <handler>\n        <name>{action}</name>\n      </handler>\n    </action>\n'
          '    <currentRowUse>Auto</currentRowUse>\n    <selectedRowsUse>Auto</selectedRowsUse>\n  </formCommands>\n')
    return s


QUERY = """ВЫБРАТЬ
	ДокументЗаказПокупателя.Ссылка КАК Ссылка,
	ДокументЗаказПокупателя.ПометкаУдаления КАК ПометкаУдаления,
	ДокументЗаказПокупателя.Проведен КАК Проведен,
	ДокументЗаказПокупателя.Номер КАК Номер,
	ДокументЗаказПокупателя.Дата КАК Дата,
	ДокументЗаказПокупателя.ДатаОтгрузки КАК ДатаОтгрузки,
	ДокументЗаказПокупателя.Контрагент КАК Контрагент,
	ДокументЗаказПокупателя.Менеджер КАК Менеджер,
	ДокументЗаказПокупателя.Сумма КАК Сумма,
	ДокументЗаказПокупателя.Комментарий КАК Комментарий,
	ДокументЗаказПокупателя.ВидОперации КАК ВидОперации,
	История.СтатусЗаказаПокупателя КАК Статус,
	История.Индикатор КАК Индикатор,
	ВЫРАЗИТЬ(ЕСТЬNULL(История.ДоляОбеспечения, 0) * 100 КАК ЧИСЛО(5, 0)) КАК ПроцентОбеспечения,
	ВЫРАЗИТЬ(ЕСТЬNULL(История.ДоляПоступления, 0) * 100 КАК ЧИСЛО(5, 0)) КАК ПроцентПоступления,
	ВЫРАЗИТЬ(ЕСТЬNULL(История.ДоляВыпуска, 0) * 100 КАК ЧИСЛО(5, 0)) КАК ПроцентВыпуска,
	ВЫРАЗИТЬ(ЕСТЬNULL(История.ДоляОтгрузки, 0) * 100 КАК ЧИСЛО(5, 0)) КАК ПроцентОтгрузки,
	ВЫРАЗИТЬ(ЕСТЬNULL(История.ДоляОплаты, 0) * 100 КАК ЧИСЛО(5, 0)) КАК ПроцентОплаты
ИЗ
	Документ.ЗаказПокупателя КАК ДокументЗаказПокупателя
		ЛЕВОЕ СОЕДИНЕНИЕ РегистрСведений.ИсторияЗаказовПокупателейПоСтатусам.СрезПоследних КАК История
		ПО ДокументЗаказПокупателя.Ссылка = История.ЗаказПокупателя
ГДЕ
	(&amp;ВсеЗаказы
			ИЛИ ДокументЗаказПокупателя.ВидОперации = ЗНАЧЕНИЕ(Перечисление.ВидыОперацийЗаказаПокупателя.Производство))"""

T = {
    'Заказ на производство': ('Заказ на производство', 'Commande en production', 'Production order', 'Pedido para producción'),
    'Клиент': ('Клиент', 'Client', 'Customer', 'Cliente'),
    'Стадия': ('Стадия', 'Étape', 'Stage', 'Etapa'),
    'Индикатор': ('Индикатор', 'Indicateur', 'Indicator', 'Indicador'),
    'Обеспечение, %': ('Обеспечение, %', 'Approvisionnement, %', 'Materials ordered, %', 'Abastecimiento, %'),
    'Поступление, %': ('Поступление, %', 'Réception, %', 'Materials received, %', 'Recepción, %'),
    'Выпуск, %': ('Выпуск, %', 'Production, %', 'Output, %', 'Producción, %'),
    'Отгрузка, %': ('Отгрузка, %', 'Expédition, %', 'Shipment, %', 'Envío, %'),
    'Оплата, %': ('Оплата, %', 'Paiement, %', 'Payment, %', 'Pago, %'),
    'Дата отгрузки': ('Дата отгрузки', "Date d'expédition", 'Shipping date', 'Fecha de envío'),
    'Продукция': ('Продукция', 'Produit', 'Product', 'Producto'),
    'Характеристика': ('Характеристика', 'Caractéristique', 'Characteristic', 'Característica'),
    'Упаковка': ('Упаковка', 'Conditionnement', 'Packaging', 'Embalaje'),
    'Количество': ('Количество', 'Quantité', 'Quantity', 'Cantidad'),
    'Цена': ('Цена', 'Prix', 'Price', 'Precio'),
    'Сумма': ('Сумма', 'Montant', 'Amount', 'Importe'),
    'Статус': ('Статус', 'Statut', 'Status', 'Estado'),
    'Материал': ('Материал', 'Matière', 'Material', 'Material'),
    'По составу': ('По составу', 'Selon composition', 'By composition', 'Según composición'),
    'Потребность': ('Потребность', 'Besoin', 'Requirement', 'Necesidad'),
    'Заказано': ('Заказано', 'Commandé', 'Ordered', 'Pedido'),
    'Пришло': ('Пришло', 'Reçu', 'Received', 'Recibido'),
    'Из остатка': ('Из остатка', 'Du stock', 'From stock', 'Del stock'),
    'Дефицит': ('Дефицит', 'Déficit', 'Shortage', 'Déficit'),
    'К поступлению': ('К поступлению', 'À recevoir', 'To receive', 'Por recibir'),
    'Документ': ('Документ', 'Document', 'Document', 'Documento'),
    'Вид': ('Вид', 'Type', 'Type', 'Tipo'),
    'Номер': ('Номер', 'Numéro', 'Number', 'Número'),
    'Дата': ('Дата', 'Date', 'Date', 'Fecha'),
    'Контрагент': ('Контрагент', 'Tiers', 'Counterparty', 'Contraparte'),
    'Через': ('Через', 'Via', 'Via', 'Vía'),
    'Заказы': ('Заказы', 'Commandes', 'Orders', 'Pedidos'),
    'Материалы': ('Материалы', 'Matières', 'Materials', 'Materiales'),
    'Документы': ('Документы', 'Documents', 'Documents', 'Documentos'),
    'Показывать': ('Показывать', 'Afficher', 'Show', 'Mostrar'),
}
TT = lambda k: T[k]

DOC_TYPES = ['ЗаказПоставщику', 'ПоступлениеТоваровУслуг', 'ПередачаВПереработку', 'ПоступлениеИзПереработки',
             'РеализацияТоваровУслуг', 'ВыпускПродукции', 'ВозвратОтПокупателя', 'ВозвратПоставщику']


def build():
    I = '  '
    L = lambda n, p, t=None, **k: (lambda ind: field(n, p, ind, title=t, **k))
    F = lambda n, p, t=None, **k: (lambda ind: field(n, p, ind, title=t, kind='InputField', **k))

    head = lambda ind: usual_group('ГруппаШапка', [
        lambda i: field('РежимОчереди', 'РежимОчереди', i, title=TT('Показывать'), radio=True, title_loc='Left',
                        hs=[('OnChange', 'РежимОчередиПриИзменении')],
                        choice_list=[(('Производство', 'Production', 'Production', 'Producción'), 0),
                                     (('Все заказы', 'Toutes les commandes', 'All orders', 'Todos los pedidos'), 1)])
    ], ind)

    orders_cols = [
        L('ЗаказыНомер', 'Заказы.Номер', TT('Номер')),
        L('ЗаказыДата', 'Заказы.Дата', TT('Дата')),
        L('ЗаказыКонтрагент', 'Заказы.Контрагент', TT('Клиент')),
        L('ЗаказыСтатус', 'Заказы.Статус', TT('Стадия')),
        L('ЗаказыИндикатор', 'Заказы.Индикатор', TT('Индикатор')),
        L('ЗаказыПроцентОбеспечения', 'Заказы.ПроцентОбеспечения', TT('Обеспечение, %')),
        L('ЗаказыПроцентПоступления', 'Заказы.ПроцентПоступления', TT('Поступление, %')),
        L('ЗаказыПроцентВыпуска', 'Заказы.ПроцентВыпуска', TT('Выпуск, %')),
        L('ЗаказыПроцентОтгрузки', 'Заказы.ПроцентОтгрузки', TT('Отгрузка, %')),
        L('ЗаказыПроцентОплаты', 'Заказы.ПроцентОплаты', TT('Оплата, %')),
        L('ЗаказыДатаОтгрузки', 'Заказы.ДатаОтгрузки', TT('Дата отгрузки')),
        L('ЗаказыСумма', 'Заказы.Сумма', TT('Сумма')),
        L('ЗаказыМенеджер', 'Заказы.Менеджер'),
        L('ЗаказыКомментарий', 'Заказы.Комментарий'),
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
        L('ПродукцияСумма', 'Продукция.Сумма', TT('Сумма')),
        L('ПродукцияДатаОтгрузки', 'Продукция.ДатаОтгрузки', TT('Дата отгрузки')),
        L('ПродукцияСтадия', 'Продукция.Стадия', TT('Стадия')),
        L('ПродукцияСтатусДокумента', 'Продукция.СтатусДокумента', TT('Статус')),
    ]
    mat_cols = [L('Материалы' + c, 'Материалы.' + c, TT(t)) for c, t in [
        ('Продукция', 'Продукция'), ('Материал', 'Материал'), ('Характеристика', 'Характеристика'),
        ('ПоСоставу', 'По составу'), ('Потребность', 'Потребность'), ('Заказано', 'Заказано'), ('Пришло', 'Пришло'),
        ('ИзОстатка', 'Из остатка'), ('Дефицит', 'Дефицит'), ('КПоступлению', 'К поступлению')]]
    doc_cols = [L('ДокументыЗаказа' + c, 'ДокументыЗаказа.' + c, TT(t)) for c, t in [
        ('Вид', 'Вид'), ('Номер', 'Номер'), ('Дата', 'Дата'), ('Контрагент', 'Контрагент'), ('Статус', 'Статус'),
        ('Через', 'Через'), ('Сумма', 'Сумма')]]

    top = lambda ind: pages('ГруппаВерх', [
        lambda i: page('СтраницаЗаказы', TT('Заказы'), [
            lambda j: table('Заказы', 'Заказы', orders_cols, j, dynamic=True, height=12,
                            hs=[('Selection', 'ЗаказыВыбор'), ('OnActivateRow', 'ЗаказыПриАктивизацииСтроки')])], i),
        lambda i: page('СтраницаПродукция', TT('Продукция'), [
            lambda j: table('Продукция', 'Продукция', prod_cols, j, height=12, change_rows=True,
                            hs=[('OnActivateRow', 'ПродукцияПриАктивизацииСтроки'),
                                ('OnStartEdit', 'ПродукцияПриНачалеРедактирования'),
                                ('BeforeAddRow', 'ПродукцияПередНачаломДобавления'),
                                ('BeforeRowChange', 'ПродукцияПередНачаломИзменения'),
                                ('BeforeDeleteRow', 'ПродукцияПередУдалением'),
                                ('OnEditEnd', 'ПродукцияПриОкончанииРедактирования')])], i),
    ], ind, hs=[('OnCurrentPageChange', 'ГруппаВерхПриСменеСтраницы')])

    bottom = lambda ind: pages('ГруппаНиз', [
        lambda i: page('СтраницаМатериалы', TT('Материалы'), [
            lambda j: table('Материалы', 'Материалы', mat_cols, j, read_only=True, height=6, multi=False,
                            stretch=False)], i),
        lambda i: page('СтраницаДокументы', TT('Документы'), [
            lambda j: table('ДокументыЗаказа', 'ДокументыЗаказа', doc_cols, j, read_only=True, height=6, multi=False,
                            stretch=False, hs=[('Selection', 'ДокументыЗаказаВыбор')])], i),
    ], ind)

    items = head(I) + top(I) + bottom(I)

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
    ]
    B = lambda n, c: (lambda ind: button('Форма' + n, 'Form.Command.' + n, ind))
    bar = '  <autoCommandBar>\n    <name>ФормаКоманднаяПанель</name>\n    <id>-1</id>\n'
    bar += popup('ПодменюСтатус', TT('Статус'), [B('СтатусВРаботу', 0), B('СтатусВЧерновик', 0), B('СтатусОтменить', 0)], '    ')
    for n in ['СоздатьЗаказПоставщику', 'СоздатьПоступление', 'СоздатьПередачу', 'СоздатьОтгрузку', 'ОткрытьПотребности',
              'Обновить']:
        bar += button('Форма' + n, 'Form.Command.' + n, '    ')
    bar += '    <horizontalAlign>Left</horizontalAlign>\n    <autoFill>true</autoFill>\n  </autoCommandBar>\n'

    form_handlers = handlers([('OnCreateAtServer', 'ПриСозданииНаСервере'),
                              ('OnLoadDataFromSettingsAtServer', 'ПриЗагрузкеДанныхИзНастроекНаСервере')], '  ')

    props = ('  <autoSaveDataInSettings>Use</autoSaveDataInSettings>\n  <saveDataInSettings>UseList</saveDataInSettings>\n'
             '  <saveWindowSettings>true</saveWindowSettings>\n  <autoTitle>true</autoTitle>\n  <autoUrl>true</autoUrl>\n'
             '  <group>Vertical</group>\n  <autoFillCheck>true</autoFillCheck>\n  <allowFormCustomize>true</allowFormCustomize>\n'
             '  <enabled>true</enabled>\n  <showTitle>auto</showTitle>\n  <showCloseButton>true</showCloseButton>\n')

    REF = lambda t: f'<types>{t}</types>'
    doc_ref_types = '\n        '.join(f'<types>DocumentRef.{d}</types>' for d in DOC_TYPES)
    attrs = attr_simple('Объект', 1, REF('DataProcessorObject.АРМПроизводство'), main=True)
    attrs += attr_simple('РежимОчереди', 2, '<types>Number</types>' + NUM(1, 0), title=TT('Показывать'), saved=True)
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
    for i, n in enumerate(['ПоказыватьСуммы', 'МожноМенятьЗаказы', 'МожноПроводитьЗаказы', 'МожноПомечатьЗаказы',
                           'МожноЗаказПоставщику', 'МожноПоступление', 'МожноПередачу', 'МожноОтгрузку',
                           'МожноНаОсновании'], 8):
        attrs += attr_simple(n, i, REF('Boolean'))

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
