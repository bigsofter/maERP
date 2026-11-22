# Final check — kp-print-terms
_20261101T153558Z_


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
.ai/reports/currency-words-fill-final-check.md
.ai/reports/input-by-string-roles-final-check.md
.ai/reports/kp-print-terms-final-check.md
.ai/reports/lot-traceability-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/manual-output-from-stock-final-check.md
.ai/reports/operator-subcontract-print-final-check.md
.ai/reports/order-list-columns-final-check.md
.ai/reports/order-money-status-final-check.md
.ai/reports/order-stock-places-final-check.md
.ai/reports/processing-by-processor-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/reports-console-final-check.md
.ai/reports/reports-variants-final-check.md
.ai/reports/role-print-commands-final-check.md
.ai/reports/sales-print-menu-final-check.md
.ai/reports/semi-finished-from-stock-final-check.md
.ai/reports/semi-finished-leaf-final-check.md
.ai/reports/semi-finished-subcontract-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reports/startup-forms-warehouse-role-final-check.md
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
.ai/reviews/kp-print-terms/02-plan-review-r2.json
.ai/reviews/kp-print-terms/02-plan-review-r3.json
.ai/reviews/kp-print-terms/02-plan-review-r4.json
.ai/reviews/kp-print-terms/02-plan-review.json
.ai/reviews/kp-print-terms/03-code-review-r1.json
.ai/reviews/kp-print-terms/03-code-review.json
.ai/reviews/kp-print-terms/03b-code-review-verify-r1.json
.ai/reviews/kp-print-terms/03b-code-review-verify.json
.ai/reviews/kp-print-terms/04-database-review.json
.ai/reviews/kp-print-terms/05-security-review.json
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
.ai/reviews/warehouse-orders-option/02-plan-review.json
.ai/reviews/warehouse-orders-option/03-code-review.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify.json
.ai/reviews/warehouse-orders-option/04-database-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/kp-print-terms.md
docs/plans/order-payment-state.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTS.xlsx
scripts/mxlxgen/branded.py
src/cf/src/CommonModules/ПраваНаФайлы/ПраваНаФайлы.mdo
src/cf/src/CommonModules/ПраваНаФайлы/Module.bsl
src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
src/cf/src/CommonModules/ПрисоединённыеФайлыВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ФирменныйДокумент/Template.mxlx
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/DefinedTypes/ВладельцыПрисоединенныхФайлов/ВладельцыПрисоединенныхФайлов.mdo
src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
src/cf/src/Documents/КоммерческоеПредложение/Commands/ПечатьКоммерческоеПредложениеСВложениями/CommandModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/ObjectModule.bsl
src/cf/src/Enums/Инкотермс/Инкотермс.mdo
src/cf/src/InformationRegisters/ПрисоединённыеФайлы/RecordSetModule.bsl
src/cf/src/Roles/Оператор/Rights.rights
src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-01T16:36:07.985+01:00  INFO 60679 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/839 (0:00:00 / ?) Analyzing files...   6% [=                       ]  58/839 (0:00:01 / 0:00:13) Analyzing files...  20% [====                    ] 173/839 (0:00:02 / 0:00:07) Analyzing files...  33% [========                ] 285/839 (0:00:03 / 0:00:05) Analyzing files...  47% [===========             ] 398/839 (0:00:04 / 0:00:04) Analyzing files...  57% [=============           ] 482/839 (0:00:05 / 0:00:03) Analyzing files...  60% [==============          ] 505/839 (0:00:06 / 0:00:03) Analyzing files...  70% [================        ] 594/839 (0:00:07 / 0:00:02) Analyzing files...  85% [====================    ] 715/839 (0:00:08 / 0:00:01) Analyzing files... 100% [========================] 839/839 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 839/839 (0:00:08 / 0:00:00) 
2026-11-01T16:36:21.091+01:00  INFO 60679 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 9
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.137.json
версия 2.0.16.137: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTS.xlsx
 M scripts/mxlxgen/branded.py
 M src/cf/src/CommonModules/ПрисоединённыеФайлыВызовСервера/Module.bsl
 M src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/CommonTemplates/ФирменныйДокумент/Template.mxlx
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/DefinedTypes/ВладельцыПрисоединенныхФайлов/ВладельцыПрисоединенныхФайлов.mdo
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/ObjectModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
 M src/cf/src/InformationRegisters/ПрисоединённыеФайлы/RecordSetModule.bsl
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
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
?? .ai/reports/currency-words-fill-final-check.md
?? .ai/reports/input-by-string-roles-final-check.md
?? .ai/reports/kp-print-terms-final-check.md
?? .ai/reports/lot-traceability-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/manual-output-from-stock-final-check.md
?? .ai/reports/operator-subcontract-print-final-check.md
?? .ai/reports/order-list-columns-final-check.md
?? .ai/reports/order-money-status-final-check.md
?? .ai/reports/order-stock-places-final-check.md
?? .ai/reports/processing-by-processor-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/reports-console-final-check.md
?? .ai/reports/reports-variants-final-check.md
?? .ai/reports/role-print-commands-final-check.md
?? .ai/reports/sales-print-menu-final-check.md
?? .ai/reports/semi-finished-from-stock-final-check.md
?? .ai/reports/semi-finished-leaf-final-check.md
?? .ai/reports/semi-finished-subcontract-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reports/startup-forms-warehouse-role-final-check.md
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
?? .ai/reviews/kp-print-terms/
?? .ai/reviews/machine-form/
?? .ai/reviews/order-list-columns/
?? .ai/reviews/order-payment-state/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/subcontract-late-receipt/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/warehouse-orders-option/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/kp-print-terms.md
?? docs/plans/order-payment-state.md
?? src/cf/src/CommonModules/ПраваНаФайлы/
?? src/cf/src/Documents/КоммерческоеПредложение/Commands/ПечатьКоммерческоеПредложениеСВложениями/
?? src/cf/src/Enums/Инкотермс/
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
+	// BSLLS:YoLetterUsage-off - имя регистра в метаданных.
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off - имя регистра в метаданных.
+	// BSLLS:YoLetterUsage-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.136 → 2.0.16.137

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
