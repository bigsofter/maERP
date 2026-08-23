
#Область Обработчики_событий_формы

&AtServer
Procedure OnCreateAtServer(Cancel, StandardProcessing)
	РозничныйДоговор = Константы.РозничныйДоговор.Получить();
	РозничныйКлиент = Константы.РозничныйКлиент.Получить();
	РозничныйСклад = РегистрыСведений.НастройкиПользователей.СкладПользователя();
	//ЭтотОбъект.Заголовок = "" + РозничныйКлиент;
	//НадписьЗаголовок = "VENTE"+": "+РозничныйКлиент;
	Элементы.СтраницыИнформации.ТекущаяСтраница = Элементы.СтраницаИнформации;
	Object.Organisation = ПараметрыСеанса.Пользователь.Организация;
	Object.ХозяйственнаяОперация = Перечисления.ХозяйственныеОперации.РеализацияКлиенту;
	CurFacture = Документы.РеализацияТоваровУслуг.ПустаяСсылка();
	НадписьИнформацияОТоваре = "";
	НадписьТекущаяСумма = "";
	ImprimerFacture = Constants.ImprimerFactureVentesEnDetail.Get();
	ImprimerBL = Константы.ImprimerBL.Получить();
	ВыводитьЧекНаЭкрнПередПечатью = Constants.ВыводитьЧекНаЭкрнПередПечатью.Get();
	НадписьСдача = НСтр("fr = 'RETOUR'; ru = 'СДАЧА'; en = 'change'; es = 'DEPÓSITO'");
	КассоваяСмена = НайтиОткрытуюСмену();
	НастроитьФорму();
	ЭтоPDV = ЭтоPDV();
	Если ЭтоPDV Тогда 
		Элементы.Ajouter.Видимость = Не Константы.ЗапретитьРучнойВводТовара.Получить();
	КонецЕсли;
	Элементы.Payer.Видимость = ЭтоКассир();
	//Элементы.Vente.Видимость = Не ЭтоPDV;
	Элементы.PaiementDeCredit.Видимость = Не ЭтоPDV;
	Элементы.Rembourser.Видимость = Не ЭтоPDV;
	Элементы.СохранитьНакладную.Видимость = ЭтоPDV;
	Элементы.ГруппаРеестр.Видимость = ЭтоPDV;
	Элементы.ГруппаКОплате.Видимость = не ЭтоPDV;
	Элементы.ОтменитьПродажу.Видимость = Не ЭтоКассир() и не ЭтоPDV;

	Элементы.ЗакрытьСмену.Видимость = Не ЭтоPDV;
	Элементы.ВыемкаИзКассы.Видимость = Не ЭтоPDV;
	Элементы.ДобавитьДоход.Видимость = Не ЭтоPDV;
	Элементы.ДобавитьРасход.Видимость = Не ЭтоPDV;
	Элементы.Отчеты.Видимость = Не ЭтоPDV;
	Элементы.ИсторияКлиента.Видимость = ПравоДоступа("Просмотр", Метаданные.Отчеты.ИсторияКлиента);
	
	//Элементы.Valider.Видимость = ЭтоPDV;
	
	ЭлементОтбора = ДокументыВОжидании.Отбор.Элементы.Добавить(Тип("ЭлементОтбораКомпоновкиДанных"));
	ЭлементОтбора.ЛевоеЗначение = Новый ПолеКомпоновкиДанных("МестоХранения");
	ЭлементОтбора.ВидСравнения = ВидСравненияКомпоновкиДанных.Равно;
	ЭлементОтбора.ПравоеЗначение = РозничныйСклад;
	ЭлементОтбора.Использование = Истина;

	ЭлементОтбора = ДокументыВОжидании.Отбор.Элементы.Добавить(Тип("ЭлементОтбораКомпоновкиДанных"));
	ЭлементОтбора.ЛевоеЗначение = Новый ПолеКомпоновкиДанных("Ответственный");
	ЭлементОтбора.ВидСравнения = ВидСравненияКомпоновкиДанных.Равно;
	ЭлементОтбора.ПравоеЗначение = ПараметрыСеанса.Пользователь;
	ЭлементОтбора.Использование = Истина;
EndProcedure

&НаКлиенте
Процедура ПриОткрытии(Отказ)
	ОперацииСПодключаемымОборудованиемКлиент.ПодключитьОборудование(УникальныйИдентификатор, Истина); 
КонецПроцедуры

#КонецОбласти

#Область Обработчики_элементов_формы

&AtClient
Procedure Ajouter(Command)
	Элементы.СтраницыИнформации.ТекущаяСтраница = Элементы.СтраницаИнформации;
	FormParameters = New Structure("Контрагент",РозничныйКлиент);
	NotDescription = New NotifyDescription("AfterChoiceProduit",ThisObject);
	OpenForm("Справочник.Номенклатура.Форма.FormProduitsOnStock", FormParameters,,,,,NotDescription,FormWindowOpeningMode.LockWholeInterface);
EndProcedure

&AtClient
Procedure Modifier(Command)
	CurStr = items.TabularSection.CurrentData;
	If CurStr = Undefined Then 
		Return;
	EndIf;
	CurParameters = New Structure;
	CurParameters.Insert("Количество",CurStr.Количество);
	CurParameters.Insert("Цена",CurStr.Цена);
	CurParameters.Insert("Номенклатура",CurStr.Номенклатура);
	CurParameters.Insert("РедактироватьЦену", True);
	NotifyDescr = New NotifyDescription("AfterEditRaw",ThisObject);
	OpenForm("DataProcessor.VentesEnDetail.Form.ФормаРедактированияСтроки",CurParameters,,,,,NotifyDescr, РежимОткрытияОкнаФормы.БлокироватьОкноВладельца);
EndProcedure

&AtClient
Procedure Avoir(Command)
	Пар = Новый Структура("Контрагент, МасТовары, МестоХранения", РозничныйКлиент, ПолучитьМассивТоваровНаСервере(),РозничныйСклад);
	Оп = Новый ОписаниеОповещения("ПослеВыбораДокумента",ЭтаФорма);
	ОткрытьФорму("Документ.РеализацияТоваровУслуг.Форма.ФормаВыбораРозница",Пар,ЭтаФорма,,,,Оп,РежимОткрытияОкнаФормы.БлокироватьОкноВладельца);
	Object.ХозяйственнаяОперация = ПредопределенноеЗначение("Перечисление.ХозяйственныеОперации.ВозвратТоваровОтКлиента");
	НастроитьФорму();
EndProcedure

&AtClient
Procedure Payer(Command)
	Если Не Object.TabularSection.НайтиСтроки(Новый Структура("Цена",0)).Количество() = 0 Тогда 
		ОбщегоНазначенияКлиент.ВывестиИнформациюДляРМКУправляемой("", НСтр("fr = 'Produits sans prix détectés. La vente est impossible!'; ru = 'Обнаружены товары без цен. Проведение продажи невозможно!'; en = 'Products without prices were found. Conducting a sale is impossible!'; es = 'Se encontraron productos sin precios. ¡La venta es imposible!'"));
		Возврат;
	КонецЕсли;
	CurParameters = New Structure;
	CurParameters.Insert("Организация",Object.Organisation);
	CurParameters.Insert("ИтогПоОрганизации", ?(ЭтоВозврат, Мин(СуммаДокументаБезСкидок,СуммаОплачено), СуммаКОплате));
	CurParameters.Insert("ХозяйственнаяОперация", Object.ХозяйственнаяОперация); 
	CurParameters.Insert("ТолькоНеоплаченные", ЭтоКредит); 
	CurParameters.Insert("РозничныйКлиент", РозничныйКлиент); 
	NotifyDescr = New NotifyDescription("AfterPayment",ThisObject);
	OpenForm("DataProcessor.VentesEnDetail.Form.ФормаСложнойОплаты",CurParameters,,,,,NotifyDescr,FormWindowOpeningMode.LockWholeInterface);
EndProcedure

&AtClient
Procedure Fermer(Command)
	//Если ЭтоPDV Тогда
	//	Ответ = Вопрос(Нстр("fr = 'Quitter le programme?'; ru = 'Завершить работу с программой?'; en = 'Finish working with the program?'; es = '¿Cerrar el programa?'"), РежимДиалогаВопрос.ДаНет); 
	//	Отказ = (Ответ = КодВозвратаДиалога.Нет);
	//	Если Не Отказ Тогда 
	//		ЗавершитьРаботуСистемы(Истина);
	//	КонецЕсли;
	//Иначе
		Close();
	//КонецЕсли;
EndProcedure

&AtClient
Procedure TabularSectionAfterDeleteRow(Item)
	CalculateSumTotal();
EndProcedure

