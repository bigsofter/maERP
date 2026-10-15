#!/usr/bin/env python3
"""Отчёт «Остатки на складах» (план warehouse-orders, фаза 4, §4.2): метаданные и схема компоновки.

Физические остатки ТоварыНаСкладах и неоформленные остатки ТоварыКОформлению на одну дату, ключ записи к оформлению
приведён к физическому (составляющая комплекта - своя номенклатура, пустые характеристика и серия; коммерческая строка
комплекта расходного ордера не идёт - его физику дают записи составляющих; у приходного ордера комплект - сама
запись). «По учёту» = на складе - приход к оформлению + расход к оформлению.
Запуск: python3 scripts/formgen/warehouse-orders/gen_report.py
"""
import os
import uuid

SRC = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src', 'cf', 'src')
ИМЯ = 'ОстаткиНаСкладах'
СИНОНИМ = ('Остатки на складах', 'Stocks en entrepôt', 'Warehouse stock', 'Existencias en almacenes')


def u():
    return str(uuid.uuid4())


def заголовок(ru, fr, en, es, отступ='\t\t\t'):
    items = ''.join(f'{отступ}\t<v8:item>\n{отступ}\t\t<v8:lang>{k}</v8:lang>\n{отступ}\t\t<v8:content>{v}</v8:content>\n'
                    f'{отступ}\t</v8:item>\n' for k, v in (('ru', ru), ('fr', fr), ('en', en), ('es', es)))
    return f'{отступ}<title xsi:type="v8:LocalStringType">\n{items}{отступ}</title>\n'


def поле(путь, измерение=False, title=None):
    роль = '\t\t\t<role>\n\t\t\t\t<dcscom:dimension>true</dcscom:dimension>\n\t\t\t</role>\n' if измерение else ''
    t = заголовок(*title) if title else ''
    return (f'\t\t<field xsi:type="DataSetFieldField">\n\t\t\t<dataPath>{путь}</dataPath>\n\t\t\t<field>{путь}</field>\n'
            f'{t}{роль}\t\t</field>\n')


ЗАПРОС = '''ВЫБРАТЬ
	Данные.МестоХранения КАК МестоХранения,
	Данные.Номенклатура КАК Номенклатура,
	Данные.Характеристика КАК Характеристика,
	Данные.Серия КАК Серия,
	Позиции.Артикул КАК Артикул,
	Позиции.Единица КАК Единица,
	СУММА(Данные.НаСкладе) КАК НаСкладе,
	СУММА(Данные.Приход) КАК КОформлениюПриход,
	СУММА(Данные.Расход) КАК КОформлениюРасход
ИЗ
	(ВЫБРАТЬ
		Физика.МестоХранения КАК МестоХранения,
		Физика.Номенклатура КАК Номенклатура,
		Физика.Характеристика КАК Характеристика,
		Физика.Серия КАК Серия,
		Физика.КоличествоОстаток КАК НаСкладе,
		0 КАК Приход,
		0 КАК Расход
	ИЗ
		РегистрНакопления.ТоварыНаСкладах.Остатки(&amp;Период, ) КАК Физика

	ОБЪЕДИНИТЬ ВСЕ

	ВЫБРАТЬ
		Оформление.МестоХранения,
		ВЫБОР
			КОГДА Оформление.Составляющая = ЗНАЧЕНИЕ(Справочник.Номенклатура.ПустаяСсылка)
				ТОГДА Оформление.Номенклатура
			ИНАЧЕ Оформление.Составляющая
		КОНЕЦ,
		ВЫБОР
			КОГДА Оформление.Составляющая = ЗНАЧЕНИЕ(Справочник.Номенклатура.ПустаяСсылка)
				ТОГДА Оформление.Характеристика
			ИНАЧЕ ЗНАЧЕНИЕ(Справочник.ХарактеристикиНоменклатуры.ПустаяСсылка)
		КОНЕЦ,
		ВЫБОР
			КОГДА Оформление.Составляющая = ЗНАЧЕНИЕ(Справочник.Номенклатура.ПустаяСсылка)
				ТОГДА Оформление.Серия
			ИНАЧЕ ЗНАЧЕНИЕ(Справочник.СерииНоменклатуры.ПустаяСсылка)
		КОНЕЦ,
		0,
		ВЫБОР
			КОГДА Оформление.Ордер ССЫЛКА Документ.ПриходныйОрдер
				ТОГДА Оформление.КоличествоОстаток
			ИНАЧЕ 0
		КОНЕЦ,
		ВЫБОР
			КОГДА Оформление.Ордер ССЫЛКА Документ.РасходныйОрдер
				ТОГДА Оформление.КоличествоОстаток
			ИНАЧЕ 0
		КОНЕЦ
	ИЗ
		РегистрНакопления.ТоварыКОформлению.Остатки(&amp;Период, ) КАК Оформление
			ВНУТРЕННЕЕ СОЕДИНЕНИЕ Справочник.Номенклатура КАК ПозицииОформления
			ПО Оформление.Номенклатура = ПозицииОформления.Ссылка
	ГДЕ
		ВЫБОР
			КОГДА Оформление.Составляющая = ЗНАЧЕНИЕ(Справочник.Номенклатура.ПустаяСсылка)
					И Оформление.Ордер ССЫЛКА Документ.РасходныйОрдер
				ТОГДА ПозицииОформления.ТипНоменклатуры &lt;&gt; ЗНАЧЕНИЕ(Перечисление.ТипыНоменклатуры.Комплект)
			ИНАЧЕ ИСТИНА
		КОНЕЦ) КАК Данные
		ЛЕВОЕ СОЕДИНЕНИЕ Справочник.Номенклатура КАК Позиции
		ПО Данные.Номенклатура = Позиции.Ссылка

СГРУППИРОВАТЬ ПО
	Данные.МестоХранения,
	Данные.Номенклатура,
	Данные.Характеристика,
	Данные.Серия,
	Позиции.Артикул,
	Позиции.Единица'''

