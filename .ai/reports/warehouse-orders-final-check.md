# Final check — warehouse-orders
_20261015T155324Z_


## Scope

```
.ai/reports/warehouse-orders-final-check.md
.ai/reports/warehouse-orders.md
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/uncommitted/03b-code-review-verify.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/warehouse-orders.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/RecordSetModule.bsl
src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
src/cf/src/CommonModules/ПодпискиНаСобытия/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/EventSubscriptions/ПрежниеПозицииСкладаПередЗаписью/ПрежниеПозицииСкладаПередЗаписью.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-15T16:53:32.220+01:00  INFO 81252 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                        ]   0/817 (0:00:00 / 0:00:02) Analyzing files...   1% [                        ]   9/817 (0:00:01 / 0:01:30) Analyzing files...   9% [==                      ]  76/817 (0:00:02 / 0:00:19) Analyzing files...  28% [======                  ] 229/817 (0:00:03 / 0:00:07) Analyzing files...  42% [==========              ] 347/817 (0:00:04 / 0:00:05) Analyzing files...  57% [=============           ] 466/817 (0:00:05 / 0:00:03) Analyzing files...  63% [===============         ] 520/817 (0:00:06 / 0:00:03) Analyzing files...  82% [===================     ] 674/817 (0:00:07 / 0:00:01) Analyzing files... 100% [========================] 817/817 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:07 / 0:00:00) 
2026-10-15T16:53:43.121+01:00  INFO 81252 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 8
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.81.json
версия 2.0.16.81: ru=2, fr=2, en=2, es=2
```
**PASS**

## Git hygiene

### git status
```
 M .ai/reports/warehouse-orders-final-check.md
 M .ai/reports/warehouse-orders.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/warehouse-orders.md
 M src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыНаСкладах/RecordSetModule.bsl
 M src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
 M src/cf/src/CommonModules/ПодпискиНаСобытия/Module.bsl
 M src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
?? .ai/reviews/uncommitted/
?? .ai/reviews/wo-techdebt2/
?? src/cf/src/EventSubscriptions/ПрежниеПозицииСкладаПередЗаписью/
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
+	// BSLLS:MagicNumber-off - заказы на 5 и 3 единицы.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - минимум 5, строки ордера по 10.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.80 → 2.0.16.81

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