&AtClient
Procedure Remise(Command)
	//CurParameters = New Structure;
	//NotifyDescr = New NotifyDescription("AfterChoisirRemise",ThisObject);
	//OpenForm("DataProcessor.VentesEnDetail.Form.FormRemise",CurParameters,,,,,NotifyDescr,FormWindowOpeningMode.LockWholeInterface);
	CurParameters = New Structure;
	CurParameters.Insert("ЧислоВвода",RemisePourCent);
	CurParameters.Insert("Заголовок","Inserez pour-cent de remise");
	NotifyDescr = New NotifyDescription("AfterEditRemise",ThisObject,"PourcentDeRemise");
	OpenForm("DataProcessor.VentesEnDetail.Form.ФормаВводаЧисла",CurParameters,,,,,NotifyDescr,FormWindowOpeningMode.LockWholeInterface);
EndProcedure

&AtClient
Procedure TabularSectionOnActivateRow(Item)
	RefreshInfo();
	CurData = items.TabularSection.CurrentData;
	If CurData <> Undefined Then 
		ShowPicture(CurData.Номенклатура);
	EndIf;
EndProcedure

&AtClient
Procedure BarCode(Command)
	CurParameters = New Structure;
	CurParameters.Insert("ЧислоВвода",RemisePourCent);
	CurParameters.Insert("Заголовок","Inserez code de produit");
	CurParameters.Insert("ВозвращатьЧислоСтрокой",True);
	NotifyDescr = New NotifyDescription("AfterInputBarcode",ThisObject);
	OpenForm("DataProcessor.VentesEnDetail.Form.ФормаВводаЧисла",CurParameters,,,,,NotifyDescr,FormWindowOpeningMode.LockWholeInterface);
EndProcedure

&НаКлиенте
Процедура Vente(Команда)
	Если Не Object.TabularSection.Количество() = 0 Тогда 
		ОП = Новый ОписаниеОповещения("ПослеОтветаНаВопросСохранитьДокумент",ЭтаФорма);
		ПоказатьВопрос(ОП,НСтр("fr = 'Enregistrer le document ?'; ru = 'Сохранить документ?'; en = 'Save the document?'; es = '¿Guardar el documento?'"),РежимДиалогаВопрос.ДаНетОтмена);
	Иначе
		NewFacture();
		Object.ХозяйственнаяОперация = ПредопределенноеЗначение("Перечисление.ХозяйственныеОперации.РеализацияКлиенту");
		НастроитьФорму();
	КонецЕсли;
КонецПроцедуры

&НаКлиенте
Процедура Credit(Команда)
	NewFacture();
	Object.ХозяйственнаяОперация = ПредопределенноеЗначение("Перечисление.ХозяйственныеОперации.ПродажаВКредит");
	НастроитьФорму();
КонецПроцедуры

&НаКлиенте
Процедура ChooseClient(Команда)
	Оп = Новый ОписаниеОповещения("ПослеВыбораКлиента",ЭтаФорма);
	ОткрытьФорму("Справочник.Контрагенты.Форма.ФормаВыбораРозница",,ЭтаФорма,,,,Оп,РежимОткрытияОкнаФормы.БлокироватьОкноВладельца);
КонецПроцедуры

&НаКлиенте
Процедура PaiementDeCredit(Команда)
	Object.ХозяйственнаяОперация = ПредопределенноеЗначение("Перечисление.ХозяйственныеОперации.ПродажаВКредит");
	НастроитьФорму();
	Пар = Новый Структура("Контрагент, Операция, МестоХранения", РозничныйКлиент, ПредопределенноеЗначение("Перечисление.ХозяйственныеОперации.ПродажаВКредит"), РозничныйСклад);
	Оп = Новый ОписаниеОповещения("ПослеВыбораДокумента",ЭтаФорма);
	ОткрытьФорму("Документ.РеализацияТоваровУслуг.Форма.ФормаВыбораРозница",Пар,ЭтаФорма,,,,Оп,РежимОткрытияОкнаФормы.БлокироватьОкноВладельца);
КонецПроцедуры

&НаКлиенте
Процедура ОткрытьСмену(Команда)
	//ПоказатьВопрос(Оп,"Vérifiez le montant dans la caisse: " + Формат(ПолучитьОстатокВКассе(),),РежимДиалогаВопрос.ДаНетОтмена);
	ОткрытьСменуНаСервере();
	НастроитьФорму();
КонецПроцедуры

&НаКлиенте
Процедура ЗакрытьСмену(Команда)
	Оп = Новый ОписаниеОповещения("ПослеОтветаНаВопросЗакрытьСмену", ЭтаФорма);
	ПоказатьВопрос(Оп,Нстр("fr = 'Clôturer la journée?'; ru = 'Закрыть смену?'; en = 'Close the shift?'; es = '¿Cerrar el turno?'"),РежимДиалогаВопрос.ДаНет,10,,,КодВозвратаДиалога.Нет);
	//ЗакрытьСменуНаСервере();
	//CurParameters = New Structure;
	//CurParameters.Insert("ЧислоВвода",RemisePourCent);
	//CurParameters.Insert("Заголовок","Inserez le montant dans la caisse");
	//NotifyDescr = New NotifyDescription("AfterInputAmountInCaisse",ThisObject);
	//OpenForm("DataProcessor.VentesEnDetail.Form.ФормаВводаЧисла",CurParameters,,,,,NotifyDescr,FormWindowOpeningMode.LockWholeInterface);
КонецПроцедуры

&НаКлиенте
Процедура ПослеОтветаНаВопросЗакрытьСмену(Результат, ДопПараметры) Экспорт
	Если Результат = Неопределено Тогда Возврат; КонецЕсли;
	Если Результат = КодВозвратаДиалога.Да Тогда 
		ЗакрытьСменуНаСервере();
	КонецЕсли;
КонецПроцедуры

&НаКлиенте
Процедура Отчеты(Команда)
	Оп = Новый ОписаниеОповещения("ПослеВыбораОтчета",ЭтаФорма);
	СписокОтчетов = Новый СписокЗначений;
	СписокОтчетов.Добавить("EtatZ","Etat Z de la journée");
	//ПоказатьВыборИзМеню(Оп,СписокОтчетов,элементы.Отчеты);
	ПослеВыбораОтчета(СписокОтчетов.НайтиПоЗначению("EtatZ"), Неопределено);
КонецПроцедуры

&НаКлиенте
Процедура ИсторияКлиента(Команда)
	//УсловияОтбора = Новый Структура("Контрагент", РозничныйКлиент);
	//ПараметрыФормы = Новый Структура("Отбор, СформироватьПриОткрытии", УсловияОтбора, Истина);
	//ОткрытьФорму("Отчет.ИсторияКлиента.ФормаОбъекта", ПараметрыФормы);
	
	ИмяОтчета = "ИсторияКлиента";
	ПараметрыОткрытия = ПолучитьПараметрыОткрытияОтчета(ИмяОтчета, РозничныйКлиент);
	ОткрытьФорму("Отчет." + ИмяОтчета + ".ФормаОбъекта", ПараметрыОткрытия, ЭтотОбъект);
КонецПроцедуры

&НаКлиенте
Процедура ВыемкаИзКассы(Команда)
	CurParameters = New Structure;
	CurParameters.Insert("ЧислоВвода",RemisePourCent);
	CurParameters.Insert("Заголовок","Inserez le solde à la caisse");
	NotifyDescr = New NotifyDescription("AfterInputAmountInCaisse",ThisObject);
	OpenForm("DataProcessor.VentesEnDetail.Form.ФормаВводаЧисла",CurParameters,,,,,NotifyDescr,FormWindowOpeningMode.LockWholeInterface);
КонецПроцедуры

&НаКлиенте
Процедура TabularSectionОтметкаПриИзменении(Элемент)
	CalculateSumTotal();
КонецПроцедуры

&НаКлиенте
Процедура Valider(Команда)
	ОшибкаПроведенияДокумента = "";
	Если Object.TabularSection.Количество() = 0 Тогда Возврат; КонецЕсли;
	Если Не Object.TabularSection.НайтиСтроки(Новый Структура("Цена",0)).Количество() = 0 Тогда 
		ОбщегоНазначенияКлиент.ВывестиИнформациюДляРМКУправляемой("", НСтр("fr = 'Produits sans prix détectés. La vente est impossible!'; ru = 'Обнаружены товары без цен. Проведение продажи невозможно!'; en = 'Products without prices were found. Conducting a sale is impossible!'; es = 'Se encontraron productos sin precios. ¡La venta es imposible!'"));
		Возврат;
	КонецЕсли;
	Если Не ЗначениеЗаполнено(CurFacture) Тогда 
		CreateFacture();
	Иначе
		CreateFacture(,Ложь);
	КонецЕсли;
	Если ЗначениеЗаполнено(ОшибкаПроведенияДокумента) Тогда 
		ОбщегоНазначенияКлиент.ВывестиИнформациюДляРМКУправляемой("", ОшибкаПроведенияДокумента);
		Элементы.СтраницыИнформации.ТекущаяСтраница = Элементы.СтраницаИнформации;
		Возврат;
	КонецЕсли;
	NewFacture();
	
	RefreshInfo();
КонецПроцедуры

