#!/usr/bin/env python3
"""Отчёт «План загрузки станков» (docs/plans/machines-analytics.md, §3): .mdo, схема с двумя внешними наборами
(«Дни», «Риски») и вариантами «По дням» и «Заказы под риском», модули. Образцы - отчёты ЗанятостьСтанков и
ПростоиСтанков. Запускать один раз: существующие файлы перезаписываются.
"""
import os
import sys
import uuid
from xml.sax.saxutils import escape

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
NAME = 'ПланЗагрузкиСтанков'
DIR = f'{ROOT}/src/cf/src/Reports/{NAME}'
LANGS = ('ru', 'fr', 'en', 'es')
CFG = 'xmlns:d5p1="http://v8.1c.ru/8.1/data/enterprise/current-config"'


def u():
    return str(uuid.uuid4())


def ls(texts, ind, tag='title', xsi=True):
    head = f'{ind}<{tag} xsi:type="v8:LocalStringType">\n' if xsi else f'{ind}<{tag}>\n'
    body = ''.join(f'{ind}\t<v8:item>\n{ind}\t\t<v8:lang>{lang}</v8:lang>\n{ind}\t\t<v8:content>{escape(t)}</v8:content>\n'
                   f'{ind}\t</v8:item>\n' for lang, t in zip(LANGS, texts))
    return head + body + f'{ind}</{tag}>\n'


def vtype(kind):
    if kind == 'num':
        return '\t\t\t\t<v8:Type>xs:decimal</v8:Type>\n\t\t\t\t<v8:NumberQualifiers>\n\t\t\t\t\t<v8:Digits>15</v8:Digits>\n' \
               '\t\t\t\t\t<v8:FractionDigits>2</v8:FractionDigits>\n\t\t\t\t\t<v8:AllowedSign>Any</v8:AllowedSign>\n' \
               '\t\t\t\t</v8:NumberQualifiers>\n'
    if kind == 'int':
        return '\t\t\t\t<v8:Type>xs:decimal</v8:Type>\n\t\t\t\t<v8:NumberQualifiers>\n\t\t\t\t\t<v8:Digits>10</v8:Digits>\n' \
               '\t\t\t\t\t<v8:FractionDigits>0</v8:FractionDigits>\n\t\t\t\t\t<v8:AllowedSign>Any</v8:AllowedSign>\n' \
               '\t\t\t\t</v8:NumberQualifiers>\n'
    if kind == 'str':
        return '\t\t\t\t<v8:Type>xs:string</v8:Type>\n\t\t\t\t<v8:StringQualifiers>\n\t\t\t\t\t<v8:Length>0</v8:Length>\n' \
               '\t\t\t\t\t<v8:AllowedLength>Variable</v8:AllowedLength>\n\t\t\t\t</v8:StringQualifiers>\n'
    if kind == 'date':
        return '\t\t\t\t<v8:Type>xs:dateTime</v8:Type>\n\t\t\t\t<v8:DateQualifiers>\n' \
               '\t\t\t\t\t<v8:DateFractions>Date</v8:DateFractions>\n\t\t\t\t</v8:DateQualifiers>\n'
    if kind == 'datetime':
        return '\t\t\t\t<v8:Type>xs:dateTime</v8:Type>\n\t\t\t\t<v8:DateQualifiers>\n' \
               '\t\t\t\t\t<v8:DateFractions>DateTime</v8:DateFractions>\n\t\t\t\t</v8:DateQualifiers>\n'
    return f'\t\t\t\t<v8:Type {CFG}>d5p1:{kind}</v8:Type>\n'


