# Final check — machines-occupancy
_20261009T154124Z_


## Scope

```
.ai/reports/machines-occupancy-final-check.md
.ai/reviews/machines-occupancy/02-plan-review.json
.ai/reviews/machines-occupancy/03-code-review.json
docs/plans/machines-occupancy.md
docs/ROADMAP.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
src/cf/src/Reports/ЗанятостьСтанков/ЗанятостьСтанков.mdo
src/cf/src/Reports/ЗанятостьСтанков/ManagerModule.bsl
src/cf/src/Reports/ЗанятостьСтанков/ObjectModule.bsl
src/cf/src/Reports/ЗанятостьСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Subsystems/Производство/Производство.mdo
src/cf/src/Subsystems/Производство/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-09T16:41:33.846+01:00  INFO 79338 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/797 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/797 (0:00:01 / 0:01:27) Analyzing files...  12% [===                     ] 102/797 (0:00:02 / 0:00:13) Analyzing files...  35% [========                ] 279/797 (0:00:03 / 0:00:05) Analyzing files...  49% [===========             ] 391/797 (0:00:04 / 0:00:04) Analyzing files...  65% [===============         ] 521/797 (0:00:05 / 0:00:02) Analyzing files...  81% [===================     ] 647/797 (0:00:06 / 0:00:01) Analyzing files...  99% [======================= ] 795/797 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:07 / 0:00:00) 
2026-10-09T16:41:44.890+01:00  INFO 79338 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 4
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.42.json
версия 2.0.16.42: ru=2, fr=2, en=2, es=2
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 A docs/plans/machines-occupancy.md
 M src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
 A src/cf/src/Reports/ЗанятостьСтанков/ManagerModule.bsl
 A src/cf/src/Reports/ЗанятостьСтанков/ObjectModule.bsl
 A src/cf/src/Reports/ЗанятостьСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 A src/cf/src/Reports/ЗанятостьСтанков/ЗанятостьСтанков.mdo
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Subsystems/Производство/CommandInterface.cmi
 M src/cf/src/Subsystems/Производство/Производство.mdo
?? .ai/reports/machines-occupancy-final-check.md
?? .ai/reviews/machines-occupancy/
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
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.41 → 2.0.16.42

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
