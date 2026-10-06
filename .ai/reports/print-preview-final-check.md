# Final check — print-preview
_20261006T122020Z_


## Scope

```
.ai/reports/print-preview-final-check.md
CLAUDE.md
docs/FORMS-STYLE.md
docs/TECHDEBT.md
scripts/colfont.py
src/cf/src/AccountingRegisters/Хозрасчетный/Forms/ФормаСписка/Form.form
src/cf/src/AccumulationRegisters/ТоварыВНаличии/Forms/ВыборПартииПоОстаткам/Form.form
src/cf/src/Catalogs/Банки/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Бренды/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/ВидыЦен/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Банки/Forms/ЗагрузкаБанков/Form.form
src/cf/src/Catalogs/Должности/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/СтраныМира/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/ВидыЗаданий/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Контрагенты/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/БанковскиеЧеки/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/БанковскиеСчета/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/ПричиныВозвратов/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораГруппы/Form.form
src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораРозница/Form.form
src/cf/src/Catalogs/ГруппыПользователей/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/ДрайверыОборудования/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/ГруппыПользователей/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/ВариантыВыходаНаРаботу/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/ВидыСвойствНоменклатуры/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/ГрафикиРаботыСотрудников/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/ЗначенияСвойствНоменклатуры/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/ФормаСпискаЕдиниц/Form.form
src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/ФормаВыбораУпаковки/Form.form
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ПараметрыФискализации/Form.form
src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/ФормаВыбораИзДокументов/Form.form
src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/КлассификаторЕдиницИзмерения/Form.form
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ПодключениеИНастройкаОборудования/Form.form
src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораECommerce/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбораECommerce/Form.form
src/cf/src/Catalogs/Контрагенты/Forms/ФормаЭлементаECommerce/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock1/Form.form
src/cf/src/Catalogs/TypesDePayment/Forms/ChoiceForm/Form.form
src/cf/src/Catalogs/TypesDePayment/Forms/ListForm/Form.form
src/cf/src/ChartsOfAccounts/Хозрасчетный/Forms/ФормаСчета/Form.form
src/cf/src/ChartsOfAccounts/Хозрасчетный/Forms/ФормаВыбора/Form.form
src/cf/src/ChartsOfCharacteristicTypes/ПоказателиРасчётаПремий/Forms/ФормаВыбора/Form.form
src/cf/src/ChartsOfCharacteristicTypes/ВидыСубконтоХозрасчетные/Forms/ФормаВыбора/Form.form
src/cf/src/ChartsOfCharacteristicTypes/ВидыНастроекПользователей/Forms/ФормаВыбора/Form.form
src/cf/src/ChartsOfCharacteristicTypes/ВидыРеквизитовКонтрагентов/Forms/ФормаСписка/Form.form
src/cf/src/ChartsOfCharacteristicTypes/ВидыРеквизитовКонтрагентов/Forms/ФормаЭлемента/Form.form
src/cf/src/CommonForms/ВыборЗначений/Form.form
src/cf/src/CommonForms/ИнтерфейсКлиент/Form.form
src/cf/src/CommonForms/ПечатьДокументов/Form.form
src/cf/src/CommonForms/ФормаПервогоЗапуска/Form.form
src/cf/src/CommonForms/ПодборОбъектовРасчётовПоОстаткам/Form.form
src/cf/src/CommonForms/КодВидаНоменклатурнойКлассификации/Form.form
src/cf/src/CommonForms/РедактированиеНДСПлатёжногоДокумента/Form.form
src/cf/src/CommonForms/ФормаНастройкиУниверсальныйДрайвер/Form.form
src/cf/src/CommonForms/ПечатьДокументов/Module.bsl
src/cf/src/CommonModules/ПечатныеФормыКлиент/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/КлиентБанк/Forms/Форма/Form.form
src/cf/src/DataProcessors/ПечатьЭтикеток/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/ПерепроведениеДокументов/Forms/Форма/Form.form
src/cf/src/DataProcessors/РегламентныеИФоновыеЗадания/Forms/Форма/Form.form
src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/Форма/Form.form
src/cf/src/DataProcessors/ПечатьЭтикеток/Forms/ВыборСерииПоОстаткам/Form.form
src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Form.form
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/Форма/Form.form
src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/ВыборВидаОбъектов/Form.form
src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/РедактированиеФормулы/Form.form
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/ВыборКонстанты/Form.form
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/ВыборУзлаПланаОбмена/Form.form
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/УзлыРегистрацииОбъекта/Form.form
src/cf/src/DataProcessors/ЗагрузкаИзExcel/Forms/Форма/Form.form
src/cf/src/DataProcessors/VentesEnDetail/Forms/ФормаСложнойОплаты/Form.form
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Form.form
src/cf/src/DocumentJournals/КассовыеДокументы/Forms/ФормаСписка/Form.form
src/cf/src/DocumentJournals/БезналичныеПлатежи/Forms/ФормаСписка/Form.form
src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ОперацияБух/Forms/ФормаВыбора/Form.form
src/cf/src/Documents/АктРазбора/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/КадровыйПриказ/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаВыбора/Form.form
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/КорректировкаДолга/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Form.form
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаВыбора/Form.form
src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаВыбора/Form.form
src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаВыбораРегистра/Form.form
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаказПоставщику/Forms/ПодборПредварительныхЗаказов/Form.form
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСпискаМобильныйКлиент/Form.form
src/cf/src/Documents/ПеремещениеТоваров/Forms/ФормаСпискаИнтерфейсКассира/Form.form
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокументаМобильныйКлиент/Form.form
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаВыбора/Form.form
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокументаECommerce/Form.form
src/cf/src/Enums/ХозяйственныеОперации/Forms/ФормаВыбора/Form.form
src/cf/src/FilterCriteria/СвязанныеДокументы/Forms/ФормаОтчета/Form.form
src/cf/src/InformationRegisters/СоставТехКарты/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ОчередьЧековККТ/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ЦеныНоменклатуры/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/КураторыДоговоров/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ЛицаСПравомПодписи/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ПрисоединённыеФайлы/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/РеквизитыКонтрагентов/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/НастройкиПользователей/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ДатыЗапретаРедактирования/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/РеквизитыКонтрагентов/Forms/ИсторияИзменений/Form.form
src/cf/src/InformationRegisters/ЦеныНоменклатурыПоставщиков/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ДополнительныеСведенияНоменклатуры/Forms/ФормаСписка/Form.form
src/cf/src/InformationRegisters/ПользовательскиеМакетыПечати/Forms/МакетыПечатныхФорм/Form.form
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-06T13:20:31.186+01:00  INFO 58909 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/760 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/760 (0:00:01 / 0:01:23) Analyzing files...   4% [                        ]  31/760 (0:00:03 / 0:01:10) Analyzing files...  14% [===                     ] 107/760 (0:00:04 / 0:00:24) Analyzing files...  21% [=====                   ] 161/760 (0:00:05 / 0:00:18) Analyzing files...  34% [========                ] 265/760 (0:00:06 / 0:00:11) Analyzing files...  51% [============            ] 392/760 (0:00:07 / 0:00:06) Analyzing files...  63% [===============         ] 481/760 (0:00:08 / 0:00:04) Analyzing files...  73% [=================       ] 556/760 (0:00:09 / 0:00:03) Analyzing files...  77% [==================      ] 590/760 (0:00:10 / 0:00:02) Analyzing files...  81% [===================     ] 616/760 (0:00:11 / 0:00:02) Analyzing files...  93% [======================  ] 710/760 (0:00:12 / 0:00:00) Analyzing files... 100% [========================] 760/760 (0:00:12 / 0:00:00) Analyzing files... 100% [========================] 760/760 (0:00:12 / 0:00:00) 
2026-10-06T13:20:50.275+01:00  INFO 58909 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 2
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.21.json
версия 2.0.16.21: ru=5, fr=5, en=5, es=5
```
**PASS**

