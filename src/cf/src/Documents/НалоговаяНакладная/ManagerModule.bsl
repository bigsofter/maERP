
#Область Печать

Процедура ПечатьТорг12(Док, Таб) Экспорт
	УстановитьПривилегированныйРежим(Истина);
	ЭтоВозвратПоставщику = ТипЗнч(Док) = Тип("ДокументСсылка.ВозвратПоставщику");
	Таб.ТолькоПросмотр = Истина;
	Таб.ОтображатьЗаголовки = Ложь;
	Таб.ОтображатьСетку = Ложь;
	Таб.ОриентацияСтраницы = ОриентацияСтраницы.Ландшафт;
	Таб.АвтоМасштаб = Истина;
	Таб.КлючПараметровПечати = "Параметры_печати_Документ_НалоговаяНакладная_Торг12";
	ТабФормирование = Новый ТабличныйДокумент;
	ТабФормирование.АвтоМасштаб = Истина;
	ТабФормирование.ОриентацияСтраницы = ОриентацияСтраницы.Ландшафт;
	// Макет
	Макет = Документы.НалоговаяНакладная.ПолучитьМакет("РасходнаяНакладная");
	// Переменные
	Если ТипЗнч(Док) = Тип("ДокументСсылка.ПоступлениеТоваровУслуг") Тогда
		Грузоотправитель = Док.Контрагент;
		Грузополучатель = Док.Организация; 
		Плательщик = Док.Организация;
		ДокНомер = Док.НомерВходящегоДокумента;
		ДокДата = Док.ДатаВходящегоДокумента;
	Иначе
		Грузоотправитель = Док.Организация;
		Грузополучатель =  Док.Контрагент;
		Плательщик = Док.Контрагент;
		ДокНомер = РаботаСДокументами.СформироватьЦифровойНомер(Док.Номер);
		ДокДата = Док.Дата;
	КонецЕсли;
    КарточкаГрузоотправителя = Справочники.Контрагенты.ПолучитьКарточку(Грузоотправитель, Док.Дата);
	КарточкаГрузополучателя = Справочники.Контрагенты.ПолучитьКарточку(Грузополучатель, Док.Дата);
	КарточкаПлательщика = Справочники.Контрагенты.ПолучитьКарточку(Плательщик, Док.Дата);
	// Шапка
	оШапка = Макет.ПолучитьОбласть("Шапка");
	оЗаголовок = Макет.ПолучитьОбласть("ЗаголовокТаблицы");
	оШапка.Параметры.НомерДокумента = ДокНомер;
	оШапка.Параметры.ДатаДокумента = ДокДата;
	оШапка.Параметры.ПредставлениеОрганизации = КарточкаГрузоотправителя.Представление;
	оШапка.Параметры.ПредставлениеПоставщика = КарточкаГрузоотправителя.Представление;
	оШапка.Параметры.ОрганизацияПоОКПО = КарточкаГрузоотправителя.Реквизиты.ОКПО;
	оШапка.Параметры.ПредставлениеГрузополучателя = КарточкаГрузополучателя.Наименование + ", " + КарточкаГрузополучателя.Реквизиты.АдресФактический;
	оШапка.Параметры.АдресДоставки = КарточкаГрузополучателя.Реквизиты.АдресДоставки;
	оШапка.Параметры.ГрузополучательПоОКПО = КарточкаГрузополучателя.Реквизиты.ОКПО;
	оШапка.Параметры.ПредставлениеПлательщика = КарточкаПлательщика.Представление;
	оШапка.Параметры.ПлательщикПоОКПО = КарточкаПлательщика.Реквизиты.ОКПО;
	оШапка.Параметры.Основание = "Договор " + СокрЛП(Док.Договор);
	ТабФормирование.Вывести(оШапка);
	ТабФормирование.Вывести(оЗаголовок);
	// Строки
	оСтрока = Макет.ПолучитьОбласть("Строка");
	оИтогоПоСтранице = Макет.ПолучитьОбласть("ИтогоПоСтранице");
	оВсего = Макет.ПолучитьОбласть("Всего");
	оПодвал = Макет.ПолучитьОбласть("Подвал");
	ИтогоКоличество = 0;
	ИтогоСумма = 0;
	ИтогоМест = 0;
	ИтогоНетто = 0;
	ИтогоБрутто = 0;
	ИтогоСтраницаКоличество = 0;
	ИтогоСтраницаСумма = 0;
	ИтогоСтраницаМест = 0;
	Ном = 1;
	МасВывод = Новый Массив;
	ТЧТовары = СерииИРазмещение.ОбъединитьТоварыССериями(Док);	
	ТЧТовары = ВыводПечатныхФорм.СформироватьТабличныеДанные(ТЧТовары);	
	КоличествоТоваров = ТЧТовары.Количество();
	Для Каждого Стр Из ТЧТовары Цикл
		оСтрока.Параметры.Заполнить(Стр);
		оСтрока.Параметры.НомерСтроки = Ном;
		//Если Док.ЦенаВключаетНДС Тогда
			СуммаБезНДС = Стр.СуммаСНДС - Стр.СуммаНДС;
			ЦенаБезНДС = ?(Стр.Количество = 0, 0, СуммаБезНДС / Стр.Количество);
			оСтрока.Параметры.Сумма = СуммаБезНДС;
			оСтрока.Параметры.Цена = ЦенаБезНДС;
		//КонецЕсли;
		МасВывод.Очистить();
		МасВывод.Добавить(оСтрока);
		МасВывод.Добавить(оИтогоПоСтранице);			
		Если Ном = КоличествоТоваров Тогда				
			МасВывод.Добавить(оВсего);
			МасВывод.Добавить(оПодвал);
			Если Не ТабФормирование.ПроверитьВывод(МасВывод) Тогда
				оИтогоПоСтранице.Параметры.ИтогоКоличествоНаСтранице = ИтогоСтраницаКоличество;
				оИтогоПоСтранице.Параметры.ИтогоМестНаСтранице = ИтогоСтраницаМест;
				оИтогоПоСтранице.Параметры.ИтогоСуммаНаСтранице = ИтогоСтраницаСумма;
				ТабФормирование.Вывести(оИтогоПоСтранице);
				ТабФормирование.ВывестиГоризонтальныйРазделительСтраниц();
				ИтогоСтраницаКоличество = 0;
				ИтогоСтраницаСумма = 0;
				ИтогоСтраницаМест = 0;
				ТабФормирование.Вывести(оЗаголовок);
			КонецЕсли;
		ИначеЕсли Не ТабФормирование.ПроверитьВывод(МасВывод) Тогда
			оИтогоПоСтранице.Параметры.ИтогоКоличествоНаСтранице = ИтогоСтраницаКоличество;
			оИтогоПоСтранице.Параметры.ИтогоМестНаСтранице = ИтогоСтраницаМест;
			оИтогоПоСтранице.Параметры.ИтогоСуммаНаСтранице = ИтогоСтраницаСумма;
			ТабФормирование.Вывести(оИтогоПоСтранице);
			ТабФормирование.ВывестиГоризонтальныйРазделительСтраниц();
			ИтогоСтраницаКоличество = 0;
			ИтогоСтраницаСумма = 0;
			ИтогоСтраницаМест = 0;
			ТабФормирование.Вывести(оЗаголовок);
		КонецЕсли;
		ТабФормирование.Вывести(оСтрока);
		ИтогоКоличество = ИтогоКоличество + Стр.Количество;
		ИтогоСумма = ИтогоСумма + Стр.Сумма;
		ИтогоМест = ИтогоМест + Стр.КоличествоУпаковок;
		//ИтогоНетто = ИтогоНетто + Стр.Количество;
		//ИтогоБрутто = ИтогоБрутто + Стр.Количество;
		ИтогоСтраницаКоличество = ИтогоСтраницаКоличество + Стр.Количество;
		ИтогоСтраницаСумма = ИтогоСтраницаСумма + Стр.СуммаСНДС;
		ИтогоСтраницаМест = ИтогоСтраницаМест + Стр.КоличествоУпаковок;
		Ном = Ном + 1;
	КонецЦикла;
	оИтогоПоСтранице.Параметры.ИтогоКоличествоНаСтранице = ИтогоСтраницаКоличество;
	оИтогоПоСтранице.Параметры.ИтогоМестНаСтранице = ИтогоСтраницаМест;
	оИтогоПоСтранице.Параметры.ИтогоСуммаНаСтранице = ИтогоСтраницаСумма;
	ТабФормирование.Вывести(оИтогоПоСтранице);
	// Всего
	оВсего.Параметры.ИтогоКоличество = ИтогоКоличество;
	оВсего.Параметры.ИтогоМест = ИтогоМест;
	оВсего.Параметры.ИтогоСумма = ИтогоСумма;
	ТабФормирование.Вывести(оВсего);
	// Подвал
	оПодвал.Параметры.КоличествоПорядковыхНомеровЗаписейПрописью = ЧислоПрописью(КоличествоТоваров,,",,,,,,,,0");
	оПодвал.Параметры.ВсегоМестПрописью = ЧислоПрописью(ИтогоМест,,",,,,,,,,0");
	оПодвал.Параметры.МассаГрузаНеттоПрописью = ЧислоПрописью(ИтогоНетто,,",,,,,,,,0");
	оПодвал.Параметры.МассаГрузаБруттоПрописью = ЧислоПрописью(ИтогоБрутто,,",,,,,,,,0");
	оПодвал.Параметры.СуммаПрописью = Справочники.Валюты.СформироватьСуммуПрописью(ИтогоСумма, Справочники.Валюты.MoroccanDirham, Перечисления.Локализации.fr_CA);
	
	оПодвал.Параметры.ФИОРуководителя = КарточкаГрузоотправителя.Руководитель.ДляПечатиПолное;		
	оПодвал.Параметры.ДолжностьРуководителя = КарточкаГрузоотправителя.Руководитель.Должность;		
	оПодвал.Параметры.ФИОГлавБухгалтера = КарточкаГрузоотправителя.ГлавныйБухгалтер.Должность; 		
	
	ТабФормирование.Вывести(оПодвал);
	ТабФормирование.ВывестиГоризонтальныйРазделительСтраниц();
	Таб.Вывести(ТабФормирование);
	Таб.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Товарная накладная");
