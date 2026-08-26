#Область ПрограммныйИнтерфейс

// Перечисляет печатные формы объекта.
// См. ПечатныеФормы.НоваяКоллекцияКомандПечати
//
// Параметры:
//  КомандыПечати - ТаблицаЗначений - пополняемая коллекция команд печати
//
Процедура ДобавитьКомандыПечати(КомандыПечати) Экспорт

	Команда = КомандыПечати.Добавить();
	Команда.ИмяМакета = "Avoir";
	Команда.Представление = НСтр("ru = 'Возврат (Avoir)'; fr = 'Avoir';
		|en = 'Credit note'; es = 'Nota de abono'");

	Команда = КомандыПечати.Добавить();
	Команда.ИмяМакета = "Чек";
	Команда.Представление = НСтр("ru = 'Чек'; fr = 'Ticket';
		|en = 'Receipt'; es = 'Recibo'");

КонецПроцедуры

// Формирует запрошенные печатные формы.
// См. ПечатныеФормы.СформироватьПечатныеФормы
//
// Параметры:
//  МассивОбъектов        - Массив          - печатаемые объекты
//  ПараметрыПечати       - Структура       - параметры команды печати
//  КоллекцияПечатныхФорм - ТаблицаЗначений - заполняемая коллекция печатных форм
//  ОбъектыПечати         - СписокЗначений  - соответствие объектов областям печати
//  ПараметрыВывода       - Структура       - параметры окна печати
//
Процедура Печать(МассивОбъектов, ПараметрыПечати, КоллекцияПечатныхФорм, ОбъектыПечати, ПараметрыВывода) Экспорт

	Если ПечатныеФормы.НужноПечататьМакет(КоллекцияПечатныхФорм, "Avoir") Тогда
		Таб = Новый ТабличныйДокумент;
		Для Каждого Док Из МассивОбъектов Цикл
			НомерСтрокиНачало = Таб.ВысотаТаблицы + 1;
			Документы.РеализацияТоваровУслуг.PrintDevisBL(Док, Таб, "Avoir");
			ПечатныеФормы.ЗадатьОбластьПечати(Таб, НомерСтрокиНачало, ОбъектыПечати, Док);
		КонецЦикла;
		ПечатныеФормы.ВывестиТабличныйДокумент(КоллекцияПечатныхФорм, "Avoir",
			НСтр("ru = 'Возврат (Avoir)'; fr = 'Avoir';
			|en = 'Credit note'; es = 'Nota de abono'"),
			Таб, "Документ.РеализацияТоваровУслуг.DevisBL");
	КонецЕсли;

	Если ПечатныеФормы.НужноПечататьМакет(КоллекцияПечатныхФорм, "Чек") Тогда
		Таб = Документы.РеализацияТоваровУслуг.НовыйТабличныйДокументЧека();
		Для Каждого Док Из МассивОбъектов Цикл
			НомерСтрокиНачало = Таб.ВысотаТаблицы + 1;
			Документы.ВозвратОтПокупателя.PrintTicket(Док, Таб);
			ПечатныеФормы.ЗадатьОбластьПечати(Таб, НомерСтрокиНачало, ОбъектыПечати, Док);
		КонецЦикла;
		ПечатныеФормы.ВывестиТабличныйДокумент(КоллекцияПечатныхФорм, "Чек",
			НСтр("ru = 'Чек'; fr = 'Ticket';
			|en = 'Receipt'; es = 'Recibo'"),
			Таб, "Документ.РеализацияТоваровУслуг.Чек");
	КонецЕсли;

КонецПроцедуры

#КонецОбласти

Процедура ОбработкаПолученияПолейПредставления(Поля, СтандартнаяОбработка)
	СтандартнаяОбработка = Ложь;
	Поля.Добавить("Дата");
	Поля.Добавить("Номер");
	Поля.Добавить("ХозяйственнаяОперация");
КонецПроцедуры

Процедура ОбработкаПолученияПредставления(Данные, Представление, СтандартнаяОбработка)
	СтандартнаяОбработка = Ложь;
	Представление = НСтр("fr = 'Retour du client comptable'; ru = 'Возврат от покупателя налоговый'; en = 'Refund from the buyer tax'; es = 'Reembolso de impuestos del comprador'");
	ОбщегоНазначенияКлиентСервер.ДобавитьКСтроке(Представление, Данные.Номер, " ");
	ОбщегоНазначенияКлиентСервер.ДобавитьКСтроке(Представление, Данные.Дата, НСтр("ru = ' от '; fr = ' du '"));	
КонецПроцедуры

Function PrintTicket(Док, Spreadsheet) Export
	//{{_PRINT_WIZARD(Печать)
	//Template = Documents.FactureSortie.GetTemplate(TemplateName);
	//TableName = Ref.MetaData().Name;
	Template = ПечатныеФормы.МакетПечатнойФормы("Документ.РеализацияТоваровУслуг.Чек");
	Query = New Query;
	Query.Text =
	"ВЫБРАТЬ
	|	Doc.Ссылка.Контрагент КАК Client,
	|	Doc.Ссылка.Ответственный КАК Createur,
	|	Doc.Ссылка.Дата КАК Date,
	|	Doc.Ссылка.Основание.Номер КАК Number,
	|	Doc.Ссылка.Договор.ВалютаВзаиморасчётов КАК Devise,
	|	Doc.Ссылка.Сумма КАК TotalSomme,
	|	Doc.Ссылка.Ссылка КАК DocRef,
	|	Doc.КодСтроки КАК LineNumber,
	|	Doc.Номенклатура КАК Produit,
	|	Doc.Количество КАК Quantite,
	|	Doc.Цена КАК Prix,
	|	Doc.СтавкаНДС КАК TVA,
	|	Doc.СуммаНДС КАК SommeTVA,
	|	Doc.Сумма КАК Somme,
	|	Doc.СуммаСНДС КАК SommeTotale,
	|	Doc.Ссылка.Организация КАК Organisation,
	|	Doc.Ссылка.Основание КАК Основание,
	|	Doc.Ссылка КАК Ссылка
	|ИЗ
	|	Документ.ВозвратОтПокупателя.ТЧТовары КАК Doc
	|ГДЕ
	|	Doc.Ссылка = &Ref
	|ИТОГИ
	|	МАКСИМУМ(Client),
	|	МАКСИМУМ(Createur),
	|	МАКСИМУМ(Date),
	|	МАКСИМУМ(Number),
	|	МАКСИМУМ(Devise),
	|	МАКСИМУМ(TotalSomme),
	|	МАКСИМУМ(DocRef),
	|	МАКСИМУМ(Organisation),
	|	МАКСИМУМ(Основание)
	|ПО
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
		Header.Parameters.TypeDeTicket = "AVOIR";
		
		If Selection.Organisation <> Catalogs.Организации.EmptyRef() Then 
			FieldPhoto = Selection.Organisation.Логотип.Get();
			Try
				Header.Drawings[0].Picture = New Picture(FieldPhoto);
			Except
			EndTry;
		EndIf;
		
		ЗапросОплаты = Новый Запрос;
		ЗапросОплаты.Текст = 
		"ВЫБРАТЬ
		|	РасходныйКассовыйОрдер.Сумма КАК Сумма
		|ИЗ
		|	Документ.РасходныйКассовыйОрдер КАК РасходныйКассовыйОрдер
		|ГДЕ
		|	РасходныйКассовыйОрдер.Основание = &Основание
		|	И РасходныйКассовыйОрдер.Проведен";
		ЗапросОплаты.УстановитьПараметр("Основание",Selection.DocRef);
		Выборка = ЗапросОплаты.Выполнить().Выбрать();
		TotalSommePaiement = 0;
		Если Выборка.Следующий() Тогда 
			TotalSommePaiement = Выборка.Сумма;
		КонецЕсли;
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
		AreaTabularSectionFooterTotal.Parameters.TotalSommePaiement =  ""+Format(TotalSommePaiement,"ЧДЦ=2; ЧРГ=' '; ЧН=0,00");
		AreaTabularSectionFooterTotal.Parameters.ОстатокОплаты =  ""+Format(Selection.TotalSomme - TotalSommePaiement,"ЧДЦ=2; ЧРГ=' '; ЧН=0,00");
		Spreadsheet.Put(AreaTabularSectionFooterTotal);
		
		//Spreadsheet.BottomMargin = 20;
		
		//InsertPageBreak = True;
		Spreadsheet.PutHorizontalPageBreak();
		//PrintManagement.SetDocumentPrintArea(Spreadsheet, FirstRowNumber, PrintObjects, Selection.DocRef);
	EndDo; 
	
	Return Spreadsheet;
	
	//}}
EndFunction
