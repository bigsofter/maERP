#!/usr/bin/env python3
"""Аналитика загрузки в форме АРМ «Управление станками» (docs/plans/machines-analytics.md, §2).

Дописывает в Form.form: поле «Окно не короче, ч» рядом с неделей (группа ГруппаНеделя), страницы «Загрузка» и
«Под риском» в ГруппаСтанкиНиз, реквизиты таблиц и команды. Идемпотентности нет: запускать по исходной форме.
XML собран по образцам этой же формы и формы АРМ производства (подменю, подвал таблицы).
"""
import re
import sys
from xml.sax.saxutils import escape

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
FORM = ROOT + '/src/cf/src/DataProcessors/АРМУправлениеСтанками/Forms/Форма/Form.form'
LANGS = ('ru', 'fr', 'en', 'es')
DAYS = 14

src = open(FORM, encoding='utf-8').read()
assert 'СтраницаЗагрузка' not in src, 'форма уже дополнена'
NEXT = [max(int(x) for x in re.findall(r'<id>(\d+)</id>', src))]


def nid():
    NEXT[0] += 1
    return NEXT[0]


def ml(tag, texts, ind):
    out = ''
    for lang, val in zip(LANGS, texts):
        out += f'{ind}<{tag}>\n{ind}  <key>{lang}</key>\n{ind}  <value>{escape(val)}</value>\n{ind}</{tag}>\n'
    return out


def vis(ind, visible=True):
    return (f'{ind}<visible>{"true" if visible else "false"}</visible>\n{ind}<enabled>true</enabled>\n'
            f'{ind}<userVisible>\n{ind}  <common>true</common>\n{ind}</userVisible>\n')


def tooltip(name, ind):
    return (f'{ind}<extendedTooltip>\n{ind}  <name>{name}РасширеннаяПодсказка</name>\n{ind}  <id>{nid()}</id>\n'
            f'{ind}  <type>Label</type>\n{ind}  <autoMaxWidth>true</autoMaxWidth>\n{ind}  <autoMaxHeight>true</autoMaxHeight>\n'
            f'{ind}  <extInfo xsi:type="form:LabelDecorationExtInfo">\n{ind}    <horizontalAlign>Left</horizontalAlign>\n'
            f'{ind}  </extInfo>\n{ind}</extendedTooltip>\n')


def cmenu(name, ind):
    return (f'{ind}<contextMenu>\n{ind}  <name>{name}КонтекстноеМеню</name>\n{ind}  <id>{nid()}</id>\n'
            f'{ind}  <autoFill>true</autoFill>\n{ind}</contextMenu>\n')


TITLE_FONT = ('<titleFont xsi:type="core:FontRef">\n  <font>Style.NormalTextFont</font>\n  <bold>false</bold>\n'
              '  <italic>false</italic>\n  <underline>false</underline>\n  <strikeout>false</strikeout>\n'
              '  <scale>100</scale>\n</titleFont>\n')


def title_font(ind):
    return ''.join(ind + line + '\n' for line in TITLE_FONT.strip('\n').split('\n'))


def column(table, col, title, width, tip=None, visible=True, fmt=None, ind=''):
    name = table + col
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormField">\n{i2}<name>{name}</name>\n{i2}<id>{nid()}</id>\n'
    s += ml('title', title, i2)
    if tip:
        s += ml('toolTip', tip, i2)
    s += title_font(i2)
    s += vis(i2, visible)
    s += f'{i2}<readOnly>true</readOnly>\n'
    s += f'{i2}<dataPath xsi:type="form:DataPath">\n{i2}  <segments>{table}.{col}</segments>\n{i2}</dataPath>\n'
    s += tooltip(name, i2) + cmenu(name, i2)
    s += (f'{i2}<type>LabelField</type>\n{i2}<editMode>Enter</editMode>\n{i2}<showInHeader>true</showInHeader>\n'
          f'{i2}<headerHorizontalAlign>Left</headerHorizontalAlign>\n{i2}<showInFooter>true</showInFooter>\n')
    s += f'{i2}<extInfo xsi:type="form:LabelFieldExtInfo">\n{i2}  <width>{width}</width>\n'
    s += f'{i2}  <autoMaxWidth>false</autoMaxWidth>\n{i2}  <autoMaxHeight>true</autoMaxHeight>\n'
    if fmt:
        s += ml('format', fmt, i2 + '  ')
    s += f'{i2}</extInfo>\n{ind}</items>\n'
    return s


