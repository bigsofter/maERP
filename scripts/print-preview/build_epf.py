#!/usr/bin/env python3
"""Собирает XML-исходник внешней обработки предпросмотра печати: форма с ПриОткрытии -> сервер -> Главная(Части, Лог).

Запуск: build_epf.py <ИмяОбработки> <тело.bsl> <каталог-вывода>; вызывается из scripts/print-preview.sh."""
import sys, os, uuid, shutil
name, body_file, out = sys.argv[1], sys.argv[2], sys.argv[3]
U = lambda: str(uuid.uuid4())
NS = ('xmlns="http://v8.1c.ru/8.3/MDClasses" xmlns:app="http://v8.1c.ru/8.2/managed-application/core" '
 'xmlns:cfg="http://v8.1c.ru/8.1/data/enterprise/current-config" xmlns:cmi="http://v8.1c.ru/8.2/managed-application/cmi" '
 'xmlns:ent="http://v8.1c.ru/8.1/data/enterprise" xmlns:lf="http://v8.1c.ru/8.2/managed-application/logform" '
 'xmlns:style="http://v8.1c.ru/8.1/data/ui/style" xmlns:sys="http://v8.1c.ru/8.1/data/ui/fonts/system" '
 'xmlns:v8="http://v8.1c.ru/8.1/data/core" xmlns:v8ui="http://v8.1c.ru/8.1/data/ui" '
 'xmlns:web="http://v8.1c.ru/8.1/data/ui/colors/web" xmlns:win="http://v8.1c.ru/8.1/data/ui/colors/windows" '
 'xmlns:xen="http://v8.1c.ru/8.3/xcf/enums" xmlns:xpr="http://v8.1c.ru/8.3/xcf/predef" '
 'xmlns:xr="http://v8.1c.ru/8.3/xcf/readable" xmlns:xs="http://www.w3.org/2001/XMLSchema" '
 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="2.21"')
FNS = NS.replace('xmlns="http://v8.1c.ru/8.3/MDClasses"', 'xmlns="http://v8.1c.ru/8.3/xcf/logform"').replace(
 'xmlns:cmi="http://v8.1c.ru/8.2/managed-application/cmi" ', 'xmlns:dcscor="http://v8.1c.ru/8.1/data-composition-system/core" xmlns:dcsset="http://v8.1c.ru/8.1/data-composition-system/settings" ')
shutil.rmtree(out, ignore_errors=True)
os.makedirs(f'{out}/{name}/Forms/Форма/Ext/Form', exist_ok=True)
w = lambda p, t: open(p, 'w', encoding='utf-8-sig').write(t)
w(f'{out}/{name}.xml', f'''<?xml version="1.0" encoding="UTF-8"?>
<MetaDataObject {NS}>
	<ExternalDataProcessor uuid="{U()}">
		<InternalInfo>
			<xr:ContainedObject>
				<xr:ClassId>c3831ec8-d8d5-4f93-8a22-f9bfae07327f</xr:ClassId>
				<xr:ObjectId>{U()}</xr:ObjectId>
			</xr:ContainedObject>
			<xr:GeneratedType name="ExternalDataProcessorObject.{name}" category="Object">
				<xr:TypeId>{U()}</xr:TypeId>
				<xr:ValueId>{U()}</xr:ValueId>
			</xr:GeneratedType>
		</InternalInfo>
		<Properties>
			<Name>{name}</Name>
			<Synonym/>
			<Comment/>
			<DefaultForm>ExternalDataProcessor.{name}.Form.Форма</DefaultForm>
			<AuxiliaryForm/>
		</Properties>
		<ChildObjects>
			<Form>Форма</Form>
		</ChildObjects>
	</ExternalDataProcessor>
</MetaDataObject>
''')
w(f'{out}/{name}/Forms/Форма.xml', f'''<?xml version="1.0" encoding="UTF-8"?>
<MetaDataObject {NS}>
	<Form uuid="{U()}">
		<Properties>
			<Name>Форма</Name>
			<Synonym/>
			<Comment/>
			<FormType>Managed</FormType>
			<IncludeHelpInContents>false</IncludeHelpInContents>
			<UsePurposes>
				<v8:Value xsi:type="app:ApplicationUsePurpose">PlatformApplication</v8:Value>
			</UsePurposes>
			<ExtendedPresentation/>
		</Properties>
	</Form>
</MetaDataObject>
''')
w(f'{out}/{name}/Forms/Форма/Ext/Form.xml', f'''<?xml version="1.0" encoding="UTF-8"?>
<Form {FNS}>
	<AutoCommandBar name="ФормаКоманднаяПанель" id="-1"/>
	<Events>
		<Event name="OnOpen">ПриОткрытии</Event>
	</Events>
	<Attributes>
		<Attribute name="Объект" id="1">
			<Type>
				<v8:Type>cfg:ExternalDataProcessorObject.{name}</v8:Type>
			</Type>
			<MainAttribute>true</MainAttribute>
		</Attribute>
	</Attributes>
</Form>
''')
body = open(body_file, encoding='utf-8').read()
w(f'{out}/{name}/Forms/Форма/Ext/Form/Module.bsl', '''&НаКлиенте
Процедура ПриОткрытии(Отказ)
	ВыполнитьНаСервере(ПараметрЗапуска);
	ЗавершитьРаботуСистемы(Ложь);
КонецПроцедуры

&НаСервереБезКонтекста
Процедура ВыполнитьНаСервере(Параметр)
	Части = СтрРазделить(Параметр, "|");
	Лог = Новый ЗаписьТекста(Части[0], КодировкаТекста.UTF8);
	Лог.ЗаписатьСтроку("СТАРТ;");
	Попытка
		Главная(Части, Лог);
		Лог.ЗаписатьСтроку("ИТОГ;ОК");
	Исключение
		Лог.ЗаписатьСтроку("ОШИБКА;" + ПодробноеПредставлениеОшибки(ИнформацияОбОшибке()));
		Лог.ЗаписатьСтроку("ИТОГ;ОШИБКА");
	КонецПопытки;
	Лог.Закрыть();
КонецПроцедуры

''' + body)