КонецПроцедуры

Процедура ПечатьСчетНаОплату(Док, Таб, РазбитьНДС = Ложь) Экспорт
	ВыбДата = Док.Дата;
	ВыбНомер = Док.Номер;
	Организация = Док.Организация;
	Контрагент = Док.Контрагент;
	Макет = Документы.НалоговаяНакладная.ПолучитьМакет("Счёт"); 
    КарточкаОрганизации = Справочники.Контрагенты.ПолучитьКарточку(Организация, Док.Дата);
    КарточкаКонтрагента = Справочники.Контрагенты.ПолучитьКарточку(Контрагент, Док.Дата);
	ОбластьЗаголовокСчета = Макет.ПолучитьОбласть("ЗаголовокСчета");
	ОбластьЗаголовокСчета.Параметры.БанкПолучателяпредставление = КарточкаОрганизации.БанковскийСчётОсновной.Наименование;
	ОбластьЗаголовокСчета.Параметры.БикБанкаПолучателя = КарточкаОрганизации.БанковскийСчётОсновной.Банк.Код;
	//ОбластьЗаголовокСчета.Параметры.СчетБанкаПолучателяПредставление = КарточкаОрганизации.БанковскийСчётОсновной.Банк.КоррСчёт;
	ОбластьЗаголовокСчета.Параметры.СчетПолучателяПредставление = КарточкаОрганизации.БанковскийСчётОсновной.НомерСчёта;
	ОбластьЗаголовокСчета.Параметры.ИННПолучателя = Организация.NIF;
	ОбластьЗаголовокСчета.Параметры.КПППолучателя = КарточкаОрганизации.Реквизиты.ICE;
	ОбластьЗаголовокСчета.Параметры.ПредставлениеПолучателя = Организация.Наименование;
	Таб.Вывести(ОбластьЗаголовокСчета);
	
	ОбластьЗаголовок = Макет.ПолучитьОбласть("Заголовок");
	ОбластьЗаголовок.Параметры.ТекстЗаголовка = "Facture proforma № " + Выбномер + " de " + Формат(ВыбДата, "ДЛФ=DD");
	Таб.Вывести(ОбластьЗаголовок);
	
	ОбластьПоставщик = Макет.ПолучитьОбласть("Поставщик");
	ОбластьПоставщик.Параметры.ПредставлениеПоставщика = Организация.Наименование 
	+ ", IF " + Организация.NIF + ", RC " + Организация.RC + ", " 
	+ КарточкаОрганизации.Реквизиты.АдресЮридический;
	Таб.Вывести(ОбластьПоставщик);
	
	ОбластьПокупатель = Макет.ПолучитьОбласть("Покупатель");
	ОбластьПокупатель.Параметры.ПредставлениеПокупателя = Контрагент.Наименование
	+ ", IF " + Контрагент.NIF + ", RC " + Контрагент.RC + ", " 
	+ КарточкаКонтрагента.Реквизиты.АдресЮридический + ", tel.: " + КарточкаКонтрагента.Реквизиты.Телефон;
	Таб.Вывести(ОбластьПокупатель);
	
	ОбластьШапкаТаблицы = Макет.ПолучитьОбласть("ШапкаТаблицы");
	Таб.Вывести(ОбластьШапкаТаблицы);
	
	ОбластьСтрока = Макет.ПолучитьОбласть("Строка");
	
	ТЗ = СерииИРазмещение.ОбъединитьТоварыССериями(Док);	
	ТЗ = ВыводПечатныхФорм.СформироватьТабличныеДанные(ТЗ);	

	Ном = 1;
	Для Каждого Стр Из ТЗ цикл
		ОбластьСтрока.Параметры.Заполнить(Стр);
		//ОбластьСтрока.Параметры.Единица = Стр.Единица.Единица;
		ОбластьСтрока.Параметры.НомерСтроки = Ном;
		Таб.Вывести(ОбластьСтрока);
		Ном = Ном + 1;
	КонецЦикла;
	
	ОбластьИтого = Макет.ПолучитьОбласть("Итого");
	ОбластьИтого.Параметры.Всего = ТЗ.Итог("Сумма");
	Таб.Вывести(ОбластьИтого);
	
	оИтогоНДС = Макет.ПолучитьОбласть("ИтогоНДС");
	оИтогоНДС.Параметры.НДС = "Сумма НДС";
	оИтогоНДС.Параметры.ВсегоНДС = ТЗ.Итог("СуммаНДС");
	Таб.Вывести(оИтогоНДС);
	
	Если РазбитьНДС тогда
		ТзНДС = ТЗ.Скопировать();
		ТзНДС.Свернуть("СтавкаНДС", "СуммаНДС");
		ТзНДС.Сортировать("СтавкаНДС");
		Для каждого Стр Из ТзНДС цикл
			оИтогоНДС.Параметры.НДС = "В т.ч. "+Стр.СтавкаНДС;
			оИтогоНДС.Параметры.ВсегоНДС = Стр.СуммаНДС;
			Таб.Вывести(оИтогоНДС);
		КонецЦикла;
	КонецЕсли;
	
	ОбластьИтогоКОплате = Макет.ПолучитьОбласть("ИтогоКОплате");
	ОбластьИтогоКОплате.Параметры.ИтогоКОплате = ТЗ.Итог("Сумма");
	Таб.Вывести(ОбластьИтогоКОплате);
	
	ОбластьСуммаПрописью = Макет.ПолучитьОбласть("СуммаПрописью");
	//ОбластьСуммаПрописью.Параметры.ИтоговаяСтрока = "Всего наименований " + ТЗ.Количество() + ", на сумму " + ТЗ.Итог("Сумма") + " руб.";
	ОбластьСуммаПрописью.Параметры.СуммаПрописью = Справочники.Валюты.СформироватьСуммуПрописью(ТЗ.Итог("Сумма"), Константы.ВалютаРегламентированногоУчета.Получить(), Перечисления.Локализации.fr_CA);
	Таб.Вывести(ОбластьСуммаПрописью);
	
	ОбластьПодвалСчета = макет.ПолучитьОбласть("ПодвалСчета");
	Таб.Вывести(ОбластьПодвалСчета);
	Таб.ОтображатьСетку = Ложь;
	Таб.ОтображатьЗаголовки = Ложь; 
	Таб.ВывестиГоризонтальныйРазделительСтраниц();