def button(name, command, ind):
    i2 = ind + '  '
    return (f'{ind}<items xsi:type="form:Button">\n{i2}<name>{name}</name>\n{i2}<id>{nid()}</id>\n' + vis(i2)
            + tooltip(name, i2) + f'{i2}<commandName>Form.Command.{command}</commandName>\n'
            f'{i2}<representation>Auto</representation>\n{i2}<autoMaxWidth>true</autoMaxWidth>\n'
            f'{i2}<autoMaxHeight>true</autoMaxHeight>\n{i2}<placementArea>UserCmds</placementArea>\n'
            f'{i2}<representationInContextMenu>Auto</representationInContextMenu>\n'
            f'{i2}<buttonImportance>Normal</buttonImportance>\n{ind}</items>\n')


def popup(name, title, buttons, ind):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{nid()}</id>\n'
    for bname, cmd in buttons:
        s += button(bname, cmd, i2)
    s += vis(i2) + ml('title', title, i2) + tooltip(name, i2)
    s += (f'{i2}<type>Popup</type>\n{i2}<extInfo xsi:type="form:PopupGroupExtInfo">\n'
          f'{i2}  <representation>Auto</representation>\n{i2}  <importance>Normal</importance>\n{i2}</extInfo>\n'
          f'{ind}</items>\n')
    return s


def table(name, columns, commands, handler, ind, footer=False):
    i2 = ind + '  '
    s = f'{ind}<items xsi:type="form:Table">\n{i2}<name>{name}</name>\n{i2}<id>{nid()}</id>\n' + vis(i2)
    s += f'{i2}<readOnly>true</readOnly>\n'
    s += f'{i2}<dataPath xsi:type="form:DataPath">\n{i2}  <segments>{name}</segments>\n{i2}</dataPath>\n'
    s += f'{i2}<titleLocation>None</titleLocation>\n' + tooltip(name, i2) + cmenu(name, i2)
    s += f'{i2}<autoCommandBar>\n{i2}  <name>{name}КоманднаяПанель</name>\n{i2}  <id>{nid()}</id>\n'
    s += commands(i2 + '  ')
    s += f'{i2}  <horizontalAlign>Left</horizontalAlign>\n{i2}  <autoFill>false</autoFill>\n{i2}</autoCommandBar>\n'
    s += f'{i2}<handlers>\n{i2}  <event>Selection</event>\n{i2}  <name>{handler}</name>\n{i2}</handlers>\n'
    for col in columns:
        s += column(name, *col, ind=i2) if not isinstance(col, str) else col
    s += (f'{i2}<changeRowSet>false</changeRowSet>\n{i2}<changeRowOrder>false</changeRowOrder>\n'
          f'{i2}<autoMaxWidth>true</autoMaxWidth>\n{i2}<autoMaxHeight>true</autoMaxHeight>\n'
          f'{i2}<heightInTableRows>4</heightInTableRows>\n{i2}<autoMaxRowsCount>true</autoMaxRowsCount>\n'
          f'{i2}<selectionMode>SingleRow</selectionMode>\n{i2}<header>true</header>\n{i2}<headerHeight>1</headerHeight>\n')
    if footer:
        s += f'{i2}<footer>true</footer>\n'
    s += (f'{i2}<footerHeight>1</footerHeight>\n{i2}<horizontalScrollBar>AutoUse</horizontalScrollBar>\n'
          f'{i2}<verticalScrollBar>AutoUse</verticalScrollBar>\n{i2}<horizontalLines>true</horizontalLines>\n'
          f'{i2}<verticalLines>true</verticalLines>\n{i2}<searchOnInput>Auto</searchOnInput>\n'
          f'{i2}<initialListView>Auto</initialListView>\n{i2}<horizontalStretch>true</horizontalStretch>\n'
          f'{i2}<verticalStretch>true</verticalStretch>\n{i2}<borderColor xsi:type="core:ColorRef">\n'
          f'{i2}  <color>Style.FormBackColor</color>\n{i2}</borderColor>\n{i2}<autoMaxCardHeight>true</autoMaxCardHeight>\n'
          f'{ind}</items>\n')
    return s


