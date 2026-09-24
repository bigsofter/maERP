# Final check — l10n-2-0-15-60
_20260924T170737Z_


## Scope

```
.ai/reports/l10n-2-0-15-60-final-check.md
src/cf/src/AccountingRegisters/Хозрасчетный/Forms/ФормаСписка/Form.form
src/cf/src/AccumulationRegisters/ОплатыЧеками/ОплатыЧеками.mdo
src/cf/src/AccumulationRegisters/ДенежныеСредстваОрганизаций/ДенежныеСредстваОрганизаций.mdo
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателямиНалоговый/ВзаиморасчётыСПокупателямиНалоговый.mdo
src/cf/src/AccumulationRegisters/ТоварыВНаличии/Forms/ВыборПартииПоОстаткам/Form.form
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоcтавщикамиНалоговый/ВзаиморасчётыСПоcтавщикамиНалоговый.mdo
src/cf/src/Catalogs/Бренды/Бренды.mdo
src/cf/src/Catalogs/КодыТНВЭД/КодыТНВЭД.mdo
src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
src/cf/src/Catalogs/УсловияОплаты/УсловияОплаты.mdo
src/cf/src/Catalogs/БанковскиеЧеки/БанковскиеЧеки.mdo
src/cf/src/Catalogs/БанковскиеСчета/БанковскиеСчета.mdo
src/cf/src/Catalogs/РодыДеятельности/РодыДеятельности.mdo
src/cf/src/Catalogs/ПроектыКонфигураций/ПроектыКонфигураций.mdo
src/cf/src/Catalogs/ДрайверыОборудования/ДрайверыОборудования.mdo
src/cf/src/Catalogs/КатегорииКонтрагентов/КатегорииКонтрагентов.mdo
src/cf/src/Catalogs/ВариантыВыходаНаРаботу/ВариантыВыходаНаРаботу.mdo
src/cf/src/Catalogs/ПодключаемоеОборудование/ПодключаемоеОборудование.mdo
src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/СтатьиДвиженияДенежныхСредств.mdo
src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаПодбора/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/СерииНоменклатуры/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораРозница/Form.form
src/cf/src/Catalogs/СтруктураПредприятия/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/ПроектыКонфигураций/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/ДоговорыСКонтрагентами/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/Кассы/Forms/ФормаСписка/Module.bsl
src/cf/src/Catalogs/БанковскиеСчета/Forms/ФормаСписка/Module.bsl
src/cf/src/Catalogs/Пользователи/Forms/УстановкаПароля/Module.bsl
src/cf/src/Catalogs/ДоговорыСКонтрагентами/Forms/ФормаСписка/Module.bsl
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ФормаЭлемента/Module.bsl
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ПараметрыФискализации/Module.bsl
src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/КлассификаторЕдиницИзмерения/Module.bsl
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/УправлениеФискальнымУстройством/Module.bsl
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/УправлениеЭквайринговымТерминалом/Module.bsl
src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораECommerce/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаСпискаECommerce/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock/Form.form
src/cf/src/Catalogs/ПодключаемоеОборудование/ObjectModule.bsl
src/cf/src/Catalogs/ДоговорыСКонтрагентами/Templates/Макет/Template.mxlx
src/cf/src/ChartsOfAccounts/Хозрасчетный/Forms/ФормаВыбора/Form.form
src/cf/src/ChartsOfCharacteristicTypes/ДополнительныеРеквизиты/ДополнительныеРеквизиты.mdo
src/cf/src/ChartsOfCharacteristicTypes/ПоказателиРасчётаПремий/Forms/ФормаВыбора/Form.form
src/cf/src/ChartsOfCharacteristicTypes/ПоказателиРасчётаПремий/Forms/ФормаЭлемента/Form.form
src/cf/src/CommonCommands/СверкаИтоговПоКартам/CommandModule.bsl
src/cf/src/CommonForms/ФормаПервогоЗапуска/ФормаПервогоЗапуска.mdo
src/cf/src/CommonForms/ФормаОтчёта/Form.form
src/cf/src/CommonForms/ФормаПервогоЗапуска/Form.form
src/cf/src/CommonForms/ФормаНастройкиУниверсальныйДрайвер/Form.form
src/cf/src/CommonForms/ФормаНастройкиУниверсальныйДрайвер/Module.bsl
src/cf/src/CommonForms/ФормаНастройки1ССканерыШтрихкода/Form.form
src/cf/src/CommonForms/ФормаНастройки1ССканерыШтрихкода/Module.bsl
src/cf/src/CommonModules/БрендированиеКлиент/БрендированиеКлиент.mdo
src/cf/src/CommonModules/БрендированиеВызовСервера/БрендированиеВызовСервера.mdo
src/cf/src/CommonModules/ОбщегоНазначения/Module.bsl
src/cf/src/CommonModules/ПодпискиНаСобытия/Module.bsl
src/cf/src/CommonModules/БухгалтерскийУчет/Module.bsl
src/cf/src/CommonModules/СерииИРазмещениеКлиент/Module.bsl
src/cf/src/CommonModules/ДлительныеОперацииКлиент/Module.bsl
src/cf/src/CommonModules/БухгалтерскиеОтчетыКлиент/Module.bsl
src/cf/src/CommonModules/МенеджерОборудованияКлиент/Module.bsl
src/cf/src/CommonModules/ОбщегоНазначенияКлиентСервер/Module.bsl
src/cf/src/CommonModules/РаботаСДокументамиКлиентСервер/Module.bsl
src/cf/src/CommonModules/БухгалтерскиеОтчетыВызовСервера/Module.bsl
src/cf/src/CommonModules/МенеджерОборудованияВызовСервера/Module.bsl
src/cf/src/CommonModules/ФорматноЛогическийКонтрольВызовСервера/Module.bsl
src/cf/src/CommonModules/ОперацииСПодключаемымОборудованиемКлиент/Module.bsl
src/cf/src/CommonModules/МенеджерОборудованияМаркировкаКлиентСервер/Module.bsl
src/cf/src/CommonModules/ПодключаемоеОборудованиеУниверсальныйДрайверКлиент/Module.bsl
src/cf/src/CommonModules/ПодключаемоеОборудованиеУниверсальныйДрайверАсинхронноКлиент/Module.bsl
src/cf/src/CommonModules/ПодключаемоеОборудование1ССканерыШтрихкодаКлиент/Module.bsl
src/cf/src/CommonPictures/КОплате/КОплате.mdo
src/cf/src/CommonPictures/ВыгрузкаФайловЗавершена/ВыгрузкаФайловЗавершена.mdo
src/cf/src/CommonPictures/ВыгрузкаФайловКонфигурации/ВыгрузкаФайловКонфигурации.mdo
src/cf/src/CommonTemplates/КодЗаполнения/КодЗаполнения.mdo
src/cf/src/CommonTemplates/ДанныеЗаполнения/ДанныеЗаполнения.mdo
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Configuration/ManagedApplicationModule.bsl
src/cf/src/DataProcessors/Дашборд/Дашборд.mdo
src/cf/src/DataProcessors/ПечатьЭтикеток/ПечатьЭтикеток.mdo
src/cf/src/DataProcessors/ЛичныйКабинетПартнера/ЛичныйКабинетПартнера.mdo
src/cf/src/DataProcessors/ГрупповоеСозданиеДокументов/ГрупповоеСозданиеДокументов.mdo
src/cf/src/DataProcessors/ОбновитьПоставляемыеДрайвера/ОбновитьПоставляемыеДрайвера.mdo
src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/Форма/Form.form
src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/Форма/Form.form
src/cf/src/DataProcessors/ПечатьЭтикеток/Forms/ВыборСерииПоОстаткам/Form.form
src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Form.form
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/Форма/Form.form
src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаЗаявкиНаПоискТовара/Form.form
src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Module.bsl
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/РедактированиеФормулы/Module.bsl
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/УзлыРегистрацииОбъекта/Module.bsl
src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/ObjectModule.bsl
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/ObjectModule.bsl
src/cf/src/DataProcessors/ЗагрузкаИзExcel/ЗагрузкаИзExcel.mdo
src/cf/src/DataProcessors/VentesEnDetail/Forms/ФормаСложнойОплаты/Form.form
src/cf/src/DataProcessors/VentesEnDetail/Forms/ФормаРедактированияСтроки/Form.form
src/cf/src/DataProcessors/VentesEnDetail/Forms/ФормаВводаЧисла/Module.bsl
src/cf/src/DataProcessors/VentesEnDetail/Forms/ФормаСложнойОплаты/Module.bsl
src/cf/src/DataProcessors/VentesEnDetail/Forms/ФормаПараметровЧека/Module.bsl
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Form.form
src/cf/src/DocumentJournals/БезналичныеПлатежи/Forms/ФормаСписка/Form.form
src/cf/src/Documents/АктРазбора/АктРазбора.mdo
src/cf/src/Documents/КассоваяСмена/КассоваяСмена.mdo
src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
src/cf/src/Documents/ЗаданиеНаПересчет/ЗаданиеНаПересчет.mdo
src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/ПрочиеРасходыВозврат/ПрочиеРасходыВозврат.mdo
src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
src/cf/src/Documents/УстановкаЦенНоменклатурыВручную/УстановкаЦенНоменклатурыВручную.mdo
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/ПоступлениеДополнительныхРасходов.mdo
src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Form.form
src/cf/src/Documents/АктРазбора/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/КадровыйПриказ/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/КорректировкаДолга/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Form.form
src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПриказНаНачислениеУдержание/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаСпискаМобильныйКлиент/Form.form
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Form.form
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокументаМобильныйКлиент/Form.form
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ОперацияБух/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ТабельУчётаРабочегоВремени/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаДокументаМобильныйКлиент/Module.bsl
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокументаECommerce/Form.form
src/cf/src/Documents/ЗаказПоставщику/ManagerModule.bsl
src/cf/src/Documents/КорректировкаДолга/ManagerModule.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ManagerModule.bsl
src/cf/src/Documents/СверкаВзаиморасчётов/ManagerModule.bsl
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ManagerModule.bsl
src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
src/cf/src/Documents/ВозвратПоставщикуНалоговый/ObjectModule.bsl
src/cf/src/Documents/ОперацияБух/Templates/ПФ_MXL_БухгалтерскаяСправка/Template.mxlx
src/cf/src/Documents/ЗаказПоставщику/Templates/ЗаказПоставщику/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/DevisBL_A4/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/DevisBL/Template.mxlx
src/cf/src/Documents/НалоговаяНакладная/Templates/Facture/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/Facture/Template.mxlx
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Templates/Facture/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/FactureModel/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/FactureModelEnTete/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/FactureOld/Template.mxlx
src/cf/src/Enums/Периодичность/Периодичность.mdo
src/cf/src/Enums/ПоказателиПродаж/ПоказателиПродаж.mdo
src/cf/src/Enums/ВариантыНапоминаний/ВариантыНапоминаний.mdo
src/cf/src/Enums/ВидыОперацийНалоговые/ВидыОперацийНалоговые.mdo
src/cf/src/Enums/ПризнакиПредметаРасчета/ПризнакиПредметаРасчета.mdo
src/cf/src/Enums/ВидыОперацийВзаимодействия/ВидыОперацийВзаимодействия.mdo
src/cf/src/FunctionalOptions/Производство/Производство.mdo
src/cf/src/InformationRegisters/Лиды/Лиды.mdo
src/cf/src/InformationRegisters/ОчередьЧековККТ/ОчередьЧековККТ.mdo
src/cf/src/InformationRegisters/НастройкиЗаданий/НастройкиЗаданий.mdo
src/cf/src/InformationRegisters/ИсторияПоискаВЛКП/ИсторияПоискаВЛКП.mdo
src/cf/src/InformationRegisters/ЛицаСПравомПодписи/ЛицаСПравомПодписи.mdo
src/cf/src/InformationRegisters/ДинамическаяКорзинаЛКП/ДинамическаяКорзинаЛКП.mdo
src/cf/src/InformationRegisters/ИсторияУправленияКонфигураций/ИсторияУправленияКонфигураций.mdo
src/cf/src/InformationRegisters/КураторыДоговоров/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ЛицаСПравомПодписи/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ПрисоединённыеФайлы/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ШтрихкодыНоменклатуры/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/НастройкиПользователей/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/РеквизитыКонтрагентов/Forms/ИсторияИзменений/Form.form
src/cf/src/InformationRegisters/ДополнительныеСведенияНоменклатуры/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/Лиды/Forms/ФормаЗаписи/Module.bsl
src/cf/src/InformationRegisters/ОчередьЧековККТ/Forms/ФормаСписка/Module.bsl
src/cf/src/InformationRegisters/РеквизитыКонтрагентов/Templates/МаскиТелефонныхНомеров/Template.mxlx
src/cf/src/Reports/ГлавнаяКнига/ГлавнаяКнига.mdo
src/cf/src/Reports/СтоимостьСклада/СтоимостьСклада.mdo
src/cf/src/Reports/РасчетыСПокупателями/РасчетыСПокупателями.mdo
src/cf/src/Reports/РеестрНалоговыхНакладных/РеестрНалоговыхНакладных.mdo
src/cf/src/Reports/ВедомостьПоПродажамНалоговая/ВедомостьПоПродажамНалоговая.mdo
src/cf/src/Reports/РеестрНалоговыхНакладныхЗакупка/РеестрНалоговыхНакладныхЗакупка.mdo
src/cf/src/Reports/АнализСчета/Forms/ФормаОтчета/Form.form
src/cf/src/Reports/ОборотыСчета/Forms/ФормаОтчета/Form.form
src/cf/src/Reports/КарточкаСчета/Forms/ФормаОтчета/Form.form
src/cf/src/Reports/АнализСубконто/Forms/ФормаОтчета/Form.form
src/cf/src/Reports/КарточкаСубконто/Forms/ФормаОтчета/Form.form
src/cf/src/Reports/ДвиженияДокумента/Forms/ФормаОтчета/Form.form
src/cf/src/Reports/ОборотноСальдоваяВедомость/Forms/ФормаОтчета/Form.form
src/cf/src/Reports/ОборотноСальдоваяВедомостьПоСчету/Forms/ФормаОтчета/Form.form
src/cf/src/Reports/АнализСчета/ManagerModule.bsl
src/cf/src/Reports/АнализСубконто/ManagerModule.bsl
src/cf/src/Reports/ОборотноСальдоваяВедомость/ManagerModule.bsl
src/cf/src/Reports/ОборотноСальдоваяВедомостьПоСчету/ManagerModule.bsl
src/cf/src/Reports/КарточкаСчета/Templates/СхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/КарточкаСубконто/Templates/СхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ГлавнаяКнига/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/СтоимостьСклада/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РасчетыСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РеестрНалоговыхНакладных/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьПоПродажамНалоговая/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РеестрНалоговыхНакладныхЗакупка/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ГлавнаяКнига/Templates/ЛоготипКомпании/Template.mxlx
src/cf/src/Reports/РасчетыСПокупателями/Templates/ЛоготипКомпании/Template.mxlx
src/cf/src/Reports/ABCАнализПродаж/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/ScheduledJobs/ЗакрытиеСеансов/ЗакрытиеСеансов.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-24T18:07:48.471+01:00  INFO 90299 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/742 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/742 (0:00:01 / 0:01:21) Analyzing files...  10% [==                      ]  80/742 (0:00:02 / 0:00:16) Analyzing files...  25% [======                  ] 186/742 (0:00:03 / 0:00:08) Analyzing files...  45% [==========              ] 340/742 (0:00:04 / 0:00:04) Analyzing files...  62% [===============         ] 465/742 (0:00:05 / 0:00:02) Analyzing files...  70% [================        ] 521/742 (0:00:06 / 0:00:02) Analyzing files...  83% [===================     ] 617/742 (0:00:07 / 0:00:01) Analyzing files...  93% [======================  ] 693/742 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 742/742 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 742/742 (0:00:08 / 0:00:00) 
2026-09-24T18:08:01.345+01:00  INFO 90299 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-09-19 09:10:00; изменённых модулей: 60
новых замечаний нет
```
**PASS**
### уровень 0.5: scripts/refcheck.py
```
Сверка ссылок: расхождений нет (известных — 49)
```
**PASS**
### уровень 0.7: scripts/listcheck.py
```
Проверка динамических списков: расхождений нет (известных — 25)
```
**PASS**
### уровень 0.8: scripts/queryfields.py
```
Сверка полей запросов: расхождений нет (известных — 4)
```
**PASS**
### ОписаниеИзменений: секция текущей версии на ru/fr/en/es
```
Языков: 4, пунктов изменений: 20
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.60.json
версия 2.0.15.60: ru=5, fr=5, en=5, es=5
```
**PASS**

## Git hygiene

### git status
```
 M .ai/reports/l10n-2-0-15-60-final-check.md
 M src/cf/src/CommonModules/ПодпискиНаСобытия/Module.bsl
```

### Запретные пути (CLAUDE.md «Не трогаю»)
нет

### Бинарники 1С в индексе/untracked
нет

### NFC/NFD-дубликаты путей (tiny1C workflow-007)
нет

### Secret heuristic (grep + значение SMOKE_PWD из env; не сканер секретов)
no hits (grep heuristic only — not a real secret scanner)

### New TODO/FIXME introduced (added lines only)
none found

### Новые подавления BSL LS (added lines only)
none found

### Версия конфигурации
версия 2.0.15.60 не поднималась относительно HEAD — если это передача владельцу на тест, подними Y и заведи секцию (CLAUDE.md «Версия и список изменений»)

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