КонецПроцедуры

Процедура ПечатьАктаОбОказанииУслуг(Док, Таб) Экспорт
	УстановитьПривилегированныйРежим(Истина);
	Таб.ОтображатьСетку = Ложь;
	Таб.ОтображатьЗаголовки = Ложь;
	Таб.ОриентацияСтраницы = ОриентацияСтраницы.Портрет;
	Таб.АвтоМасштаб = Истина;
	Таб.КлючПараметровПечати = "Параметры_печати_Документ_НалоговаяНакладная_АктОбОказанииУслуг";
	Макет = ПолучитьОбщийМакет("АктОбОказанииУслуг");	
	оЗаголовок = Макет.ПолучитьОбласть("Заголовок");
	оЗаголовок.Параметры.ТекстЗаголовка = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Акт");
	Таб.Вывести(оЗаголовок);
	оПоставщик = Макет.ПолучитьОбласть("Поставщик");	
	оПоставщик.Параметры.ПредставлениеПоставщика = Док.Организация;
	Таб.Вывести(оПоставщик);
	оПолучатель = Макет.ПолучитьОбласть("Получатель");	
	оПолучатель.Параметры.ПредставлениеПолучателя = Док.Контрагент;
	оПолучатель.Параметры.Основание = Док.Договор;
	Таб.Вывести(оПолучатель);
	Таб.Вывести(Макет.ПолучитьОбласть("ШапкаТаблицы"));
	ТЗ = Док.ТЧУслуги.Выгрузить();	
	Для Каждого Стр Из ТЗ Цикл
		оСтрока = Макет.ПолучитьОбласть("Строка"); 
		оСтрока.Параметры.Заполнить(Стр);
		оСтрока.Параметры.Номенклатура = ОбщегоНазначенияКлиентСервер.ПредставлениеНоменклатуры(Стр.Номенклатура, Стр.Содержание);
		оСтрока.Параметры.ЕдиницаИзмерения = Стр.Номенклатура.Единица;
		Таб.Вывести(оСтрока);
	КонецЦикла;
	ОИтого = Макет.ПолучитьОбласть("Итого");
	ОИтого.Параметры.Всего = ТЗ.Итог("Сумма");
	Таб.Вывести(ОИтого);
	оИтогоНДС = Макет.ПолучитьОбласть("ИтогоНДС");
	оИтогоНДС.Параметры.НДС = "Сумма НДС";
	оИтогоНДС.Параметры.ВсегоНДС = ТЗ.Итог("СуммаНДС");
	Таб.Вывести(оИтогоНДС);
	ОСуммаПрописью = Макет.ПолучитьОбласть("СуммаПрописью");
	ОСуммаПрописью.Параметры.ИтоговаяСтрока = "Всего наименований " + ТЗ.Количество() 
	+ ", на сумму " + ТЗ.Итог("Сумма") + " руб.";
	ОСуммаПрописью.Параметры.СуммаПрописью = Справочники.Валюты.СформироватьСуммуПрописью(ТЗ.Итог("Сумма"),Константы.ВалютаРегламентированногоУчета.Получить(), Перечисления.Локализации.fr_CA);
	Таб.Вывести(ОСуммаПрописью);
	
	ОПодписи = Макет.ПолучитьОбласть("Подписи");
	ОПодписи.Параметры.НазваниеОрганизации = Док.Организация;
	ОПодписи.Параметры.НазваниеЗаказчика = Док.Контрагент;
	Таб.Вывести(ОПодписи);
	Таб.ВывестиГоризонтальныйРазделительСтраниц();
	Таб.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Акт");
КонецПроцедуры