def page(name, title, body, ind):
    i2 = ind + '  '
    return (f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{nid()}</id>\n'
            + ml('title', title, i2) + vis(i2) + tooltip(name, i2) + body
            + f'{i2}<type>Page</type>\n{i2}<extInfo xsi:type="form:PageGroupExtInfo">\n{i2}  <group>Vertical</group>\n'
            f'{i2}  <showTitle>true</showTitle>\n{i2}</extInfo>\n{ind}</items>\n')


def hgroup(name, body, ind, group='AlwaysHorizontal'):
    i2 = ind + '  '
    return (f'{ind}<items xsi:type="form:FormGroup">\n{i2}<name>{name}</name>\n{i2}<id>{nid()}</id>\n' + vis(i2)
            + tooltip(name, i2) + body + f'{i2}<type>UsualGroup</type>\n{i2}<extInfo xsi:type="form:UsualGroupExtInfo">\n'
            f'{i2}  <group>{group}</group>\n{i2}  <representation>None</representation>\n'
            f'{i2}  <showLeftMargin>false</showLeftMargin>\n{i2}  <united>true</united>\n{i2}  <showTitle>false</showTitle>\n'
            f'{i2}  <throughAlign>Auto</throughAlign>\n{i2}  <currentRowUse>Auto</currentRowUse>\n{i2}</extInfo>\n'
            f'{ind}</items>\n')


def reindent(block, extra):
    return ''.join(extra + line if line else line for line in block.splitlines(True))


# --- Поле «Окно не короче, ч» и группа недели -------------------------------------------------------------------
m = re.search(r'  <items xsi:type="form:FormField">\n    <name>НеделяСтанков</name>.*?\n  </items>\n', src, re.S)
week = m.group(0)
i4 = '      '
window = (f'    <items xsi:type="form:FormField">\n{i4}<name>ЧасовОкна</name>\n{i4}<id>{nid()}</id>\n'
          + ml('title', ('Окно не короче, ч', 'Créneau d\'au moins, h', 'Slot of at least, h', 'Hueco de al menos, h'), i4)
          + ml('toolTip', ('Длина свободного окна, которое ищется у каждого станка на закладке «Загрузка»',
                           'Durée du créneau libre recherché pour chaque machine dans l\'onglet « Charge »',
                           'Length of the free slot searched for each machine on the "Load" tab',
                           'Duración del hueco libre que se busca en cada máquina en la pestaña «Carga»'), i4)
          + vis(i4) + f'{i4}<dataPath xsi:type="form:DataPath">\n{i4}  <segments>ЧасовОкна</segments>\n{i4}</dataPath>\n'
          + f'{i4}<titleLocation>Left</titleLocation>\n' + tooltip('ЧасовОкна', i4) + cmenu('ЧасовОкна', i4)
          + f'{i4}<type>InputField</type>\n{i4}<editMode>Enter</editMode>\n{i4}<showInHeader>true</showInHeader>\n'
          f'{i4}<headerHorizontalAlign>Left</headerHorizontalAlign>\n{i4}<showInFooter>true</showInFooter>\n'
          f'{i4}<extInfo xsi:type="form:InputFieldExtInfo">\n{i4}  <width>5</width>\n{i4}  <autoMaxWidth>false</autoMaxWidth>\n'
          f'{i4}  <autoMaxHeight>true</autoMaxHeight>\n{i4}  <horizontalStretch>false</horizontalStretch>\n'
          f'{i4}  <wrap>true</wrap>\n{i4}  <handlers>\n{i4}    <event>OnChange</event>\n'
          f'{i4}    <name>ЧасовОкнаПриИзменении</name>\n{i4}  </handlers>\n{i4}  <chooseType>true</chooseType>\n'
          f'{i4}  <typeDomainEnabled>true</typeDomainEnabled>\n{i4}  <textEdit>true</textEdit>\n'
          f'{i4}  <minValue xsi:type="core:NumberValue">\n{i4}    <value>0.25</value>\n{i4}  </minValue>\n'
          f'{i4}  <textSize>Normal</textSize>\n{i4}</extInfo>\n    </items>\n')
