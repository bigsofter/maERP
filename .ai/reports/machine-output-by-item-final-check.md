# Final check — machine-output-by-item
_20261009T175646Z_


## Scope

```
.ai/reports/machine-output-by-item-final-check.md
.ai/reviews/demo-data-button/02-plan-review.json
.ai/reviews/machine-output-by-item/02-plan-review.json
.ai/reviews/machine-output-by-item/03-code-review.json
.ai/reviews/machine-output-by-item/03b-code-review-verify.json
.ai/reviews/machine-output-by-item/04-database-review.json
docs/plans/demo-data-button.md
docs/plans/machine-output-by-item.md
docs/ROADMAP.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/Catalogs/ПроизводственноеОборудование/ПроизводственноеОборудование.mdo
src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаЭлемента/Module.bsl
src/cf/src/Catalogs/ПроизводственноеОборудование/ObjectModule.bsl
src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
src/cf/src/Reports/ЭффективностьСтанков/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-09T18:56:55.256+01:00  INFO 52163 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/797 (0:00:00 / ?) Analyzing files...   4% [                        ]  33/797 (0:00:01 / 0:00:23) Analyzing files...  12% [===                     ] 101/797 (0:00:02 / 0:00:14) Analyzing files...  32% [=======                 ] 261/797 (0:00:03 / 0:00:06) Analyzing files...  47% [===========             ] 382/797 (0:00:04 / 0:00:04) Analyzing files...  62% [===============         ] 499/797 (0:00:05 / 0:00:02) Analyzing files...  81% [===================     ] 647/797 (0:00:06 / 0:00:01) Analyzing files...  99% [======================= ] 791/797 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:07 / 0:00:00) 
2026-10-09T18:57:06.536+01:00  INFO 52163 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 6
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
Языков: 4, пунктов изменений: 4
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.46.json
версия 2.0.16.46: ru=1, fr=1, en=1, es=1
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаЭлемента/Module.bsl
 M src/cf/src/Catalogs/ПроизводственноеОборудование/ObjectModule.bsl
 M src/cf/src/Catalogs/ПроизводственноеОборудование/ПроизводственноеОборудование.mdo
 M src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
 M src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
 M src/cf/src/Reports/ЭффективностьСтанков/ManagerModule.bsl
?? .ai/reports/machine-output-by-item-final-check.md
?? .ai/reviews/demo-data-button/
?? .ai/reviews/machine-output-by-item/
?? docs/plans/demo-data-button.md
?? docs/plans/machine-output-by-item.md
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
+	// BSLLS:MagicNumber-off - станок 120 кг/ч и 15 мин на смену заказа; продукция P1 - 200 кг/ч, сырьё M1 - 60 кг/ч.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.45 → 2.0.16.46

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