Function PrintFacture(Док, Spreadsheet) Export
	//{{_PRINT_WIZARD(Печать)
	//Template = Documents.FactureSortie.GetTemplate(TemplateName);
	//TableName = Ref.MetaData().Name;
	Template = Документы.НалоговаяНакладная.ПолучитьМакет("Facture");
	Query = New Query;
	Query.Text =
	"ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент КАК Client,
	|	Doc.Ссылка.Ответственный КАК Createur,
	|	Doc.Ссылка.Дата КАК Date,
	|	Doc.Ссылка.Номер КАК Number,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов КАК Devise,
	|	Doc.Ссылка.Сумма КАК TotalSomme,
	|	Doc.Ссылка.СуммаНДС КАК TotalSommeTVA,
	|	Doc.Ссылка.Ссылка КАК DocRef,
	|	Doc.НомерСтроки КАК LineNumber,
	|	Doc.Номенклатура КАК Produit,
	|	Doc.Количество КАК Quantite,
	|	Doc.Цена КАК Prix,
	|	Doc.СтавкаНДС КАК TVA,
	|	Doc.СуммаНДС КАК SommeTVA,
	|	Doc.СуммаСкидки КАК Remise,
	|	Doc.Сумма КАК Somme,
	|	Doc.СуммаСНДС КАК SommeTotale,
	|	Doc.Ссылка.Организация КАК Organisation,
	|	Doc.Ссылка.Основание КАК Основание,
	|	Doc.Ссылка КАК Ссылка
	|ИЗ
	|	Документ.НалоговаяНакладная.ТЧТовары КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|
	|ОБЪЕДИНИТЬ ВСЕ
	|
	|ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент,
	|	Doc.Ссылка.Ответственный,
	|	Doc.Ссылка.Дата,
	|	Doc.Ссылка.Номер,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов,
	|	Doc.Ссылка.Сумма,
	|	Doc.Ссылка.СуммаНДС,
	|	Doc.Ссылка.Ссылка,
	|	0,
	|	Doc.Номенклатура,
	|	Doc.Количество,
	|	Doc.Цена,
	|	Doc.СтавкаНДС,
	|	Doc.СуммаНДС,
	|	0,
	|	Doc.Сумма,
	|	Doc.СуммаСНДС,
	|	Doc.Ссылка.Организация,
	|	Doc.Ссылка.Основание,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.НалоговаяНакладная.ТЧУслуги КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|
	|ОБЪЕДИНИТЬ ВСЕ
	|
	|ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент,
	|	Doc.Ссылка.Ответственный,
	|	Doc.Ссылка.Дата,
	|	Doc.Ссылка.Номер,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов,
	|	Doc.Ссылка.Сумма,
	|	0,
	|	Doc.Ссылка.Ссылка,
	|	0,
	|	Doc.Номенклатура,
	|	Doc.Количество,
	|	Doc.Цена,
	|	Doc.СтавкаНДС,
	|	Doc.СуммаНДС,
	|	0,
	|	Doc.Сумма,
	|	Doc.СуммаСНДС,
	|	Doc.Ссылка.Организация,
	|	Doc.Ссылка.Основание,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.ВозвратОтПокупателя.ТЧТовары КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|
	|ОБЪЕДИНИТЬ ВСЕ
	|
	|ВЫБРАТЬ
	|	ЗаказПокупателяТЧТовары.Ссылка.Контрагент,
	|	ЗаказПокупателяТЧТовары.Ссылка.Ответственный,
	|	ЗаказПокупателяТЧТовары.Ссылка.Дата,
	|	ЗаказПокупателяТЧТовары.Ссылка.Номер,
	|	ЗаказПокупателяТЧТовары.Ссылка.Договор.ВалютаВзаиморасчётов,
	|	ЗаказПокупателяТЧТовары.Ссылка.Сумма,
	|	0,
	|	ЗаказПокупателяТЧТовары.Ссылка.Ссылка,
	|	0,
	|	ЗаказПокупателяТЧТовары.Номенклатура,
	|	ЗаказПокупателяТЧТовары.Количество,
	|	ЗаказПокупателяТЧТовары.Цена,
	|	ЗаказПокупателяТЧТовары.СтавкаНДС,
	|	ЗаказПокупателяТЧТовары.СуммаНДС,
	|	0,
	|	ЗаказПокупателяТЧТовары.Сумма,
	|	ЗаказПокупателяТЧТовары.СуммаСНДС,
	|	ЗаказПокупателяТЧТовары.Ссылка.Организация,
	|	NULL,
	|	ЗаказПокупателяТЧТовары.Ссылка
	|ИЗ
	|	Документ.ЗаказПокупателя.ТЧТовары КАК ЗаказПокупателяТЧТовары
	|ГДЕ
	|	ЗаказПокупателяТЧТовары.Ссылка = &Ref
	|ИТОГИ ПО
	|	Ссылка";
	Query.Parameters.Insert("Ref", Док);
	Selection = Query.Execute().Select(ОбходРезультатаЗапроса.ПоГруппировкам);

	//AreaCaption = Template.GetArea("Caption");
	Header = Template.GetArea("Header");
	AreaTabularSectionHeader = Template.GetArea("TabularSectionHeader");
	AreaTabularSection = Template.GetArea("TabularSection");
	AreaTabularSectionFooterSousTotal = Template.GetArea("TabularSectionFooterSousTotal");
	AreaTabularSectionFooterRemise = Template.GetArea("TabularSectionFooterRemise");
	AreaTabularSectionFooterTotal = Template.GetArea("TabularSectionFooterTotal"); 
	AreaTabularSectionFooterTotalTaxe = Template.GetArea("TabularSectionFooterTotalTaxe"); 
	//AreaTabularSectionEmpty = Template.GetArea("TabularSectionEmpty");
	//Spreadsheet = New SpreadsheetDocument;
	
	InsertPageBreak = False;
	While Selection.Next() Do
		//If InsertPageBreak Then
		//	Spreadsheet.PutHorizontalPageBreak();
		//EndIf;

		FirstRowNumber = Spreadsheet.TableHeight + 1;
		//StrNumber = 11;
		Header.Parameters.Fill(Selection);
		FactureTitle = "";
		Если ТипЗНЧ(Selection.Ссылка) = Тип("ДокументСсылка.ВозвратОтПокупателя") Тогда 
			FactureTitle = "Avoir № ";
		ИначеЕсли ТипЗНЧ(Selection.Ссылка) = Тип("ДокументСсылка.ЗаказПокупателя") Тогда
			FactureTitle = "Devis № ";
		Иначе
			FactureTitle = "Facture № ";
		КонецЕсли;
		Header.Parameters.Facture = FactureTitle + Selection.Number;
		
		If Selection.Organisation <> Catalogs.Организации.EmptyRef() Then 
			FieldPhoto = Selection.Organisation.Логотип.Get();
			Try
				Header.Drawings[0].Picture = New Picture(FieldPhoto);
			Except
			EndTry;
		EndIf;
		
    	OrganisationCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Organisation, Док.Дата);
		Organisation = ""+Selection.Organisation.Description+", "+OrganisationCard.АдресЮридический + "
		|Tel: "+OrganisationCard.Телефоны+",  e-mail: "+OrganisationCard.Реквизиты.email;
		
		Если ЗначениеЗаполнено(OrganisationCard.БанковскийСчётОсновной.НомерСчёта) Тогда 
			Banque = ""+OrganisationCard.БанковскийСчётОсновной.Банк+", "+OrganisationCard.БанковскийСчётОсновной.Банк.Адрес + "
			|Numero de compte: "+OrganisationCard.БанковскийСчётОсновной.НомерСчёта;
		Иначе
			Banque = "";
		КонецЕсли;
		
    	ClientCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Client, Док.Дата);
		Client = ""+Selection.Client.Description;
		Если ЗначениеЗаполнено(ClientCard.Реквизиты.ICE) Тогда 
			Client = Client +", ICE: "+ClientCard.Реквизиты.ICE;
		КонецЕсли;
		Если ЗначениеЗаполнено(ClientCard.Реквизиты.АдресДоставки) Тогда 
			Client = Client +", "+ClientCard.Реквизиты.АдресДоставки;
		КонецЕсли;
		Если ЗначениеЗаполнено(ClientCard.Телефоны) Тогда 
			Client = Client +"
			|Tel: "+ClientCard.Телефоны;
		КонецЕсли;
		
		VT = РегистрыНакопления.ВзаиморасчётыСПокупателями.GetTableOfPayments(Selection.DocRef);
		If VT.Count() = 0 OR VT.Total("Somme") > 0 Then
			PaiementStatus = ВРЕГ("NON PAYéE");
		Else
			PaiementStatus = ВРЕГ("PAYéE");
		EndIf;
		MethodeDePaiement = "Méthode De Paiement: ";
		If VT.Count() = 0 Then
			MethodeDePaiement = MethodeDePaiement + "
			|Virement bancaire";
		Else
			For Each StrVT in VT do
				If Not ValueIsFilled(StrVT.TypesDePayment) then continue; EndIf;
				MethodeDePaiement = MethodeDePaiement + "
				|"+StrVT.TypesDePayment;
			EndDo;
		endif;
		//Header.Parameters.PaiementStatus = PaiementStatus;
		Header.Parameters.MethodeDePaiement = MethodeDePaiement;
		
		Header.Parameters.Date = Format(Selection.Date,"DLF = 'DD'; Л = 'en'");
		//Header.Parameters.Organisation = Organisation;
		//Header.Parameters.Banque = Banque;
		//TextBonDeCommande = "";
		//BonDeCommande = "";
		//If GetFunctionalOption("FunctionalOptionUtiliserCommandeDuClient") And ValueIsFilled(Selection.CommandeDuClient) Then 
		//	TextBonDeCommande = "Bon de commande: ";
		//	If ValueIsFilled(Selection.CommandeDuClient.NumeroClient) Then 
		//		BonDeCommande = "" + Selection.CommandeDuClient.NumeroClient + " de "+ Format(Selection.CommandeDuClient.DateClient,"DLF = 'DD'; Л = 'en'");
		//	Else
		//		BonDeCommande = "" + Selection.CommandeDuClient.Numero + " de "+ Format(Selection.CommandeDuClient.Date,"DLF = 'DD'; Л = 'en'");
		//	EndIf;
		//EndIf;	
		//Header.Parameters.TextBonDeCommande = TextBonDeCommande;
		//Header.Parameters.BonDeCommande = BonDeCommande;
		Header.Parameters.Client = Client;
		Spreadsheet.Put(Header, Selection.Level());
		
		TotalRemise = 0;
		TotalSomme = 0;

		//AreaTabularSectionHeader.Parameters.DetailsParameter = "";
		//AreaTabularSectionHeader.Parameters.Devise = Selection.Devise;
		Spreadsheet.Put(AreaTabularSectionHeader);
		SelectionTabularSection = Selection.Select();
		While SelectionTabularSection.Next() Do
			AreaTabularSection.Parameters.Fill(SelectionTabularSection);
			AreaTabularSection.Parameters.Descriptif = ОбщегоНазначенияКлиентСервер.ПредставлениеНоменклатуры(SelectionTabularSection.Produit,"");
			AreaTabularSection.Parameters.Prix = SelectionTabularSection.Prix;
			AreaTabularSection.Parameters.TauxTVA = SelectionTabularSection.TVA;
			AreaTabularSection.Parameters.TVA = SelectionTabularSection.SommeTVA;
			//AreaTabularSection.Parameters.DetailsParameter = ""; 
			МасОбластей = Новый Массив;
			МасОбластей.Добавить(AreaTabularSection);
			МасОбластей.Добавить(AreaTabularSectionFooterSousTotal);
			МасОбластей.Добавить(AreaTabularSectionFooterTotalTaxe);
			МасОбластей.Добавить(AreaTabularSectionFooterTotal);
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда 
				Spreadsheet.ВывестиГоризонтальныйРазделительСтраниц();
				Spreadsheet.Put(AreaTabularSectionHeader);
			КонецЕсли;
			Spreadsheet.Put(AreaTabularSection, SelectionTabularSection.Level());
			TotalRemise = TotalRemise + SelectionTabularSection.Remise;
			TotalSomme = TotalSomme + SelectionTabularSection.Somme;
			//StrNumber = StrNumber - 1;
		EndDo;
		
		AreaTabularSectionFooterSousTotal.Parameters.SousTotal = ""+Format(TotalSomme,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		//AreaTabularSectionFooterSousTotal.Parameters.DetailsParameter = "";
		Spreadsheet.Put(AreaTabularSectionFooterSousTotal);
		If TotalRemise <> 0 Then 
			AreaTabularSectionFooterRemise.Parameters.Remise = ""+Format(TotalRemise,"NFD=2; NZ=0,00")+" "+Selection.Devise;
			//AreaTabularSectionFooterRemise.Parameters.DetailsParameter = "";
			Spreadsheet.Put(AreaTabularSectionFooterRemise);
		EndIf;
		
		AreaTabularSectionFooterTotalTaxe.Parameters.TotalTaxe = ""+Format(Selection.TotalSommeTVA,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		//AreaTabularSectionFooterTotalTaxe.Parameters.DetailsParameter = "";
		Spreadsheet.Put(AreaTabularSectionFooterTotalTaxe);
		
		AreaTabularSectionFooterTotal.Parameters.Total = ""+Format(Selection.TotalSomme,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		//AreaTabularSectionFooterTotal.Parameters.DetailsParameter = "Spreadsheet";
		Spreadsheet.Put(AreaTabularSectionFooterTotal);
		//StrNumber = StrNumber - 1;
		
		//If StrNumber > 0 Then
		//	For CurStrNumber = 1 to StrNumber do
		//		Spreadsheet.Put(AreaTabularSectionEmpty);
		//	EndDo;
		//EndIf;
		Capital = ?(ValueIsFilled(OrganisationCard.Реквизиты.УставныйКапитал)," ● Capital " + OrganisationCard.Реквизиты.УставныйКапитал + " dirhams","");
		Footer = ""+Selection.Organisation.Description + Capital + " ● " + OrganisationCard.АдресЮридический;
		FooterAdd = "";
		If ValueIsFilled(OrganisationCard.Реквизиты.RC) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd + "RC " + СокрЛП(OrganisationCard.Реквизиты.RC);
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.TaxeProfessionnelle) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "Patente " + СокрЛП(OrganisationCard.Реквизиты.TaxeProfessionnelle);
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.NIF) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "IF " + СокрЛП(OrganisationCard.Реквизиты.NIF);
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.CNSS) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "CNSS " + СокрЛП(OrganisationCard.Реквизиты.CNSS);
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.ICE) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "ICE " + СокрЛП(OrganisationCard.Реквизиты.ICE);
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.Web) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "Site " + СокрЛП(OrganisationCard.Реквизиты.Web);
		EndIf;
		
		If FooterAdd <> "" Then 
			Footer = Footer + "
			|" + FooterAdd;
		EndIf;
		
		Spreadsheet.Footer.StartPage = 1;
		Spreadsheet.Footer.CenterText = Footer;
		Spreadsheet.Footer.Enabled = Истина;
		Spreadsheet.FooterSize = 10;
		
		Spreadsheet.BottomMargin = 10;
		
		//InsertPageBreak = True;
		Spreadsheet.PutHorizontalPageBreak();
		//PrintManagement.SetDocumentPrintArea(Spreadsheet, FirstRowNumber, PrintObjects, Selection.DocRef);
	EndDo; 
	
	Return Spreadsheet;
	
	//}}
