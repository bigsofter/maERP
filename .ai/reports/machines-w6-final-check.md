# Final check — machines-w6
_20261010T141907Z_


## Scope

```
.ai/reports/machines-w6-final-check.md
.ai/reports/machines-w6.md
.ai/reviews/machines-w6-s5/03-code-review.json
.ai/reviews/machines-w6-s5/03b-code-review-verify.json
.ai/reviews/machines-w6-s5/04-database-review.json
.ai/reviews/machines-w6-s5/05-security-review.json
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTS.xlsx
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ЗагрузкаСтанков/ЗагрузкаСтанков.mdo
src/cf/src/DataProcessors/ЗагрузкаСтанков/Forms/ПробаПланировщика/Form.form
src/cf/src/DataProcessors/ЗагрузкаСтанков/Forms/ПробаПланировщика/Module.bsl
src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
src/cf/src/Reports/ТоварыДляЗаказа/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/НедостаточныеЗапасы/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/MobileClient/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-10T15:19:15.675+01:00  INFO 25379 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/804 (0:00:00 / ?) Analyzing files...   1% [                        ]  10/804 (0:00:01 / 0:01:19) Analyzing files...  17% [====                    ] 143/804 (0:00:02 / 0:00:09) Analyzing files...  29% [=======                 ] 238/804 (0:00:03 / 0:00:07) Analyzing files...  54% [=============           ] 438/804 (0:00:04 / 0:00:03) Analyzing files...  74% [=================       ] 600/804 (0:00:05 / 0:00:01) Analyzing files...  85% [====================    ] 691/804 (0:00:06 / 0:00:00) Analyzing files...  99% [======================= ] 803/804 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 804/804 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 804/804 (0:00:07 / 0:00:00) 
2026-10-10T15:19:26.018+01:00  INFO 25379 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 16
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.58.json
версия 2.0.16.58: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTS.xlsx
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
D  src/cf/src/DataProcessors/ЗагрузкаСтанков/Forms/ПробаПланировщика/Form.form
D  src/cf/src/DataProcessors/ЗагрузкаСтанков/Forms/ПробаПланировщика/Module.bsl
D  src/cf/src/DataProcessors/ЗагрузкаСтанков/ЗагрузкаСтанков.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/Forms/Форма/Module.bsl
 M src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
 M src/cf/src/Reports/НедостаточныеЗапасы/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыДляЗаказа/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Roles/MobileClient/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
?? .ai/reports/machines-w6-final-check.md
?? .ai/reports/machines-w6.md
?? .ai/reviews/machines-w6-s5/
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
2.0.16.57 → 2.0.16.58

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
