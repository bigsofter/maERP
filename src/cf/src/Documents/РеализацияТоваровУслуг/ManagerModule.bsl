
#Область Печать

Процедура ПечатьТорг12(Док, Таб) Экспорт
	УстановитьПривилегированныйРежим(Истина);
	ЭтоВозвратПоставщику = ТипЗнч(Док) = Тип("ДокументСсылка.ВозвратПоставщику");
	Таб.ТолькоПросмотр = Истина;
	Таб.ОтображатьЗаголовки = Ложь;
	Таб.ОтображатьСетку = Ложь;
	Таб.ОриентацияСтраницы = ОриентацияСтраницы.Ландшафт;
	Таб.АвтоМасштаб = Истина;
	Таб.КлючПараметровПечати = "Параметры_печати_Документ_РеализацияТоваровУслуг_Торг12";
	ТабФормирование = Новый ТабличныйДокумент;
	ТабФормирование.АвтоМасштаб = Истина;
	ТабФормирование.ОриентацияСтраницы = ОриентацияСтраницы.Ландшафт;
	// Макет
	Макет = Документы.РеализацияТоваровУслуг.ПолучитьМакет("РасходнаяНакладная");
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
	Макет = Документы.РеализацияТоваровУслуг.ПолучитьМакет("Счёт"); 
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
	Таб.КлючПараметровПечати = "Параметры_печати_Документ_РеализацияТоваровУслуг_АктОбОказанииУслуг";
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
		оСтрока.Параметры.Номенклатура = ОбщегоНазначенияКлиентСервер.ПредставлениеНоменклатуры(Стр.Номенклатура, Стр.Содержание, , Истина);
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

Function PrintFactureOld(Док, Spreadsheet) Export
	//{{_PRINT_WIZARD(Печать)
	//Template = Documents.FactureSortie.GetTemplate(TemplateName);
	//TableName = Ref.MetaData().Name;
	Template = Документы.РеализацияТоваровУслуг.ПолучитьМакет("FactureOld");
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
	|	Документ.РеализацияТоваровУслуг.ТЧТовары КАК Doc
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
	|	Документ.РеализацияТоваровУслуг.ТЧУслуги КАК Doc
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
			AreaTabularSection.Parameters.Descriptif = ОбщегоНазначенияКлиентСервер.ПредставлениеНоменклатуры(
				SelectionTabularSection.Produit, "", , Истина);
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
	
	Spreadsheet.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Facture");
	Return Spreadsheet;
	
	//}}
EndFunction