&НаКлиенте
Процедура ПечатьОтгрузкиТоваров(Команда)
	Если ЗначениеЗаполнено(CurFacture) Тогда
		Таб = Новый ТабличныйДокумент;
		ПечатьОтгрузкиТоваровНаСервере(Таб);
		ВыводПечатныхФормКлиент.ОткрытьПредварительныйПросмотр(Таб);
	КонецЕсли;
КонецПроцедуры

#КонецОбласти

#Область Оповещения

&НаКлиенте
Процедура ОбработкаОповещения(ИмяСобытия, Параметр, Источник)
	Если ИмяСобытия = "ScanData" и ВводДоступен() и ЭтоНоваяПродажа Тогда 
		Штрихкод = ОперацииСПодключаемымОборудованиемКлиент.ПолучитьШтрихкод(ИмяСобытия, Параметр, Источник);
		ТекстОшибки = "";
		РаботаСДокументамиКлиентСервер.ДобавитьНоменклатуруПоШтрихкоду(Штрихкод,Object,,"TabularSection",,ЭтаФорма, ТекстОшибки);
		Если Не ТекстОшибки = "" Тогда 
			ОбщегоНазначенияКлиент.ВывестиИнформациюДляРМКУправляемой("", ТекстОшибки);
		Иначе
			CalculateSumTotal();
			RefreshInfo();
		КонецЕсли;
	КонецЕсли;
КонецПроцедуры

&AtClient
Procedure AfterChoiceProduit(ResultOfChoice,AdParameters) Export
	If ResultOfChoice <> Undefined Then
		If Object.TabularSection.FindRows(New Structure("Номенклатура",ResultOfChoice.Номенклатура)).Count() = 0 Then 
			Str = Object.TabularSection.Add();
			FillPropertyValues(Str,ResultOfChoice);
			Str.СтавкаНДС = GetVATRateArServer(Str.Номенклатура);
			//Str.TVA = DocumentMethodes.GetTVARate(Object.Organisation,Str.Produit);
			РаботаСДокументамиКлиентСервер.РассчитатьСтроку(Str,Истина,"Цена");
			Items.TabularSection.CurrentRow = Str.GetID();
		EndIf;
		Modifier(Undefined);
	EndIf;
	CalculateSumTotal();
	RefreshInfo();
EndProcedure

&AtClient
Procedure AfterEditRaw(ResultOfEdit,AdParameters) Export
	If ResultOfEdit = Undefined Then
		Return;
	EndIf;
	CurStr = items.TabularSection.CurrentData;
	If CurStr = Undefined Then 
		Return;
	EndIf;
	FillPropertyValues(CurStr,ResultOfEdit);
	CalculateSum();
	RefreshInfo();
EndProcedure

&AtClient
Procedure AfterPayment(ResultOfEdit,AdParameters) Export
	If ResultOfEdit = Undefined Then
		Return;
	EndIf;
	
	AfterPaymentAtServer(ResultOfEdit);
	Если ЗначениеЗаполнено(ОшибкаПроведенияДокумента) Тогда 
		ОбщегоНазначенияКлиент.ВывестиИнформациюДляРМКУправляемой("", ОшибкаПроведенияДокумента);
		Элементы.СтраницыИнформации.ТекущаяСтраница = Элементы.СтраницаИнформации;
		Возврат;
	КонецЕсли;
	
	If (ImprimerFacture Или ImprimerBL) And CurFacture <> PredefinedValue("Документ.РеализацияТоваровУслуг.ПустаяСсылка") Then
		Spreadsheet = New SpreadsheetDocument;
		Печатать = ImprimerFacture;
		Если ЭтоВозврат И Не ДокВозврат = ПредопределенноеЗначение("Документ.ВозвратОтПокупателя.ПустаяСсылка") Тогда 
			PrintAtServer(ДокВозврат,Spreadsheet);
			Таб = Новый ТабличныйДокумент;
			СформироватьПечатнуюФормуВозврата(ДокВозврат, Таб);	
			ВыводПечатныхФормКлиент.ОткрытьПредварительныйПросмотр(Таб);
		ИначеЕсли (ЭтоПродажа или ЭтоКредит) и не CurFacture = PredefinedValue("Документ.РеализацияТоваровУслуг.ПустаяСсылка") Then
			PrintAtServer(CurFacture,Spreadsheet);
			// Накладная (BL) печатается при включённой константе ImprimerBL для любой продажи, а не только в кредит.
			Если ImprimerBL И ЗначениеЗаполнено(CurFacture) Тогда
				Таб = Новый ТабличныйДокумент;
				ПечатьОтгрузкиТоваровНаСервере(Таб);
				ВыводПечатныхФормКлиент.ОткрытьПредварительныйПросмотр(Таб);
			КонецЕсли;
		Иначе
			Печатать = Ложь;
		КонецЕсли;
		Если Печатать Тогда 
			Spreadsheet.PageOrientation = PageOrientation.Portrait;
			//Spreadsheet.PageSize = "A4";
			Spreadsheet.FitToPage = True;
			Spreadsheet.ShowGrid = False;
			Spreadsheet.ShowHeaders = False;
			Spreadsheet.Protection = False;
			Spreadsheet.ПолеСверху = 5;
			Spreadsheet.ПолеСлева = 0;
			Spreadsheet.ПолеСнизу = 15;
			Spreadsheet.ПолеСправа = 10;
			Spreadsheet.ИмяПринтера = ОбщегоНазначенияВызовСервера.ПолучитьИмяПринтераЧековНаСервере();
			//Spreadsheet.ИмяПринтера = "ZKP8008";
			Если ВыводитьЧекНаЭкрнПередПечатью Тогда 
				Spreadsheet.Показать();
			Иначе
				Spreadsheet.Напечатать(РежимИспользованияДиалогаПечати.НеИспользовать);
			КонецЕсли;
		КонецЕсли;
	EndIf;
	NewFacture();
	
	RefreshInfo();
EndProcedure

&AtClient
Procedure AfterChoisirRemise(ResultOfEdit,AdParameters) Export
	//If ResultOfEdit = Undefined Then
	//	Return;
	//EndIf;
	//CurParameters = New Structure;
	//If ResultOfEdit = "PourcentDeRemise" Then
	//	CurParameters.Insert("ЧислоВвода",RemisePourCent);
	//	CurParameters.Insert("Заголовок","Inserez pour-cent de remise");
	//Else 
	//	CurParameters.Insert("ЧислоВвода",СуммаСкидки);
	//	CurParameters.Insert("Заголовок","Inserez somme de remise");
	//EndIf;
	//NotifyDescr = New NotifyDescription("AfterEditRemise",ThisObject,ResultOfEdit);
	//OpenForm("DataProcessor.VentesEnDetail.Form.ФормаВводаЧисла",CurParameters,,,,,NotifyDescr,FormWindowOpeningMode.LockWholeInterface);
EndProcedure

&AtClient
Procedure AfterEditRemise(ResultOfEdit,AdParameters) Export
	If ResultOfEdit = Undefined Then
		Return;
	EndIf;
	For each Str in Object.TabularSection Do
		РаботаСДокументамиКлиентСервер.РассчитатьСтроку(Str,Истина,"Цена");
	EndDo;
	СуммаДокументаБезСкидок = Object.TabularSection.Total("СуммаСНДС");
	RemisePourCent = ResultOfEdit.ВведенноеЧисло;
	CalculateSumTotal();
	//If AdParameters = "PourcentDeRemise" Then 
	//	СуммаСкидки = СуммаДокументаБезСкидок * RemisePourCent/100;
	//Else
	//	СуммаСкидки = ResultOfEdit.ВведенноеЧисло;
	//	RemisePourCent = ?(СуммаДокументаБезСкидок = 0,0,Round(СуммаСкидки/СуммаДокументаБезСкидок*100,2));
	//EndIf;
	//СуммаСкидки = Object.TabularSection.Total("СуммаСкидки")
	Items.СуммаСкидки.Title = "Remise "+RemisePourCent+"%";
	RefreshInfo();
EndProcedure

&AtClient
Procedure AfterInputBarcode(ResultOfEdit,AdParameters) Export
	If ResultOfEdit = Undefined Then
		Return;
	EndIf;
	BarCode = ResultOfEdit.ВведенноеЧисло;
	If СокрЛП(BarCode) = "" Then 
		Return;
	EndIf;
	ProductStructure = StructureProductByBarCode(BarCode);
	If ProductStructure = Undefined Then
		Return;
	EndIf;
	If Object.TabularSection.FindRows(New Structure("Номенклатура,Серия",ProductStructure.Номенклатура,ProductStructure.Серия)).Count() = 0 Then 
		Str = Object.TabularSection.Add();
		FillPropertyValues(Str,ProductStructure);
		//Str.TVA = DocumentMethodes.GetTVARate(Object.Organisation,Str.Produit);
		РаботаСДокументамиКлиентСервер.РассчитатьСтроку(Str,Истина);
		Items.TabularSection.CurrentRow = Str.GetID();
	EndIf;
	CalculateSumTotal();
	RefreshInfo();
EndProcedure

