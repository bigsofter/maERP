# Final check — multicurrency-orders
_20261006T164516Z_


## Scope

```
.ai/reports/multicurrency-orders-final-check.md
.ai/reviews/multicurrency-orders/01-plan-review-claude.md
.ai/reviews/multicurrency-orders/02-code-review-claude.md
.ai/reviews/multicurrency-orders/03-database-review-claude.md
.ai/reviews/multicurrency-orders/04-verify-claude.md
docs/plans/multicurrency-orders.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ЗаказыПоставщикам/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
src/cf/src/CommonModules/РаботаСВалютами/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonModules/РаботаСВалютамиКлиентСервер/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
src/cf/src/Documents/ПредложениеПоставщика/ПредложениеПоставщика.mdo
src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокументаМобильныйКлиент/Module.bsl
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокументаECommerce/Module.bsl
src/cf/src/Documents/ПредложениеПоставщика/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
src/cf/src/Documents/ПредложениеПоставщика/ObjectModule.bsl
src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/ObjectModule.bsl
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-06T17:45:25.909+01:00  INFO 66245 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/763 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/763 (0:00:01 / 0:01:24) Analyzing files...   3% [                        ]  30/763 (0:00:02 / 0:00:49) Analyzing files...  15% [===                     ] 118/763 (0:00:03 / 0:00:16) Analyzing files...  16% [===                     ] 125/763 (0:00:04 / 0:00:20) Analyzing files...  22% [=====                   ] 175/763 (0:00:05 / 0:00:16) Analyzing files...  25% [======                  ] 197/763 (0:00:06 / 0:00:17) Analyzing files...  27% [======                  ] 210/763 (0:00:07 / 0:00:18) Analyzing files...  28% [======                  ] 220/763 (0:00:08 / 0:00:19) Analyzing files...  31% [=======                 ] 245/763 (0:00:09 / 0:00:19) Analyzing files...  36% [========                ] 282/763 (0:00:10 / 0:00:17) Analyzing files...  44% [==========              ] 339/763 (0:00:11 / 0:00:13) Analyzing files...  50% [============            ] 387/763 (0:00:12 / 0:00:11) Analyzing files...  62% [==============          ] 474/763 (0:00:13 / 0:00:07) Analyzing files...  69% [================        ] 533/763 (0:00:14 / 0:00:06) Analyzing files...  87% [====================    ] 666/763 (0:00:15 / 0:00:02) Analyzing files...  96% [======================= ] 733/763 (0:00:16 / 0:00:00) Analyzing files... 100% [========================] 763/763 (0:00:16 / 0:00:00) Analyzing files... 100% [========================] 763/763 (0:00:16 / 0:00:00) 
2026-10-06T17:45:49.128+01:00  INFO 66245 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 20
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
Языков: 4, пунктов изменений: 32
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.24.json
версия 2.0.16.24: ru=8, fr=8, en=8, es=8
```
**PASS**

## Git hygiene

### git status
```
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ЗаказыПоставщикам/ManagerModule.bsl
 M src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
 M src/cf/src/CommonModules/РаботаСВалютами/Module.bsl
 M src/cf/src/CommonModules/РаботаСВалютамиКлиентСервер/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокументаECommerce/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ЗаказПоставщику/ObjectModule.bsl
 M src/cf/src/Documents/ЗаказПоставщику/ЗаказПоставщику.mdo
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/ObjectModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПредложениеПоставщика/ManagerModule.bsl
 M src/cf/src/Documents/ПредложениеПоставщика/ObjectModule.bsl
 M src/cf/src/Documents/ПредложениеПоставщика/ПредложениеПоставщика.mdo
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокументаМобильныйКлиент/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
?? .ai/reports/multicurrency-orders-final-check.md
?? .ai/reviews/multicurrency-orders/
?? docs/plans/multicurrency-orders.md
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
2.0.16.23 → 2.0.16.24

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