РЕСУРСЫ = [
    ('НаСкладе', ('На складе', 'En entrepôt', 'In warehouse', 'En almacén')),
    ('КОформлениюПриход', ('К оформлению: приход', 'À régulariser : entrée', 'To document: receipt',
                           'Por formalizar: entrada')),
    ('КОформлениюРасход', ('К оформлению: расход', 'À régulariser : sortie', 'To document: issue',
                           'Por formalizar: salida')),
]
ПО_УЧЕТУ = ('По учёту', 'Selon la comptabilité', 'Per accounting', 'Según contabilidad')


def группа(поля, вложенная=''):
    элементы = ''.join(f'''					<dcsset:item xsi:type="dcsset:GroupItemField">
						<dcsset:field>{п}</dcsset:field>
						<dcsset:groupType>Items</dcsset:groupType>
						<dcsset:periodAdditionType>None</dcsset:periodAdditionType>
						<dcsset:periodAdditionBegin xsi:type="xs:dateTime">0001-01-01T00:00:00</dcsset:periodAdditionBegin>
						<dcsset:periodAdditionEnd xsi:type="xs:dateTime">0001-01-01T00:00:00</dcsset:periodAdditionEnd>
					</dcsset:item>
''' for п in поля)
    return f'''				<dcsset:item xsi:type="dcsset:StructureItemGroup">
				<dcsset:groupItems>
{элементы}				</dcsset:groupItems>
				<dcsset:order>
					<dcsset:item xsi:type="dcsset:OrderItemAuto"/>
				</dcsset:order>
				<dcsset:selection>
					<dcsset:item xsi:type="dcsset:SelectedItemAuto"/>
				</dcsset:selection>
{вложенная}				</dcsset:item>
'''