&НаКлиенте
Процедура ПослеВыбораКлиента(Результат, ДопПараметры) Экспорт
	Если Результат = Неопределено Тогда возврат; КонецЕсли;
	РозничныйКлиент = Результат;
	РозничныйДоговор = ОбщегоНазначенияВызовСервера.ПолучитьОсновнойДоговор(РозничныйКлиент, Object.Organisation, Истина);
	//Если РозничныйДоговор = ПредопределенноеЗначение("Справочник.ДоговорыСКонтрагентами.ПустаяСсылка") Тогда
	//	РозничныйДоговор = СоздатьДоговорНаСервере(РозничныйКлиент);
	//КонецЕсли;
	НастроитьФорму();
КонецПроцедуры

&НаКлиенте
Процедура ПослеВыбораДокумента(Результат, ДопПараметры) Экспорт
	Если Результат = Неопределено Тогда 
		NewFacture();
		Object.ХозяйственнаяОперация = ПредопределенноеЗначение("Перечисление.ХозяйственныеОперации.РеализацияКлиенту");
		НастроитьФорму();
		возврат;
	КонецЕсли;
	CurFacture = Результат.Документ;
	ЗаполнитьПоДокументуНаСЕрвере();
	CalculateSumTotal();
	RefreshInfo();
	СуммаОплачено = Object.TabularSection.Total("СуммаСНДС") - Результат.СуммаОстаток;
	СуммаКОплате = Результат.СуммаОстаток;
	НастроитьФорму();
КонецПроцедуры

&AtClient
Procedure AfterInputAmountInCaisse(ResultOfEdit,AdParameters) Export
	If ResultOfEdit = Undefined Then
		Return;
	EndIf;
	//ЗакрытьСменуНаСервере(ResultOfEdit.ВведенноеЧисло);
	ВведенноеЧисло = ?(ResultOfEdit.ВведенноеЧисло = Неопределено, 0, ResultOfEdit.ВведенноеЧисло);
	Док = ВыемкаИзКассыНаСервере(ВведенноеЧисло);
	ПоказатьЗначение(,Док);
	//НастроитьФорму();
EndProcedure

&НаКлиенте
Процедура ПослеВыбораОтчета(Результат, ДопПараметры) Экспорт
	Если Результат = Неопределено Тогда возврат; КонецЕсли;
	Если Результат.Значение = "EtatZ" Тогда 
		Если ЗначениеЗаполнено(КассоваяСмена) Тогда 
			Spreadsheet = Новый ТабличныйДокумент;
			ПечатьEtatZНаСервере(Spreadsheet);
			Spreadsheet.PageOrientation = PageOrientation.Portrait;
			//Spreadsheet.PageSize = "A4";
			Spreadsheet.FitToPage = True;
			Spreadsheet.ShowGrid = False;
			Spreadsheet.ShowHeaders = False;
			Spreadsheet.Protection = False;
			Spreadsheet.ПолеСверху = 5;
			Spreadsheet.ПолеСлева = 0;
			Spreadsheet.ПолеСнизу = 20;
			Spreadsheet.ПолеСправа = 10;
			Spreadsheet.ИмяПринтера = ОбщегоНазначенияВызовСервера.ПолучитьИмяПринтераЧековНаСервере();
			//Spreadsheet.ИмяПринтера = "ZKP8008";
			Spreadsheet.Напечатать(РежимИспользованияДиалогаПечати.НеИспользовать);
		КонецЕсли;
	КонецЕсли;
КонецПроцедуры

&НаКлиенте
Процедура ПослеОтветаНаВопросСохранитьДокумент(Результат, ДопПараметры) Экспорт
	Если Результат = Неопределено Тогда возврат; КонецЕсли;
	Если Результат = КодВозвратаДиалога.Отмена Тогда
		Возврат;
	ИначеЕсли Результат = КодВозвратаДиалога.Да Тогда 
		СохранитьНакладную(Неопределено);
	КонецЕсли;
	Если ЗначениеЗаполнено(CurFacture) Или Результат = КодВозвратаДиалога.Нет Тогда 
		NewFacture();
		Object.ХозяйственнаяОперация = ПредопределенноеЗначение("Перечисление.ХозяйственныеОперации.РеализацияКлиенту");
		НастроитьФорму();
	КонецЕсли;
КонецПроцедуры

#КонецОбласти

#Область Дополнительно  

&AtServer
Функция СоздатьВозвратНаСервере(Док)
	CurDoc = Документы.ВозвратОтПокупателя.СоздатьДокумент();
	CurDoc.Date = ТекущаяДатаСеанса();
	CurDoc.Заполнить(Док);
	CurDoc.Ответственный = ПараметрыСеанса.Пользователь;
	CurDoc.КассоваяСмена = КассоваяСмена;
    CurDoc.ТЧТовары.Очистить();
	
	For Each Str in Object.TabularSection Do
		Если Не Str.Отметка Тогда Продолжить; КонецЕсли;
		NewStr = CurDoc.ТЧТовары.Add();
		FillPropertyValues(NewStr,Str);
		NewStr.СтавкаНДС = NewStr.Номенклатура.СтавкаНДС;
		NewStr.КоличествоУпаковок = Str.Количество;
		РаботаСДокументамиКлиентСервер.РассчитатьСтроку(NewStr,Истина,"Цена");
		//NewStr.SommeTotale = NewStr.Somme - NewStr.Remise;
	EndDo;
	CurDoc.Сумма = CurDoc.ТЧТовары.Итог("СуммаСНДС");
	
	Try
		CurDoc.Write(DocumentWriteMode.Posting);
	Except
		WriteLogEvent("CreateAvoir",,,,ErrorDescription());
		Return Документы.ВозвратОтПокупателя.EmptyRef();
	EndTry;
	
	Return CurDoc.Ref;
КонецФункции

&AtServer
Procedure AfterPaymentAtServer(ResultOfEdit) 
	
	ТаблицаОплаты = ПолучитьИзВременногоХранилища(ResultOfEdit.АдресТаблицыОплата);
	
	Сдача = Макс(ТаблицаОплаты.Итог("Сумма") - ?(ЭтоВозврат, Мин(СуммаДокументаБезСкидок,СуммаОплачено), СуммаКОплате),0);
	Если Сдача = 0 Тогда
		НадписьСуммаСдачи = "0,00";
	Иначе
		НадписьСуммаСдачи = Формат(Сдача, "ЧЦ=15; ЧДЦ=2; ЧГ=3,0");
	КонецЕсли;
	
	ВыведенаСдача = Истина;
	ОставлятьФлагТаблоСдачи = Истина;
	Элементы.СтраницыИнформации.ТекущаяСтраница = Элементы.СтраницаСдача;
	ОшибкаПроведенияДокумента = "";
	Если ЭтоПродажа Тогда
		ЭтоКредит = Не ТаблицаОплаты.Найти(PredefinedValue("Справочник.TypesDePayment.Credit")) = Неопределено;
		Если ЭтоКредит Тогда 
			Object.ХозяйственнаяОперация = ПредопределенноеЗначение("Перечисление.ХозяйственныеОперации.ПродажаВКредит");
		КонецЕсли;
		CurFacture = CreateFacture(,CurFacture = Документы.РеализацияТоваровУслуг.ПустаяСсылка());
		ОснованиеОплаты = CurFacture;
	ИначеЕсли ЭтоВозврат Тогда 
		Если CurFacture = Документы.РеализацияТоваровУслуг.ПустаяСсылка() Тогда 
			возврат;
		КонецЕсли;
		ДокВозврат = СоздатьВозвратНаСервере(CurFacture);
		ОснованиеОплаты = ДокВозврат.Основание;
	ИначеЕсли ЭтоКредит Тогда 
		ОснованиеОплаты = CurFacture;
	КонецЕсли;
	
	If Не ЗначениеЗаполнено(ОснованиеОплаты) Then
		Return;
	EndIf;
	
	For Each Str in ТаблицаОплаты Do
		If Str.ВидОплаты = PredefinedValue("Справочник.TypesDePayment.Cash") Then 
			SommeOfPayment = Str.Сумма - Сдача;
		ИначеЕсли Str.ВидОплаты = PredefinedValue("Справочник.TypesDePayment.Credit") Then
			Продолжить;
		ИначеЕсли Str.ВидОплаты = PredefinedValue("Справочник.TypesDePayment.Сертификат") Then
			Сертификат = Документы.СертификатНаОплату.НайтиПоНомеру(Str.Сертификат);
			Если Не Сертификат = Документы.СертификатНаОплату.ПустаяСсылка() Тогда 
				ДокСертификат = Сертификат.ПолучитьОбъект();
				ДокСертификат.Реализация = CurFacture;
				ДокСертификат.КассоваяСмена = КассоваяСмена;
				ДокСертификат.Записать(РежимЗаписиДокумента.Проведение);
			КонецЕсли;
			Продолжить;
		Else 
			SommeOfPayment = Str.Сумма;
		EndIf;
		CreatePayment(Str,ОснованиеОплаты,SommeOfPayment,Str.ВидОплаты, Str.Чек);
	EndDo;
	
	//If ImprimerFacture And CurFacture <> PredefinedValue("Document.FactureSortie.EmptyRef") Then
	//	Spreadsheet = PrintAtServer(CurFacture);
	//EndIf;
	