def field(path, title, kind, dimension=False, fmt=None, column=None):
    # Поле с тем же путём в двух несвязанных наборах компоновка не допускает: путь задаётся отдельно от колонки.
    s = f'\t\t<field xsi:type="DataSetFieldField">\n\t\t\t<dataPath>{path}</dataPath>\n\t\t\t<field>{column or path}</field>\n'
    s += ls(title, '\t\t\t')
    if dimension:
        s += '\t\t\t<role>\n\t\t\t\t<dcscom:dimension>true</dcscom:dimension>\n\t\t\t</role>\n'
    s += '\t\t\t<valueType>\n' + vtype(kind) + '\t\t\t</valueType>\n'
    if fmt:
        s += ('\t\t\t<appearance>\n\t\t\t\t<dcscor:item xsi:type="dcsset:SettingsParameterValue">\n'
              '\t\t\t\t\t<dcscor:parameter>Format</dcscor:parameter>\n'
              f'\t\t\t\t\t<dcscor:value xsi:type="xs:string">{escape(fmt)}</dcscor:value>\n'
              '\t\t\t\t</dcscor:item>\n\t\t\t</appearance>\n')
    s += '\t\t</field>\n'
    return s


MACHINE = ('Станок', 'Machine', 'Machine', 'Máquina')
days = [
    field('Станок', MACHINE, 'CatalogRef.ПроизводственноеОборудование', True),
    field('День', ('День', 'Jour', 'Day', 'Día'), 'date', True, "ДФ='ddd dd.MM'"),
    field('Фонд', ('Фонд, ч', 'Capacité, h', 'Capacity, h', 'Capacidad, h'), 'num'),
    field('Занято', ('Занято, ч', 'Occupé, h', 'Busy, h', 'Ocupado, h'), 'num'),
    field('Свободно', ('Свободно, ч', 'Libre, h', 'Free, h', 'Libre, h'), 'num'),
    field('Процент', ('Занято, %', 'Occupé, %', 'Busy, %', 'Ocupado, %'), 'int'),
]
risks = [
    field('Источник', ('Источник', 'Source', 'Source', 'Origen'), 'str', True),
    field('Заказ', ('Заказ', 'Commande', 'Order', 'Pedido'), 'DocumentRef.ЗаказПокупателя', True),
    field('Клиент', ('Клиент', 'Client', 'Customer', 'Cliente'), 'CatalogRef.Контрагенты', True),
    field('ДатаОтгрузки', ('Отгрузка', 'Expédition', 'Shipment', 'Envío'), 'date', True),
    field('Номенклатура', ('Продукция', 'Produit', 'Product', 'Producto'), 'CatalogRef.Номенклатура', True),
    field('Количество', ('Количество', 'Quantité', 'Quantity', 'Cantidad'), 'num'),
    field('СтанокЗаказа', MACHINE, 'CatalogRef.ПроизводственноеОборудование', True, column='Станок'),
    field('Окончание', ('Окончание', 'Fin', 'End', 'Fin'), 'datetime'),
    field('Часы', ('Часы', 'Heures', 'Hours', 'Horas'), 'num'),
    field('ОпозданиеДней', ('Опоздание, дн', 'Retard, j', 'Delay, days', 'Retraso, días'), 'int'),
    field('ТекстОшибки', ('Причина', 'Motif', 'Reason', 'Motivo'), 'str'),
    field('Документ', ('Требование', 'Bon de consommation', 'Requisition', 'Requisición'),
          'DocumentRef.ТребованиеНакладная', True),
]


def dataset(name, fields):
    return (f'\t<dataSet xsi:type="DataSetObject">\n\t\t<name>{name}</name>\n' + ''.join(fields)
            + f'\t\t<dataSource>ИсточникДанных1</dataSource>\n\t\t<objectName>{name}</objectName>\n\t</dataSet>\n')


def total(path, expr, groups=()):
    return (f'\t<totalField>\n\t\t<dataPath>{path}</dataPath>\n\t\t<expression>{escape(expr)}</expression>\n'
            + ''.join(f'\t\t<group>{g}</group>\n' for g in groups) + '\t</totalField>\n')


def param(name, title, kind_xml, value_xml, use_restriction='false'):
    return (f'\t<parameter>\n\t\t<name>{name}</name>\n' + ls(title, '\t\t') + f'\t\t<valueType>\n{kind_xml}\t\t</valueType>\n'
            f'{value_xml}\t\t<useRestriction>{use_restriction}</useRestriction>\n\t</parameter>\n')