def схема():
    поля = ''.join([поле('МестоХранения', True), поле('Номенклатура', True), поле('Характеристика', True),
                    поле('Серия', True),
                    поле('Артикул', title=('Артикул', 'Article', 'Reference', 'Articulo')),
                    поле('Единица', title=('Единица', 'Unité', 'Unit', 'Unidad'))]
                   + [поле(имя, title=t) for имя, t in РЕСУРСЫ])
    итоги = ''.join(f'\t<totalField>\n\t\t<dataPath>{имя}</dataPath>\n\t\t<expression>Сумма({имя})</expression>\n'
                    f'\t</totalField>\n' for имя, _ in РЕСУРСЫ)
    итоги += ('\t<totalField>\n\t\t<dataPath>ПоУчету</dataPath>\n\t\t<expression>Сумма(НаСкладе) - Сумма(КОформлениюПриход) '
              '+ Сумма(КОформлениюРасход)</expression>\n\t</totalField>\n')
    выбор = ''.join(f'\t\t\t\t<dcsset:item xsi:type="dcsset:SelectedItemField">\n\t\t\t\t\t<dcsset:field>{имя}</dcsset:field>\n'
                    f'\t\t\t\t</dcsset:item>\n' for имя in [р[0] for р in РЕСУРСЫ] + ['ПоУчету'])
    формат_поля = ''.join(f'\t\t\t\t\t\t<dcsset:item>\n\t\t\t\t\t\t\t<dcsset:field>{имя}</dcsset:field>\n\t\t\t\t\t\t</dcsset:item>\n'
                          for имя in [р[0] for р in РЕСУРСЫ] + ['ПоУчету'])
    формат = ''.join(f'\t\t\t\t\t\t\t\t<v8:item>\n\t\t\t\t\t\t\t\t\t<v8:lang>{k}</v8:lang>\n\t\t\t\t\t\t\t\t\t<v8:content>ЧЦ=15; ЧДЦ=3</v8:content>\n'
                     f'\t\t\t\t\t\t\t\t</v8:item>\n' for k in ('ru', 'fr', 'en', 'es'))
    структура = группа(['МестоХранения'], группа(['Номенклатура', 'Характеристика', 'Серия']))
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<DataCompositionSchema xmlns="http://v8.1c.ru/8.1/data-composition-system/schema" xmlns:dcscom="http://v8.1c.ru/8.1/data-composition-system/common" xmlns:dcscor="http://v8.1c.ru/8.1/data-composition-system/core" xmlns:dcsset="http://v8.1c.ru/8.1/data-composition-system/settings" xmlns:v8="http://v8.1c.ru/8.1/data/core" xmlns:v8ui="http://v8.1c.ru/8.1/data/ui" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<dataSource>
		<name>ИсточникДанных1</name>
		<dataSourceType>Local</dataSourceType>
	</dataSource>
	<dataSet xsi:type="DataSetQuery">
		<name>Данные</name>
{поля}		<dataSource>ИсточникДанных1</dataSource>
		<query>{ЗАПРОС}</query>
	</dataSet>
	<calculatedField>
		<dataPath>ПоУчету</dataPath>
		<expression>НаСкладе - КОформлениюПриход + КОформлениюРасход</expression>
{заголовок(*ПО_УЧЕТУ, отступ=chr(9) + chr(9))}	</calculatedField>
{итоги}	<parameter>
		<name>Период</name>
{заголовок('Дата остатков', 'Date des stocks', 'Stock date', 'Fecha de existencias', отступ=chr(9) + chr(9))}		<valueType>
			<v8:Type>xs:dateTime</v8:Type>
			<v8:DateQualifiers>
				<v8:DateFractions>Date</v8:DateFractions>
			</v8:DateQualifiers>
		</valueType>
		<value xsi:type="xs:dateTime">0001-01-01T00:00:00</value>
		<useRestriction>false</useRestriction>
		<expression>ДобавитьКДате(НачалоПериода(&amp;Период, "ДЕНЬ"), "ДЕНЬ", 1)</expression>
		<availableAsField>false</availableAsField>
		<use>Always</use>
	</parameter>
	<settingsVariant>
		<dcsset:name>Основной</dcsset:name>
		<dcsset:presentation xsi:type="xs:string">Основной</dcsset:presentation>
		<dcsset:settings xmlns:style="http://v8.1c.ru/8.1/data/ui/style">
			<dcsset:selection>
{выбор}			</dcsset:selection>
			<dcsset:filter>
				<dcsset:item xsi:type="dcsset:FilterItemComparison">
					<dcsset:use>false</dcsset:use>
					<dcsset:left xsi:type="dcscor:Field">МестоХранения</dcsset:left>
					<dcsset:comparisonType>Equal</dcsset:comparisonType>
					<dcsset:userSettingID>{u()}</dcsset:userSettingID>
				</dcsset:item>
				<dcsset:item xsi:type="dcsset:FilterItemComparison">
					<dcsset:use>false</dcsset:use>
					<dcsset:left xsi:type="dcscor:Field">Номенклатура</dcsset:left>
					<dcsset:comparisonType>Equal</dcsset:comparisonType>
					<dcsset:userSettingID>{u()}</dcsset:userSettingID>
				</dcsset:item>
				<dcsset:userSettingID>{u()}</dcsset:userSettingID>
			</dcsset:filter>
			<dcsset:dataParameters>
				<dcscor:item xsi:type="dcsset:SettingsParameterValue">
					<dcscor:parameter>Период</dcscor:parameter>
					<dcscor:value xsi:type="v8:StandardBeginningDate">
						<v8:variant xsi:type="v8:StandardBeginningDateVariant">BeginningOfThisDay</v8:variant>
					</dcscor:value>
					<dcsset:userSettingID>{u()}</dcsset:userSettingID>
				</dcscor:item>
			</dcsset:dataParameters>
			<dcsset:conditionalAppearance>
				<dcsset:item>
					<dcsset:selection>
{формат_поля}					</dcsset:selection>
					<dcsset:filter/>
					<dcsset:appearance>
						<dcscor:item xsi:type="dcsset:SettingsParameterValue">
							<dcscor:parameter>Format</dcscor:parameter>
							<dcscor:value xsi:type="v8:LocalStringType">
{формат}							</dcscor:value>
						</dcscor:item>
						<dcscor:item xsi:type="dcsset:SettingsParameterValue">
							<dcscor:parameter>MarkNegatives</dcscor:parameter>
							<dcscor:value xsi:type="xs:boolean">true</dcscor:value>
						</dcscor:item>
					</dcsset:appearance>
				</dcsset:item>
			</dcsset:conditionalAppearance>
			<dcsset:outputParameters>
				<dcscor:item xsi:type="dcsset:SettingsParameterValue">
					<dcscor:parameter>AttributePlacement</dcscor:parameter>
					<dcscor:value xsi:type="dcsset:DataCompositionAttributesPlacement">Separately</dcscor:value>
				</dcscor:item>
				<dcscor:item xsi:type="dcsset:SettingsParameterValue">
					<dcscor:parameter>TitleOutput</dcscor:parameter>
					<dcscor:value xsi:type="dcsset:DataCompositionTextOutputType">Output</dcscor:value>
				</dcscor:item>
				<dcscor:item xsi:type="dcsset:SettingsParameterValue">
					<dcscor:parameter>Title</dcscor:parameter>
					<dcscor:value xsi:type="v8:LocalStringType">
{''.join(f"""						<v8:item>
							<v8:lang>{k}</v8:lang>
							<v8:content>{v}</v8:content>
						</v8:item>
""" for k, v in zip(('ru', 'fr', 'en', 'es'), СИНОНИМ))}					</dcscor:value>
				</dcscor:item>
				<dcscor:item xsi:type="dcsset:SettingsParameterValue">
					<dcscor:parameter>DataParametersOutput</dcscor:parameter>
					<dcscor:value xsi:type="dcsset:DataCompositionTextOutputType">Output</dcscor:value>
				</dcscor:item>
				<dcscor:item xsi:type="dcsset:SettingsParameterValue">
					<dcscor:parameter>FilterOutput</dcscor:parameter>
					<dcscor:value xsi:type="dcsset:DataCompositionTextOutputType">Output</dcscor:value>
				</dcscor:item>
			</dcsset:outputParameters>
{структура}		</dcsset:settings>
	</settingsVariant>
