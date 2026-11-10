# Final check — customer-order-number
_20261110T212745Z_


## Scope

```
.ai/reports/customer-order-number-final-check.md
.ai/reviews/customer-order-number/02-plan-review.json
.ai/reviews/customer-order-number/03-code-review.json
docs/plans/customer-order-number.md
src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-10T22:27:53.241+01:00  INFO 63457 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/860 (0:00:00 / ?) Analyzing files...   5% [=                       ]  47/860 (0:00:01 / 0:00:17) Analyzing files...  19% [====                    ] 169/860 (0:00:02 / 0:00:08) Analyzing files...  39% [=========               ] 340/860 (0:00:03 / 0:00:04) Analyzing files...  57% [=============           ] 496/860 (0:00:04 / 0:00:02) Analyzing files...  74% [=================       ] 640/860 (0:00:05 / 0:00:01) Analyzing files...  90% [=====================   ] 775/860 (0:00:06 / 0:00:00) Analyzing files...  99% [======================= ] 859/860 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 860/860 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 860/860 (0:00:08 / 0:00:00) 
2026-11-10T22:28:04.785+01:00  INFO 63457 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-11-10 19:03:41; изменённых модулей: 5
новых замечаний нет
```
**PASS**
### уровень 0.5: scripts/refcheck.py
```
Сверка ссылок: расхождений нет (известных — 48)
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/changelog-2.0.17.10.json
версия 2.0.17.10: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
?? .ai/reports/customer-order-number-final-check.md
?? .ai/reviews/customer-order-number/
?? docs/plans/customer-order-number.md
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
2.0.17.9 → 2.0.17.10

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
