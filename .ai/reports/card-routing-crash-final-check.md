# Final check — card-routing-crash
_20261027T121421Z_


## Scope

```
.ai/reports/arm-production-print-final-check.md
.ai/reports/arm-purchasing-receipts-final-check.md
.ai/reports/arm-purchasing-receipts-s2-final-check.md
.ai/reports/card-routing-crash-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/order-stock-places-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reviews/arm-production-print/03-code-review.json
.ai/reviews/arm-production-print/03b-code-review-verify.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/semi-finished-subcontract/02-plan-review-r2.json
.ai/reviews/semi-finished-subcontract/02-plan-review-r3.json
.ai/reviews/semi-finished-subcontract/02-plan-review-r4.json
.ai/reviews/semi-finished-subcontract/02-plan-review-r5.json
.ai/reviews/semi-finished-subcontract/02-plan-review.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/semi-finished-subcontract.md
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-27T13:14:30.769+01:00  INFO 57200 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/822 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/822 (0:00:01 / 0:01:30) Analyzing files...   8% [=                       ]  67/822 (0:00:02 / 0:00:22) Analyzing files...  16% [====                    ] 139/822 (0:00:03 / 0:00:14) Analyzing files...  25% [======                  ] 210/822 (0:00:04 / 0:00:11) Analyzing files...  42% [==========              ] 349/822 (0:00:05 / 0:00:06) Analyzing files...  59% [==============          ] 486/822 (0:00:06 / 0:00:04) Analyzing files...  70% [================        ] 576/822 (0:00:07 / 0:00:02) Analyzing files...  78% [==================      ] 646/822 (0:00:08 / 0:00:02) Analyzing files...  85% [====================    ] 700/822 (0:00:09 / 0:00:01) Analyzing files... 100% [========================] 822/822 (0:00:09 / 0:00:00) Analyzing files... 100% [========================] 822/822 (0:00:09 / 0:00:00) 
2026-10-27T13:14:45.317+01:00  INFO 57200 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 1
новых замечаний нет
```
**PASS**
### уровень 0.5: scripts/refcheck.py
```
Сверка ссылок: расхождений нет (известных — 51)
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
Языков: 4, пунктов изменений: 4
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.102.json
версия 2.0.16.102: ru=1, fr=1, en=1, es=1
```
**PASS**

## Git hygiene

### git status
```
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
?? .ai/reports/arm-production-print-final-check.md
?? .ai/reports/arm-purchasing-receipts-final-check.md
?? .ai/reports/arm-purchasing-receipts-s2-final-check.md
?? .ai/reports/card-routing-crash-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/order-stock-places-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reviews/arm-production-print/
?? .ai/reviews/machine-form/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/semi-finished-subcontract/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/semi-finished-subcontract.md
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
2.0.16.101 → 2.0.16.102

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