PERIOD_T = '\t\t\t<v8:Type>v8:StandardPeriod</v8:Type>\n'
PERIOD_V = ('\t\t<value xsi:type="v8:StandardPeriod">\n\t\t\t<v8:variant xsi:type="v8:StandardPeriodVariant">Custom</v8:variant>\n'
            '\t\t\t<v8:startDate>0001-01-01T00:00:00</v8:startDate>\n\t\t\t<v8:endDate>0001-01-01T00:00:00</v8:endDate>\n'
            '\t\t</value>\n')
DATE_T = ('\t\t\t<v8:Type>xs:dateTime</v8:Type>\n\t\t\t<v8:DateQualifiers>\n\t\t\t\t<v8:DateFractions>DateTime</v8:DateFractions>\n'
          '\t\t\t</v8:DateQualifiers>\n')
DATE_V = '\t\t<value xsi:type="xs:dateTime">0001-01-01T00:00:00</value>\n'
STR_T = ('\t\t\t<v8:Type>xs:string</v8:Type>\n\t\t\t<v8:StringQualifiers>\n\t\t\t\t<v8:Length>20</v8:Length>\n'
         '\t\t\t\t<v8:AllowedLength>Variable</v8:AllowedLength>\n\t\t\t</v8:StringQualifiers>\n')


def group_item(path, ind):
    return (f'{ind}<dcsset:item xsi:type="dcsset:GroupItemField">\n{ind}\t<dcsset:field>{path}</dcsset:field>\n'
            f'{ind}\t<dcsset:groupType>Items</dcsset:groupType>\n{ind}\t<dcsset:periodAdditionType>None</dcsset:periodAdditionType>\n'
            f'{ind}\t<dcsset:periodAdditionBegin xsi:type="xs:dateTime">0001-01-01T00:00:00</dcsset:periodAdditionBegin>\n'
            f'{ind}\t<dcsset:periodAdditionEnd xsi:type="xs:dateTime">0001-01-01T00:00:00</dcsset:periodAdditionEnd>\n'
            f'{ind}</dcsset:item>\n')


def auto(ind):
    return (f'{ind}<dcsset:order>\n{ind}\t<dcsset:item xsi:type="dcsset:OrderItemAuto"/>\n{ind}</dcsset:order>\n'
            f'{ind}<dcsset:selection>\n{ind}\t<dcsset:item xsi:type="dcsset:SelectedItemAuto"/>\n{ind}</dcsset:selection>\n')


def selection(fields, ind):
    return (f'{ind}<dcsset:selection>\n' + ''.join(
        f'{ind}\t<dcsset:item xsi:type="dcsset:SelectedItemField">\n{ind}\t\t<dcsset:field>{f}</dcsset:field>\n'
        f'{ind}\t</dcsset:item>\n' for f in fields) + f'{ind}\t<dcsset:userSettingID>{u()}</dcsset:userSettingID>\n'
            f'{ind}</dcsset:selection>\n')


def data_params(items, ind):
    s = f'{ind}<dcsset:dataParameters>\n'
    for name, value, user in items:
        s += (f'{ind}\t<dcscor:item xsi:type="dcsset:SettingsParameterValue">\n{ind}\t\t<dcscor:parameter>{name}</dcscor:parameter>\n'
              f'{value.replace("@", ind + chr(9) + chr(9))}')
        if user:
            s += f'{ind}\t\t<dcsset:userSettingID>{u()}</dcsset:userSettingID>\n'
        s += f'{ind}\t</dcscor:item>\n'
    return s + f'{ind}</dcsset:dataParameters>\n'


