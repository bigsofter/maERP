#Область ПрограммныйИнтерфейс

// Перечисляет печатные формы объекта.
// См. ПечатныеФормы.НоваяКоллекцияКомандПечати
//
// Параметры:
//  КомандыПечати - ТаблицаЗначений - пополняемая коллекция команд печати
//
Процедура ДобавитьКомандыПечати(КомандыПечати) Экспорт

	// Avoir - фирменная форма под прежним именем и названием команды (docs/plans/branded-print.md, 11.3).
	ФирменнаяПечать.ДобавитьКоманду(КомандыПечати, "Avoir", "Avoir");

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

	ФирменнаяПечать.Напечатать("Avoir", "Avoir", МассивОбъектов, ПараметрыПечати, КоллекцияПечатныхФорм, ОбъектыПечати);

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

// Адаптер фирменной печати (см. ФирменнаяПечать.Напечатать): Avoir налоговых возвратов - общий запрос возвратов
// (Документы.ВозвратОтПокупателя.ДанныеВозвратовДляПечати).
//
// Параметры:
//  Ссылки          - Массив из ДокументСсылка.ВозвратОтПокупателяНалоговый - печатаемые возвраты.
//  ВидФормы        - Строка - вид фирменной формы: Avoir.
//  КодЯзыка        - Строка - язык печати.
//  ПараметрыПечати - Структура - параметры команды печати.
//
// Возвращаемое значение:
//  Соответствие - возврат -> источник печати (см. ФирменнаяПечать.ИсточникТоварногоДокумента).
//
Функция ДанныеФирменнойПечати(Ссылки, ВидФормы, КодЯзыка, ПараметрыПечати) Экспорт
	Возврат Документы.ВозвратОтПокупателя.ДанныеВозвратовДляПечати(Метаданные.Документы.ВозвратОтПокупателяНалоговый.Имя,
		Ссылки, КодЯзыка, ПараметрыПечати);
КонецФункции

#КонецОбласти

Процедура ОбработкаПолученияПолейПредставления(Поля, СтандартнаяОбработка)
	СтандартнаяОбработка = Ложь;
	Поля.Добавить("Дата");
	Поля.Добавить("Номер");
	Поля.Добавить("ХозяйственнаяОперация");
КонецПроцедуры

Процедура ОбработкаПолученияПредставления(Данные, Представление, СтандартнаяОбработка)
	СтандартнаяОбработка = Ложь;
	Представление = НСтр("fr = 'Avoir client'; ru = 'Возврат от покупателя налоговый'; en = 'Customer credit note'; es = 'Factura rectificativa emitida'");
	ОбщегоНазначенияКлиентСервер.ДобавитьКСтроке(Представление, Данные.Номер, " ");
	ОбщегоНазначенияКлиентСервер.ДобавитьКСтроке(Представление, Данные.Дата, НСтр("ru = ' от '; fr = ' du '; en = 'from'; es = 'de'"));	
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
