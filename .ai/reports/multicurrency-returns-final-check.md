# Final check — multicurrency-returns
_20261006T173124Z_


## Scope

```
.ai/reports/multicurrency-returns-final-check.md
.ai/reports/multicurrency-returns.md
.ai/reviews/multicurrency-returns/01-plan-review-claude.md
.ai/reviews/multicurrency-returns/02-code-review-claude.md
.ai/reviews/multicurrency-returns/03-database-review-claude.md
.ai/reviews/multicurrency-returns/04-verify-claude.md
docs/plans/multicurrency-returns.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/Убытки/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСКонтрагентамиПрочие/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателямиНалоговый/ManagerModule.bsl
src/cf/src/CommonModules/РаботаСВалютами/Module.bsl
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonModules/РаботаСДокументамиВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ПрочиеРасходы/ПрочиеРасходы.mdo
src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/ПрочиеРасходыВозврат/ПрочиеРасходыВозврат.mdo
src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/КорректировкаДолга/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокументаМобильныйКлиент/Module.bsl
src/cf/src/Documents/НалоговаяНакладная/ManagerModule.bsl
src/cf/src/Documents/ПрочиеРасходы/ObjectModule.bsl
src/cf/src/Documents/НалоговаяНакладная/ObjectModule.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
src/cf/src/Documents/ПрочиеРасходыВозврат/ObjectModule.bsl
src/cf/src/Documents/РасходныйКассовыйОрдер/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеИзПереработки/ObjectModule.bsl
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ObjectModule.bsl
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
src/cf/src/Reports/РеестрНалоговыхНакладных/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьПоПродажамНалоговая/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-06T18:31:33.735+01:00  INFO 62367 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/763 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/763 (0:00:01 / 0:01:24) Analyzing files...  12% [==                      ]  95/763 (0:00:02 / 0:00:14) Analyzing files...  19% [====                    ] 145/763 (0:00:03 / 0:00:12) Analyzing files...  37% [========                ] 285/763 (0:00:04 / 0:00:06) Analyzing files...  52% [============            ] 404/763 (0:00:05 / 0:00:04) Analyzing files...  69% [================        ] 529/763 (0:00:06 / 0:00:02) Analyzing files...  93% [======================  ] 717/763 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 763/763 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 763/763 (0:00:07 / 0:00:00) 
2026-10-06T18:31:45.455+01:00  INFO 62367 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 25
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.25.json
версия 2.0.16.25: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСКонтрагентамиПрочие/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателямиНалоговый/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/Убытки/ManagerModule.bsl
 M src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
 M src/cf/src/CommonModules/РаботаСВалютами/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиВызовСервера/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ObjectModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
 M src/cf/src/Documents/КорректировкаДолга/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокументаМобильныйКлиент/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладная/ManagerModule.bsl
 M src/cf/src/Documents/НалоговаяНакладная/ObjectModule.bsl
 M src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
 M src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПрочиеРасходы/ObjectModule.bsl
 M src/cf/src/Documents/ПрочиеРасходы/ПрочиеРасходы.mdo
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПрочиеРасходыВозврат/ObjectModule.bsl
 M src/cf/src/Documents/ПрочиеРасходыВозврат/ПрочиеРасходыВозврат.mdo
 M src/cf/src/Documents/РасходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/СертификатНаОплату/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/СертификатНаОплату/ObjectModule.bsl
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
 M src/cf/src/Reports/ВедомостьПоПродажамНалоговая/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РеестрНалоговыхНакладных/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
?? .ai/reports/multicurrency-returns-final-check.md
?? .ai/reports/multicurrency-returns.md
?? .ai/reviews/multicurrency-returns/
?? docs/plans/multicurrency-returns.md
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
2.0.16.24 → 2.0.16.25

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