EndProcedure

&AtClient
Procedure CalculateSum(CurRaw = Undefined)
	if CurRaw = Undefined Then 
		CurRaw = Items.TabularSection.CurrentData;
	EndIf;
	if CurRaw = Undefined Then 
		Return;
	EndIf;
	//Str = DocumentMethodes.GetRawStructure();
	//FillPropertyValues(Str,CurRaw);
	РаботаСДокументамиКлиентСервер.РассчитатьСтроку(CurRaw,Истина);
	//FillPropertyValues(CurRaw,Str);
	CalculateSumTotal();
EndProcedure

&AtClient
Procedure CalculateSumTotal()
	СуммаДокументаБезСкидок = 0; //Object.TabularSection.Total("СуммаСНДС");
	//СуммаСкидки = СуммаДокументаБезСкидок * RemisePourCent/100;
	//СуммаКОплате = СуммаДокументаБезСкидок - СуммаСкидки;
	
	RemiseTotal = 0;
	For Each Str in Object.TabularSection Do
		Если ЭтоВозврат и Не Str.Отметка Тогда Продолжить; КонецЕсли;
		СуммаДокументаБезСкидок = СуммаДокументаБезСкидок+Str.СуммаСНДС;
		//If Object.TabularSection.IndexOf(Str)+1 = Object.TabularSection.Count() Then 
		//	Str.СуммаСкидки = СуммаСкидки - RemiseTotal;
		//Else
			Str.ПроцентСкидки = RemisePourCent;
			Str.СуммаСкидки = Str.СуммаСНДС*RemisePourCent/100;
			RemiseTotal = RemiseTotal + Str.СуммаСкидки;
		//EndIf;
		Str.СуммаСНДС = Str.СуммаСНДС - Str.СуммаСкидки;
	EndDo;
	СуммаСкидки = RemiseTotal;
	СуммаКОплате = СуммаДокументаБезСкидок - СуммаОплачено - СуммаСкидки;
	
EndProcedure

&AtServer
Function GetVATRateArServer(Номенклатура)
	Return Номенклатура.СтавкаНДС;
EndFunction

&AtServer
Function GetFactureNumber()
	Return CurFacture.Number;
EndFunction

&AtServer
Function PrintAtServer(CurDoc,Spreadsheet)
	Spreadsheet = New SpreadsheetDocument;
	//Template = "Facture";
	//Documents.FactureSortie.Print(Spreadsheet, CurFacture.Ref,Template);
	Если ЭтоВозврат Тогда 
		Документы.ВозвратОтПокупателя.PrintTicket(CurDoc, Spreadsheet);
	Иначе
		Документы.РеализацияТоваровУслуг.PrintTicket(CurDoc, Spreadsheet);
	КонецЕсли;
	Return Spreadsheet;
EndFunction

&AtServer
Procedure CreatePayment(Str,ОснованиеОплаты,SommeOfPayment, ТипОплаты = Неопределено, Чек = Неопределено)
	If ТипОплаты = PredefinedValue("Справочник.TypesDePayment.VirementBanquaire") Then
		CurDoc = ?(ЭтоВозврат, Документы.СписаниеБезналичныхДенежныхСредств.СоздатьДокумент(), Документы.ПоступлениеБезналичныхДенежныхСредств.СоздатьДокумент());
		CurDoc.БанковскийСчёт = Str.Счет;
	Else
		CurDoc = ?(ЭтоВозврат, Документы.РасходныйКассовыйОрдер.СоздатьДокумент(), Документы.ПриходныйКассовыйОрдер.СоздатьДокумент());
		CurDoc.Касса = РегистрыСведений.НастройкиПользователей.КассаПользователя();
		Если ТипОплаты = Справочники.TypesDePayment.Cheque Тогда 
			CurDoc.Чек = Чек;
		КонецЕсли;
	EndIf;
	CurDoc.КассоваяСмена = КассоваяСмена; 
	Structure = New Structure("Документ,Сумма,ТипОплаты",ОснованиеОплаты,SommeOfPayment,ТипОплаты);
	CurDoc.Заполнить(Structure);
	CurDoc.Date = ТекущаяДатаСеанса();
	Если ЭтоВозврат Тогда 
		CurDoc.Основание = ДокВозврат;
	КонецЕсли;
	Попытка
		CurDoc.write(DocumentWriteMode.Posting);
	Исключение
		WriteLogEvent("CreatePayment",,,,ErrorDescription());
	Конецпопытки;
EndProcedure

&AtServer
Procedure NewFacture()
	Object.ХозяйственнаяОперация = Перечисления.ХозяйственныеОперации.РеализацияКлиенту;
	//CurDoc = Документы.РеализацияТоваровУслуг.ПустаяСсылка();
	CurFacture = Документы.РеализацияТоваровУслуг.ПустаяСсылка();
	РозничныйДоговор = Константы.РозничныйДоговор.Получить();
	РозничныйКлиент = Константы.РозничныйКлиент.Получить();
	СуммаДокументаБезСкидок = 0;
	СуммаСкидки = 0;
	СуммаОплачено = 0;
	СуммаКОплате = 0;
	RemisePourCent = 0;
	FieldPhoto = "";
	Object.TabularSection.Clear();
	НастроитьФорму();
EndProcedure

&AtServer
Function CreateFacture(Черновик = Ложь, СоздаватьДокумент = Истина)
	Если СоздаватьДокумент Тогда 
		CurDoc = Документы.РеализацияТоваровУслуг.СоздатьДокумент();
		CurDoc.Date = ТекущаяДатаСеанса();
		CurDoc.Контрагент = РозничныйКлиент;
		CurDoc.Договор = РозничныйДоговор;
		CurDoc.КассоваяСмена = КассоваяСмена;
		CurDoc.Ответственный = ПараметрыСеанса.Пользователь;
		CurDoc.ХозяйственнаяОперация = Object.ХозяйственнаяОперация;
		CurDoc.МестоХранения = РозничныйСклад;
		CurDoc.Организация = Object.Organisation;
	Иначе
		CurDoc = CurFacture.ПолучитьОбъект();
		//CurDoc.Записать(РежимЗаписиДокумента.ОтменаПроведения);
		CurDoc.Контрагент = РозничныйКлиент;
		CurDoc.Договор = РозничныйДоговор;
		CurDoc.КассоваяСмена = КассоваяСмена;
		CurDoc.ХозяйственнаяОперация = Object.ХозяйственнаяОперация;
		CurDoc.Date = ТекущаяДатаСеанса();
	КонецЕсли;
	
	CurDoc.ТЧТовары.Очистить();
	For Each Str in Object.TabularSection Do
		NewStr = CurDoc.ТЧТовары.Add();
		FillPropertyValues(NewStr,Str);
		NewStr.ВидЦены = Справочники.ВидыЦен.Розничная;
		NewStr.СтавкаНДС = NewStr.Номенклатура.СтавкаНДС;
		NewStr.КоличествоУпаковок = Str.Количество;
		NewStr.ПроцентСкидки = Str.ПроцентСкидки;
		РаботаСДокументамиКлиентСервер.РассчитатьСтроку(NewStr,Истина,"Цена");
		//NewStr.SommeTotale = NewStr.Somme - NewStr.Remise;
	EndDo;
	CurDoc.Сумма = CurDoc.ТЧТовары.Итог("СуммаСНДС")+CurDoc.ТЧУслуги.Итог("СуммаСНДС");
	CurDoc.СуммаНДС = CurDoc.ТЧТовары.Итог("СуммаНДС")+CurDoc.ТЧУслуги.Итог("СуммаНДС");
	
	Try
		CurDoc.ДополнительныеСвойства.Вставить("ЭтоИнтерфейсПродавца",Истина);
		CurDoc.Write(?(Черновик, DocumentWriteMode.Write, DocumentWriteMode.Posting));
	Except
		Если CurDoc.ДополнительныеСвойства.Свойство("ТекстОшибки") Тогда 
			ОшибкаПроведенияДокумента = CurDoc.ДополнительныеСвойства.ТекстОшибки;
		КонецЕсли;
		WriteLogEvent("CreateFacture",,,,ErrorDescription());
		Return Документы.РеализацияТоваровУслуг.EmptyRef();
	EndTry;
	
	Return CurDoc.Ref;
	
EndFunction

