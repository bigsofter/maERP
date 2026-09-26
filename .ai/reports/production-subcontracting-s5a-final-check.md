# Final check — production-subcontracting-s5a
_20260921T160705Z_


## Scope

```
.ai/reports/production-subcontracting-s5.md
.ai/reports/production-subcontracting-s5a-final-check.md
docs/plans/production-subcontracting-s4.md
docs/plans/production-subcontracting-s5.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ТоварыВПереработке/ManagerModule.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПередачаВПереработку/ManagerModule.bsl
src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеИзПереработки/ObjectModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-21T17:07:13.909+01:00  INFO 17203 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/740 (0:00:00 / ?) Analyzing files...   3% [                        ]  27/740 (0:00:01 / 0:00:26) Analyzing files...  20% [====                    ] 152/740 (0:00:02 / 0:00:07) Analyzing files...  47% [===========             ] 348/740 (0:00:03 / 0:00:03) Analyzing files...  75% [==================      ] 562/740 (0:00:04 / 0:00:01) Analyzing files...  95% [======================  ] 704/740 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 740/740 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 740/740 (0:00:05 / 0:00:00) 
2026-09-21T17:07:23.337+01:00  INFO 17203 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-09-19 09:10:00; изменённых модулей: 6
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
Языков: 4, пунктов изменений: 24
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.44.json
версия 2.0.15.44: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTS.xlsx
 M docs/plans/production-subcontracting-s4.md
 M src/cf/src/AccumulationRegisters/ТоварыВПереработке/ManagerModule.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ManagerModule.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
?? .ai/reports/production-subcontracting-s5.md
?? .ai/reports/production-subcontracting-s5a-final-check.md
?? docs/plans/production-subcontracting-s5.md
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
+	// BSLLS:MagicNumber-off - два заказа и одна беззаказная передача на один и тот же переработчик.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - поступило 3 из ожидаемых 4.
+	// BSLLS:MagicNumber-off - отгрузка 3 при поступивших 3; вторая передача 2, поздний приход 1.
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.15.43 → 2.0.15.44

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