</DataCompositionSchema>
'''


def метаданные():
    синонимы = ''.join(f'  <synonym>\n    <key>{k}</key>\n    <value>{v}</value>\n  </synonym>\n'
                       for k, v in zip(('ru', 'fr', 'en', 'es'), СИНОНИМ))
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<mdclass:Report xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:core="http://g5.1c.ru/v8/dt/mcore" xmlns:mdclass="http://g5.1c.ru/v8/dt/metadata/mdclass" uuid="{u()}">
  <producedTypes>
    <objectType typeId="{u()}" valueTypeId="{u()}"/>
    <managerType typeId="{u()}" valueTypeId="{u()}"/>
  </producedTypes>
  <name>{ИМЯ}</name>
{синонимы}  <useStandardCommands>true</useStandardCommands>
  <defaultForm>CommonForm.ФормаОтчёта</defaultForm>
  <mainDataCompositionSchema>Report.{ИМЯ}.Template.ОсновнаяСхемаКомпоновкиДанных</mainDataCompositionSchema>
  <templates uuid="{u()}">
    <name>ОсновнаяСхемаКомпоновкиДанных</name>
    <synonym>
      <key>ru</key>
      <value>Основная схема компоновки данных</value>
    </synonym>
    <synonym>
      <key>fr</key>
      <value>Schéma de base de la mise en page des données</value>
    </synonym>
    <synonym>
      <key>en</key>
      <value>Basic scheme of the data layout</value>
    </synonym>
    <synonym>
      <key>es</key>
      <value>Esquema básico de diseño de datos</value>
    </synonym>
    <templateType>DataCompositionSchema</templateType>
  </templates>
</mdclass:Report>
'''


каталог = os.path.join(SRC, 'Reports', ИМЯ)
os.makedirs(os.path.join(каталог, 'Templates', 'ОсновнаяСхемаКомпоновкиДанных'), exist_ok=True)
with open(os.path.join(каталог, ИМЯ + '.mdo'), 'w', encoding='utf-8') as f:
    f.write(метаданные())
with open(os.path.join(каталог, 'Templates', 'ОсновнаяСхемаКомпоновкиДанных', 'Template.dcs'), 'w', encoding='utf-8') as f:
    f.write(схема())
print('ok', каталог)