src = src.replace(week, hgroup('ГруппаНеделя', reindent(week, '  ') + window, '  ', 'HorizontalIfPossible'), 1)

# --- Страница «Загрузка» -------------------------------------------------------------------------------------------
DAY_TIP = ('Занято, % рабочего времени дня', 'Occupé, % du temps de travail du jour', 'Busy, % of the day\'s working time',
           'Ocupado, % del tiempo de trabajo del día')
HOURS_FMT = ('ЧДЦ=2; ЧН=', 'NFD=2; NZ=', 'NFD=2; NZ=', 'NFD=2; NZ=')
EMPTY_ZERO = ('ЧН=', 'NZ=', 'NZ=', 'NZ=')
load_cols = [
    ('Станок', ('Станок', 'Machine', 'Machine', 'Máquina'), 14),
    ('Фонд', ('Фонд, ч', 'Capacité, h', 'Capacity, h', 'Capacidad, h'), 6, None, True, HOURS_FMT),
    ('Занято', ('Занято, ч', 'Occupé, h', 'Busy, h', 'Ocupado, h'), 6, None, True, HOURS_FMT),
    ('Обслуживание', ('ТО, ч', 'Maint., h', 'Maint., h', 'Mant., h'), 5, None, True, HOURS_FMT),
    ('Свободно', ('Свободно, ч', 'Libre, h', 'Free, h', 'Libre, h'), 6,
     ('Свободные рабочие часы от текущего момента', 'Heures de travail libres à partir de maintenant',
      'Free working hours from now', 'Horas de trabajo libres desde ahora'), True, HOURS_FMT),
    ('Процент', ('Занято, %', 'Occupé, %', 'Busy, %', 'Ocupado, %'), 5,
     ('Работа и обслуживание / фонд двух недель', 'Travail et maintenance / capacité de deux semaines',
      'Work and maintenance / two-week capacity', 'Trabajo y mantenimiento / capacidad de dos semanas')),
    ('ОкноС', ('Окно с', 'Créneau dès', 'Slot from', 'Hueco desde'), 9,
     ('Начало первого свободного окна заданной длины; пусто - окна нет в двух неделях',
      'Début du premier créneau libre de la durée choisie ; vide - aucun créneau sur deux semaines',
      'Start of the first free slot of the chosen length; empty - no slot within two weeks',
      'Inicio del primer hueco libre de la duración elegida; vacío - no hay hueco en dos semanas'), True,
     ('ДФ=\'dd.MM HH:mm\'', 'DF=\'dd.MM HH:mm\'', 'DF=\'dd.MM HH:mm\'', 'DF=\'dd.MM HH:mm\'')),
]
for n in range(1, DAYS + 1):
    load_cols.append((f'День{n}', (f'Д{n}',) * 4, 4, DAY_TIP, True, EMPTY_ZERO))
for n in range(1, DAYS + 1):
    load_cols.append((f'Выходной{n}', (f'Выходной {n}', f'Repos {n}', f'Day off {n}', f'Descanso {n}'), 3, None, False))
    load_cols.append((f'Свободно{n}', (f'Свободно {n}', f'Libre {n}', f'Free {n}', f'Libre {n}'), 3, None, False))


def load_commands(ind):
    return (button('КнопкаЗагрузкаОбновить', 'СтанкиОбновить', ind)
            + popup('ЗагрузкаПодменюОтчеты', ('Отчёты', 'Rapports', 'Reports', 'Informes'),
                    [('КнопкаОтчетПланПоДням', 'ОтчетПланПоДням'), ('КнопкаОтчетЗагрузкаСтанков', 'ОтчетЗагрузкаСтанков'),
                     ('КнопкаОтчетПростоиСтанков', 'ОтчетПростоиСтанков'),
                     ('КнопкаОтчетЗанятостьСтанков', 'ОтчетЗанятостьСтанков')], ind))


def risk_commands(ind):
    return (button('КнопкаРискиПересчитать', 'СтанкиПересчитатьРиски', ind)
            + button('КнопкаОтчетЗаказыПодРиском', 'ОтчетЗаказыПодРиском', ind))


