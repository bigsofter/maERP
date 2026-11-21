# Final check — order-number-tax-invoice
_20261111T071703Z_


## Scope

```
.ai/reports/order-number-tax-invoice-final-check.md
.ai/reviews/order-number-tax-invoice/03-code-review.json
.ai/reviews/order-number-tax-invoice/03b-code-review-verify.json
docs/plans/customer-order-number.md
docs/TECHDEBT.md
docs/TESTING.md
src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
src/cf/src/Documents/НалоговаяНакладная/ManagerModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-11T08:17:13.110+01:00  INFO 72650 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/860 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/860 (0:00:01 / 0:01:35) Analyzing files...   6% [=                       ]  52/860 (0:00:02 / 0:00:31) Analyzing files...  15% [===                     ] 135/860 (0:00:03 / 0:00:16) Analyzing files...  25% [======                  ] 218/860 (0:00:04 / 0:00:11) Analyzing files...  36% [========                ] 317/860 (0:00:05 / 0:00:08) Analyzing files...  47% [===========             ] 411/860 (0:00:06 / 0:00:06) Analyzing files...  62% [===============         ] 541/860 (0:00:07 / 0:00:04) Analyzing files...  77% [==================      ] 670/860 (0:00:08 / 0:00:02) Analyzing files...  91% [======================  ] 791/860 (0:00:09 / 0:00:00) Analyzing files...  99% [======================= ] 858/860 (0:00:10 / 0:00:00) Analyzing files... 100% [========================] 860/860 (0:00:10 / 0:00:00) Analyzing files... 100% [========================] 860/860 (0:00:10 / 0:00:00) 
2026-11-11T08:17:27.941+01:00  INFO 72650 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-11-10 19:03:41; изменённых модулей: 6
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
Языков: 4, пунктов изменений: 8
Описание изменений: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/changelog-2.0.17.11.json
версия 2.0.17.11: ru=2, fr=2, en=2, es=2
```
**PASS**

## Git hygiene

### git status
```
 M docs/TECHDEBT.md
MM docs/TESTING.md
 M docs/plans/customer-order-number.md
M  src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
MM src/cf/src/Configuration/Configuration.mdo
MM src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
M  src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Form.form
M  src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
M  src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
M  src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
MM src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
 M src/cf/src/Documents/НалоговаяНакладная/ManagerModule.bsl
M  src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
?? .ai/reports/order-number-tax-invoice-final-check.md
?? .ai/reviews/order-number-tax-invoice/
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
2.0.17.10 → 2.0.17.11

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
