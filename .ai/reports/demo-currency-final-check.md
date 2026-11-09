# Final check — demo-currency
_20261015T223829Z_


## Scope

```
.ai/reports/demo-currency-final-check.md
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Module.bsl
src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-15T23:38:38.101+01:00  INFO 68761 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/818 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/818 (0:00:01 / 0:01:30) Analyzing files...  14% [===                     ] 115/818 (0:00:02 / 0:00:12) Analyzing files...  25% [======                  ] 211/818 (0:00:03 / 0:00:08) Analyzing files...  55% [=============           ] 457/818 (0:00:04 / 0:00:03) Analyzing files...  73% [=================       ] 601/818 (0:00:05 / 0:00:01) Analyzing files...  82% [===================     ] 676/818 (0:00:06 / 0:00:01) Analyzing files...  98% [======================= ] 804/818 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 818/818 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 818/818 (0:00:07 / 0:00:00) 
2026-10-15T23:38:48.807+01:00  INFO 68761 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 4
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.86.json
версия 2.0.16.86: ru=1, fr=1, en=1, es=1
```
**PASS**

## Git hygiene

### git status
```
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Module.bsl
 M src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
?? .ai/reports/demo-currency-final-check.md
?? .ai/reviews/performance-vt/
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
2.0.16.85 → 2.0.16.86

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