def no_commands(ind):
    return ''


P = '    '
load_page = page('СтраницаЗагрузка', ('Загрузка', 'Charge', 'Load', 'Carga'),
                 table('ЗагрузкаПоДням', load_cols, load_commands, 'ЗагрузкаПоДнямВыбор', P + '  ', footer=True), P)
risk_cols = [
    ('Источник', ('Источник', 'Source', 'Source', 'Origen'), 18, (
        'Почему заказ опаздывает к дате отгрузки: запланированная работа, незапущенная работа или черновик автоплана. '
        'Черновик - оценка: другое размещение может успеть',
        'Pourquoi la commande est en retard : travail planifié, travail non lancé ou brouillon de planification. '
        'Le brouillon est une estimation : un autre placement peut tenir le délai',
        'Why the order is late: scheduled work, work not started or the auto-plan draft. '
        'The draft is an estimate: another placement may be in time',
        'Por qué el pedido se retrasa: trabajo planificado, no iniciado o borrador de planificación. '
        'El borrador es una estimación: otra ubicación puede llegar a tiempo')),
    ('НомерЗаказа', ('Заказ', 'Commande', 'Order', 'Pedido'), 8),
    ('Клиент', ('Клиент', 'Client', 'Customer', 'Cliente'), 14),
    ('ДатаОтгрузки', ('Отгрузка', 'Expédition', 'Shipment', 'Envío'), 9),
    ('Номенклатура', ('Продукция', 'Produit', 'Product', 'Producto'), 16),
    ('Количество', ('Кол-во', 'Qté', 'Qty', 'Cant.'), 6),
    ('Станок', ('Станок', 'Machine', 'Machine', 'Máquina'), 12),
    ('Окончание', ('Окончание', 'Fin', 'End', 'Fin'), 11, None, True,
     ('ДФ=\'dd.MM.yy HH:mm\'', 'DF=\'dd.MM.yy HH:mm\'', 'DF=\'dd.MM.yy HH:mm\'', 'DF=\'dd.MM.yy HH:mm\'')),
    ('ОпозданиеДней', ('Опоздание, дн', 'Retard, j', 'Delay, days', 'Retraso, días'), 6, None, True, EMPTY_ZERO),
    ('ТекстОшибки', ('Причина', 'Motif', 'Reason', 'Motivo'), 30),
]
deficit_cols = [
    ('ДатаОтгрузки', ('Отгрузка до', 'Expédition au', 'Ship by', 'Envío hasta'), 9),
    ('Потребность', ('Нужно, ч', 'Besoin, h', 'Needed, h', 'Necesario, h'), 6, None, True, HOURS_FMT),
    ('Мощность', ('Свободно, ч', 'Libre, h', 'Free, h', 'Libre, h'), 6, None, True, HOURS_FMT),
    ('Дефицит', ('Дефицит, ч', 'Déficit, h', 'Shortfall, h', 'Déficit, h'), 6, None, True, HOURS_FMT),
]
risk_body = hgroup('ГруппаРиски',
                   table('РискиСрыва', risk_cols, risk_commands, 'РискиСрываВыбор', P + '    ')
                   + table('ДефицитМощности', deficit_cols, no_commands, 'ДефицитМощностиВыбор', P + '    '),
                   P + '  ', 'AutoScreenTypeSensitive')
risk_page = page('СтраницаРиски', ('Под риском', 'À risque', 'At risk', 'En riesgo'), risk_body, P)
anchor = '\n    <type>Pages</type>\n'
assert src.count(anchor) == 1
src = src.replace(anchor, '\n' + load_page + risk_page + '    <type>Pages</type>\n', 1)
# Обработчик смены страницы
grp = '''    <name>ГруппаСтанкиНиз</name>
    <id>745</id>
    <visible>true</visible>
    <enabled>true</enabled>
    <userVisible>
      <common>true</common>
    </userVisible>
'''
assert src.count(grp) == 1
src = src.replace(grp, grp + '''    <handlers>
      <event>OnCurrentPageChange</event>
      <name>ГруппаСтанкиНизПриСменеСтраницы</name>
    </handlers>
''', 1)