EndFunction

Function PrintTicket(Док, Spreadsheet) Export
	//{{_PRINT_WIZARD(Печать)
	//Template = Documents.FactureSortie.GetTemplate(TemplateName);
	//TableName = Ref.MetaData().Name;
	Template = Документы.НалоговаяНакладная.ПолучитьМакет("Чек");
	Query = New Query;
	Query.Text =
	"ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент КАК Client,
	|	Doc.Ссылка.Ответственный КАК Createur,
	|	Doc.Ссылка.Дата КАК Date,
	|	Doc.Ссылка.Номер КАК Number,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов КАК Devise,
	|	Doc.Ссылка.Сумма КАК TotalSomme,
	|	Doc.Ссылка.СуммаНДС КАК TotalSommeTVA,
	|	Doc.Ссылка.Ссылка КАК DocRef,
	|	Doc.КодСтроки КАК LineNumber,
	|	Doc.Номенклатура КАК Produit,
	|	Doc.Количество КАК Quantite,
	|	Doc.Цена КАК Prix,
	|	Doc.СтавкаНДС КАК TVA,
	|	Doc.СуммаНДС КАК SommeTVA,
	|	Doc.СуммаСкидки КАК Remise,
	|	Doc.Сумма КАК Somme,
	|	Doc.СуммаСНДС КАК SommeTotale,
	|	Doc.Ссылка.Организация КАК Organisation,
	|	Doc.Ссылка.Основание КАК Основание,
	|	Doc.Ссылка КАК Ссылка
	|ИЗ
	|	Документ.НалоговаяНакладная.ТЧТовары КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|
	|ОБЪЕДИНИТЬ ВСЕ
	|
	|ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент,
	|	Doc.Ссылка.Ответственный,
	|	Doc.Ссылка.Дата,
	|	Doc.Ссылка.Номер,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов,
	|	Doc.Ссылка.Сумма,
	|	Doc.Ссылка.СуммаНДС,
	|	Doc.Ссылка.Ссылка,
	|	0,
	|	Doc.Номенклатура,
	|	Doc.Количество,
	|	Doc.Цена,
	|	Doc.СтавкаНДС,
	|	Doc.СуммаНДС,
	|	0,
	|	Doc.Сумма,
	|	Doc.СуммаСНДС,
	|	Doc.Ссылка.Организация,
	|	Doc.Ссылка.Основание,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.НалоговаяНакладная.ТЧУслуги КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|ИТОГИ ПО
	|	Ссылка";
	Query.Parameters.Insert("Ref", Док);
	Selection = Query.Execute().Select(ОбходРезультатаЗапроса.ПоГруппировкам);

	//AreaCaption = Template.GetArea("Caption");
	Header = Template.GetArea("Шапка");
	AreaTabularSection = Template.GetArea("Строка");
	AreaTabularSectionFooterTotal = Template.GetArea("Подвал"); 
	
	InsertPageBreak = False;
	While Selection.Next() Do
		//If InsertPageBreak Then
		//	Spreadsheet.PutHorizontalPageBreak();
		//EndIf;

		FirstRowNumber = Spreadsheet.TableHeight + 1;
		//StrNumber = 11;
		Header.Parameters.Fill(Selection);
		Header.Parameters.TypeDeTicket = ?(Selection.DocRef.ХозяйственнаяОперация = Перечисления.ХозяйственныеОперации.ПродажаВКредит,"CREDIT","VENTE");
		
		If Selection.Organisation <> Catalogs.Организации.EmptyRef() Then 
			FieldPhoto = Selection.Organisation.Логотип.Get();
			Try
				Header.Drawings[0].Picture = New Picture(FieldPhoto);
			Except
			EndTry;
		EndIf;
		
		
		VT = РегистрыНакопления.ВзаиморасчётыСПокупателями.GetTableOfPayments(Selection.DocRef);
		TotalSommePaiementBA = 0;
		СтрСертификат = VT.Найти(Справочники.TypesDePayment.Сертификат);
		Если Не СтрСертификат = Неопределено Тогда 
			TotalSommePaiementBA = СтрСертификат.Somme;
		КонецЕсли;
		TotalSommePaiement = VT.Total("Somme") - TotalSommePaiementBA;
		Spreadsheet.Put(Header, Selection.Level());
		
		TotalSomme = 0;

		SelectionTabularSection = Selection.Select();
		While SelectionTabularSection.Next() Do
			AreaTabularSection.Parameters.Fill(SelectionTabularSection);
			AreaTabularSection.Parameters.Code = SelectionTabularSection.Produit.Артикул;
			AreaTabularSection.Parameters.Descriptif = SelectionTabularSection.Produit.Наименование;
			AreaTabularSection.Parameters.Prix = SelectionTabularSection.Prix;
			Spreadsheet.Put(AreaTabularSection, SelectionTabularSection.Level());
			TotalSomme = TotalSomme + SelectionTabularSection.Somme;
			//StrNumber = StrNumber - 1;
		EndDo;
		
		AreaTabularSectionFooterTotal.Parameters.Total = ""+Format(Selection.TotalSomme,"ЧДЦ=2; ЧРГ=' '; ЧН=0,00");
		AreaTabularSectionFooterTotal.Parameters.НадписьСертификат =  ?(TotalSommePaiementBA = 0, "", "Règlé par BA:");
		Если Не TotalSommePaiementBA = 0 Тогда 
			AreaTabularSectionFooterTotal.Parameters.TotalSommePaiementBA =  ""+Format(TotalSommePaiementBA,"ЧДЦ=2; ЧРГ=' '; ЧН=0,00");
		КонецЕсли;
		AreaTabularSectionFooterTotal.Parameters.TotalSommePaiement =  ""+Format(TotalSommePaiement,"ЧДЦ=2; ЧРГ=' '; ЧН=0,00");
		AreaTabularSectionFooterTotal.Parameters.ОстатокОплаты =  ""+Format(Selection.TotalSomme - TotalSommePaiement - TotalSommePaiementBA,"ЧДЦ=2; ЧРГ=' '; ЧН=0,00");
		
		//Spreadsheet.BottomMargin = 20;
			ПараметрыШтрихкода = ГенерацияШтрихкода.ПараметрыГенерацииШтрихкода();
			ПараметрыШтрихкода.УровеньКоррекцииQR = 0;
			ПараметрыШтрихкода.Штрихкод = Selection.Ссылка.УникальныйИдентификатор();
			ПараметрыШтрихкода.УбратьЛишнийФон = Истина;
			ПараметрыШтрихкода.ТипКода  = 16; //QR
			ПараметрыШтрихкода.Ширина = 40;
			ПараметрыШтрихкода.Высота = 40;
			
			Штрихкод = AreaTabularSectionFooterTotal.Рисунки.QRcode;
			Штрихкод.РазмерКартинки = РазмерКартинки.Пропорционально;
			
			Изображение = ГенерацияШтрихкода.ИзображениеШтрихкода(ПараметрыШтрихкода);
			Если Изображение = Неопределено Тогда
				Штрихкод.Картинка = Новый Картинка;
			Иначе
				Штрихкод.Картинка = Изображение.Картинка;
			КонецЕсли;
			Штрихкод.ГраницаСверху = Ложь;
			Штрихкод.ГраницаСнизу  = Ложь;
			Штрихкод.ГраницаСправа = Ложь;
			Штрихкод.ГраницаСлева  = Ложь;
		
		Spreadsheet.Put(AreaTabularSectionFooterTotal);
		//InsertPageBreak = True;
		Spreadsheet.PutHorizontalPageBreak();
		//PrintManagement.SetDocumentPrintArea(Spreadsheet, FirstRowNumber, PrintObjects, Selection.DocRef);
	EndDo; 
	
	Return Spreadsheet;
	
	//}}
