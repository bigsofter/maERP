# Final check — forms-no-scroll-messages
_20261018T083333Z_


## Scope

```
.ai/reports/forms-no-scroll-messages-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reviews/forms-no-scroll-messages/02-plan-review.json
.ai/reviews/forms-no-scroll-messages/03-code-review.json
.ai/reviews/forms-no-scroll-messages/03b-code-review-verify.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/FORMS-STYLE.md
docs/plans/forms-no-scroll-messages.md
docs/ROADMAP.md
docs/TECHDEBT.md
src/cf/src/CommonModules/РаботаСДокументамиКлиентСервер/Module.bsl
src/cf/src/CommonPictures/ПанельСообщения/ПанельСообщения.mdo
src/cf/src/CommonPictures/ПанельСообщения/Picture.zip
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-18T09:34:02.409+01:00  INFO 1465 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/818 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/818 (0:00:01 / 0:01:30) Analyzing files...   3% [                        ]  29/818 (0:00:02 / 0:00:54) Analyzing files...   5% [=                       ]  44/818 (0:00:03 / 0:00:53) Analyzing files...   7% [=                       ]  59/818 (0:00:04 / 0:00:51) Analyzing files...   9% [==                      ]  75/818 (0:00:05 / 0:00:49) Analyzing files...  11% [==                      ]  95/818 (0:00:06 / 0:00:45) Analyzing files...  13% [===                     ] 110/818 (0:00:07 / 0:00:45) Analyzing files...  15% [===                     ] 130/818 (0:00:08 / 0:00:42) Analyzing files...  16% [===                     ] 132/818 (0:00:09 / 0:00:46) Analyzing files...  16% [===                     ] 136/818 (0:00:10 / 0:00:50) Analyzing files...  19% [====                    ] 160/818 (0:00:11 / 0:00:45) Analyzing files...  20% [====                    ] 168/818 (0:00:12 / 0:00:46) Analyzing files...  22% [=====                   ] 180/818 (0:00:13 / 0:00:46) Analyzing files...  24% [=====                   ] 199/818 (0:00:14 / 0:00:43) Analyzing files...  29% [=======                 ] 240/818 (0:00:15 / 0:00:36) Analyzing files...  34% [========                ] 279/818 (0:00:16 / 0:00:30) Analyzing files...  38% [=========               ] 313/818 (0:00:17 / 0:00:27) Analyzing files...  40% [=========               ] 329/818 (0:00:18 / 0:00:26) Analyzing files...  42% [==========              ] 346/818 (0:00:19 / 0:00:25) Analyzing files...  52% [============            ] 432/818 (0:00:20 / 0:00:17) Analyzing files...  68% [================        ] 563/818 (0:00:21 / 0:00:09) Analyzing files...  78% [==================      ] 646/818 (0:00:22 / 0:00:05) Analyzing files...  89% [=====================   ] 732/818 (0:00:23 / 0:00:02) Analyzing files... 100% [========================] 818/818 (0:00:23 / 0:00:00) Analyzing files... 100% [========================] 818/818 (0:00:23 / 0:00:00) 
2026-10-18T09:34:40.731+01:00  INFO 1465 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Сверка ссылок: расхождений нет (известных — 50)
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.93.json
версия 2.0.16.93: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/FORMS-STYLE.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 A docs/plans/forms-no-scroll-messages.md
 M src/cf/src/CommonModules/РаботаСДокументамиКлиентСервер/Module.bsl
 A src/cf/src/CommonPictures/ПанельСообщения/Picture.zip
 A src/cf/src/CommonPictures/ПанельСообщения/ПанельСообщения.mdo
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
?? .ai/reports/forms-no-scroll-messages-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reviews/forms-no-scroll-messages/
?? .ai/reviews/machine-form/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/wo-techdebt2/
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
2.0.16.92 → 2.0.16.93

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