# --- Реквизиты -----------------------------------------------------------------------------------------------------


def vtype(kind):
    if kind == 'hours':
        return '<types>Number</types>\n<numberQualifiers>\n  <precision>10</precision>\n  <scale>2</scale>\n</numberQualifiers>'
    if kind == 'pct':
        return '<types>Number</types>\n<numberQualifiers>\n  <precision>5</precision>\n</numberQualifiers>'
    if kind == 'qty':
        return '<types>Number</types>\n<numberQualifiers>\n  <precision>15</precision>\n  <scale>3</scale>\n</numberQualifiers>'
    if kind == 'bool':
        return '<types>Boolean</types>'
    if kind == 'date':
        return '<types>Date</types>\n<dateQualifiers>\n  <dateFractions>Date</dateFractions>\n</dateQualifiers>'
    if kind == 'datetime':
        return '<types>Date</types>\n<dateQualifiers>\n  <dateFractions>DateTime</dateFractions>\n</dateQualifiers>'
    if kind == 'str':
        return '<types>String</types>'
    if kind == 'str20':
        return '<types>String</types>\n<stringQualifiers>\n  <length>20</length>\n</stringQualifiers>'
    return f'<types>{kind}</types>'


def indent(text, ind):
    return ''.join(ind + line + '\n' for line in text.split('\n'))


def attribute(name, kind, columns=(), title=None):
    s = f'  <attributes>\n    <name>{name}</name>\n'
    if title:
        s += ml('title', title, '    ')
    s += f'    <id>{nid()}</id>\n    <valueType>\n' + indent(vtype(kind), '      ') + '    </valueType>\n'
    s += '    <view>\n      <common>true</common>\n    </view>\n    <edit>\n      <common>true</common>\n    </edit>\n'
    for n, (col, ckind) in enumerate(columns, start=1):
        s += (f'    <columns>\n      <name>{col}</name>\n      <id>{n}</id>\n      <valueType>\n'
              + indent(vtype(ckind), '        ') + '      </valueType>\n      <view>\n        <common>true</common>\n'
              '      </view>\n      <edit>\n        <common>true</common>\n      </edit>\n    </columns>\n')
    if name == 'ЧасовОкна':
        s += '    <savedData>true</savedData>\n'
    s += '  </attributes>\n'
    return s


MACHINE = 'CatalogRef.ПроизводственноеОборудование'
load_attr = [('Станок', MACHINE), ('Выведен', 'bool'), ('Фонд', 'hours'), ('Занято', 'hours'), ('Обслуживание', 'hours'),
             ('Свободно', 'hours'), ('Процент', 'pct'), ('ОкноС', 'datetime'), ('УзкоеМесто', 'bool')]
load_attr += [(f'День{n}', 'pct') for n in range(1, DAYS + 1)]
load_attr += [(f'Выходной{n}', 'bool') for n in range(1, DAYS + 1)]
load_attr += [(f'Свободно{n}', 'hours') for n in range(1, DAYS + 1)]
risk_attr = [('Источник', 'str'), ('Заказ', 'DocumentRef.ЗаказПокупателя'), ('НомерЗаказа', 'str20'),
             ('Клиент', 'CatalogRef.Контрагенты'), ('ДатаОтгрузки', 'date'), ('Номенклатура', 'CatalogRef.Номенклатура'),
             ('Количество', 'qty'), ('Станок', MACHINE), ('Окончание', 'datetime'), ('ОпозданиеДней', 'pct'),
             ('ТекстОшибки', 'str'), ('Документ', 'DocumentRef.ТребованиеНакладная'), ('НеЗапущено', 'bool')]
deficit_attr = [('ДатаОтгрузки', 'date'), ('Потребность', 'hours'), ('Мощность', 'hours'), ('Дефицит', 'hours')]
attrs = (attribute('ЧасовОкна', 'Number', title=('Окно не короче, ч', 'Créneau d\'au moins, h', 'Slot of at least, h',
                                                  'Hueco de al menos, h'))
         + attribute('ЗагрузкаПоДням', 'ValueTable', load_attr)
         + attribute('РискиСрыва', 'ValueTable', risk_attr)
         + attribute('ДефицитМощности', 'ValueTable', deficit_attr)
         + attribute('РискиРассчитаны', 'bool'))