EndFunction

Function PrintBonDeLivtaison(Док, Spreadsheet) Export
	//{{_PRINT_WIZARD(Печать)
	//Template = Documents.FactureSortie.GetTemplate(TemplateName);
	//TableName = Ref.MetaData().Name;
	Template = Документы.ОтгрузкаТовара.ПолучитьМакет("ОтгрузкаТовара");
	Query = New Query;
	Query.Text =
	"ВЫБРАТЬ
	|	Doc.Контрагент КАК Client,
	|	Doc.Ответственный КАК Createur,
	|	Doc.Дата КАК Date,
	|	Doc.Номер КАК Number,
	|	Doc.Договор.ВалютаВзаиморасчётов КАК Devise,
	|	Doc.Сумма КАК Somme,
	|	Doc.СуммаНДС КАК SommeTVA,
	|	Doc.Ссылка КАК DocRef,
	|	Doc.ТЧТовары.(
	|		КодСтроки КАК LineNumber,
	|		Номенклатура КАК Produit,
	|		Количество КАК Quantite,
	|		Цена КАК Prix,
	|		СтавкаНДС КАК TVA,
	|		СуммаНДС КАК SommeTVA,
	|		СуммаСкидки КАК Remise,
	|		Сумма КАК Somme,
	|		СуммаСНДС КАК SommeTotale
	|	) КАК TabularSection,
	|	Doc.Организация КАК Organisation,
	|	Doc.Основание КАК Основание
	|ИЗ
	|	Документ.ОтгрузкаТовара КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref";
	Query.Parameters.Insert("Ref", Док);
	Selection = Query.Execute().Select();

	//AreaCaption = Template.GetArea("Caption");
	Header = Template.GetArea("Header");
	AreaTabularSectionHeader = Template.GetArea("TabularSectionHeader");
	AreaTabularSection = Template.GetArea("TabularSection");
	AreaTabularSectionFooterSousTotal = Template.GetArea("TabularSectionFooterSousTotal");
	AreaTabularSectionFooterRemise = Template.GetArea("TabularSectionFooterRemise");
	AreaTabularSectionFooterTotal = Template.GetArea("TabularSectionFooterTotal"); 
	AreaTabularSectionFooterTotalTaxe = Template.GetArea("TabularSectionFooterTotalTaxe"); 
	//AreaTabularSectionEmpty = Template.GetArea("TabularSectionEmpty");
	//Spreadsheet = New SpreadsheetDocument;
	
	InsertPageBreak = False;
	While Selection.Next() Do
		//If InsertPageBreak Then
		//	Spreadsheet.PutHorizontalPageBreak();
		//EndIf;

		FirstRowNumber = Spreadsheet.TableHeight + 1;
		//StrNumber = 11;
		Header.Parameters.Fill(Selection);
		//Header.Parameters.DetailsParameter = "";
		
		If Selection.Organisation <> Catalogs.Организации.EmptyRef() Then 
			FieldPhoto = Selection.Organisation.Логотип.Get();
			Try
				Header.Drawings[0].Picture = New Picture(FieldPhoto);
			Except
			EndTry;
		EndIf;
		
    	OrganisationCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Organisation, Док.Дата);
		Organisation = ""+Selection.Organisation.Description+", "+OrganisationCard.АдресЮридический + "
		|Tel: "+OrganisationCard.Телефоны+",  e-mail: "+OrganisationCard.Реквизиты.email;
		
		//Banque = ""+OrganisationCard.БанковскийСчётОсновной.Банк+", "+OrganisationCard.БанковскийСчётОсновной.Банк.Адрес + "
		//|Numero de compte: "+OrganisationCard.БанковскийСчётОсновной.НомерСчёта;
		
    	ClientCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Client, Док.Дата);
		Client = ""+Selection.Client.Description+"
		|ICE: "+ClientCard.Реквизиты.ICE;
		
		//VT = РегистрыНакопления.ВзаиморасчётыСПокупателями.GetTableOfPayments(Selection.DocRef);
		//If VT.Count() = 0 OR VT.Total("Somme") > 0 Then
		//	PaiementStatus = ВРЕГ("NON PAYéE");
		//Else
		//	PaiementStatus = ВРЕГ("PAYéE");
		//EndIf;
		//MethodeDePaiement = "Méthode De Paiement: ";
		//If VT.Count() = 0 Then
		//	MethodeDePaiement = MethodeDePaiement + "
		//	|Virement bancaire";
		//Else
		//	For Each StrVT in VT do
		//		If Not ValueIsFilled(StrVT.TypesDePayment) then continue; EndIf;
		//		MethodeDePaiement = MethodeDePaiement + "
		//		|"+StrVT.TypesDePayment;
		//	EndDo;
		//endif;
		//Header.Parameters.PaiementStatus = PaiementStatus;
		//Header.Parameters.MethodeDePaiement = MethodeDePaiement;
		
		Header.Parameters.Date = Format(Selection.Date,"DLF = 'DD'; Л = 'en'");
		Header.Parameters.Organisation = Organisation;
		//Header.Parameters.Banque = Banque;
		TextBonDeCommande = "";
		BonDeCommande = "";
		//If GetFunctionalOption("FunctionalOptionUtiliserCommandeDuClient") And ValueIsFilled(Selection.CommandeDuClient) Then 
		//	TextBonDeCommande = "Bon de commande: ";
		//	If ValueIsFilled(Selection.CommandeDuClient.NumeroClient) Then 
		//		BonDeCommande = "" + Selection.CommandeDuClient.NumeroClient + " de "+ Format(Selection.CommandeDuClient.DateClient,"DLF = 'DD'; Л = 'en'");
		//	Else
		//		BonDeCommande = "" + Selection.CommandeDuClient.Numero + " de "+ Format(Selection.CommandeDuClient.Date,"DLF = 'DD'; Л = 'en'");
		//	EndIf;
		//EndIf;	
		Header.Parameters.TextBonDeCommande = TextBonDeCommande;
		Header.Parameters.BonDeCommande = BonDeCommande;
		Header.Parameters.Client = Client;
		Spreadsheet.Put(Header, Selection.Level());
		
		TotalRemise = 0;
		TotalSomme = 0;

		//AreaTabularSectionHeader.Parameters.DetailsParameter = "";
		//AreaTabularSectionHeader.Parameters.Devise = Selection.Devise;
		Spreadsheet.Put(AreaTabularSectionHeader);
		SelectionTabularSection = Selection.TabularSection.Select();
		While SelectionTabularSection.Next() Do
			AreaTabularSection.Parameters.Fill(SelectionTabularSection);
			AreaTabularSection.Parameters.Descriptif = SelectionTabularSection.Produit.Наименование;
			AreaTabularSection.Parameters.Prix = SelectionTabularSection.Prix;
			AreaTabularSection.Parameters.TauxTVA = SelectionTabularSection.TVA;
			AreaTabularSection.Parameters.TVA = SelectionTabularSection.SommeTVA;
			//AreaTabularSection.Parameters.DetailsParameter = "";
			Spreadsheet.Put(AreaTabularSection, SelectionTabularSection.Level());
			TotalRemise = TotalRemise + SelectionTabularSection.Remise;
			TotalSomme = TotalSomme + SelectionTabularSection.Somme;
			//StrNumber = StrNumber - 1;
		EndDo;
		
		AreaTabularSectionFooterSousTotal.Parameters.SousTotal = ""+Format(TotalSomme,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		//AreaTabularSectionFooterSousTotal.Parameters.DetailsParameter = "";
		Spreadsheet.Put(AreaTabularSectionFooterSousTotal);
		If TotalRemise <> 0 Then 
			AreaTabularSectionFooterRemise.Parameters.Remise = ""+Format(TotalRemise,"NFD=2; NZ=0,00")+" "+Selection.Devise;
			//AreaTabularSectionFooterRemise.Parameters.DetailsParameter = "";
			Spreadsheet.Put(AreaTabularSectionFooterRemise);
		EndIf;
		
		AreaTabularSectionFooterTotalTaxe.Parameters.TotalTaxe = ""+Format(Selection.SommeTVA,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		//AreaTabularSectionFooterTotalTaxe.Parameters.DetailsParameter = "";
		Spreadsheet.Put(AreaTabularSectionFooterTotalTaxe);
		
		AreaTabularSectionFooterTotal.Parameters.Total = ""+Format(Selection.Somme,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		//AreaTabularSectionFooterTotal.Parameters.DetailsParameter = "Spreadsheet";
		Spreadsheet.Put(AreaTabularSectionFooterTotal);
		//StrNumber = StrNumber - 1;
		
		//If StrNumber > 0 Then
		//	For CurStrNumber = 1 to StrNumber do
		//		Spreadsheet.Put(AreaTabularSectionEmpty);
		//	EndDo;
		//EndIf;
		Capital = ?(ValueIsFilled(OrganisationCard.Реквизиты.УставныйКапитал)," ● Capital " + OrganisationCard.Реквизиты.УставныйКапитал + " dirhams","");
		Footer = ""+Selection.Organisation.Description + Capital + " ● " + OrganisationCard.АдресЮридический;
		FooterAdd = "";
		If ValueIsFilled(OrganisationCard.Реквизиты.RC) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd + "RC " + OrganisationCard.Реквизиты.RC;
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.TaxeProfessionnelle) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "Patente " + OrganisationCard.Реквизиты.TaxeProfessionnelle;
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.NIF) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "IF " + OrganisationCard.Реквизиты.NIF;
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.CNSS) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "CNSS " + OrganisationCard.Реквизиты.CNSS;
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.ICE) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "ICE " + OrganisationCard.Реквизиты.ICE;
		EndIf;
		If ValueIsFilled(OrganisationCard.Реквизиты.Web) Then 
			If FooterAdd <> "" Then 
				FooterAdd = FooterAdd + " ● ";
			EndIf;
			FooterAdd = FooterAdd +  "Site " + OrganisationCard.Реквизиты.Web;
		EndIf;
		
		If FooterAdd <> "" Then 
			Footer = Footer + "
			|" + FooterAdd;
		EndIf;
		
		Spreadsheet.Footer.StartPage = 1;
		Spreadsheet.Footer.CenterText = Footer;
		Spreadsheet.Footer.Enabled = Истина;
		Spreadsheet.FooterSize = 10;
		
		Spreadsheet.BottomMargin = 20;
		
		//InsertPageBreak = True;
		Spreadsheet.PutHorizontalPageBreak();
		//PrintManagement.SetDocumentPrintArea(Spreadsheet, FirstRowNumber, PrintObjects, Selection.DocRef);
	EndDo; 
	
	Return Spreadsheet;
	
	//}}
EndFunction

Процедура ОбработкаПолученияФормы(ВидФормы, Параметры, ВыбраннаяФорма, ДополнительнаяИнформация, СтандартнаяОбработка)
	Если ВидФормы = "ФормаОбъекта" Тогда
		СтандартнаяОбработка = Ложь;
		Если ПараметрыСеанса.ПараметрыКлиентаНаСервере.ЭтоМобильныйКлиент Тогда
			ВыбраннаяФорма = "ФормаДокументаМобильныйКлиент";
		Иначе
			ВыбраннаяФорма = "ФормаДокумента";	
		КонецЕсли;	
	ИначеЕсли ВидФормы = "ФормаСписка" Тогда
		СтандартнаяОбработка = Ложь;
		Если ПараметрыСеанса.ПараметрыКлиентаНаСервере.ЭтоМобильныйКлиент Тогда
			ВыбраннаяФорма = "ФормаСпискаМобильныйКлиент";
		Иначе
			ВыбраннаяФорма = "ФормаСписка";	
		КонецЕсли;	
	КонецЕсли;	
КонецПроцедуры

#КонецОбласти
