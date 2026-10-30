# Final check — warehouse-orders-cost-f2
_20261030T181823Z_


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
.ai/reports/warehouse-orders-cost-f2-final-check.md
.ai/reports/warehouse-orders-cost.md
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
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r1.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r10.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r11.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r12.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r13.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r2.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r3.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r4.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r5.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r6.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r7.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r8.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review-r9.json
.ai/reviews/warehouse-orders-cost-f2/02-plan-review.json
.ai/reviews/warehouse-orders-cost-f2/03-code-review-r1.json
.ai/reviews/warehouse-orders-cost-f2/03-code-review.json
.ai/reviews/warehouse-orders-cost-f2/03b-code-review-verify.json
.ai/reviews/warehouse-orders-cost-f2/04-database-review-r1.json
.ai/reviews/warehouse-orders-cost-f2/04-database-review-r2.json
.ai/reviews/warehouse-orders-cost-f2/04-database-review.json
.ai/reviews/warehouse-orders-cost-f2/05-security-review-r1.json
.ai/reviews/warehouse-orders-cost-f2/05-security-review-r2.json
.ai/reviews/warehouse-orders-cost-f2/05-security-review.json
.ai/reviews/warehouse-orders-option/02-plan-review.json
.ai/reviews/warehouse-orders-option/03-code-review.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify.json
.ai/reviews/warehouse-orders-option/04-database-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/order-payment-state.md
docs/plans/warehouse-orders-cost-phase2-prompt.md
docs/plans/warehouse-orders-cost.md
docs/RELEASING.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/СебестоимостьПродаж/СебестоимостьПродаж.mdo
src/cf/src/AccumulationRegisters/Убытки/ManagerModule.bsl
src/cf/src/AccumulationRegisters/Продажи/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/СебестоимостьПродаж/ManagerModule.bsl
src/cf/src/CommonModules/НалоговыйУчет/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/КорректировкаРегистров/КорректировкаРегистров.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
src/cf/src/Reports/ПроданныйТоварБезНакладной/ObjectModule.bsl
src/cf/src/Reports/ВедомостьПоПродажам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ПроданныйТоварБезНакладной/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ABCАнализПродаж/ObjectModule.bsl
src/cf/src/Reports/ABCАнализПродаж/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Логист/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
src/cf/src/Roles/MobileClient/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
src/cf/src/Sequences/Основная/Основная.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-30T19:18:31.687+01:00  INFO 88096 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/828 (0:00:00 / ?) Analyzing files...   1% [                        ]  10/828 (0:00:01 / 0:01:22) Analyzing files...   9% [==                      ]  76/828 (0:00:02 / 0:00:19) Analyzing files...  24% [=====                   ] 206/828 (0:00:03 / 0:00:09) Analyzing files...  38% [=========               ] 316/828 (0:00:04 / 0:00:06) Analyzing files...  46% [===========             ] 382/828 (0:00:05 / 0:00:05) Analyzing files...  56% [=============           ] 470/828 (0:00:06 / 0:00:04) Analyzing files...  67% [================        ] 563/828 (0:00:07 / 0:00:03) Analyzing files...  83% [====================    ] 693/828 (0:00:08 / 0:00:01) Analyzing files...  90% [=====================   ] 750/828 (0:00:09 / 0:00:00) Analyzing files... 100% [========================] 828/828 (0:00:09 / 0:00:00) Analyzing files... 100% [========================] 828/828 (0:00:09 / 0:00:00) 
2026-10-30T19:18:44.374+01:00  INFO 88096 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 12
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
Языков: 4, пунктов изменений: 24
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.121.json
версия 2.0.16.121: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
 M .ai/reports/warehouse-orders-cost.md
 M docs/RELEASING.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/warehouse-orders-cost.md
 M src/cf/src/AccumulationRegisters/Продажи/ManagerModule.bsl
 A src/cf/src/AccumulationRegisters/СебестоимостьПродаж/ManagerModule.bsl
 A src/cf/src/AccumulationRegisters/СебестоимостьПродаж/СебестоимостьПродаж.mdo
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/Убытки/ManagerModule.bsl
 M src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/Module.bsl
 M src/cf/src/CommonModules/НалоговыйУчет/Module.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиВызовСервера/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
 M src/cf/src/Documents/КорректировкаРегистров/КорректировкаРегистров.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Reports/ABCАнализПродаж/ObjectModule.bsl
 M src/cf/src/Reports/ABCАнализПродаж/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьПоПродажам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 A src/cf/src/Reports/ПроданныйТоварБезНакладной/ObjectModule.bsl
 M src/cf/src/Reports/ПроданныйТоварБезНакладной/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ФинансовыйРезультат/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Roles/MobileClient/Rights.rights
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Sequences/Основная/Основная.mdo
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
?? .ai/reports/warehouse-orders-cost-f2-final-check.md
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
?? .ai/reviews/warehouse-orders-cost-f2/
?? .ai/reviews/warehouse-orders-option/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/order-payment-state.md
?? docs/plans/warehouse-orders-cost-phase2-prompt.md
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
+	// BSLLS:MagicNumber-off - две партии по 10 штук ценой 10 и 30, продажа 15 штук по 50 - себестоимость 250.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - партии 10 по 10 и 5 по 30, продажа 15; возвраты 12 и 3.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - партии 1 по 10 и 1 по 30, продажа 2, возврат двумя строками по 1.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - партия 20 по 10, продажа 3, возврат 1; позже - поступление задним числом 20 по 4.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - партии 1 по 10 и 1 по 30, продажа 2 по 50; исторический возврат 1 из партии 2 со
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.120 → 2.0.16.121

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