def output(title, ind):
    return (f'{ind}<dcsset:outputParameters>\n{ind}\t<dcscor:item xsi:type="dcsset:SettingsParameterValue">\n'
            f'{ind}\t\t<dcscor:parameter>AppearanceTemplate</dcscor:parameter>\n'
            f'{ind}\t\t<dcscor:value xsi:type="xs:string">Арктика</dcscor:value>\n{ind}\t</dcscor:item>\n'
            f'{ind}\t<dcscor:item xsi:type="dcsset:SettingsParameterValue">\n{ind}\t\t<dcscor:parameter>TitleOutput</dcscor:parameter>\n'
            f'{ind}\t\t<dcscor:value xsi:type="dcsset:DataCompositionTextOutputType">Output</dcscor:value>\n{ind}\t</dcscor:item>\n'
            f'{ind}\t<dcscor:item xsi:type="dcsset:SettingsParameterValue">\n{ind}\t\t<dcscor:parameter>Title</dcscor:parameter>\n'
            + ls(title, ind + '\t\t', 'dcscor:value') + f'{ind}\t</dcscor:item>\n{ind}</dcsset:outputParameters>\n')


def color_rule(path, comparisons, color, ind):
    s = (f'{ind}<dcsset:item>\n{ind}\t<dcsset:selection>\n{ind}\t\t<dcsset:item>\n{ind}\t\t\t<dcsset:field>{path}</dcsset:field>\n'
         f'{ind}\t\t</dcsset:item>\n{ind}\t</dcsset:selection>\n{ind}\t<dcsset:filter>\n')
    for comp, value in comparisons:
        s += (f'{ind}\t\t<dcsset:item xsi:type="dcsset:FilterItemComparison">\n'
              f'{ind}\t\t\t<dcsset:left xsi:type="dcscor:Field">{path}</dcsset:left>\n'
              f'{ind}\t\t\t<dcsset:comparisonType>{comp}</dcsset:comparisonType>\n'
              f'{ind}\t\t\t<dcsset:right xsi:type="xs:decimal">{value}</dcsset:right>\n{ind}\t\t</dcsset:item>\n')
    s += (f'{ind}\t</dcsset:filter>\n{ind}\t<dcsset:appearance>\n{ind}\t\t<dcscor:item xsi:type="dcsset:SettingsParameterValue">\n'
          f'{ind}\t\t\t<dcscor:parameter>BackColor</dcscor:parameter>\n'
          f'{ind}\t\t\t<dcscor:value xsi:type="v8ui:Color">{color}</dcscor:value>\n'
          f'{ind}\t\t</dcscor:item>\n{ind}\t</dcsset:appearance>\n{ind}</dcsset:item>\n')
    return s


SETTINGS_NS = ('xmlns:pal="http://v8.1c.ru/8.1/data/ui/colors/palette" xmlns:style="http://v8.1c.ru/8.1/data/ui/style" '
               'xmlns:sys="http://v8.1c.ru/8.1/data/ui/fonts/system" xmlns:web="http://v8.1c.ru/8.1/data/ui/colors/web" '
               'xmlns:win="http://v8.1c.ru/8.1/data/ui/colors/windows"')
I3 = '\t\t\t'
KIND = '@<dcscor:value xsi:type="xs:string">{}</dcscor:value>\n'
PERIOD_THIS_WEEK = ('@<dcscor:value xsi:type="v8:StandardPeriod">\n@\t<v8:variant xsi:type="v8:StandardPeriodVariant">ThisWeek'
                    '</v8:variant>\n@\t<v8:startDate>0001-01-01T00:00:00</v8:startDate>\n'
                    '@\t<v8:endDate>0001-01-01T00:00:00</v8:endDate>\n@</dcscor:value>\n')
MOMENT_EMPTY = '@<dcscor:value xsi:type="xs:dateTime">0001-01-01T00:00:00</dcscor:value>\n'
TITLE = ('План загрузки станков', 'Plan de charge des machines', 'Machine load plan', 'Plan de carga de máquinas')