## Git hygiene

### git status
```
 M CLAUDE.md
 M docs/FORMS-STYLE.md
 M docs/TECHDEBT.md
 M src/cf/src/AccountingRegisters/Хозрасчетный/Forms/ФормаСписка/Form.form
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/Forms/ВыборПартииПоОстаткам/Form.form
 M src/cf/src/Catalogs/TypesDePayment/Forms/ChoiceForm/Form.form
 M src/cf/src/Catalogs/TypesDePayment/Forms/ListForm/Form.form
 M src/cf/src/Catalogs/Банки/Forms/ЗагрузкаБанков/Form.form
 M src/cf/src/Catalogs/Банки/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/Банки/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/БанковскиеСчета/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/БанковскиеСчета/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/БанковскиеЧеки/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/БанковскиеЧеки/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Бренды/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/Бренды/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Валюты/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Валюты/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/ВариантыВыходаНаРаботу/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ВидыЗаданий/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/ВидыЗаданий/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ВидыСвойствНоменклатуры/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ВидыЦен/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/ВидыЦен/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ГрафикиРаботыСотрудников/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ГруппыПользователей/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/ГруппыПользователей/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ГруппыПользователей/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/ДоговорыСКонтрагентами/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ДокументыФизическихЛиц/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Должности/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/Должности/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ДрайверыОборудования/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ЗначенияСвойствНоменклатуры/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Каналы/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Кассы/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/КатегорииКонтрагентов/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/КатегорииКонтрагентов/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/КодыТНВЭД/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/КодыТНВЭД/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораECommerce/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораГруппы/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораРозница/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаСпискаECommerce/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаЭлементаECommerce/Form.form
 M src/cf/src/Catalogs/МестаХранения/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/НаборыУпаковок/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock1/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбораECommerce/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбораГруппы/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбораМобильныйКлиент/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбораУпаковок/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаПодбора/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСпискаECommerce/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/НоменклатураКонтрагентов/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/НоменклатураКонтрагентов/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/НомераГТД/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/НомераГТД/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Организации/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Организации/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ПараметрыФискализации/Form.form
 M src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ПодключениеИНастройкаОборудования/Form.form
 M src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/Пользователи/Forms/ВыборПользователяОС/Form.form
 M src/cf/src/Catalogs/Пользователи/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/Пользователи/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Пользователи/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/ПричиныВозвратов/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/ПричиныВозвратов/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/РодыДеятельности/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/РодыДеятельности/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/СерииНоменклатуры/Forms/ВыборСерииПоОстаткам/Form.form
 M src/cf/src/Catalogs/СерииНоменклатуры/Forms/УстановкаСерий/Form.form
 M src/cf/src/Catalogs/СерииНоменклатуры/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/СерииНоменклатуры/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/СтавкиНДС/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/СтраныМира/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/СтраныМира/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/СтруктураПредприятия/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/СтруктураПредприятия/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ТоварныеГруппы/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/ТоварныеГруппы/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/КлассификаторЕдиницИзмерения/Form.form
 M src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/ФормаВыбораЕдиницы/Form.form
 M src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/ФормаВыбораИзДокументов/Form.form
 M src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/ФормаВыбораУпаковки/Form.form
 M src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/ФормаСпискаЕдиниц/Form.form
 M src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/Forms/ФормаСпискаУпаковок/Form.form
 M src/cf/src/Catalogs/УсловияОплаты/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/УсловияОплаты/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/УчётныеЗаписиЭлектроннойПочты/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/УчётныеЗаписиЭлектроннойПочты/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ФизическиеЛица/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/ФизическиеЛица/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ФизическиеЛица/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/ХарактеристикиНоменклатуры/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ЯчейкиСклада/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/ЯчейкиСклада/Forms/ФормаСписка/Form.form
 M src/cf/src/ChartsOfAccounts/Хозрасчетный/Forms/ФормаВыбора/Form.form
 M src/cf/src/ChartsOfAccounts/Хозрасчетный/Forms/ФормаСписка/Form.form
 M src/cf/src/ChartsOfAccounts/Хозрасчетный/Forms/ФормаСчета/Form.form
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыНастроекПользователей/Forms/ФормаВыбора/Form.form
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыНастроекПользователей/Forms/ФормаСписка/Form.form
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыРеквизитовКонтрагентов/Forms/ФормаСписка/Form.form
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыРеквизитовКонтрагентов/Forms/ФормаЭлемента/Form.form
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыСубконтоХозрасчетные/Forms/ФормаВыбора/Form.form
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыСубконтоХозрасчетные/Forms/ФормаСписка/Form.form
 M src/cf/src/ChartsOfCharacteristicTypes/ПоказателиРасчётаПремий/Forms/ФормаВыбора/Form.form
 M src/cf/src/ChartsOfCharacteristicTypes/ПоказателиРасчётаПремий/Forms/ФормаСписка/Form.form
 M src/cf/src/ChartsOfCharacteristicTypes/ПоказателиРасчётаПремий/Forms/ФормаЭлемента/Form.form
 M src/cf/src/CommonForms/ВыборЗначений/Form.form
 M src/cf/src/CommonForms/ИнтерфейсКлиент/Form.form
 M src/cf/src/CommonForms/КодВидаНоменклатурнойКлассификации/Form.form
 M src/cf/src/CommonForms/ПечатьДокументов/Form.form
 M src/cf/src/CommonForms/ПечатьДокументов/Module.bsl
 M src/cf/src/CommonForms/ПодборОбъектовРасчётовПоОстаткам/Form.form
 M src/cf/src/CommonForms/РедактированиеНДСПлатёжногоДокумента/Form.form
 M src/cf/src/CommonForms/ФормаНастройкиУниверсальныйДрайвер/Form.form
 M src/cf/src/CommonForms/ФормаПервогоЗапуска/Form.form
 M src/cf/src/CommonModules/ПечатныеФормыКлиент/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Form.form
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/ФормаСложнойОплаты/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/ВыборВидаОбъектов/Form.form
 M src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/ВыбранныеЭлементы/Form.form
 M src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/РедактированиеФормулы/Form.form
 M src/cf/src/DataProcessors/ГрупповоеИзменениеРеквизитов/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/ЗагрузкаИзExcel/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/КлиентБанк/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Form.form
 M src/cf/src/DataProcessors/ПерепроведениеДокументов/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/ПечатьЭтикеток/Forms/ВыборСерииПоОстаткам/Form.form
 M src/cf/src/DataProcessors/ПечатьЭтикеток/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/ВыборКонстанты/Form.form
 M src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/ВыборУзлаПланаОбмена/Form.form
 M src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/УзлыРегистрацииОбъекта/Form.form
 M src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/РегламентныеИФоновыеЗадания/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/Forms/Форма/Form.form
 M src/cf/src/DocumentJournals/БезналичныеПлатежи/Forms/ФормаСписка/Form.form
 M src/cf/src/DocumentJournals/КассовыеДокументы/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/АктРазбора/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокументаECommerce/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ПодборПредварительныхЗаказов/Form.form
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/КадровыйПриказ/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/КадровыйПриказ/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/КассоваяСмена/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/КассоваяСмена/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/КорректировкаДолга/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/КорректировкаДолга/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/КорректировкаДолга/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаВыбораРегистра/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокументаМобильныйКлиент/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСпискаМобильныйКлиент/Form.form
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НачислениеЗарплаты/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/НачислениеЗарплаты/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/НачислениеЗарплаты/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ОперацияБух/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ОперацияБух/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ОперацияБух/Forms/ФормаНастройки/Form.form
 M src/cf/src/Documents/ОперацияБух/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПеремещениеТоваров/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПеремещениеТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПеремещениеТоваров/Forms/ФормаСпискаИнтерфейсКассира/Form.form
 M src/cf/src/Documents/ПересортицаТоваров/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПересортицаТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПересчётТоваров/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ПересчётТоваров/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПересчётТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПлатёжнаяВедомостьНаАванс/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПлатёжнаяВедомостьНаАванс/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПравилоЦенообразования/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПравилоЦенообразования/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПриказНаНачислениеУдержание/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПриказНаНачислениеУдержание/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокументаМобильныйКлиент/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСпискаМобильныйКлиент/Form.form
 M src/cf/src/Documents/СверкаВзаиморасчётов/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/СверкаВзаиморасчётов/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СертификатНаОплату/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ТабельУчётаРабочегоВремени/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ТабельУчётаРабочегоВремени/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ТабельУчётаРабочегоВремени/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ТехнологическаяКарта/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ТехнологическаяКарта/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/УстановкаПлановыхПоказателей/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/УстановкаПлановыхПоказателей/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/УстановкаЦенНоменклатуры/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/УстановкаЦенНоменклатуры/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/УстановкаЦенНоменклатурыВручную/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/УстановкаЦенНоменклатурыВручную/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/УценкаТоваров/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/УценкаТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Enums/ХозяйственныеОперации/Forms/ФормаВыбора/Form.form
 M src/cf/src/FilterCriteria/СвязанныеДокументы/Forms/ФормаОтчета/Form.form
 M src/cf/src/InformationRegisters/ДатыЗапретаРедактирования/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/ДополнительныеСведенияНоменклатуры/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/КураторыДоговоров/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/ЛицаСПравомПодписи/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/НастройкиПользователей/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/НепроведенныеДокументы/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/ОчередьЧековККТ/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/ПараметрыОбменаДанными/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/ПользовательскиеМакетыПечати/Forms/МакетыПечатныхФорм/Form.form
 M src/cf/src/InformationRegisters/ПрисоединённыеФайлы/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/РеквизитыКонтрагентов/Forms/ИсторияИзменений/Form.form
 M src/cf/src/InformationRegisters/РеквизитыКонтрагентов/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/СоставТехКарты/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/ФискальныеОперации/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/ЦеныНоменклатуры/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/ЦеныНоменклатурыПоставщиков/Forms/ФормаСписка/Form.form
 M src/cf/src/InformationRegisters/ШтрихкодыНоменклатуры/Forms/ФормаСписка/Form.form
?? .ai/reports/print-preview-final-check.md
?? scripts/colfont.py
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
```
+// BSLLS:UsingObjectNotAvailableUnix-off
+// BSLLS:UsingObjectNotAvailableUnix-off
+// BSLLS:UsingObjectNotAvailableUnix-off
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.20 → 2.0.16.21

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