&AtClient
Procedure RefreshInfo()
	CurStr = items.TabularSection.CurrentData;
	
	Если CurStr = Неопределено Тогда
		НадписьИнформацияОТоваре = "";
		НадписьТекущаяСумма = "";
		Возврат;
	КонецЕсли;
	ProduitDescriptif = ОбщегоНазначенияВызовСервера.ЗначениеРеквизитаОбъекта(CurStr.Номенклатура,"НаименованиеПолное");	
	НадписьИнформацияОТоваре = ?(ValueIsFilled(ProduitDescriptif),ProduitDescriptif,ОбщегоНазначенияВызовСервера.ЗначениеРеквизитаОбъекта(CurStr.Номенклатура,"Наименование"));
	//НадписьИнформацияОТоваре = ОбщегоНазначенияВызовСервера.ЗначениеРеквизитаОбъекта(CurStr.Номенклатура,"Наименование") + Символы.ПС 
	//	+ ОбщегоНазначенияВызовСервера.ЗначениеРеквизитаОбъекта(CurStr.Номенклатура,"НаименованиеПолное");
	НадписьИнформацияОТоваре = НадписьИнформацияОТоваре + Символы.ПС;
	НадписьЯчейка = "Emplacement: " + ПолучитьЯчейкиНаСервере(CurStr.Номенклатура);
	InfoDiscount = "";
	If CurStr.СуммаСкидки <> 0 and CurStr.СуммаСНДС <> 0 Then
		InfoDiscount = " - " + Format(CurStr.СуммаСкидки,"NFD=2") + " ( " + Round(CurStr.ПроцентСкидки*100,2) + "%) ";
	EndIf;
	VATRate = ОбщегоНазначенияВызовСервераПовтИсп.ПроцентСтавкиНДС(GetVATRateArServer(CurStr.Номенклатура));
	НадписьТекущаяСумма = "" + Format(CurStr.Цена,"NFD=2") + " x " + 
		CurStr.Количество + InfoDiscount + " = " + Format(CurStr.СуммаСНДС,"NFD=2");
EndProcedure

&AtServer
Function StructureProductByBarCode(BarCode)
	Query = New Query;
	Query.Text = "ВЫБРАТЬ
	             |	ШтрихкодыНоменклатуры.Номенклатура КАК Номенклатура,
	             |	ШтрихкодыНоменклатуры.Характеристика КАК Характеристика,
	             |	ШтрихкодыНоменклатуры.Упаковка КАК Упаковка,
	             |	ШтрихкодыНоменклатуры.Серия КАК Серия
	             |ПОМЕСТИТЬ ВТ
	             |ИЗ
	             |	РегистрСведений.ШтрихкодыНоменклатуры КАК ШтрихкодыНоменклатуры
	             |ГДЕ
	             |	ШтрихкодыНоменклатуры.Штрихкод = &Штрихкод
	             |;
	             |
	             |////////////////////////////////////////////////////////////////////////////////
	             |ВЫБРАТЬ
	             |	StockBalance.Номенклатура КАК Номенклатура,
	             |	StockBalance.Характеристика КАК Характеристика,
	             |	StockBalance.КоличествоОстаток КАК Количество,
	             |	ЕСТЬNULL(PrixDeProduitSliceLast.Цена, 0) КАК Цена,
	             |	StockBalance.Серия КАК Серия
	             |ИЗ
	             |	РегистрНакопления.ТоварыВНаличии.Остатки(
	             |			,
	             |			(Номенклатура, Характеристика, Серия) В
	             |				(ВЫБРАТЬ
	             |					ВТ.Номенклатура,
	             |					ВТ.Характеристика,
	             |					ВТ.Серия
	             |				ИЗ
	             |					ВТ)) КАК StockBalance
	             |		ЛЕВОЕ СОЕДИНЕНИЕ РегистрСведений.ЦеныНоменклатуры.СрезПоследних КАК PrixDeProduitSliceLast
	             |		ПО StockBalance.Номенклатура = PrixDeProduitSliceLast.Номенклатура
	             |			И StockBalance.Характеристика = PrixDeProduitSliceLast.Характеристика
	             |			И (PrixDeProduitSliceLast.ВидЦены = ЗНАЧЕНИЕ(Справочник.ВидыЦен.Розничная))
	             |			И (PrixDeProduitSliceLast.Активность)";
	Query.SetParameter("Штрихкод",BarCode);
	Result = Query.Execute();
	If Result.IsEmpty() Then
		Return Undefined;
	EndIf;
	
	ResultOfChoice = Result.Select();
	ResultOfChoice.Next();
	
	ProductStructure = New Structure("Номенклатура,Характеристика,Серия,Количество,Цена",ResultOfChoice.Номенклатура,ResultOfChoice.Характеристика,ResultOfChoice.Серия,1,ResultOfChoice.Цена);
	Return ProductStructure;
	
EndFunction

&AtServer
Procedure ShowPicture(Produit)
	НЗ = РегистрыСведений.ПрисоединённыеФайлы.СоздатьНаборЗаписей();
	НЗ.Отбор.Объект.Установить(Produit);
	НЗ.Прочитать();
	Если НЗ.Количество() = 0 Тогда 
		FieldPhoto = "";
	Иначе
		ID = НЗ.Получить(0).ID;
		КлючЗаписиРег = РегистрыСведений.ПрисоединённыеФайлы.СоздатьКлючЗаписи(Новый Структура("Объект,ID", Produit.Ссылка,ID));
		Если Не КлючЗаписиРег.Пустой() Тогда
			FieldPhoto = ПолучитьНавигационнуюСсылку(КлючЗаписиРег, "Данные");
		КонецЕсли;
	КонецЕсли;
EndProcedure

&НаСервере
Процедура НастроитьФорму()
	СменаОткрыта = ЗначениеЗаполнено(КассоваяСмена) и КассоваяСмена.Статус = Перечисления.СтатусыКассовойСмены.Открыта;
	ЭтоНоваяПродажа = CurFacture = Документы.РеализацияТоваровУслуг.ПустаяСсылка() Или Не CurFacture.Проведен;
	ЭтоПродажа = Object.ХозяйственнаяОперация = Перечисления.ХозяйственныеОперации.РеализацияКлиенту;
	ЭтоКредит = Object.ХозяйственнаяОперация = Перечисления.ХозяйственныеОперации.ПродажаВКредит;
	ЭтоВозврат = Object.ХозяйственнаяОперация = Перечисления.ХозяйственныеОперации.ВозвратТоваровОтКлиента;
	МассивКонтрагентов = Новый Массив;
	МассивКонтрагентов.Добавить(РозничныйКлиент);
	ТЗОстатокДолга = РегистрыНакопления.ВзаиморасчётыСПокупателями.ПолучитьЗадолженностьКлиентовПоКлассификации(ТекущаяДата(), Новый Структура("Контрагенты",МассивКонтрагентов));
	ОстатокДолга = Формат(ТЗОстатокДолга.Итог("Долг"),"ЧДЦ=2; ЧН=0,00");
	ДатаПоследнейПродажи = ПолучитьДатуПоследнейПродажи();
	НадписьДатаПоследнейПродажи = "";
	Если ЗначениеЗаполнено(ДатаПоследнейПродажи) Тогда 
		НадписьДатаПоследнейПродажи = ". "+Формат(ДатаПоследнейПродажи,"ДЛФ=D");
	КонецЕсли;
	Если ЭтоПродажа Тогда 
		НадписьЗаголовок = "VENTE"+": "+РозничныйКлиент + " Solde: "+ ОстатокДолга + НадписьДатаПоследнейПродажи;
		Элементы.Payer.Заголовок = "Payer";
	ИначеЕсли ЭтоВозврат Тогда 
		НадписьЗаголовок = "AVOIR"+": "+РозничныйКлиент + " Solde: "+ ОстатокДолга + НадписьДатаПоследнейПродажи;
		Элементы.Payer.Заголовок = "Rembourser";
	Иначе
		НадписьЗаголовок = "CREDIT"+": "+РозничныйКлиент + " Solde: "+ ОстатокДолга + НадписьДатаПоследнейПродажи;
		Элементы.Payer.Заголовок = "Payer";
	КонецЕсли;
	Элементы.Vente.КнопкаПоУмолчанию = ЭтоПродажа;
	//Элементы.Credit.КнопкаПоУмолчанию = ЭтоКредит;
	Элементы.Rembourser.КнопкаПоУмолчанию = ЭтоВозврат;
	//Элементы.ChooseClient.Доступность = Не ЭтоПродажа;
	//Элементы.PaiementDeCredit.Доступность = Не ЭтоПродажа;
	Элементы.PaiementDeCredit.КнопкаПоУмолчанию = ЭтоКредит;
	Элементы.СтраницыИнформации.ТекущаяСтраница = Элементы.СтраницаИнформации;
	Элементы.Ajouter.Доступность = ЭтоНоваяПродажа;
	Элементы.BarCode.Доступность = ЭтоНоваяПродажа;
	Элементы.Valider.Доступность = ЭтоНоваяПродажа;
	Элементы.Modifier.Доступность = ЭтоНоваяПродажа или ЭтоВозврат;
	Элементы.Suprimer.Доступность = ЭтоНоваяПродажа или ЭтоВозврат;
	Элементы.TabularSection.ТолькоПросмотр = Не (ЭтоНоваяПродажа или ЭтоВозврат);
	Элементы.GroupInfo.Доступность = СменаОткрыта;
	Элементы.ОткрытьСмену.Доступность = не СменаОткрыта;
	Элементы.ЗакрытьСмену.Доступность = СменаОткрыта;
	Элементы.Отчеты.Доступность = ЗначениеЗаполнено(КассоваяСмена);
	Элементы.TabularSectionОтметка.Видимость = ЭтоВозврат;
	ЭтотОбъект.Заголовок = "" + РозничныйКлиент;