by_days = (f'\t<settingsVariant>\n\t\t<dcsset:name>ПоДням</dcsset:name>\n'
           + ls(('По дням', 'Par jour', 'By day', 'Por días'), '\t\t', 'dcsset:presentation')
           + f'\t\t<dcsset:settings {SETTINGS_NS}>\n'
           + selection(('Процент', 'Свободно'), I3)
           + f'{I3}<dcsset:filter>\n{I3}\t<dcsset:userSettingID>{u()}</dcsset:userSettingID>\n{I3}</dcsset:filter>\n'
           + data_params([('ВидДанных', KIND.format('Дни'), False), ('Период', PERIOD_THIS_WEEK, True)], I3)
           + f'{I3}<dcsset:conditionalAppearance>\n'
           + color_rule('Процент', [('GreaterOrEqual', 100)], 'web:LightPink', I3 + '\t')
           + color_rule('Процент', [('GreaterOrEqual', 85), ('Less', 100)], 'web:LightYellow', I3 + '\t')
           + color_rule('Процент', [('Greater', 0), ('Less', 85)], 'web:LightGreen', I3 + '\t')
           + f'{I3}</dcsset:conditionalAppearance>\n'
           + output(TITLE, I3)
           + f'{I3}<dcsset:item xsi:type="dcsset:StructureItemTable">\n{I3}\t<dcsset:row>\n{I3}\t\t<dcsset:groupItems>\n'
           + group_item('Станок', I3 + '\t\t\t') + f'{I3}\t\t</dcsset:groupItems>\n' + auto(I3 + '\t\t')
           + f'{I3}\t</dcsset:row>\n{I3}\t<dcsset:column>\n{I3}\t\t<dcsset:groupItems>\n'
           + group_item('День', I3 + '\t\t\t') + f'{I3}\t\t</dcsset:groupItems>\n' + auto(I3 + '\t\t')
           + f'{I3}\t</dcsset:column>\n{I3}</dcsset:item>\n'
           + '\t\t</dcsset:settings>\n\t</settingsVariant>\n')
at_risk = (f'\t<settingsVariant>\n\t\t<dcsset:name>ЗаказыПодРиском</dcsset:name>\n'
           + ls(('Заказы под риском', 'Commandes à risque', 'Orders at risk', 'Pedidos en riesgo'), '\t\t', 'dcsset:presentation')
           + f'\t\t<dcsset:settings {SETTINGS_NS}>\n'
           + selection(('Заказ', 'Клиент', 'ДатаОтгрузки', 'Номенклатура', 'Количество', 'СтанокЗаказа', 'Окончание',
                        'ОпозданиеДней', 'ТекстОшибки'), I3)
           + f'{I3}<dcsset:filter>\n{I3}\t<dcsset:userSettingID>{u()}</dcsset:userSettingID>\n{I3}</dcsset:filter>\n'
           + data_params([('ВидДанных', KIND.format('Риски'), False), ('Момент', MOMENT_EMPTY, True)], I3)
           + f'{I3}<dcsset:order>\n{I3}\t<dcsset:item xsi:type="dcsset:OrderItemField">\n'
           f'{I3}\t\t<dcsset:field>ДатаОтгрузки</dcsset:field>\n{I3}\t\t<dcsset:orderType>Asc</dcsset:orderType>\n'
           f'{I3}\t</dcsset:item>\n{I3}</dcsset:order>\n'
           + output(('Заказы под риском срыва', 'Commandes à risque de retard', 'Orders at risk of delay',
                     'Pedidos en riesgo de retraso'), I3)
           + f'{I3}<dcsset:item xsi:type="dcsset:StructureItemGroup">\n{I3}\t<dcsset:groupItems>\n'
           + group_item('Источник', I3 + '\t\t') + f'{I3}\t</dcsset:groupItems>\n' + auto(I3 + '\t')
           + f'{I3}\t<dcsset:item xsi:type="dcsset:StructureItemGroup">\n' + auto(I3 + '\t\t')
           + f'{I3}\t</dcsset:item>\n{I3}</dcsset:item>\n'
           + '\t\t</dcsset:settings>\n\t</settingsVariant>\n')

