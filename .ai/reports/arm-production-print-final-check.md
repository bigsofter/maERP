# Final check — arm-production-print
_20261027T061153Z_


## Scope

```
.ai/reports/arm-production-print-final-check.md
.ai/reports/arm-purchasing-receipts-final-check.md
.ai/reports/arm-purchasing-receipts-s2-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reviews/arm-production-print/03-code-review.json
.ai/reviews/arm-production-print/03b-code-review-verify.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/ai1c-extension-compat-prompt.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/refcheck-known.txt
src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
src/cf/src/Documents/ПриходныйОрдер/ManagerModule.bsl
src/cf/src/Documents/ЗаказПоставщику/ManagerModule.bsl
src/cf/src/Documents/ПередачаВПереработку/ManagerModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ManagerModule.bsl
src/cf/src/Documents/ПоступлениеИзПереработки/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-27T07:12:02.713+01:00  INFO 80983 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/822 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/822 (0:00:01 / 0:01:31) Analyzing files...   7% [=                       ]  59/822 (0:00:02 / 0:00:25) Analyzing files...  17% [====                    ] 143/822 (0:00:03 / 0:00:14) Analyzing files...  29% [=======                 ] 244/822 (0:00:04 / 0:00:09) Analyzing files...  49% [===========             ] 408/822 (0:00:05 / 0:00:05) Analyzing files...  65% [===============         ] 537/822 (0:00:06 / 0:00:03) Analyzing files...  73% [=================       ] 601/822 (0:00:07 / 0:00:02) Analyzing files...  74% [=================       ] 609/822 (0:00:08 / 0:00:02) Analyzing files...  75% [==================      ] 623/822 (0:00:09 / 0:00:02) Analyzing files...  84% [====================    ] 697/822 (0:00:10 / 0:00:01) Analyzing files...  96% [======================= ] 796/822 (0:00:11 / 0:00:00) Analyzing files... 100% [========================] 822/822 (0:00:11 / 0:00:00) Analyzing files... 100% [========================] 822/822 (0:00:11 / 0:00:00) 
2026-10-27T07:12:17.961+01:00  INFO 80983 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 10
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.100.json
версия 2.0.16.100: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M scripts/refcheck-known.txt
 M src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
 M src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПоставщику/ManagerModule.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ManagerModule.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/ManagerModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ManagerModule.bsl
 M src/cf/src/Documents/ПриходныйОрдер/ManagerModule.bsl
 M src/cf/src/Documents/РасходныйОрдер/ManagerModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
?? .ai/reports/arm-production-print-final-check.md
?? .ai/reports/arm-purchasing-receipts-final-check.md
?? .ai/reports/arm-purchasing-receipts-s2-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reviews/arm-production-print/
?? .ai/reviews/machine-form/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/ai1c-extension-compat-prompt.md
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
2.0.16.99 → 2.0.16.100

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