КонецПроцедуры

&НаСервере
Функция СоздатьДоговорНаСервере(Клиент);
	НовыйДоговор = Справочники.ДоговорыСКонтрагентами.СоздатьДоговор(Клиент,Перечисления.ВидыДоговоров.СПокупателем,Справочники.ВидыЦен.Розничная);
	Возврат НовыйДоговор.Ссылка;
КонецФункции

&НаСервере
Процедура ЗаполнитьПоДокументуНаСЕрвере()
	ТЗ = CurFacture.ТЧТовары.Выгрузить();
	ТЗ.Колонки.Добавить("Отметка",Новый ОписаниеТипов("БУлево"));
	//ТЗ.ЗаполнитьЗначения(Истина,"Отметка");
	Object.TabularSection.Загрузить(ТЗ);
	//Запрос = Новый Запрос;
	//Запрос.Текст = "ВЫБРАТЬ
	//               |	ДвиженияСвязанныхДокументов.Регистратор КАК ссылка
	//               |ИЗ
	//               |	РегистрНакопления.ДвиженияСвязанныхДокументов.Обороты(, , Регистратор, Основание = &ДокРеализация) КАК ДвиженияСвязанныхДокументов
	//               |ГДЕ
	//               |	НЕ ДвиженияСвязанныхДокументов.Регистратор = &ДокРеализация";
	//Запрос.УстановитьПараметр("ДокРеализация", CurFacture);
	//Выборка = Запрос.Выполнить().Выбрать();
	//ПОка Выборка.Следующий() Цикл
	//	ДокВозврат = Выборка.ссылка;
	//	Для Каждого Стр из ДокВозврат.ТЧТовары Цикл 
	//		НС = Object.TabularSection.Добавить();
	//		ЗаполнитьЗначенияСвойств(НС,Стр);
	//		НС.Количество = - Стр.Количество;
	//		НС.Сумма = - Стр.Сумма;
	//		НС.СуммаНДС = - Стр.СуммаНДС;
	//		НС.СуммаСНДС = - Стр.СуммаСНДС;
	//	КонецЦикла;
	//КонецЦикла;
	
КонецПроцедуры

&НаКлиенте
Процедура TabularSectionПередУдалением(Элемент, Отказ)
	Если Не (ЭтоНоваяПродажа или ЭтоВозврат) Тогда 
		Отказ = Истина;
		Возврат;
	КонецЕсли;
КонецПроцедуры

&НаСервере
Функция ПолучитьМассивТоваровНаСервере()
	возврат Object.TabularSection.Выгрузить().ВыгрузитьКолонку("Номенклатура");
КонецФункции

&НаСервере
Функция НайтиОткрытуюСмену()
	Возврат РаботаСДокументами.НайтиОткрытуюСмену();
КонецФункции

&НаСервере
Процедура ОткрытьСменуНаСервере()
	ОткрытаяСмена = НайтиОткрытуюСмену();
	Если ОткрытаяСмена = Документы.КассоваяСмена.ПустаяСсылка() Тогда 
		Док = Документы.КассоваяСмена.СоздатьДокумент();
		Док.Дата = ТекущаяДатаСеанса();
		Док.Касса = РегистрыСведений.НастройкиПользователей.КассаПользователя();
		Док.Организация = Object.Organisation;
		Док.МестоХранения = Док.Касса.МестоХранения;
		Док.Статус = Перечисления.СтатусыКассовойСмены.Открыта;
		Док.СуммаОткрытия = РаботаСДокументами.ПолучитьОстатокВКассе(Док.Касса);
		Док.Записать();
		КассоваяСмена = Док.Ссылка;
	Иначе
		КассоваяСмена = ОткрытаяСмена;
	КонецЕсли;
КонецПроцедуры

&НаСервере
Процедура ЗакрытьСменуНаСервере()
	Док = КассоваяСмена.ПолучитьОбъект();
	Док.Статус = Перечисления.СтатусыКассовойСмены.Закрыта;
	Док.СуммаЗакрытия = РаботаСДокументами.ПолучитьОстатокВКассе(Док.Касса);
	Док.Записать();
	НастроитьФорму();
КонецПроцедуры

&НаСервере
Функция ПолучитьОстатокОплатыПоДокументу(Док)
	ОстатокОплаты = 0;
	Запрос = Новый Запрос;
	Запрос.Текст = 
	"ВЫБРАТЬ
	|	ВзаиморасчётыСПокупателямиОстатки.СуммаОстаток КАК СуммаОстаток
	|ИЗ
	|	РегистрНакопления.ВзаиморасчётыСПокупателями.Остатки(, ОбъектРасчётов = &ОбъектРасчётов) КАК ВзаиморасчётыСПокупателямиОстатки";
	Запрос.УстановитьПараметр("ОбъектРасчётов",Док);
	РезультатЗапроса = Запрос.Выполнить();
	Если Не РезультатЗапроса.Пустой() Тогда 
		Выборка = РезультатЗапроса.Выбрать();
		Если Выборка.Следующий() Тогда 
			ОстатокОплаты = Выборка.СуммаОстаток;
		КонецЕсли;
	КонецЕсли;
	ВОзврат ОстатокОплаты;
КонецФункции

&НаСервере
Функция ПолучитьДокументНаСЕрвере(УИ)
	Возврат Документы.РеализацияТоваровУслуг.ПолучитьСсылку(УИ);
КонецФункции

&НаСервере
Процедура ПечатьEtatZНаСервере(Таб)
	Документы.КассоваяСмена.ПечатьEtatZ(КассоваяСмена, Таб);
КонецПроцедуры

&НаСервереБезКонтекста
Процедура УстановитьЭлементПользовательскогоОтбораСКД(КомпоновщикНастроек, ВидСравнения, ИмяПоля, Значение)
	ИдентификаторПользовательскойНастройки = "";
	Для Каждого Стр из КомпоновщикНастроек.Настройки.Отбор.Элементы Цикл
		Если СТр.ЛевоеЗначение = Новый ПолеКомпоновкиДанных("Контрагент") Тогда 
			ИдентификаторПользовательскойНастройки = СТр.ИдентификаторПользовательскойНастройки;
		КонецЕсли;
	КонецЦикла;
	ЭлементОтбораПользовательский = КомпоновщикНастроек.ПользовательскиеНастройки.Элементы.Найти(ИдентификаторПользовательскойНастройки);
	
	//ЭлементОтбораПользовательский =  ПользовательскийОтбор.Элементы.Добавить(Тип("ЭлементОтбораКомпоновкиДанных"));
	
	//ЭлементОтбораПользовательский.ИдентификаторПользовательскойНастройки = Новый УникальныйИдентификатор();
	ЭлементОтбораПользовательский.ВидСравнения = ВидСравнения;
	//ЭлементОтбораПользовательский.ЛевоеЗначение = Новый ПолеКомпоновкиДанных(ИмяПоля);
	ЭлементОтбораПользовательский.ПравоеЗначение = Значение;
	ЭлементОтбораПользовательский.Использование = Истина;

КонецПроцедуры

&НаСервереБезКонтекста
Функция ПолучитьПараметрыОткрытияОтчета(ИмяОтчета, Контрагент)
	
	ОтчетОбъект = Отчеты[ИмяОтчета].Создать();
	
	КомпоновщикНастроек = ОтчетОбъект.КомпоновщикНастроек;
	
	УстановитьЭлементПользовательскогоОтбораСКД(КомпоновщикНастроек, ВидСравненияКомпоновкиДанных.Равно, 
		"Контрагент", Контрагент);
		
	ПараметрыОткрытия = Новый Структура(); 	
	ПараметрыОткрытия.Вставить("СформироватьПриОткрытии", Истина);
	ПараметрыОткрытия.Вставить("Вариант", КомпоновщикНастроек.Настройки);
	ПараметрыОткрытия.Вставить("ПользовательскиеНастройки", КомпоновщикНастроек.ПользовательскиеНастройки);
				
	Возврат ПараметрыОткрытия;

КонецФункции

