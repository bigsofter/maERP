
#Область Печать

Процедура ПечатьПоступлениеТоваров(Док, Таб) Экспорт
	УстановитьПривилегированныйРежим(Истина);
	Таб.ОтображатьСетку = Ложь;
	Таб.ОтображатьЗаголовки = Ложь;
	Таб.ОриентацияСтраницы = ОриентацияСтраницы.Портрет;
	Таб.Автомасштаб = Истина;
	Таб.КлючПараметровПечати = "Параметры_печати_Документ_ПоступлениеТоваровУслуг_ПоступлениеТоваров";
	Макет = Документы.ПоступлениеТоваровУслуг.ПолучитьМакет("ПоступлениеТоваров");
	// Шапка
	оШапка = Макет.ПолучитьОбласть("Шапка");
	оШапка.Параметры.ТекстЗаголовка = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Bon de réception");
	//оШапка.Параметры.Контрагент = Док.Контрагент;
	оШапка.Параметры.Организация = Док.Организация;
	Таб.Вывести(оШапка);
	// Строки
	оСтрока = Макет.ПолучитьОбласть("Строка");
	Для Каждого Стр Из Док.ТЧТовары Цикл
		оСтрока.Параметры.НомерСтроки = Стр.НомерСтроки;
		оСтрока.Параметры.Номенклатура = Стр.Номенклатура;
		оСтрока.Параметры.ID = Стр.Номенклатура.Артикул;
		//оСтрока.Параметры.Количество = Стр.Количество;
		оСтрока.Параметры.Единица = Стр.Номенклатура.Единица;
		Таб.Вывести(оСтрока);
	КонецЦикла;
	//// Итого
	//оИтого = Макет.ПолучитьОбласть("Итого");
	//оИтого.Параметры.Всего = Док.Сумма;
	//Таб.Вывести(оИтого);
	//// НДС
	//оНДС = Макет.ПолучитьОбласть("ИтогоНДС");
	//оНДС.Параметры.НДС = "TVA";
	//оНДС.Параметры.ВсегоНДС = Док.ТЧТовары.Итог("СуммаНДС");
	//Таб.Вывести(оНДС);
	//// Сумма прописью
	//Валюта = Справочники.Валюты.MoroccanDirham;
	//оСуммаПрописью = Макет.ПолучитьОбласть("СуммаПрописью");
	////оСуммаПрописью.Параметры.ИтоговаяСтрока = "Всего наименований " + СокрЛП(Док.ТЧТовары.Количество()) 
	////	+ ", на сумму " + Формат(Док.Сумма, "ЧЦ=12; ЧДЦ=2") + " руб.";
	//оСуммаПрописью.Параметры.СуммаПрописью = Справочники.Валюты.СформироватьСуммуПрописью(Док.Сумма, Валюта, Перечисления.Локализации.fr_CA);
	//Таб.Вывести(оСуммаПрописью);
	// Подписи
	Таб.Вывести(Макет.ПолучитьОбласть("Подписи"));
	Таб.ВывестиГоризонтальныйРазделительСтраниц();
КонецПроцедуры

Процедура ПечатьАктаОбОказанииУслуг(Док, Таб) Экспорт
	УстановитьПривилегированныйРежим(Истина);
	Таб.ОтображатьСетку = Ложь;
	Таб.ОтображатьЗаголовки = Ложь;
	Таб.ОриентацияСтраницы = ОриентацияСтраницы.Портрет;
	Таб.АвтоМасштаб = Истина;
	Таб.КлючПараметровПечати = "Параметры_печати_Документ_ПоступлениеТоваровУслуг_АктОбОказанииУслуг";
	Макет = ПолучитьОбщийМакет("АктОбОказанииУслуг");	
	оЗаголовок = Макет.ПолучитьОбласть("Заголовок");
	оЗаголовок.Параметры.ТекстЗаголовка = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Акт");
	Таб.Вывести(оЗаголовок);
	оПоставщик = Макет.ПолучитьОбласть("Поставщик");	
	оПоставщик.Параметры.ПредставлениеПоставщика = Док.Контрагент;
	Таб.Вывести(оПоставщик);
	оПолучатель = Макет.ПолучитьОбласть("Получатель");	
	оПолучатель.Параметры.ПредставлениеПолучателя = Док.Организация;
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
	ОПодписи.Параметры.НазваниеОрганизации = Док.Контрагент;
	ОПодписи.Параметры.НазваниеЗаказчика = Док.Организация;
	Таб.Вывести(ОПодписи);
	Таб.ВывестиГоризонтальныйРазделительСтраниц();
	Таб.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Акт");
КонецПроцедуры

