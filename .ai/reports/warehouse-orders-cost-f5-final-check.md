# Final check — warehouse-orders-cost-f5
_20261031T023512Z_


## Scope

```
.ai/reports/arm-pf-output-final-check.md
.ai/reports/arm-production-print-final-check.md
.ai/reports/arm-purch-tabs-final-check.md
.ai/reports/arm-purchasing-invoice-cols-final-check.md
.ai/reports/arm-purchasing-lines-columns-final-check.md
.ai/reports/arm-purchasing-receipt-lines-final-check.md
.ai/reports/arm-purchasing-receipts-final-check.md
.ai/reports/arm-purchasing-receipts-s2-final-check.md
.ai/reports/arm-receipt-lines-edit-final-check.md
.ai/reports/card-crash-filters-final-check.md
.ai/reports/card-routing-crash-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/manual-output-from-stock-final-check.md
.ai/reports/order-list-columns-final-check.md
.ai/reports/order-stock-places-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/semi-finished-from-stock-final-check.md
.ai/reports/semi-finished-leaf-final-check.md
.ai/reports/semi-finished-subcontract-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reports/subcontract-late-receipt-final-check.md
.ai/reports/tabs-handlers-final-check.md
.ai/reports/transfer-act-print-final-check.md
.ai/reports/warehouse-orders-cost-f3-final-check.md
.ai/reports/warehouse-orders-cost-f4-final-check.md
.ai/reports/warehouse-orders-cost-f5-final-check.md
.ai/reports/warehouse-orders-option-final-check.md
.ai/reviews/arm-production-print/03-code-review.json
.ai/reviews/arm-production-print/03b-code-review-verify.json
.ai/reviews/arm-purchasing-receipt-lines/02-plan-review.json
.ai/reviews/arm-purchasing-receipt-lines/03-code-review.json
.ai/reviews/arm-purchasing-receipt-lines/03b-code-review-verify.json
.ai/reviews/card-crash-filters/03-code-review.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/order-list-columns/03-code-review.json
.ai/reviews/order-list-columns/03b-code-review-verify.json
.ai/reviews/order-payment-state/02-plan-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/subcontract-late-receipt/03-code-review.json
.ai/reviews/subcontract-late-receipt/03b-code-review-verify.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/warehouse-orders-cost-f5/02-plan-review-r1.json
.ai/reviews/warehouse-orders-cost-f5/02-plan-review-r2.json
.ai/reviews/warehouse-orders-cost-f5/02-plan-review.json
.ai/reviews/warehouse-orders-cost-f5/03-code-review-r1.json
.ai/reviews/warehouse-orders-cost-f5/03-code-review.json
.ai/reviews/warehouse-orders-cost-f5/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-cost-f5/03b-code-review-verify-r2.json
.ai/reviews/warehouse-orders-cost-f5/03b-code-review-verify.json
.ai/reviews/warehouse-orders-cost-f5/04-database-review-r1.json
.ai/reviews/warehouse-orders-cost-f5/04-database-review.json
.ai/reviews/warehouse-orders-cost-f5/05-security-review-r1.json
.ai/reviews/warehouse-orders-cost-f5/05-security-review.json
.ai/reviews/warehouse-orders-option/02-plan-review.json
.ai/reviews/warehouse-orders-option/03-code-review.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify.json
.ai/reviews/warehouse-orders-option/04-database-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/order-payment-state.md
docs/plans/warehouse-orders-cost.md
docs/RELEASING.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ТоварыНаСкладах.mdo
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыКОформлению/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыВНаличии/RecordSetModule.bsl
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/RecordSetModule.bsl
src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/СерииНоменклатуры/Forms/ВыборСерииПоОстаткам/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock/Module.bsl
src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
src/cf/src/CommonModules/ОрдераСклада/Module.bsl
src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
src/cf/src/CommonModules/ОбщегоНазначения/Module.bsl
src/cf/src/CommonModules/ПодпискиНаСобытия/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
src/cf/src/CommonModules/ТехнологическиеКарты/Module.bsl
src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ПечатьЭтикеток/Forms/ВыборСерииПоОстаткам/Form.form
src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Form.form
src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/ManagerModule.bsl
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
src/cf/src/Documents/АктРазбора/АктРазбора.mdo
src/cf/src/Documents/ПриходныйОрдер/ПриходныйОрдер.mdo
src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
src/cf/src/Documents/КорректировкаРегистров/КорректировкаРегистров.mdo
src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаВыбораРегистра/Module.bsl
src/cf/src/Documents/ПересчётТоваров/ManagerModule.bsl
src/cf/src/Documents/КорректировкаРегистров/ObjectModule.bsl
src/cf/src/Reports/ДвиженияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ТоварыДляЗаказа/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ОстаткиНаСкладах/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/НедостаточныеЗапасы/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ОтчетПоНедостаткамТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ПроданныйТоварБезНакладной/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Логист/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/Руководитель/Rights.rights
src/cf/src/Roles/ЛичныйКабинет/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Roles/MobileClient/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-31T03:35:19.426+01:00  INFO 85803 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/826 (0:00:00 / ?) Analyzing files...  11% [==                      ]  94/826 (0:00:01 / 0:00:07) Analyzing files...  31% [=======                 ] 261/826 (0:00:02 / 0:00:04) Analyzing files...  57% [=============           ] 474/826 (0:00:03 / 0:00:02) Analyzing files...  79% [===================     ] 658/826 (0:00:04 / 0:00:01) Analyzing files...  99% [======================= ] 824/826 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 826/826 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 826/826 (0:00:05 / 0:00:00) 
2026-10-31T03:35:27.805+01:00  INFO 85803 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 32
новых замечаний нет
```
**PASS**
### уровень 0.5: scripts/refcheck.py
```
Сверка ссылок: расхождений нет (известных — 48)
```
**PASS**
### уровень 0.7: scripts/listcheck.py
```
Проверка динамических списков: расхождений нет (известных — 0)
```
**PASS**
### уровень 0.8: scripts/queryfields.py
```
Сверка полей запросов: расхождений нет (известных — 4)
```
**PASS**
### ОписаниеИзменений: секция текущей версии на ru/fr/en/es
```
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.124.json
версия 2.0.16.124: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/RELEASING.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/warehouse-orders-cost.md
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/RecordSetModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыКОформлению/ManagerModule.bsl
 D src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
 D src/cf/src/AccumulationRegisters/ТоварыНаСкладах/RecordSetModule.bsl
 D src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ТоварыНаСкладах.mdo
 M src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock/Module.bsl
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
 M src/cf/src/Catalogs/СерииНоменклатуры/Forms/ВыборСерииПоОстаткам/Form.form
 M src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
 M src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/Module.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ОбщегоНазначения/Module.bsl
 M src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
 M src/cf/src/CommonModules/ОрдераСклада/Module.bsl
 M src/cf/src/CommonModules/ПодпискиНаСобытия/Module.bsl
 M src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
 M src/cf/src/CommonModules/Производство/Module.bsl
 M src/cf/src/CommonModules/ПроцедурыРегламентныхЗаданий/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonModules/СерииИРазмещение/Module.bsl
 M src/cf/src/CommonModules/ТехнологическиеКарты/Module.bsl
 M src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
 M src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
 M src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
 M src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
 M src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Form.form
 M src/cf/src/DataProcessors/ПечатьЭтикеток/Forms/ВыборСерииПоОстаткам/Form.form
 M src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/ManagerModule.bsl
 M src/cf/src/Documents/АктРазбора/АктРазбора.mdo
 M src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
 M src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаВыбораРегистра/Module.bsl
 M src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/КорректировкаРегистров/ObjectModule.bsl
 M src/cf/src/Documents/КорректировкаРегистров/КорректировкаРегистров.mdo
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
 M src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
 M src/cf/src/Documents/ПередачаВПереработку/ПередачаВПереработку.mdo
 M src/cf/src/Documents/ПеремещениеТоваров/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПеремещениеТоваров/ПеремещениеТоваров.mdo
 M src/cf/src/Documents/ПересортицаТоваров/ПересортицаТоваров.mdo
 M src/cf/src/Documents/ПересчётТоваров/ManagerModule.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
 M src/cf/src/Documents/ПриходныйОрдер/ПриходныйОрдер.mdo
 M src/cf/src/Documents/РасходныйОрдер/РасходныйОрдер.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/СписаниеТоваров/СписаниеТоваров.mdo
 M src/cf/src/Documents/ТребованиеНакладная/ТребованиеНакладная.mdo
 M src/cf/src/Reports/ДвиженияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/НедостаточныеЗапасы/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОстаткиНаСкладах/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОтчетПоНедостаткамТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПланированиеЗакупок/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПроданныйТоварБезНакладной/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыВНаличии/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыДляЗаказа/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Roles/MobileClient/Rights.rights
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/ЛичныйКабинет/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Roles/Руководитель/Rights.rights
?? .ai/reports/arm-pf-output-final-check.md
?? .ai/reports/arm-production-print-final-check.md
?? .ai/reports/arm-purch-tabs-final-check.md
?? .ai/reports/arm-purchasing-invoice-cols-final-check.md
?? .ai/reports/arm-purchasing-lines-columns-final-check.md
?? .ai/reports/arm-purchasing-receipt-lines-final-check.md
?? .ai/reports/arm-purchasing-receipts-final-check.md
?? .ai/reports/arm-purchasing-receipts-s2-final-check.md
?? .ai/reports/arm-receipt-lines-edit-final-check.md
?? .ai/reports/card-crash-filters-final-check.md
?? .ai/reports/card-routing-crash-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/manual-output-from-stock-final-check.md
?? .ai/reports/order-list-columns-final-check.md
?? .ai/reports/order-stock-places-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/semi-finished-from-stock-final-check.md
?? .ai/reports/semi-finished-leaf-final-check.md
?? .ai/reports/semi-finished-subcontract-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reports/subcontract-late-receipt-final-check.md
?? .ai/reports/tabs-handlers-final-check.md
?? .ai/reports/transfer-act-print-final-check.md
?? .ai/reports/warehouse-orders-cost-f3-final-check.md
?? .ai/reports/warehouse-orders-cost-f4-final-check.md
?? .ai/reports/warehouse-orders-cost-f5-final-check.md
?? .ai/reports/warehouse-orders-option-final-check.md
?? .ai/reviews/arm-production-print/
?? .ai/reviews/arm-purchasing-receipt-lines/
?? .ai/reviews/card-crash-filters/
?? .ai/reviews/machine-form/
?? .ai/reviews/order-list-columns/
?? .ai/reviews/order-payment-state/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/subcontract-late-receipt/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/warehouse-orders-cost-f5/
?? .ai/reviews/warehouse-orders-option/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/order-payment-state.md
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
+	// BSLLS:SetPrivilegedMode-off - остатки и прежние позиции склада читаются служебно, как прежде физика
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off - остатки и прежние позиции склада читаются служебно, как прежде физика
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off - остатки и прежние позиции склада читаются служебно, как прежде физика
+	// BSLLS:SetPrivilegedMode-on
+// независимо от прав роли. BSLLS:SetPrivilegedMode-off
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.123 → 2.0.16.124

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
