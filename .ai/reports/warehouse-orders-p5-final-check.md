# Final check — warehouse-orders-p5
_20261015T125026Z_


## Scope

```
.ai/reports/warehouse-orders-p5-final-check.md
.ai/reports/warehouse-orders.md
.ai/reviews/warehouse-orders-p5/02-plan-review.json
.ai/reviews/warehouse-orders-p5/03-code-review.json
.ai/reviews/warehouse-orders-p5/03b-code-review-verify.json
.ai/reviews/warehouse-orders-p5/04-database-review.json
docs/plans/warehouse-orders.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/formgen/warehouse-orders/mobile.py
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокументаМобильныйКлиент/Form.form
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокументаМобильныйКлиент/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
src/cf/src/Reports/ТоварыВНаличии/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ПланированиеЗакупок/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-15T13:50:35.021+01:00  INFO 73367 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/817 (0:00:00 / ?) Analyzing files...   4% [=                       ]  38/817 (0:00:01 / 0:00:20) Analyzing files...  21% [=====                   ] 172/817 (0:00:02 / 0:00:07) Analyzing files...  41% [=========               ] 337/817 (0:00:03 / 0:00:04) Analyzing files...  65% [===============         ] 536/817 (0:00:04 / 0:00:02) Analyzing files...  83% [====================    ] 685/817 (0:00:05 / 0:00:00) Analyzing files...  94% [======================  ] 770/817 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:06 / 0:00:00) 
2026-10-15T13:50:44.338+01:00  INFO 73367 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 5
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.80.json
версия 2.0.16.80: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M .ai/reports/warehouse-orders.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/warehouse-orders.md
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокументаМобильныйКлиент/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокументаМобильныйКлиент/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
 M src/cf/src/Reports/ПланированиеЗакупок/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыВНаличии/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
?? .ai/reports/warehouse-orders-p5-final-check.md
?? .ai/reviews/warehouse-orders-p5/
?? scripts/formgen/warehouse-orders/mobile.py
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
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.79 → 2.0.16.80

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