attrs = attrs.replace('      <types>Number</types>\n    </valueType>\n',
                      '      <types>Number</types>\n      <numberQualifiers>\n        <precision>5</precision>\n'
                      '        <scale>2</scale>\n        <nonNegative>true</nonNegative>\n      </numberQualifiers>\n'
                      '    </valueType>\n', 1)
last_attr = src.rindex('  </attributes>\n') + len('  </attributes>\n')
src = src[:last_attr] + attrs + src[last_attr:]

# --- Команды -------------------------------------------------------------------------------------------------------


def command(name, title, tip):
    return (f'  <formCommands>\n    <name>{name}</name>\n' + ml('title', title, '    ') + f'    <id>{nid()}</id>\n'
            + ml('toolTip', tip, '    ') + '    <use>\n      <common>true</common>\n    </use>\n'
            f'    <action xsi:type="form:FormCommandHandlerContainer">\n      <handler>\n        <name>{name}</name>\n'
            '      </handler>\n    </action>\n    <currentRowUse>Auto</currentRowUse>\n  </formCommands>\n')


cmds = (command('СтанкиПересчитатьРиски', ('Пересчитать', 'Recalculer', 'Recalculate', 'Recalcular'),
                ('Пересчитать заказы под риском и дефицит мощности от текущего момента',
                 'Recalculer les commandes à risque et le déficit de capacité à partir de maintenant',
                 'Recalculate orders at risk and the capacity shortfall from now',
                 'Recalcular los pedidos en riesgo y el déficit de capacidad desde ahora'))
        + command('ОтчетПланПоДням', ('План загрузки по дням', 'Plan de charge par jour', 'Load plan by day',
                                     'Plan de carga por días'),
                  ('План загрузки станков по дням за две недели закладки', 'Plan de charge des machines par jour sur les deux semaines',
                   'Machine load plan by day for the two weeks of the tab', 'Plan de carga por días de las dos semanas'))
        + command('ОтчетЗагрузкаСтанков', ('Загрузка станков', 'Charge des machines', 'Machine load', 'Carga de máquinas'),
                  ('Отчёт «Загрузка станков» за две недели закладки', 'Rapport « Charge des machines » sur les deux semaines',
                   'The "Machine load" report for the two weeks of the tab', 'Informe «Carga de máquinas» de las dos semanas'))
        + command('ОтчетПростоиСтанков', ('Простои станков (с планом ТО)', 'Arrêts des machines (avec maintenance prévue)',
                                         'Machine downtime (with planned maintenance)', 'Paradas de máquinas (con mantenimiento previsto)'),
                  ('Отчёт «Простои станков» за две недели закладки с плановым обслуживанием',
                   'Rapport « Arrêts des machines » sur les deux semaines, maintenance prévue comprise',
                   'The "Machine downtime" report for the two weeks of the tab, planned maintenance included',
                   'Informe «Paradas de máquinas» de las dos semanas, con mantenimiento previsto'))
        + command('ОтчетЗанятостьСтанков', ('Занятость станков', 'Occupation des machines', 'Machine occupancy',
                                           'Ocupación de máquinas'),
                  ('Отчёт «Занятость станков» на текущий момент', 'Rapport « Occupation des machines » à cet instant',
                   'The "Machine occupancy" report at the current moment', 'Informe «Ocupación de máquinas» en este momento'))
        + command('ОтчетЗаказыПодРиском', ('Отчёт', 'Rapport', 'Report', 'Informe'),
                  ('Отчёт «План загрузки станков», вариант «Заказы под риском»',
                   'Rapport « Plan de charge des machines », variante « Commandes à risque »',
                   'The "Machine load plan" report, "Orders at risk" variant',
                   'Informe «Plan de carga de máquinas», variante «Pedidos en riesgo»')))
last = src.rindex('  </formCommands>\n') + len('  </formCommands>\n')
src = src[:last] + cmds + src[last:]

open(FORM, 'w', encoding='utf-8').write(src)
print('Form.form дополнена, последний id', NEXT[0])
