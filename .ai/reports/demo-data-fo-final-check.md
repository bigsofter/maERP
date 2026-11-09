# Final check — demo-data-fo
_20261009T210617Z_


## Scope

```
.ai/reports/demo-data-fo-final-check.md
.ai/reviews/arm-machines/02-plan-review.json
.ai/reviews/demo-data-fo/03-code-review.json
docs/plans/arm-machines.md
docs/plans/demo-data-button.md
docs/TESTING.md
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Module.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-09T22:06:25.064+01:00  INFO 71834 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/797 (0:00:00 / ?) Analyzing files...   4% [=                       ]  35/797 (0:00:01 / 0:00:21) Analyzing files...  19% [====                    ] 156/797 (0:00:02 / 0:00:08) Analyzing files...  38% [=========               ] 304/797 (0:00:03 / 0:00:04) Analyzing files...  60% [==============          ] 480/797 (0:00:04 / 0:00:02) Analyzing files...  80% [===================     ] 640/797 (0:00:05 / 0:00:01) Analyzing files...  99% [======================= ] 795/797 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:06 / 0:00:00) 
2026-10-09T22:06:34.839+01:00  INFO 71834 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 8
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.48.json
версия 2.0.16.48: ru=2, fr=2, en=2, es=2
```
**PASS**

## Git hygiene

### git status
```
 M docs/TESTING.md
 M docs/plans/demo-data-button.md
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Module.bsl
?? .ai/reports/demo-data-fo-final-check.md
?? .ai/reviews/arm-machines/
?? .ai/reviews/demo-data-fo/
?? docs/plans/arm-machines.md
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
2.0.16.47 → 2.0.16.48

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
