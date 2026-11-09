# Final check — warehouse-orders-cost
_20261030T103758Z_


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
.ai/reports/warehouse-orders-cost-final-check.md
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
.ai/reviews/warehouse-orders-cost/02-plan-review-r1.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r10.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r11.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r2.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r3.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r4.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r5.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r6.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r7.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r8.json
.ai/reviews/warehouse-orders-cost/02-plan-review-r9.json
.ai/reviews/warehouse-orders-cost/02-plan-review.json
.ai/reviews/warehouse-orders-cost/03-code-review.json
.ai/reviews/warehouse-orders-cost/03b-code-review-verify.json
.ai/reviews/warehouse-orders-cost/04-database-review.json
.ai/reviews/warehouse-orders-option/02-plan-review.json
.ai/reviews/warehouse-orders-option/03-code-review.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify.json
.ai/reviews/warehouse-orders-option/04-database-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/order-payment-state.md
docs/plans/warehouse-orders-cost-prompt.md
docs/plans/warehouse-orders-cost.md
docs/plans/warehouse-orders.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
src/cf/src/CommonModules/ПроцедурыРегламентныхЗаданий/Module.bsl
src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/Дашборд/Forms/ДашбордПродаж/Module.bsl
src/cf/src/DataProcessors/Дашборд/Forms/БазовыйДашборд/Module.bsl
src/cf/src/DataProcessors/ПерепроведениеДокументов/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
src/cf/src/Documents/ТребованиеНакладная/ObjectModule.bsl
src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
src/cf/src/Documents/КорректировкаРегистров/ObjectModule.bsl
src/cf/src/InformationRegisters/НепроведенныеДокументы/НепроведенныеДокументы.mdo
src/cf/src/InformationRegisters/НепроведенныеДокументы/ManagerModule.bsl
src/cf/src/Reports/СтоимостьСклада/ObjectModule.bsl
src/cf/src/Reports/ВедомостьПоПродажам/ObjectModule.bsl
src/cf/src/Reports/СебестоимостьПродукции/ObjectModule.bsl
src/cf/src/Reports/ВедомостьПоТоварамНаСкладах/ObjectModule.bsl
src/cf/src/Sequences/Основная/Основная.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-30T11:38:06.778+01:00  INFO 37250 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/826 (0:00:00 / ?) Analyzing files...   3% [                        ]  27/826 (0:00:01 / 0:00:29) Analyzing files...  13% [===                     ] 115/826 (0:00:02 / 0:00:12) Analyzing files...  27% [======                  ] 228/826 (0:00:03 / 0:00:07) Analyzing files...  42% [==========              ] 354/826 (0:00:04 / 0:00:05) Analyzing files...  67% [================        ] 559/826 (0:00:05 / 0:00:02) Analyzing files...  88% [=====================   ] 733/826 (0:00:06 / 0:00:00) Analyzing files...  99% [======================= ] 818/826 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 826/826 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 826/826 (0:00:07 / 0:00:00) 
2026-10-30T11:38:17.530+01:00  INFO 37250 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 19
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
Языков: 4, пунктов изменений: 16
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.120.json
версия 2.0.16.120: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/warehouse-orders.md
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 M src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/Module.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ПроцедурыРегламентныхЗаданий/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/Дашборд/Forms/БазовыйДашборд/Module.bsl
 M src/cf/src/DataProcessors/Дашборд/Forms/ДашбордПродаж/Module.bsl
 M src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
 M src/cf/src/DataProcessors/ПерепроведениеДокументов/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
 M src/cf/src/Documents/КорректировкаРегистров/ObjectModule.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
 M src/cf/src/Documents/ТребованиеНакладная/ObjectModule.bsl
 M src/cf/src/InformationRegisters/НепроведенныеДокументы/ManagerModule.bsl
 M src/cf/src/InformationRegisters/НепроведенныеДокументы/НепроведенныеДокументы.mdo
 M src/cf/src/Reports/ВедомостьПоПродажам/ObjectModule.bsl
 M src/cf/src/Reports/ВедомостьПоТоварамНаСкладах/ObjectModule.bsl
 A src/cf/src/Reports/СебестоимостьПродукции/ObjectModule.bsl
 A src/cf/src/Reports/СтоимостьСклада/ObjectModule.bsl
 A src/cf/src/Reports/ФинансовыйРезультат/ObjectModule.bsl
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
?? .ai/reports/warehouse-orders-cost-final-check.md
?? .ai/reports/warehouse-orders-cost.md
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
?? .ai/reviews/warehouse-orders-cost/
?? .ai/reviews/warehouse-orders-option/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/order-payment-state.md
?? docs/plans/warehouse-orders-cost-prompt.md
?? docs/plans/warehouse-orders-cost.md
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
+	// BSLLS:MagicNumber-off - три выбора подряд: дальше параллельные правки - повод остановиться до следующего запуска
+	// BSLLS:MagicNumber-on
+	// BSLLS:QueryNestedFieldsByDot-off - признак проведения составного регистратора
+	// BSLLS:QueryNestedFieldsByDot-on
+	// BSLLS:QueryNestedFieldsByDot-off - признак проведения составного регистратора
+	// BSLLS:QueryNestedFieldsByDot-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:QueryNestedFieldsByDot-off
+	// BSLLS:QueryNestedFieldsByDot-on
+	// BSLLS:QueryNestedFieldsByDot-off - дата составного документа отметки
+	// BSLLS:QueryNestedFieldsByDot-on
+	// BSLLS:MagicNumber-off - материал 10 по 10, выпуск 5 продукции по 2 материала, продажа 5; поступление задним
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - заказ 10 продукции x 2 сырья, запуск и завершение 8 из 16.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.119 → 2.0.16.120

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
