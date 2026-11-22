# Final check — warehouse-orders-cost-f4
_20261031T015144Z_


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
.ai/reviews/warehouse-orders-cost-f4/03-code-review-r1.json
.ai/reviews/warehouse-orders-cost-f4/03-code-review.json
.ai/reviews/warehouse-orders-cost-f4/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-cost-f4/03b-code-review-verify-r2.json
.ai/reviews/warehouse-orders-cost-f4/03b-code-review-verify.json
.ai/reviews/warehouse-orders-cost-f4/04-database-review-r1.json
.ai/reviews/warehouse-orders-cost-f4/04-database-review.json
.ai/reviews/warehouse-orders-cost-f4/05-security-review-r1.json
.ai/reviews/warehouse-orders-cost-f4/05-security-review.json
.ai/reviews/warehouse-orders-cost-f5/02-plan-review-r1.json
.ai/reviews/warehouse-orders-cost-f5/02-plan-review-r2.json
.ai/reviews/warehouse-orders-cost-f5/02-plan-review.json
.ai/reviews/warehouse-orders-option/02-plan-review.json
.ai/reviews/warehouse-orders-option/03-code-review.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify.json
.ai/reviews/warehouse-orders-option/04-database-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/order-payment-state.md
docs/plans/warehouse-orders-cost.md
docs/TECHDEBT.md
docs/TESTING.md
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыКОформлению/ManagerModule.bsl
src/cf/src/AccumulationRegisters/СебестоимостьПродаж/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ДополнительныеРасходы/ManagerModule.bsl
src/cf/src/CommonModules/ОрдераСклада/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/ПроцедурыРегламентныхЗаданий/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Constants/ДнейОжиданияОформления/ДнейОжиданияОформления.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ПриходныйОрдер/ПриходныйОрдер.mdo
src/cf/src/Documents/ПриходныйОрдер/ManagerModule.bsl
src/cf/src/Documents/ПриходныйОрдер/ObjectModule.bsl
src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/ObjectModule.bsl
src/cf/src/Reports/ОстаткиНаСкладах/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-31T02:51:50.970+01:00  INFO 26186 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/828 (0:00:00 / ?) Analyzing files...   1% [                        ]  12/828 (0:00:01 / 0:01:08) Analyzing files...  17% [====                    ] 145/828 (0:00:02 / 0:00:09) Analyzing files...  41% [=========               ] 342/828 (0:00:03 / 0:00:04) Analyzing files...  62% [===============         ] 520/828 (0:00:04 / 0:00:02) Analyzing files...  82% [===================     ] 685/828 (0:00:05 / 0:00:01) Analyzing files...  99% [======================= ] 823/828 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 828/828 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 828/828 (0:00:06 / 0:00:00) 
2026-10-31T02:52:00.739+01:00  INFO 26186 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 15
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
Языков: 4, пунктов изменений: 36
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.123.json
версия 2.0.16.123: ru=9, fr=9, en=9, es=9
```
**PASS**

## Git hygiene

### git status
```
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/plans/warehouse-orders-cost.md
 M src/cf/src/AccumulationRegisters/ДополнительныеРасходы/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/СебестоимостьПродаж/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыКОформлению/ManagerModule.bsl
 M src/cf/src/CommonModules/ОрдераСклада/Module.bsl
 M src/cf/src/CommonModules/ПроцедурыРегламентныхЗаданий/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/ПриходныйОрдер/ManagerModule.bsl
 M src/cf/src/Documents/ПриходныйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/ПриходныйОрдер/ПриходныйОрдер.mdo
 M src/cf/src/Documents/РасходныйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РасходныйОрдер/РасходныйОрдер.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Reports/ОстаткиНаСкладах/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
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
?? .ai/reviews/warehouse-orders-cost-f4/03-code-review-r1.json
?? .ai/reviews/warehouse-orders-cost-f4/03-code-review.json
?? .ai/reviews/warehouse-orders-cost-f4/03b-code-review-verify-r1.json
?? .ai/reviews/warehouse-orders-cost-f4/03b-code-review-verify-r2.json
?? .ai/reviews/warehouse-orders-cost-f4/03b-code-review-verify.json
?? .ai/reviews/warehouse-orders-cost-f4/04-database-review-r1.json
?? .ai/reviews/warehouse-orders-cost-f4/04-database-review.json
?? .ai/reviews/warehouse-orders-cost-f4/05-security-review-r1.json
?? .ai/reviews/warehouse-orders-cost-f4/05-security-review.json
?? .ai/reviews/warehouse-orders-cost-f5/
?? .ai/reviews/warehouse-orders-option/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/order-payment-state.md
?? src/cf/src/Constants/ДнейОжиданияОформления/
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
+	// BSLLS:MagicNumber-off - копейки
+	// BSLLS:MagicNumber-on
+	// BSLLS:SetPrivilegedMode-off - регламентное задание читает ордера и пишет оповещения всем получателям
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:MagicNumber-off - секунд в сутках
+	// BSLLS:MagicNumber-on
+	// BSLLS:VirtualTableCallWithoutParameters-off - все неоформленные остатки на текущий момент
+	// BSLLS:VirtualTableCallWithoutParameters-on
+	// BSLLS:MagicNumber-off - порог по умолчанию
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - цена продажи
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.122 → 2.0.16.123

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- новые объекты/формы (1 файлов), а реестр docs/TESTS.xlsx не менялся — изменение состава тестов фиксируется в реестре
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
