# Final check — subcontract-multi-order-b2
_20261102T202107Z_


## Scope

```
.ai/reports/arm-pf-output-final-check.md
.ai/reports/arm-production-print-final-check.md
.ai/reports/arm-props-from-gp-final-check.md
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
.ai/reports/nomenclature-card-layout-final-check.md
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
.ai/reports/subcontract-multi-order-b2-final-check.md
.ai/reports/subcontract-multi-order-b2.md
.ai/reports/subcontract-multi-order-final-check.md
.ai/reports/subcontract-partial-receipt-final-check.md
.ai/reports/tabs-handlers-final-check.md
.ai/reports/transfer-act-print-final-check.md
.ai/reports/transfer-row-product-field-final-check.md
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
.ai/reviews/subcontract-multi-order-b2/03-code-review.json
.ai/reviews/subcontract-multi-order-b2/03b-code-review-verify.json
.ai/reviews/subcontract-multi-order-b2/04-database-review.json
.ai/reviews/subcontract-multi-order-documents/02-plan-review.json
.ai/reviews/subcontract-partial-receipt/03-code-review.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/warehouse-orders-option/02-plan-review.json
.ai/reviews/warehouse-orders-option/03-code-review.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify.json
.ai/reviews/warehouse-orders-option/04-database-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/order-payment-state.md
docs/plans/subcontract-multi-order-documents.md
docs/plans/subcontract-multi-order.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/АРМПроизводство.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/ЗаполнениеПередачи/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/Forms/ЗаполнениеПередачи/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/ПередачаВПереработку/ManagerModule.bsl
src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-02T21:21:16.047+01:00  INFO 10485 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/840 (0:00:00 / ?) Analyzing files...   3% [                        ]  28/840 (0:00:01 / 0:00:29) Analyzing files...  16% [===                     ] 135/840 (0:00:02 / 0:00:10) Analyzing files...  33% [========                ] 282/840 (0:00:03 / 0:00:05) Analyzing files...  53% [============            ] 450/840 (0:00:04 / 0:00:03) Analyzing files...  69% [================        ] 581/840 (0:00:05 / 0:00:02) Analyzing files...  92% [======================  ] 780/840 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 840/840 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 840/840 (0:00:07 / 0:00:00) 
2026-11-02T21:21:26.299+01:00  INFO 10485 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 6
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
Языков: 4, пунктов изменений: 20
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.143.json
версия 2.0.16.143: ru=5, fr=5, en=5, es=5
```
**PASS**

## Git hygiene

### git status
```
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/subcontract-multi-order.md
 M src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/АРМПроизводство.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ManagerModule.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
?? .ai/reports/arm-pf-output-final-check.md
?? .ai/reports/arm-production-print-final-check.md
?? .ai/reports/arm-props-from-gp-final-check.md
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
?? .ai/reports/nomenclature-card-layout-final-check.md
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
?? .ai/reports/subcontract-multi-order-b2-final-check.md
?? .ai/reports/subcontract-multi-order-b2.md
?? .ai/reports/subcontract-multi-order-final-check.md
?? .ai/reports/subcontract-partial-receipt-final-check.md
?? .ai/reports/tabs-handlers-final-check.md
?? .ai/reports/transfer-act-print-final-check.md
?? .ai/reports/transfer-row-product-field-final-check.md
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
?? .ai/reviews/subcontract-multi-order-b2/
?? .ai/reviews/subcontract-multi-order-documents/
?? .ai/reviews/subcontract-partial-receipt/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/warehouse-orders-option/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/order-payment-state.md
?? docs/plans/subcontract-multi-order-documents.md
?? src/cf/src/DataProcessors/АРМПроизводство/Forms/ЗаполнениеПередачи/
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
+	// BSLLS:MagicNumber-off - заказы на 5 и 3 изделия, норма сырья 1, закуплено 20.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.142 → 2.0.16.143

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
