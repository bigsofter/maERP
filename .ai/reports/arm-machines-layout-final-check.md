# Final check — arm-machines-layout
_20261009T174015Z_


## Scope

```
.ai/reports/arm-machines-layout-final-check.md
.ai/reviews/arm-machines-layout/03-code-review.json
.ai/reviews/arm-machines-layout/03b-code-review-verify.json
.ai/reviews/machine-output-by-item/02-plan-review.json
docs/plans/demo-data-button.md
docs/plans/machine-output-by-item.md
docs/ROADMAP.md
docs/TECHDEBT.md
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
2026-10-09T18:40:24.189+01:00  INFO 22584 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/797 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/797 (0:00:01 / 0:01:28) Analyzing files...  13% [===                     ] 108/797 (0:00:02 / 0:00:12) Analyzing files...  28% [======                  ] 224/797 (0:00:03 / 0:00:07) Analyzing files...  41% [==========              ] 334/797 (0:00:04 / 0:00:05) Analyzing files...  57% [=============           ] 461/797 (0:00:05 / 0:00:03) Analyzing files...  71% [=================       ] 571/797 (0:00:06 / 0:00:02) Analyzing files...  84% [====================    ] 671/797 (0:00:07 / 0:00:01) Analyzing files...  99% [======================= ] 795/797 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:08 / 0:00:00) 
2026-10-09T18:40:36.071+01:00  INFO 22584 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 1
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.45.json
версия 2.0.16.45: ru=1, fr=1, en=1, es=1
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
?? .ai/reports/arm-machines-layout-final-check.md
?? .ai/reviews/arm-machines-layout/
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
none found

### Версия конфигурации
2.0.16.44 → 2.0.16.45

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