Function PrintFacture(Док, Spreadsheet) Export
	Template = Документы.НалоговаяНакладнаяПокупка.ПолучитьМакет("Facture");
	Query = New Query;
	Query.Text =
	"ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент КАК Client,
	|	Doc.Ссылка.Ответственный КАК Createur,
	|	Doc.Ссылка.Дата КАК Date,
	|	Doc.Ссылка.Номер КАК Number,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов КАК Devise,
	|	Doc.Ссылка.Сумма КАК TotalSomme,
	|	Doc.Ссылка.Ссылка КАК DocRef,
	|	Doc.НомерСтроки КАК LineNumber,
	|	Doc.Номенклатура КАК Produit,
	|	Doc.Количество КАК Quantite,
	|	Doc.Цена КАК Prix,
	|	Doc.СтавкаНДС КАК TVA,
	|	Doc.СуммаНДС КАК SommeTVA,
	|	Doc.Сумма КАК Somme,
	|	Doc.СуммаСНДС КАК SommeTotale,
	|	Doc.Ссылка.Организация КАК Organisation,
	|	Doc.Ссылка.Основание КАК Основание,
	|	Doc.ПоступлениеТовара КАК BL,
	|	Doc.Ссылка КАК Ссылка
	|ИЗ
	|	Документ.НалоговаяНакладнаяПокупка.ТЧТовары КАК Doc
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
	|	Doc.Ссылка.Ссылка,
	|	0,
	|	Doc.Номенклатура,
	|	Doc.Количество,
	|	Doc.Цена,
	|	Doc.СтавкаНДС,
	|	Doc.СуммаНДС,
	|	Doc.Сумма,
	|	Doc.СуммаСНДС,
	|	Doc.Ссылка.Организация,
	|	Doc.Ссылка.Основание,
	|	Doc.ПоступлениеТовара,
	|	Doc.Ссылка
	|ИЗ
	|	Документ.НалоговаяНакладнаяПокупка.ТЧУслуги КАК Doc
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
		
		//TotalRemise = 0;
		TotalSommeTVA = 0;
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
			AreaTabularSection.Parameters.Prix = SelectionTabularSection.Prix;
			AreaTabularSection.Parameters.TauxTVA = SelectionTabularSection.TVA;
			AreaTabularSection.Parameters.TVA = SelectionTabularSection.SommeTVA;
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
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				МасОбластей = Новый Массив;
				МасОбластей.Добавить(ОбластьПустаяСтрока);
				//Пока Spreadsheet.ПроверитьВывод(МасОбластей) Цикл 
				Для НомерПроверки = 1 по 5 Цикл 
					МасОбластей = Новый Массив;
					МасОбластей.Добавить(ОбластьПустаяСтрока);
					//МасОбластей.Добавить(ОбластьПустаяСтрока);
					//МасОбластей.Добавить(ОбластьПустаяСтрока);
					Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
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
			//TotalRemise = TotalRemise + SelectionTabularSection.Remise;
			TotalSomme = TotalSomme + SelectionTabularSection.Somme;
			TotalSommeTVA = TotalSommeTVA + SelectionTabularSection.SommeTVA;
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
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				//Если СФоном Тогда 
				//	Spreadsheet.Put(ОбластьНизРеквизиты);
				//КонецЕсли;
				Прервать;
			иначе
				Spreadsheet.Put(AreaTabularSectionEmptyLine);
			КонецЕсли;
		КонецЦикла;
		
		AreaTabularSectionFooterSousTotal.Parameters.SousTotal = ""+Format(Selection.TotalSomme-TotalSommeTVA,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		//СпособОплаты = РаботаСДокументами.ПолучитьСпособОплаты(Док);
		СпособОплаты = РаботаСДокументами.ПолучитьСпособОплаты(Док);
		Если Не ЗначениеЗаполнено(СпособОплаты) Тогда 
			СпособОплаты = Selection.Client.ТипОплаты;
		КонецЕсли;
		AreaTabularSectionFooterSousTotal.Parameters.СпособОплаты = СпособОплаты;
		Spreadsheet.Put(AreaTabularSectionFooterSousTotal);
		//If TotalRemise <> 0 Then 
		//	AreaTabularSectionFooterRemise.Parameters.Remise = ""+Format(TotalRemise,"NFD=2; NZ=0,00")+" "+Selection.Devise;
		//	Spreadsheet.Put(AreaTabularSectionFooterRemise);
		//EndIf;
		
		AreaTabularSectionFooterTotalTaxe.Parameters.TotalTaxe = ""+Format(TotalSommeTVA,"NFD=2; NZ=0,00")+" "+Selection.Devise;
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
			Если Не Spreadsheet.ПроверитьВывод(МасОбластей) Тогда
				Прервать;
			иначе
				Spreadsheet.Put(ОбластьПустаяСтрока);
			КонецЕсли;
		КонецЦикла;
		Spreadsheet.PutHorizontalPageBreak();
	EndDo; 
	
	Spreadsheet.FitToPage = True;
	Spreadsheet.ИспользуемоеИмяФайла = РаботаСДокументами.КраткоеПредставлениеДокумента(Док, "Facture");
	Return Spreadsheet;
	
EndFunction

#КонецОбласти 