Function PrintFacture(Док, Spreadsheet, СФоном = Ложь) Export
	БезНДС = Док.Контрагент.ПечатьНакладнойЦеныБезНДС;
	Если СФоном Тогда 
		Template = Документы.РеализацияТоваровУслуг.ПолучитьМакет("FactureModelEnTete");
	Иначе
		Template = Документы.РеализацияТоваровУслуг.ПолучитьМакет("FactureModel");
	КонецЕсли;
	//Если СФоном Тогда 
	//	Spreadsheet.ФоноваяКартинка		= Template.Рисунки.ФоновыйРисунок.Картинка;
	//	Spreadsheet.ФиксированныйФон = Истина;
	//КонецЕсли;
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
	|	Doc.Ссылка КАК BL,
	|	Doc.Ссылка КАК Ссылка
	|ИЗ
	|	Документ.РеализацияТоваровУслуг.ТЧТовары КАК Doc
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
	|	Doc.Ссылка,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.РеализацияТоваровУслуг.ТЧУслуги КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|
	|ОБЪЕДИНИТЬ ВСЕ
	|
	|ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент,
	|	Doc.Ссылка.Ответственный,
	|	ВЫБОР
	|		КОГДА Doc.Ссылка.ДатаИнвойса = ДАТАВРЕМЯ(1, 1, 1, 0, 0, 0)
	|			ТОГДА Doc.Ссылка.Дата
	|		ИНАЧЕ Doc.Ссылка.ДатаИнвойса
	|	КОНЕЦ,
	|	Doc.Ссылка.Номер,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов,
	|	Doc.Ссылка.Сумма,
	|	Doc.Ссылка.СуммаНДС,
	|	Doc.Ссылка.Ссылка,
	|	Doc.НомерСтроки,
	|	Doc.Номенклатура,
	|	Doc.Количество,
	|	Doc.Цена,
	|	Doc.СтавкаНДС,
	|	Doc.СуммаНДС,
	|	Doc.СуммаСкидки,
	|	Doc.Сумма,
	|	Doc.СуммаСНДС,
	|	Doc.Ссылка.Организация,
	|	Doc.Ссылка.Основание,
	|	Doc.ОтгрузкаТовара,
	|	Doc.Ссылка
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
	|	ВЫБОР
	|		КОГДА Doc.Ссылка.ДатаИнвойса = ДАТАВРЕМЯ(1, 1, 1, 0, 0, 0)
	|			ТОГДА Doc.Ссылка.Дата
	|		ИНАЧЕ Doc.Ссылка.ДатаИнвойса
	|	КОНЕЦ,
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
	|	Doc.ОтгрузкаТовара,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.НалоговаяНакладная.ТЧУслуги КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|
	|УПОРЯДОЧИТЬ ПО
	|	BL
	|ИТОГИ ПО
	|	Ссылка";
	Query.Parameters.Insert("Ref", Док);
	Selection = Query.Execute().Select(ОбходРезультатаЗапроса.ПоГруппировкам);

	//AreaCaption = Template.GetArea("Caption");
	Header = Template.GetArea("Header");
	AreaTabularSectionHeader = Template.GetArea("TabularSectionHeader");
	AreaTabularSection = Template.GetArea("TabularSection");
	AreaTabularSectionEmptyLine = Template.GetArea("EmptyLine");
	AreaTabularSectionFooterSousTotal = Template.GetArea("TabularSectionFooterSousTotal");
	AreaTabularSectionFooterRemise = Template.GetArea("TabularSectionFooterRemise");
	AreaTabularSectionFooterTotal = Template.GetArea("TabularSectionFooterTotal"); 
	AreaTabularSectionFooterTotalTaxe = Template.GetArea("TabularSectionFooterTotalTaxe");
	AreaTabularSectionAmountInWritten = Template.GetArea("AmountInWritten");
	AreaTabularSectionLineBC = Template.GetArea("LineBC");
	ОбластьПустаяСтрока = Template.GetArea("ОбластьПустаяСтрока");
	Если СФоном Тогда 
		ОбластьНизРеквизиты = Template.GetArea("ОбластьНизРеквизиты");
	КонецЕсли;
	Spreadsheet.РазмерСтраницы = "A4";
	
	InsertPageBreak = False;
	While Selection.Next() Do
	  //FieldPhoto = Selection.Organisation.ФонПечатныхФорм.Get();
	  //  Try
	  //  	Картинка = New Picture(FieldPhoto,Истина);
	  //  	Spreadsheet.ФоноваяКартинка = Картинка;
	  //  Except
	  //  EndTry;
        НомерСтраницы = 1;
		FirstRowNumber = Spreadsheet.TableHeight + 1;
		Header.Parameters.Fill(Selection);
		Header.Parameters.Number = Selection.Number+"/"+Format(Selection.Date,"Л=fr; ДФ=yy; ДЛФ=DD");
		Header.Parameters.Date = Format(Selection.Date,"Л=fr; ДФ=dd/MM/yyyy; ДЛФ=DD");
		
    	ClientCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Client, Док.Дата);
		Client = ""+Selection.Client.Description;
		Если ЗначениеЗаполнено(ClientCard.Реквизиты.АдресФактический) Тогда 
			Client = Client +Символы.ПС+ClientCard.Реквизиты.АдресФактический;
		ИначеЕсли ЗначениеЗаполнено(ClientCard.Реквизиты.АдресЮридический) Тогда 
			Client = Client + Символы.ПС + ClientCard.Реквизиты.АдресЮридический;
		КонецЕсли;
		
		Header.Parameters.Client = Client;
		Header.Parameters.Комментарий = Док.Комментарий;
		Header.Parameters.ICE = ClientCard.Реквизиты.ICE;
		Header.Parameters.CodeClient = Selection.Client.Код;
		Spreadsheet.Put(Header, Selection.Level());
		
		TotalRemise = 0;
		TotalSomme = 0;
        BL = Документы.РеализацияТоваровУслуг.ПустаяСсылка();
		Spreadsheet.Put(AreaTabularSectionHeader);
		SelectionTabularSection = Selection.Select();
		While SelectionTabularSection.Next() Do
			Если Не BL = SelectionTabularSection.BL И ЗначениеЗаполнено(SelectionTabularSection.BL) Тогда
				BL = SelectionTabularSection.BL;
				AreaTabularSectionLineBC.Parameters.BL = "BL: "+РаботаСДокументами.СформироватьЦифровойНомер(BL.Number)+"/"+Format(BL.Date,"Л=fr; ДФ=yy; ДЛФ=DD") + " " + Format(BL.Date,"Л=fr; ДФ=dd/MM/yyyy; ДЛФ=DD");
				Spreadsheet.Put(AreaTabularSectionLineBC);
			КонецЕсли;
			AreaTabularSection.Parameters.Fill(SelectionTabularSection);
			AreaTabularSection.Parameters.ID = SelectionTabularSection.Produit.Артикул;
			AreaTabularSection.Parameters.Descriptif = SelectionTabularSection.Produit;
			AreaTabularSection.Parameters.TauxTVA = SelectionTabularSection.TVA;
			AreaTabularSection.Parameters.TVA = SelectionTabularSection.SommeTVA;
			Если БезНДС Тогда 
				AreaTabularSection.Parameters.Prix = (SelectionTabularSection.SommeTotale - SelectionTabularSection.SommeTVA)/SelectionTabularSection.Quantite;
				AreaTabularSection.Parameters.Somme = SelectionTabularSection.SommeTotale - SelectionTabularSection.SommeTVA;
			КонецЕсли;
			МасОбластей = Новый Массив;
			МасОбластей.Добавить(AreaTabularSection);
			МасОбластей.Добавить(AreaTabularSection);
			//МасОбластей.Добавить(AreaTabularSectionFooterSousTotal);
			//МасОбластей.Добавить(AreaTabularSectionFooterTotalTaxe);
			//МасОбластей.Добавить(AreaTabularSectionFooterTotal);
			//МасОбластей.Добавить(AreaTabularSectionAmountInWritten);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			Если СФоном Тогда 
				МасОбластей.Добавить(ОбластьНизРеквизиты);
			КонецЕсли;
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				МасОбластей = Новый Массив;
				МасОбластей.Добавить(ОбластьПустаяСтрока);
				Если СФоном Тогда 
					МасОбластей.Добавить(ОбластьНизРеквизиты);
				КонецЕсли;
				//Пока Spreadsheet.ПроверитьВывод(МасОбластей) Цикл 
				Для НомерПроверки = 1 по 5 Цикл 
					МасОбластей = Новый Массив;
					МасОбластей.Добавить(ОбластьПустаяСтрока);
					Если СФоном Тогда 
						МасОбластей.Добавить(ОбластьНизРеквизиты);
					КонецЕсли;
					//МасОбластей.Добавить(ОбластьПустаяСтрока);
					//МасОбластей.Добавить(ОбластьПустаяСтрока);
					Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
						Если СФоном Тогда 
							Spreadsheet.Put(ОбластьНизРеквизиты);
						КонецЕсли;
						Прервать;
					иначе
						Spreadsheet.Put(ОбластьПустаяСтрока);
					КонецЕсли;
				КонецЦикла;
				Spreadsheet.ВывестиГоризонтальныйРазделительСтраниц();
				НомерСтраницы = НомерСтраницы + 1;
				//Header.Parameters.PageNumber = НомерСтраницы;
				Spreadsheet.Put(Header, Selection.Level());
				Spreadsheet.Put(AreaTabularSectionHeader, Selection.Level());
			КонецЕсли;
			Spreadsheet.Put(AreaTabularSection, SelectionTabularSection.Level());
			TotalRemise = TotalRemise + SelectionTabularSection.Remise;
			TotalSomme = TotalSomme + SelectionTabularSection.Somme;
		EndDo;
		
		Для НомерПроверки = 1 по 50 Цикл 
			МасОбластей = Новый Массив;
			МасОбластей.Добавить(AreaTabularSection);
			МасОбластей.Добавить(AreaTabularSection);
			МасОбластей.Добавить(AreaTabularSectionFooterSousTotal);
			МасОбластей.Добавить(AreaTabularSectionFooterTotalTaxe);
			МасОбластей.Добавить(AreaTabularSectionFooterTotal);
			МасОбластей.Добавить(AreaTabularSectionAmountInWritten);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			Если СФоном Тогда 
				МасОбластей.Добавить(ОбластьНизРеквизиты);
			КонецЕсли;
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				//Если СФоном Тогда 
				//	Spreadsheet.Put(ОбластьНизРеквизиты);
				//КонецЕсли;
				Прервать;
			иначе
				Spreadsheet.Put(AreaTabularSectionEmptyLine);
			КонецЕсли;
		КонецЦикла;
		
		AreaTabularSectionFooterSousTotal.Parameters.SousTotal = ""+Format(Selection.TotalSomme-Selection.TotalSommeTVA,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		СпособОплаты = РаботаСДокументами.ПолучитьСпособОплаты(Док);
		Если Не ЗначениеЗаполнено(СпособОплаты) Тогда 
			СпособОплаты = Selection.Client.ТипОплаты;
		КонецЕсли;
		AreaTabularSectionFooterSousTotal.Parameters.СпособОплаты = СпособОплаты;
		Spreadsheet.Put(AreaTabularSectionFooterSousTotal);
		If TotalRemise <> 0 Then 
			AreaTabularSectionFooterRemise.Parameters.Remise = ""+Format(TotalRemise,"NFD=2; NZ=0,00")+" "+Selection.Devise;
			Spreadsheet.Put(AreaTabularSectionFooterRemise);
		EndIf;
		
		AreaTabularSectionFooterTotalTaxe.Parameters.TotalTaxe = ""+Format(Selection.TotalSommeTVA,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		Spreadsheet.Put(AreaTabularSectionFooterTotalTaxe);
		
		AreaTabularSectionFooterTotal.Parameters.Total = ""+Format(Selection.TotalSomme,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		Spreadsheet.Put(AreaTabularSectionFooterTotal);
		
		TextAmountInWritten = "Arrêtée la présente facture à la somme de :";
		AmountInWritten = Справочники.Валюты.СформироватьСуммуПрописью(Selection.TotalSomme,Константы.ВалютаРегламентированногоУчета.Получить(),Перечисления.Локализации.fr_CA);
		TextAmountInWritten = TextAmountInWritten + Символы.ПС +" *** "+ ВРег(AmountInWritten) + " *** ";
		AreaTabularSectionAmountInWritten.Параметры.AmountInWritten = TextAmountInWritten;
		Spreadsheet.Put(AreaTabularSectionAmountInWritten);
		
		//Spreadsheet.BottomMargin = 10;
		Для НомерПроверки = 1 по 5 Цикл 
			МасОбластей = Новый Массив;
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			Если СФоном Тогда 
				МасОбластей.Добавить(ОбластьНизРеквизиты);
			КонецЕсли;
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				Прервать;
			иначе
				Spreadsheet.Put(ОбластьПустаяСтрока);
			КонецЕсли;
		КонецЦикла;
		Если СФоном Тогда 
			Spreadsheet.Put(ОбластьНизРеквизиты);
		КонецЕсли;
		
		Spreadsheet.PutHorizontalPageBreak();
	EndDo; 
	
	Spreadsheet.FitToPage = True;
	Spreadsheet.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Facture");
	Return Spreadsheet;
	
EndFunction

Function PrintFactureEnTete(Док, Spreadsheet, СФоном = Ложь) Export
	БезНДС = Док.Контрагент.ПечатьНакладнойЦеныБезНДС;
	Template = Документы.РеализацияТоваровУслуг.ПолучитьМакет("FactureModelEnTete");
	Spreadsheet.ФоноваяКартинка		= Template.Рисунки.ФоновыйРисунок.Картинка;
	//Spreadsheet.ФиксированныйФон = true;
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
	|	Doc.Ссылка КАК BL,
	|	Doc.Ссылка КАК Ссылка
	|ИЗ
	|	Документ.РеализацияТоваровУслуг.ТЧТовары КАК Doc
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
	|	Doc.Ссылка,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.РеализацияТоваровУслуг.ТЧУслуги КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|
	|ОБЪЕДИНИТЬ ВСЕ
	|
	|ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент,
	|	Doc.Ссылка.Ответственный,
	|	ВЫБОР
	|		КОГДА Doc.Ссылка.ДатаИнвойса = ДАТАВРЕМЯ(1, 1, 1, 0, 0, 0)
	|			ТОГДА Doc.Ссылка.Дата
	|		ИНАЧЕ Doc.Ссылка.ДатаИнвойса
	|	КОНЕЦ,
	|	Doc.Ссылка.Номер,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов,
	|	Doc.Ссылка.Сумма,
	|	Doc.Ссылка.СуммаНДС,
	|	Doc.Ссылка.Ссылка,
	|	Doc.НомерСтроки,
	|	Doc.Номенклатура,
	|	Doc.Количество,
	|	Doc.Цена,
	|	Doc.СтавкаНДС,
	|	Doc.СуммаНДС,
	|	Doc.СуммаСкидки,
	|	Doc.Сумма,
	|	Doc.СуммаСНДС,
	|	Doc.Ссылка.Организация,
	|	Doc.Ссылка.Основание,
	|	Doc.ОтгрузкаТовара,
	|	Doc.Ссылка
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
	|	ВЫБОР
	|		КОГДА Doc.Ссылка.ДатаИнвойса = ДАТАВРЕМЯ(1, 1, 1, 0, 0, 0)
	|			ТОГДА Doc.Ссылка.Дата
	|		ИНАЧЕ Doc.Ссылка.ДатаИнвойса
	|	КОНЕЦ,
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
	|	Doc.ОтгрузкаТовара,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.НалоговаяНакладная.ТЧУслуги КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|
	|УПОРЯДОЧИТЬ ПО
	|	BL
	|ИТОГИ ПО
	|	Ссылка";
	Query.Parameters.Insert("Ref", Док);
	Selection = Query.Execute().Select(ОбходРезультатаЗапроса.ПоГруппировкам);

	Header = Template.GetArea("Header");
	AreaTabularSectionHeader = Template.GetArea("TabularSectionHeader");
	AreaTabularSection = Template.GetArea("TabularSection");
	AreaTabularSectionEmptyLine = Template.GetArea("EmptyLine");
	AreaTabularSectionFooterSousTotal = Template.GetArea("TabularSectionFooterSousTotal");
	AreaTabularSectionFooterRemise = Template.GetArea("TabularSectionFooterRemise");
	AreaTabularSectionFooterTotal = Template.GetArea("TabularSectionFooterTotal"); 
	AreaTabularSectionFooterTotalTaxe = Template.GetArea("TabularSectionFooterTotalTaxe");
	AreaTabularSectionAmountInWritten = Template.GetArea("AmountInWritten");
	AreaTabularSectionLineBC = Template.GetArea("LineBC");
	ОбластьПустаяСтрока = Template.GetArea("ОбластьПустаяСтрока");
	ОбластьНизРеквизиты = Template.GetArea("ОбластьНизРеквизиты");
	Spreadsheet.РазмерСтраницы = "A4";
	
	InsertPageBreak = False;
	While Selection.Next() Do
        НомерСтраницы = 1;
		FirstRowNumber = Spreadsheet.TableHeight + 1;
		Header.Parameters.Fill(Selection);
		Header.Parameters.Number = Selection.Number+"/"+Format(Selection.Date,"Л=fr; ДФ=yy; ДЛФ=DD");
		Header.Parameters.Date = Format(Selection.Date,"Л=fr; ДФ=dd/MM/yyyy; ДЛФ=DD");
		
    	ClientCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Client, Док.Дата);
		Client = ""+Selection.Client.Description;
		Если ЗначениеЗаполнено(ClientCard.Реквизиты.АдресФактический) Тогда 
			Client = Client +Символы.ПС+ClientCard.Реквизиты.АдресФактический;
		ИначеЕсли ЗначениеЗаполнено(ClientCard.Реквизиты.АдресЮридический) Тогда 
			Client = Client + Символы.ПС + ClientCard.Реквизиты.АдресЮридический;
		КонецЕсли;
		
		Header.Parameters.Client = Client;
		Header.Parameters.Комментарий = Док.Комментарий;
		Header.Parameters.ICE = ClientCard.Реквизиты.ICE;
		Header.Parameters.CodeClient = Selection.Client.Код;
		Spreadsheet.Put(Header, Selection.Level());
		
		TotalRemise = 0;
		TotalSomme = 0;
        BL = Документы.РеализацияТоваровУслуг.ПустаяСсылка();
		Spreadsheet.Put(AreaTabularSectionHeader);
		SelectionTabularSection = Selection.Select();
		While SelectionTabularSection.Next() Do
			Если Не BL = SelectionTabularSection.BL И ЗначениеЗаполнено(SelectionTabularSection.BL) Тогда
				BL = SelectionTabularSection.BL;
				AreaTabularSectionLineBC.Parameters.BL = "BL: "+РаботаСДокументами.СформироватьЦифровойНомер(BL.Number)+"/"+Format(BL.Date,"Л=fr; ДФ=yy; ДЛФ=DD") + " " + Format(BL.Date,"Л=fr; ДФ=dd/MM/yyyy; ДЛФ=DD");
				Spreadsheet.Put(AreaTabularSectionLineBC);
			КонецЕсли;
			AreaTabularSection.Parameters.Fill(SelectionTabularSection);
			AreaTabularSection.Parameters.ID = SelectionTabularSection.Produit.Артикул;
			AreaTabularSection.Parameters.Descriptif = SelectionTabularSection.Produit;
			AreaTabularSection.Parameters.TauxTVA = SelectionTabularSection.TVA;
			AreaTabularSection.Parameters.TVA = SelectionTabularSection.SommeTVA;
			Если БезНДС Тогда 
				AreaTabularSection.Parameters.Prix = (SelectionTabularSection.SommeTotale - SelectionTabularSection.SommeTVA)/SelectionTabularSection.Quantite;
				AreaTabularSection.Parameters.Somme = SelectionTabularSection.SommeTotale - SelectionTabularSection.SommeTVA;
			КонецЕсли;
			МасОбластей = Новый Массив;
			МасОбластей.Добавить(AreaTabularSection);
			//МасОбластей.Добавить(AreaTabularSection);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьНизРеквизиты);
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				//МасОбластей = Новый Массив;
				//МасОбластей.Добавить(ОбластьПустаяСтрока);
				//МасОбластей.Добавить(ОбластьНизРеквизиты);
				//Для НомерПроверки = 1 по 5 Цикл 
				//	МасОбластей = Новый Массив;
				//	МасОбластей.Добавить(ОбластьПустаяСтрока);
				//	МасОбластей.Добавить(ОбластьНизРеквизиты);
				//	Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
						Spreadsheet.Put(ОбластьНизРеквизиты);
				//		Прервать;
				//	иначе
				//		Spreadsheet.Put(ОбластьПустаяСтрока);
				//	КонецЕсли;
				//КонецЦикла;
				Spreadsheet.ВывестиГоризонтальныйРазделительСтраниц();
				НомерСтраницы = НомерСтраницы + 1;
				//Header.Parameters.PageNumber = НомерСтраницы;
				Spreadsheet.Put(Header, Selection.Level());
				Spreadsheet.Put(AreaTabularSectionHeader, Selection.Level());
			КонецЕсли;
			Spreadsheet.Put(AreaTabularSection, SelectionTabularSection.Level());
			TotalRemise = TotalRemise + SelectionTabularSection.Remise;
			TotalSomme = TotalSomme + SelectionTabularSection.Somme;
		EndDo;
		
		Для НомерПроверки = 1 по 50 Цикл 
			МасОбластей = Новый Массив;
			//МасОбластей.Добавить(AreaTabularSection);
			//МасОбластей.Добавить(AreaTabularSection);
			МасОбластей.Добавить(AreaTabularSectionFooterSousTotal);
			МасОбластей.Добавить(AreaTabularSectionFooterTotalTaxe);
			МасОбластей.Добавить(AreaTabularSectionFooterTotal);
			МасОбластей.Добавить(AreaTabularSectionAmountInWritten);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			//МасОбластей.Добавить(ОбластьПустаяСтрока);
			МасОбластей.Добавить(ОбластьНизРеквизиты);
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				Если НомерПроверки = 1 Тогда 
				Для НомерПроверки = 1 по 50 Цикл 
					МасОбластей = Новый Массив;
					МасОбластей.Добавить(AreaTabularSectionEmptyLine);
					//МасОбластей.Добавить(ОбластьПустаяСтрока);
					МасОбластей.Добавить(ОбластьНизРеквизиты);
					Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
						Spreadsheet.Put(ОбластьНизРеквизиты);
						Прервать;
					иначе
						Spreadsheet.Put(AreaTabularSectionEmptyLine);
					КонецЕсли;
				КонецЦикла;
				КонецЕсли;
				Прервать;
			иначе
				Spreadsheet.Put(AreaTabularSectionEmptyLine);
			КонецЕсли;
		КонецЦикла;
		
		AreaTabularSectionFooterSousTotal.Parameters.SousTotal = ""+Format(Selection.TotalSomme-Selection.TotalSommeTVA,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		СпособОплаты = РаботаСДокументами.ПолучитьСпособОплаты(Док);
		Если Не ЗначениеЗаполнено(СпособОплаты) Тогда 
			СпособОплаты = Selection.Client.ТипОплаты;
		КонецЕсли;
		AreaTabularSectionFooterSousTotal.Parameters.СпособОплаты = СпособОплаты;
		//AreaTabularSectionFooterSousTotal.Рисунки.Печать.Высота = 50;
		//AreaTabularSectionFooterSousTotal.Рисунки.Печать.Ширина = 75;
		МасОбластей = Новый Массив;
 		МасОбластей.Добавить(AreaTabularSectionFooterSousTotal);
		МасОбластей.Добавить(AreaTabularSectionFooterTotalTaxe);
		МасОбластей.Добавить(AreaTabularSectionFooterTotal);
		МасОбластей.Добавить(AreaTabularSectionAmountInWritten);
		МасОбластей.Добавить(ОбластьНизРеквизиты);
		Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
			Spreadsheet.ВывестиГоризонтальныйРазделительСтраниц();
			НомерСтраницы = НомерСтраницы + 1;
		КонецЕсли;
		Spreadsheet.Put(AreaTabularSectionFooterSousTotal);
		If TotalRemise <> 0 Then 
			AreaTabularSectionFooterRemise.Parameters.Remise = ""+Format(TotalRemise,"NFD=2; NZ=0,00")+" "+Selection.Devise;
			Spreadsheet.Put(AreaTabularSectionFooterRemise);
		EndIf;
		
		AreaTabularSectionFooterTotalTaxe.Parameters.TotalTaxe = ""+Format(Selection.TotalSommeTVA,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		Spreadsheet.Put(AreaTabularSectionFooterTotalTaxe);
		
		AreaTabularSectionFooterTotal.Parameters.Total = ""+Format(Selection.TotalSomme,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		Spreadsheet.Put(AreaTabularSectionFooterTotal);
		
		TextAmountInWritten = "Arrêtée la présente facture à la somme de :";
		AmountInWritten = Справочники.Валюты.СформироватьСуммуПрописью(Selection.TotalSomme,Константы.ВалютаРегламентированногоУчета.Получить(),Перечисления.Локализации.fr_CA);
		TextAmountInWritten = TextAmountInWritten + Символы.ПС +" *** "+ ВРег(AmountInWritten) + " *** ";
		AreaTabularSectionAmountInWritten.Параметры.AmountInWritten = TextAmountInWritten;
		Spreadsheet.Put(AreaTabularSectionAmountInWritten);
		
		////Spreadsheet.BottomMargin = 10;
		//Для НомерПроверки = 1 по 5 Цикл 
		//	МасОбластей = Новый Массив;
		//	МасОбластей.Добавить(ОбластьПустаяСтрока);
		//	//МасОбластей.Добавить(ОбластьПустаяСтрока);
		//	МасОбластей.Добавить(ОбластьНизРеквизиты);
		//	Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
		//		Прервать;
		//	иначе
		//		Spreadsheet.Put(ОбластьПустаяСтрока);
		//	КонецЕсли;
		//КонецЦикла;
		Spreadsheet.Put(ОбластьНизРеквизиты);
		//AreaTabularSectionFooterSousTotal.Рисунки.Печать.Высота = 100;
		//AreaTabularSectionFooterSousTotal.Рисунки.Печать.Ширина = 150;
		Spreadsheet.PutHorizontalPageBreak();
	EndDo; 
	
	Spreadsheet.FitToPage = True;
	Spreadsheet.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Facture");
	Return Spreadsheet;
	
EndFunction

Function PrintFactureSocassif(Док, Spreadsheet, СФоном = Ложь) Export
	//{{_PRINT_WIZARD(Печать)
	//Template = Documents.FactureSortie.GetTemplate(TemplateName);
	//TableName = Ref.MetaData().Name;
	БезНДС = Док.Контрагент.ПечатьНакладнойЦеныБезНДС;
	Template = Документы.РеализацияТоваровУслуг.ПолучитьМакет("FactureSocassif");
	Query = New Query;
	Query.Text =
	"ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент КАК Client,
	|	Doc.Ссылка.Ответственный КАК Createur,
	|	Doc.Ссылка.Дата КАК DocumentDate,
	|	ВЫБОР
	|		КОГДА Doc.Ссылка.ДатаИнвойса = ДАТАВРЕМЯ(1, 1, 1, 0, 0, 0)
	|			ТОГДА Doc.Ссылка.Дата
	|		ИНАЧЕ Doc.Ссылка.ДатаИнвойса
	|	КОНЕЦ КАК DocumentNumber,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов КАК Devise,
	|	Doc.Ссылка.Сумма КАК TotalSomme,
	|	Doc.Ссылка.СуммаНДС КАК TotalSommeTVA,
	|	Doc.Ссылка.Ссылка КАК DocRef,
	|	Doc.НомерСтроки КАК LineNumber,
	|	Doc.Номенклатура КАК Produit,
	|	Doc.Номенклатура.Единица КАК UOM,
	|	Doc.Количество КАК Quantity,
	|	Doc.Цена КАК Price,
	|	Doc.СтавкаНДС КАК TVA,
	|	Doc.СуммаНДС КАК VATAmount,
	|	Doc.СуммаСкидки КАК Remise,
	|	Doc.Сумма КАК NetAmount,
	|	Doc.СуммаСНДС КАК Total,
	|	Doc.Ссылка.Организация КАК Organisation,
	|	Doc.Ссылка.Основание КАК Основание,
	|	Doc.ОтгрузкаТовара КАК BL,
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
	|	ВЫБОР
	|		КОГДА Doc.Ссылка.ДатаИнвойса = ДАТАВРЕМЯ(1, 1, 1, 0, 0, 0)
	|			ТОГДА Doc.Ссылка.Дата
	|		ИНАЧЕ Doc.Ссылка.ДатаИнвойса
	|	КОНЕЦ,
	|	Doc.Ссылка.Номер,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов,
	|	Doc.Ссылка.Сумма,
	|	Doc.Ссылка.СуммаНДС,
	|	Doc.Ссылка.Ссылка,
	|	0,
	|	Doc.Номенклатура,
	|	Doc.Номенклатура.Единица,
	|	Doc.Количество,
	|	Doc.Цена,
	|	Doc.СтавкаНДС,
	|	Doc.СуммаНДС,
	|	0,
	|	Doc.Сумма,
	|	Doc.СуммаСНДС,
	|	Doc.Ссылка.Организация,
	|	Doc.Ссылка.Основание,
	|	Doc.ОтгрузкаТовара,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.НалоговаяНакладная.ТЧУслуги КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|
	|УПОРЯДОЧИТЬ ПО
	|	BL
	|ИТОГИ ПО
	|	Ссылка";
	Query.Parameters.Insert("Ref", Док);
	Selection = Query.Execute().Select(ОбходРезультатаЗапроса.ПоГруппировкам);

	//AreaCaption = Template.GetArea("Caption");
	Title = Template.GetArea("Title");
	CounterpartyInfo = Template.GetArea("CounterpartyInfo");
	Comment = Template.GetArea("Comment");	
	LineHeader = Template.GetArea("LineHeader");	
	LineSection = Template.GetArea("LineSection");	
	LineTotal = Template.GetArea("LineTotal");	
	BottomBorder = Template.GetArea("BottomBorder");	
	LineTotalDue = Template.GetArea("LineTotalDue");	
	TaxSectionHeader = Template.GetArea("TaxSectionHeader");	
	TaxSectionLine = Template.GetArea("TaxSectionLine");	
	EmptyLine = Template.GetArea("EmptyLine");	
	PageNumberSection = Template.GetArea("PageNumber");	
	CompanyInfo = Template.GetArea("CompanyInfo");	
	AreaTabularSectionLineBC = Template.GetArea("LineBL");
	LineHeaderWOVAT = Template.GetArea("LineHeaderWOVAT");	
	LineSectionWOVAT = Template.GetArea("LineSectionWOVAT");	
	LineTotalWOVAT = Template.GetArea("LineTotalWOVAT");	
	
	PageNumber = 0;
	InsertPageBreak = False;
	While Selection.Next() Do
		//If InsertPageBreak Then
		//	Spreadsheet.PutHorizontalPageBreak();
		//EndIf;
 		ОсновнойУчет = Selection.Organisation.ОсновнойУчет;

		FirstRowNumber = Spreadsheet.TableHeight + 1;
		//Header
		Title.Parameters.Fill(Selection);
		If Selection.Organisation <> Catalogs.Организации.EmptyRef() Then 
			FieldPhoto = Selection.Organisation.Логотип.Get();
			Try
				Title.Drawings.Logo.Picture = New Picture(FieldPhoto);
			Except
			EndTry;
		EndIf;
		Spreadsheet.Put(Title, Selection.Level());
		//Organisation
    	OrganisationCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Organisation, Док.Дата);
		CompanyInfo.Параметры.FullDescr = Selection.Organisation.Description;
		CompanyInfo.Параметры.RegistrationNumber = СокрЛП(OrganisationCard.Реквизиты.ICE);
		CompanyInfo.Параметры.VATNumber = СокрЛП(OrganisationCard.Реквизиты.NIF);
		CompanyInfo.Параметры.AccountNo = OrganisationCard.БанковскийСчётОсновной.НомерСчёта;
		CompanyInfo.Параметры.Bank = OrganisationCard.БанковскийСчётОсновной.Банк;
		CompanyInfo.Параметры.Webpage = СокрЛП(OrganisationCard.Реквизиты.Web);
		CompanyInfo.Параметры.EMail = OrganisationCard.Реквизиты.email;
		CompanyInfo.Параметры.LegalAddress = OrganisationCard.АдресЮридический;
		CompanyInfo.Параметры.PhoneNumbers = OrganisationCard.Телефоны;
		Spreadsheet.Put(CompanyInfo, Selection.Level());
		//Client
    	ClientCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Client, Док.Дата);
		Client = Selection.Client.Description;
		CounterpartyInfo.Параметры.FullDescr = Client;
		CounterpartyInfo.Параметры.VATNumber = ClientCard.Реквизиты.NIF;
		CounterpartyInfo.Параметры.RegistrationNumber = ClientCard.Реквизиты.ICE;
		CounterpartyInfo.Параметры.LegalAddress = ClientCard.Реквизиты.АдресЮридический;
		CounterpartyInfo.Параметры.DeliveryAddress = ClientCard.Реквизиты.АдресДоставки;
		CounterpartyInfo.Параметры.FullDescrShipTo = Client;
		CounterpartyInfo.Параметры.CounterpartyContactPerson = "";
		CounterpartyInfo.Параметры.PhoneNumbers = ClientCard.Телефоны;
		СпособОплаты = РаботаСДокументами.ПолучитьСпособОплаты(Док);
		Если Не ЗначениеЗаполнено(СпособОплаты) Тогда 
			СпособОплаты = Selection.Client.ТипОплаты;
		КонецЕсли;
		CounterpartyInfo.Параметры.PaymentTerms = СпособОплаты;
		Spreadsheet.Put(CounterpartyInfo, Selection.Level());
		//Comment
		Comment.Параметры.Comment = Selection.DocRef.Комментарий;
		Spreadsheet.Put(Comment, Selection.Level());
		//LineHeader
		Spreadsheet.Put(?(ОсновнойУчет, LineHeader, LineHeaderWOVAT), Selection.Level()); 
		//LineSection
		SelectionTabularSection = Selection.Select();
		LineNumber = 0;
        BL = Документы.РеализацияТоваровУслуг.ПустаяСсылка();
		While SelectionTabularSection.Next() Do
			Если Не BL = SelectionTabularSection.BL И ЗначениеЗаполнено(SelectionTabularSection.BL) Тогда
				BL = SelectionTabularSection.BL;
				AreaTabularSectionLineBC.Parameters.BL = "BL: "+РаботаСДокументами.СформироватьЦифровойНомер(BL.Number)+"/"+Format(BL.Date,"Л=fr; ДФ=yy; ДЛФ=DD") + " du " + Format(BL.Date,"Л=fr; ДФ=dd/MM/yyyy; ДЛФ=DD");
				
				МасОбластей = Новый Массив;
				МасОбластей.Добавить(AreaTabularSectionLineBC);
				МасОбластей.Добавить(PageNumberSection);
				Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
					PageNumber = PageNumber + 1;
					PageNumberSection.Parameters.PageNumber = PageNumber;
					Spreadsheet.Put(PageNumberSection);
					Spreadsheet.ВывестиГоризонтальныйРазделительСтраниц();
					Spreadsheet.Put(?(ОсновнойУчет, LineHeader, LineHeaderWOVAT));
				КонецЕсли;
				Spreadsheet.Put(AreaTabularSectionLineBC);
			КонецЕсли;
			LineNumber = LineNumber + 1;
			Если ОсновнойУчет Тогда 
				LineSection.Parameters.Fill(SelectionTabularSection);
				LineSection.Parameters.SKU = SelectionTabularSection.Produit.Артикул;
				LineSection.Parameters.ProductDescription = SelectionTabularSection.Produit;
				LineSection.Parameters.VATRate = SelectionTabularSection.TVA;
				Если БезНДС Тогда 
					LineSection.Parameters.Price = (SelectionTabularSection.Total - SelectionTabularSection.VATAmount)/SelectionTabularSection.Quantity;
					LineSection.Parameters.NetAmount = SelectionTabularSection.Total - SelectionTabularSection.VATAmount;
				КонецЕсли;
			Иначе
				LineSectionWOVAT.Parameters.Fill(SelectionTabularSection);
				LineSectionWOVAT.Parameters.SKU = SelectionTabularSection.Produit.Артикул;
				LineSectionWOVAT.Parameters.ProductDescription = SelectionTabularSection.Produit;
			КонецЕсли;
			МасОбластей = Новый Массив;
			МасОбластей.Добавить(?(ОсновнойУчет, LineSection, LineSectionWOVAT));
			МасОбластей.Добавить(PageNumberSection);
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				МасОбластей.Очистить();
				МасОбластей.Добавить(EmptyLine);
				МасОбластей.Добавить(PageNumberSection);
				For i = 1 To 50 Do
					If Not Spreadsheet.ПроверитьВывод(МасОбластей) 
						Or i = 50 Then
						PageNumber = PageNumber + 1;
						PageNumberSection.Parameters.PageNumber = PageNumber;
						Spreadsheet.Put(PageNumberSection);
						Break;
					Else
						Spreadsheet.Put(EmptyLine);
					EndIf;
				EndDo;
				Spreadsheet.ВывестиГоризонтальныйРазделительСтраниц();
				Spreadsheet.Put(?(ОсновнойУчет, LineHeader, LineHeaderWOVAT));
			КонецЕсли;
			Spreadsheet.Put(?(ОсновнойУчет, LineSection, LineSectionWOVAT), SelectionTabularSection.Level());
		EndDo;
		Если ОсновнойУчет Тогда 
			LineTotal.Parameters.LineNumber = LineNumber;
			LineTotal.Parameters.DocumentCurrency = Константы.ВалютаРегламентированногоУчета.Получить();
			LineTotal.Parameters.Subtotal = Format(Selection.TotalSomme - Selection.TotalSommeTVA,"NFD=2; NZ=0,00");
			LineTotal.Parameters.VATAmount = Format(Selection.TotalSommeTVA,"NFD=2; NZ=0,00");
			LineTotal.Parameters.Total = Format(Selection.TotalSomme,"NFD=2; NZ=0,00");
			Spreadsheet.Put(LineTotal);
		Иначе
			LineTotalWOVAT.Parameters.LineNumber = LineNumber;
			LineTotalWOVAT.Parameters.DocumentCurrency = Константы.ВалютаРегламентированногоУчета.Получить();
			LineTotalWOVAT.Parameters.Total = Format(Selection.TotalSomme,"NFD=2; NZ=0,00");
			Spreadsheet.Put(LineTotalWOVAT);
		КонецЕсли;
		
		Spreadsheet.Put(BottomBorder);
		ТЗОплат = РегистрыНакопления.ДенежныеСредстваОрганизаций.ПолучитьОплаты(Док, Истина);
		Оплачено = ТЗОплат.Итог("Сумма");
		LineTotalDue.Parameters.Paid = Format(Оплачено,"NFD=2; NZ=0,00");
		LineTotalDue.Parameters.TotalDue = Format(Selection.TotalSomme - Оплачено,"NFD=2; NZ=0,00");
		LineTotalDue.Parameters.DocumentCurrency = Константы.ВалютаРегламентированногоУчета.Получить();
		Spreadsheet.Put(LineTotalDue);
		
		МасОбластей.Clear();
		МасОбластей.Add(EmptyLine);
		МасОбластей.Add(PageNumberSection);
		
		For i = 1 To 50 Do
			
			If Not Spreadsheet.ПроверитьВывод(МасОбластей)
				Or i = 50 Then
				
				PageNumber = PageNumber + 1;
				PageNumberSection.Parameters.PageNumber = PageNumber;
				Spreadsheet.Put(PageNumberSection);
				Break;
				
			Else
				
				Spreadsheet.Put(EmptyLine);
				
			EndIf;
			
		EndDo;

		Spreadsheet.PutHorizontalPageBreak();
		//PrintManagement.SetDocumentPrintArea(Spreadsheet, FirstRowNumber, PrintObjects, Selection.DocRef);
	EndDo; 
	
	Spreadsheet.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Facture");
	ЭтоНалоговаяНакладная = СтрНайти(Spreadsheet.ИспользуемоеИмяФайла ,"Facture");
	
	If ЭтоНалоговаяНакладная > 0 Then
		Spreadsheet.ИспользуемоеИмяФайла = СтрЗаменить(Spreadsheet.ИспользуемоеИмяФайла, "Facture", "Facture " + Client);
	EndIf;
	
	Return Spreadsheet;
	
	//}}
EndFunction

Function PrintDevisBL(Док, Spreadsheet, НазваниеДокумента = "Devis", БезЦен = Ложь) Export
	Template = Документы.РеализацияТоваровУслуг.ПолучитьМакет("DevisBL");
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
	|	Документ.РеализацияТоваровУслуг.ТЧТовары КАК Doc
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
	|	Документ.РеализацияТоваровУслуг.ТЧУслуги КАК Doc
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
	|
	|ОБЪЕДИНИТЬ ВСЕ
	|
	|ВЫБРАТЬ
	|	ВозвратОтПокупателяТЧТовары.Ссылка.Контрагент,
	|	ВозвратОтПокупателяТЧТовары.Ссылка.Ответственный,
	|	ВозвратОтПокупателяТЧТовары.Ссылка.Дата,
	|	ВозвратОтПокупателяТЧТовары.Ссылка.Номер,
	|	ВозвратОтПокупателяТЧТовары.Ссылка.Договор.ВалютаВзаиморасчётов,
	|	ВозвратОтПокупателяТЧТовары.Ссылка.Сумма,
	|	ВозвратОтПокупателяТЧТовары.СуммаНДС,
	|	ВозвратОтПокупателяТЧТовары.Ссылка.Ссылка,
	|	0,
	|	ВозвратОтПокупателяТЧТовары.Номенклатура,
	|	ВозвратОтПокупателяТЧТовары.Количество,
	|	ВозвратОтПокупателяТЧТовары.Цена,
	|	ВозвратОтПокупателяТЧТовары.СтавкаНДС,
	|	ВозвратОтПокупателяТЧТовары.СуммаНДС,
	|	0,
	|	ВозвратОтПокупателяТЧТовары.Сумма,
	|	ВозвратОтПокупателяТЧТовары.СуммаСНДС,
	|	ВозвратОтПокупателяТЧТовары.Ссылка.Организация,
	|	NULL,
	|	ВозвратОтПокупателяТЧТовары.Ссылка
	|ИЗ
	|	Документ.ВозвратОтПокупателя.ТЧТовары КАК ВозвратОтПокупателяТЧТовары
	|ГДЕ
	|	ВозвратОтПокупателяТЧТовары.Ссылка = &Ref
	|
	|ОБЪЕДИНИТЬ ВСЕ
	|
	|ВЫБРАТЬ
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка.Контрагент,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка.Ответственный,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка.Дата,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка.Номер,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка.Договор.ВалютаВзаиморасчётов,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка.Сумма,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.СуммаНДС,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка.Ссылка,
	|	0,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Номенклатура,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Количество,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Цена,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.СтавкаНДС,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.СуммаНДС,
	|	0,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Сумма,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.СуммаСНДС,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка.Организация,
	|	NULL,
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка
	|ИЗ
	|	Документ.ВозвратОтПокупателяНалоговый.ТЧТовары КАК ВозвратОтПокупателяНалоговыйТЧТовары
	|ГДЕ
	|	ВозвратОтПокупателяНалоговыйТЧТовары.Ссылка = &Ref
	|ИТОГИ ПО
	|	Ссылка";
	Query.Parameters.Insert("Ref", Док);
	Selection = Query.Execute().Select(ОбходРезультатаЗапроса.ПоГруппировкам);

	//AreaCaption = Template.GetArea("Caption");
	Header = Template.GetArea("Header");
	AreaTabularSectionHeader = Template.GetArea("TabularSectionHeader");
	AreaTabularSection = Template.GetArea("TabularSection");
	AreaTabularSectionEmptyLine = Template.GetArea("EmptyLine");
	AreaTabularSectionFooterTotal = Template.GetArea("TabularSectionFooterTotal"); 
	AreaTabularSectionFooter = Template.GetArea("TabularSectionFooter"); 
	Spreadsheet.РазмерСтраницы = "A5";
	Spreadsheet.FitToPage = True;
	
	InsertPageBreak = False;
	While Selection.Next() Do
        НомерСтраницы = 1;
		FirstRowNumber = Spreadsheet.TableHeight + 1;
		Header.Parameters.Fill(Selection);
		Header.Parameters.Организация = Selection.Organisation;
		Header.Parameters.Number = "Numéro: "+РаботаСДокументами.СформироватьЦифровойНомер(Selection.Number)+"/"+Format(Selection.Date,"Л=fr; ДФ=yy; ДЛФ=DD");
		Header.Parameters.Date = "Date: "+Format(Selection.Date,"Л=fr; ДФ=dd/MM/yyyy; ДЛФ=DD");
		
    	OrganisationCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Organisation, Док.Дата);
		Header.Parameters.Адрес = OrganisationCard.АдресЮридический;
		Header.Parameters.Телефоны = "Tel: "+OrganisationCard.Телефоны;
		Header.Parameters.RC = "RC: "+OrganisationCard.Реквизиты.RC;
		Header.Parameters.Patente = "PATENTE: "+OrganisationCard.Реквизиты.TaxeProfessionnelle;
		Header.Parameters.IF = "IF: "+OrganisationCard.Реквизиты.NIF;
		Header.Parameters.ICE = "ICE: "+OrganisationCard.Реквизиты.ICE;
		Header.Parameters.Site = "Site web: "+OrganisationCard.Реквизиты.Web;
		Header.Parameters.Email = "EMail: "+OrganisationCard.Реквизиты.EMail;
		
		If Selection.Organisation <> Catalogs.Организации.EmptyRef() Then 
			FieldPhoto = Selection.Organisation.Логотип.Get();
			Try
				Header.Drawings[0].Picture = New Picture(FieldPhoto);
			Except
			EndTry;
		EndIf;

		ClientCard = Справочники.Контрагенты.ПолучитьКарточку(Selection.Client, Док.Дата);
		Client = РаботаСДокументами.СформироватьЦифровойНомер(Selection.Client.Код) + Символы.ПС+Selection.Client.Description;
		Client = Client + Символы.ПС+ "Tel: "+ClientCard.Телефоны;
		
		Header.Parameters.Client = Client;
		Header.Parameters.НазваниеДокумента = НазваниеДокумента;
		Header.Parameters.Комментарий = Selection.DocRef.Комментарий;
		Header.Parameters.НомерЗаказа = РаботаСДокументами.СформироватьЦифровойНомер(?(ТипЗнч(Selection.DocRef) = Тип("ДокументСсылка.РеализацияТоваровУслуг"),Selection.DocRef.Основание.Номер,Selection.DocRef.Номер));
		Spreadsheet.Put(Header, Selection.Level());
		
		TotalRemise = 0;
		TotalSomme = 0;

		Spreadsheet.Put(AreaTabularSectionHeader);
		SelectionTabularSection = Selection.Select();
		НомерСтроки = 0;
		While SelectionTabularSection.Next() Do
			НомерСтроки = НомерСтроки+1;
			AreaTabularSection.Parameters.Fill(SelectionTabularSection);
			AreaTabularSection.Parameters.LineNumber = НомерСтроки;
			AreaTabularSection.Parameters.Descriptif = ОбщегоНазначенияКлиентСервер.ПредставлениеНоменклатуры(
				SelectionTabularSection.Produit, "", , Истина);
			AreaTabularSection.Parameters.Prix = ?(БезЦен, 0, SelectionTabularSection.Prix);
			AreaTabularSection.Parameters.Prix = ?(БезЦен, 0, SelectionTabularSection.Prix);
			AreaTabularSection.Parameters.Somme = ?(БезЦен, 0, SelectionTabularSection.Somme);
			//AreaTabularSection.Parameters.TauxTVA = SelectionTabularSection.TVA;
			//AreaTabularSection.Parameters.TVA = SelectionTabularSection.SommeTVA;
			МасОбластей = Новый Массив;
			МасОбластей.Добавить(AreaTabularSection);
			МасОбластей.Добавить(AreaTabularSectionFooterTotal);
			МасОбластей.Добавить(AreaTabularSectionFooter);
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда 
				Spreadsheet.ВывестиГоризонтальныйРазделительСтраниц();
				НомерСтраницы = НомерСтраницы + 1;
				//Header.Parameters.PageNumber = НомерСтраницы;
				Spreadsheet.Put(Header, Selection.Level());
				Spreadsheet.Put(AreaTabularSectionHeader);
			КонецЕсли;
			Spreadsheet.Put(AreaTabularSection, SelectionTabularSection.Level());
			TotalRemise = TotalRemise + ?(БезЦен, 0, SelectionTabularSection.Remise);
			TotalSomme = TotalSomme + ?(БезЦен, 0, SelectionTabularSection.Somme);
		EndDo;
		
		Если Не БезЦен Тогда 
			AreaTabularSectionFooterTotal.Parameters.Total = ""+Format(Selection.TotalSomme,"NFD=2; NZ=0,00")+" "+Selection.Devise;
			VT = РегистрыНакопления.ВзаиморасчётыСПокупателями.GetTableOfPayments(Selection.DocRef);
			TotalSommePaiement = VT.Total("Somme");
			AreaTabularSectionFooterTotal.Parameters.TotalSommePaiement = ""+Format(TotalSommePaiement,"ЧДЦ=2; ЧРГ=' '; ЧН=0,00")+" "+Selection.Devise;
			AreaTabularSectionFooterTotal.Parameters.ОстатокОплаты =  ""+Format(Selection.TotalSomme - TotalSommePaiement,"ЧДЦ=2; ЧРГ=' '; ЧН=0,00")+" "+Selection.Devise;
		КонецЕсли;
		Spreadsheet.Put(AreaTabularSectionFooterTotal);
		
		Для НомерПроверки = 1 по 50 Цикл 
			МасОбластей = Новый Массив;
			МасОбластей.Добавить(AreaTabularSection);
			МасОбластей.Добавить(AreaTabularSection);
			//МасОбластей.Добавить(AreaTabularSectionFooterTotal);
			МасОбластей.Добавить(AreaTabularSectionFooter);
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				Прервать;
			иначе
				Spreadsheet.Put(AreaTabularSectionEmptyLine);
			КонецЕсли;
		КонецЦикла;
		
		AreaTabularSectionFooter.Parameters.PrintDate = Формат(ТекущаяДатаСеанса(),"ДЛФ=D");
		AreaTabularSectionFooter.Parameters.PrintTime = Формат(ТекущаяДатаСеанса(),"ДЛФ=T");
		AreaTabularSectionFooter.Parameters.Author = Selection.DocRef.Ответственный;
		Spreadsheet.Put(AreaTabularSectionFooter);
		
		Spreadsheet.BottomMargin = 10;
		
		Spreadsheet.PutHorizontalPageBreak();
	EndDo; 
	
	Spreadsheet.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, НазваниеДокумента);
	Return Spreadsheet;
	
EndFunction

Function PrintTicket(Док, Spreadsheet) Export
	//{{_PRINT_WIZARD(Печать)
	//Template = Documents.FactureSortie.GetTemplate(TemplateName);
	//TableName = Ref.MetaData().Name;
	Template = Документы.РеализацияТоваровУслуг.ПолучитьМакет("Чек");
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
	//|	Doc.Цена КАК Prix,
	|	Doc.СуммаСНДС/Doc.Количество КАК Prix,
	|	Doc.СтавкаНДС КАК TVA,
	|	Doc.СуммаНДС КАК SommeTVA,
	|	Doc.СуммаСкидки КАК Remise,
	|	Doc.СуммаСНДС КАК Somme,
	|	Doc.СуммаСНДС КАК SommeTotale,
	|	Doc.Ссылка.Организация КАК Organisation,
	|	Doc.Ссылка.Основание КАК Основание,
	|	Doc.Ссылка КАК Ссылка
	|ИЗ
	|	Документ.РеализацияТоваровУслуг.ТЧТовары КАК Doc
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
	//|	Doc.Цена,
	|	Doc.СуммаСНДС/Doc.Количество,
	|	Doc.СтавкаНДС,
	|	Doc.СуммаНДС,
	|	0,
	|	Doc.СуммаСНДС,
	|	Doc.СуммаСНДС,
	|	Doc.Ссылка.Организация,
	|	Doc.Ссылка.Основание,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.РеализацияТоваровУслуг.ТЧУслуги КАК Doc
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
	
	Spreadsheet.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "BL");
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