schema = ('<?xml version="1.0" encoding="UTF-8"?>\n'
          '<DataCompositionSchema xmlns="http://v8.1c.ru/8.1/data-composition-system/schema" '
          'xmlns:dcscom="http://v8.1c.ru/8.1/data-composition-system/common" '
          'xmlns:dcscor="http://v8.1c.ru/8.1/data-composition-system/core" '
          'xmlns:dcsset="http://v8.1c.ru/8.1/data-composition-system/settings" xmlns:v8="http://v8.1c.ru/8.1/data/core" '
          'xmlns:v8ui="http://v8.1c.ru/8.1/data/ui" xmlns:xs="http://www.w3.org/2001/XMLSchema" '
          'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
          '\t<dataSource>\n\t\t<name>ИсточникДанных1</name>\n\t\t<dataSourceType>Local</dataSourceType>\n\t</dataSource>\n'
          + dataset('Дни', days) + dataset('Риски', risks)
          + total('Фонд', 'Сумма(Фонд)') + total('Занято', 'Сумма(Занято)') + total('Свободно', 'Сумма(Свободно)')
          + total('Процент', 'Выбор Когда Сумма(Фонд) > 0 Тогда Окр(Сумма(Занято) * 100 / Сумма(Фонд), 0) Иначе 0 Конец')
          + total('Количество', 'Сумма(Количество)') + total('Часы', 'Сумма(Часы)')
          + total('ОпозданиеДней', 'Максимум(ОпозданиеДней)')
          + param('Период', ('Период', 'Période', 'Period', 'Período'), PERIOD_T, PERIOD_V)
          + param('Момент', ('Момент', 'Moment', 'Moment', 'Momento'), DATE_T, DATE_V)
          + param('ВидДанных', ('Вид данных', 'Type de données', 'Data kind', 'Tipo de datos'), STR_T,
                  '\t\t<value xsi:type="xs:string">Дни</value>\n', 'true')
          + by_days + at_risk + '</DataCompositionSchema>\n')

synonym = ''.join(f'  <synonym>\n    <key>{lang}</key>\n    <value>{t}</value>\n  </synonym>\n' for lang, t in zip(LANGS, TITLE))
tsyn = ''.join(f'    <synonym>\n      <key>{lang}</key>\n      <value>{t}</value>\n    </synonym>\n' for lang, t in zip(
    LANGS, ('Основная схема компоновки данных', 'Schéma principal de composition des données', 'Main data composition schema',
            'Esquema principal de composición de datos')))
mdo = (f'<?xml version="1.0" encoding="UTF-8"?>\n<mdclass:Report xmlns:mdclass="http://g5.1c.ru/v8/dt/metadata/mdclass" '
       f'uuid="{u()}">\n  <producedTypes>\n    <objectType typeId="{u()}" valueTypeId="{u()}"/>\n'
       f'    <managerType typeId="{u()}" valueTypeId="{u()}"/>\n  </producedTypes>\n  <name>{NAME}</name>\n' + synonym
       + '  <useStandardCommands>true</useStandardCommands>\n  <defaultForm>CommonForm.ФормаОтчёта</defaultForm>\n'
       f'  <mainDataCompositionSchema>Report.{NAME}.Template.ОсновнаяСхемаКомпоновкиДанных</mainDataCompositionSchema>\n'
       f'  <templates uuid="{u()}">\n    <name>ОсновнаяСхемаКомпоновкиДанных</name>\n' + tsyn
       + '    <templateType>DataCompositionSchema</templateType>\n  </templates>\n</mdclass:Report>\n')

os.makedirs(f'{DIR}/Templates/ОсновнаяСхемаКомпоновкиДанных', exist_ok=True)
if not os.path.exists(f'{DIR}/{NAME}.mdo'):
    # uuid объекта не меняется при перегенерации схемы.
    open(f'{DIR}/{NAME}.mdo', 'w', encoding='utf-8').write(mdo)
open(f'{DIR}/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs', 'w', encoding='utf-8').write(schema)
print('Отчёт', NAME, 'записан')