&НаСервере
Функция ВыемкаИзКассыНаСервере(СуммаВКассе)
	СуммаВыемки = РаботаСДокументами.ПолучитьОстатокВКассе(КассоваяСмена.Касса) - СуммаВКассе;
	CurDoc = Документы.РасходныйКассовыйОрдер.СоздатьДокумент();
	РаботаСДокументами.ЗаполнитьРеквизитыПоУмолчанию(CurDoc);
	CurDoc.КассоваяСмена = ?(КассоваяСмена.Статус = Перечисления.СтатусыКассовойСмены.Открыта,КассоваяСмена,Документы.КассоваяСмена.ПустаяСсылка());
	CurDoc.Date = ТекущаяДатаСеанса();
	CurDoc.Организация = Object.Organisation;
	ДанныеОрганизации = ОбщегоНазначенияВызовСервера.ПолучитьДанныеОрганизации(CurDoc.Организация);
	//CurDoc.Касса = ДанныеОрганизации.Касса;
	CurDoc.Касса = РегистрыСведений.НастройкиПользователей.КассаПользователя();	
	CurDoc.СтатьяДДС = Справочники.СтатьиДвиженияДенежныхСредств.ВыемкаИзКассы;
	CurDoc.Сумма = СуммаВыемки;
	CurDoc.ХозяйственнаяОперация = Перечисления.ХозяйственныеОперации.ПрочийРасходДенежныхСредств;
	CurDoc.ТипОплаты = Справочники.TypesDePayment.Cash;
	CurDoc.Записать(РежимЗаписиДокумента.Запись);
	Возврат CurDoc.Ссылка;
КонецФункции

&НаСервере
Функция ЭтоPDV()
	Возврат РольДоступна("PDV");
КонецФункции

&НаСервере
Функция ЭтоКассир()
	Возврат РегистрыСведений.НастройкиПользователей.ЭтоКассир();
КонецФункции

&НаКлиенте
Процедура ДобавитьРасход(Команда)
	ОткрытьФорму("Документ.РасходныйКассовыйОрдер.Форма.ФормаДокумента");
КонецПроцедуры

&НаКлиенте
Процедура ДобавитьДоход(Команда)
	ОткрытьФорму("Документ.ПриходныйКассовыйОрдер..Форма.ФормаДокумента");
КонецПроцедуры

Функция ПолучитьЯчейкиНаСервере(Номенклатура)
	Запрос = Новый Запрос;
	Запрос.Текст = 
	"ВЫБРАТЬ
	|	НоменклатураХранение.Зона.Наименование КАК ЗонаНаименование
	|ИЗ
	|	Справочник.Номенклатура.Хранение КАК НоменклатураХранение
	|ГДЕ
	|	НоменклатураХранение.Склад = &Склад
	|	И НоменклатураХранение.Ссылка = &Ссылка";
	Запрос.УстановитьПараметр("Склад",РозничныйСклад);
	Запрос.УстановитьПараметр("Ссылка",Номенклатура);
	Возврат СтрСоединить(Запрос.Выполнить().Выгрузить().ВыгрузитьКолонку("ЗонаНаименование"));
КонецФункции

&НаКлиенте
Процедура СохранитьНакладную(Команда)
	//Если Object.TabularSection.Количество() = 0 Тогда Возврат; КонецЕсли;
	Если Не Object.TabularSection.НайтиСтроки(Новый Структура("Цена",0)).Количество() = 0 Тогда 
		ОбщегоНазначенияКлиент.ВывестиИнформациюДляРМКУправляемой("", НСтр("fr = 'Produits sans prix détectés. La vente est impossible!'; ru = 'Обнаружены товары без цен. Проведение продажи невозможно!'; en = 'Products without prices were found. Conducting a sale is impossible!'; es = 'Se encontraron productos sin precios. ¡La venta es imposible!'"));
		Возврат;
	КонецЕсли;
	ОшибкаПроведенияДокумента = "";
	CurFacture = CreateFacture(Истина, Не ЗначениеЗаполнено(CurFacture));
	Если ЗначениеЗаполнено(ОшибкаПроведенияДокумента) Тогда 
		ОбщегоНазначенияКлиент.ВывестиИнформациюДляРМКУправляемой("", ОшибкаПроведенияДокумента);
		Элементы.СтраницыИнформации.ТекущаяСтраница = Элементы.СтраницаИнформации;
		Возврат;
	КонецЕсли;
	//CreateFacture(Истина);
	ОповеститьОбИзменении(Тип("ДокументСсылка.РеализацияТоваровУслуг"));
КонецПроцедуры

&НаКлиенте
Процедура ДокументыВОжиданииВыбор(Элемент, ВыбраннаяСтрока, Поле, СтандартнаяОбработка)
	СтандартнаяОбработка = Ложь;
	CurFacture = ВыбраннаяСтрока;
	ЗаполнитьПоДокументуНаСЕрвере();
	РозничныйКлиент = ОбщегоНазначенияВызовСервера.ЗначениеРеквизитаОбъекта(ВыбраннаяСтрока,"Контрагент");
	РозничныйДоговор = ОбщегоНазначенияВызовСервера.ПолучитьОсновнойДоговор(РозничныйКлиент, Object.Organisation, Истина);
	Если РозничныйДоговор = ПредопределенноеЗначение("Справочник.ДоговорыСКонтрагентами.ПустаяСсылка") Тогда
		РозничныйДоговор = СоздатьДоговорНаСервере(РозничныйКлиент);
	КонецЕсли;
	CalculateSumTotal();
	RefreshInfo();
	НастроитьФорму();
КонецПроцедуры

&НаКлиенте
Процедура ДокументыКОплатеВыбор(Элемент, ВыбраннаяСтрока, Поле, СтандартнаяОбработка)
	СтандартнаяОбработка = Ложь;
	CurFacture = Элемент.ТекущиеДанные.Ссылка;
	ЗаполнитьПоДокументуНаСЕрвере();
	РозничныйКлиент = ОбщегоНазначенияВызовСервера.ЗначениеРеквизитаОбъекта(CurFacture,"Контрагент");
	РозничныйДоговор = ОбщегоНазначенияВызовСервера.ПолучитьОсновнойДоговор(РозничныйКлиент, Object.Organisation, Истина);
	//Если РозничныйДоговор = ПредопределенноеЗначение("Справочник.ДоговорыСКонтрагентами.ПустаяСсылка") Тогда
	//	РозничныйДоговор = СоздатьДоговорНаСервере(РозничныйКлиент);
	//КонецЕсли;
	CalculateSumTotal();
	RefreshInfo();
	Если Не Элемент.ТекущиеДанные = Неопределено Тогда 
		СуммаОплачено = Object.TabularSection.Total("СуммаСНДС") - Элемент.ТекущиеДанные.СуммаОстаток;
		СуммаКОплате = Элемент.ТекущиеДанные.СуммаОстаток;
	КонецЕсли;
	НастроитьФорму();
КонецПроцедуры

&НаСервере
Процедура ПечатьОтгрузкиТоваровНаСервере(Таб)
	Документы.РеализацияТоваровУслуг.PrintDevisBL(CurFacture, Таб, "Bon de livraison", ЭтоPDV);
КонецПроцедуры

&НаСервере
Процедура СформироватьПечатнуюФормуВозврата(ПараметрКоманды, Таб)
	Документы.РеализацияТоваровУслуг.PrintDevisBL(ПараметрКоманды, Таб, "Avoir");
КонецПроцедуры

&НаСервере
Функция ПолучитьДатуПоследнейПродажи()
	ДатаПоследнейПродажи = Дата(1,1,1);
	Запрос = Новый Запрос;
	Запрос.Текст = 
	"ВЫБРАТЬ ПЕРВЫЕ 1
	|	ПродажиОбороты.Период КАК Период
	|ИЗ
	|	РегистрНакопления.Продажи.Обороты(
	|			,
	|			,
	|			Регистратор,
	|			Контрагент = &Контрагент
	|				И ХозяйственнаяОперация В (ЗНАЧЕНИЕ(Перечисление.ХозяйственныеОперации.РеализацияКлиенту), ЗНАЧЕНИЕ(Перечисление.ХозяйственныеОперации.ПродажаВКредит))) КАК ПродажиОбороты
	|
	|УПОРЯДОЧИТЬ ПО
	|	Период УБЫВ";
	Запрос.УстановитьПараметр("Контрагент",РозничныйКлиент);
	Выборка  = Запрос.Выполнить().Выбрать();
	Если Выборка.Следующий() Тогда
		ДатаПоследнейПродажи = Выборка.Период;
	КонецЕсли;
	
	Возврат ДатаПоследнейПродажи;
	
КонецФункции

&НаКлиенте
Процедура ОтменитьПродажу(Команда)
	Если ЗначениеЗаполнено(CurFacture) Тогда 
		ОтменитьПродажуНаСервере();
		ОповеститьОбИзменении(CurFacture);
	КонецЕсли;
	NewFacture();
	Object.ХозяйственнаяОперация = ПредопределенноеЗначение("Перечисление.ХозяйственныеОперации.РеализацияКлиенту");
	НастроитьФорму();
КонецПроцедуры

&НаСервере
Процедура ОтменитьПродажуНаСервере()
	ДокОбъект = CurFacture.ПолучитьОбъект();
	ДокОбъект.Записать(РежимЗаписиДокумента.ОтменаПроведения);
	ДокОбъект.ПометкаУдаления = Истина;
	ДокОбъект.Записать(РежимЗаписиДокумента.Запись);
КонецПроцедуры

#КонецОбласти
