# Final check — print-language
_20261006T074028Z_


## Scope

```
.ai/reports/print-language-final-check.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/CommonForms/ПечатьДокументов/Form.form
src/cf/src/CommonForms/ПечатьДокументов/Module.bsl
src/cf/src/CommonModules/ПечатныеФормыПовтИсп/ПечатныеФормыПовтИсп.mdo
src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
src/cf/src/CommonModules/ПечатныеФормыПовтИсп/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
src/cf/src/Subsystems/ПечатныеФормы/ПечатныеФормы.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-06T08:40:37.016+01:00  INFO 98542 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/760 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/760 (0:00:01 / 0:01:23) Analyzing files...  10% [==                      ]  83/760 (0:00:02 / 0:00:16) Analyzing files...  24% [=====                   ] 183/760 (0:00:03 / 0:00:09) Analyzing files...  38% [=========               ] 293/760 (0:00:04 / 0:00:06) Analyzing files...  51% [============            ] 388/760 (0:00:05 / 0:00:04) Analyzing files...  66% [===============         ] 503/760 (0:00:06 / 0:00:03) Analyzing files...  80% [===================     ] 609/760 (0:00:07 / 0:00:01) Analyzing files...  89% [=====================   ] 680/760 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 760/760 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 760/760 (0:00:08 / 0:00:00) 
2026-10-06T08:40:49.655+01:00  INFO 98542 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.18.json
версия 2.0.16.18: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/CommonForms/ПечатьДокументов/Form.form
 M src/cf/src/CommonForms/ПечатьДокументов/Module.bsl
 M src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
 M src/cf/src/Subsystems/ПечатныеФормы/ПечатныеФормы.mdo
?? .ai/reports/print-language-final-check.md
?? src/cf/src/CommonModules/ПечатныеФормыПовтИсп/
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
+		// BSLLS:DeprecatedMethodCall-off
+		// BSLLS:DeprecatedMethodCall-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.17 → 2.0.16.18

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
