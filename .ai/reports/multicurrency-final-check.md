# Final check — multicurrency
_20261006T140125Z_


## Scope

```
.ai/reports/multicurrency-final-check.md
.ai/reviews/multicurrency/01-plan-review-claude.md
.ai/reviews/multicurrency/02-code-review-claude.md
.ai/reviews/multicurrency/03-database-review-claude.md
.ai/reviews/multicurrency/04-security-review-claude.md
.ai/reviews/multicurrency/05-verify-claude.md
docs/plans/multicurrency.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ВзаиморасчётыСПокупателями.mdo
src/cf/src/AccumulationRegisters/Продажи/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ЗаказыПоставщикам/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ДополнительныеРасходы/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
src/cf/src/Catalogs/ВидыЦен/ВидыЦен.mdo
src/cf/src/Catalogs/ВидыЦен/Forms/ФормаЭлемента/Form.form
src/cf/src/CommonModules/РаботаСВалютами/РаботаСВалютами.mdo
src/cf/src/CommonModules/РаботаСВалютамиКлиентСервер/РаботаСВалютамиКлиентСервер.mdo
src/cf/src/CommonModules/РаботаСВалютами/Module.bsl
src/cf/src/CommonModules/СерииИРазмещение/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/РаботаСДокументамиКлиент/Module.bsl
src/cf/src/CommonModules/РаботаСВалютамиКлиентСервер/Module.bsl
src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonModules/ОбщегоНазначенияВызовСервераПовтИсп/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокументаМобильныйКлиент/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ManagerModule.bsl
src/cf/src/Documents/НалоговаяНакладная/ObjectModule.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
src/cf/src/InformationRegisters/КурсыВалют/КурсыВалют.mdo
src/cf/src/InformationRegisters/ЦеныНоменклатурыПоставщиков/ManagerModule.bsl
src/cf/src/Roles/Клиент/Rights.rights
src/cf/src/Roles/Оператор/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/ЛичныйКабинет/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Roles/MobileClient/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
src/cf/src/Subsystems/Казначейство/Subsystems/Справочники/Справочники.mdo
src/cf/src/Subsystems/Казначейство/Subsystems/Справочники/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-06T15:01:37.545+01:00  INFO 12809 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/762 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/762 (0:00:01 / 0:01:24) Analyzing files...  16% [===                     ] 124/762 (0:00:02 / 0:00:10) Analyzing files...  30% [=======                 ] 235/762 (0:00:03 / 0:00:06) Analyzing files...  34% [========                ] 260/762 (0:00:04 / 0:00:07) Analyzing files...  39% [=========               ] 304/762 (0:00:05 / 0:00:07) Analyzing files...  51% [============            ] 392/762 (0:00:06 / 0:00:05) Analyzing files...  68% [================        ] 520/762 (0:00:07 / 0:00:03) Analyzing files...  79% [===================     ] 607/762 (0:00:08 / 0:00:02) Analyzing files...  96% [======================= ] 736/762 (0:00:09 / 0:00:00) Analyzing files... 100% [========================] 762/762 (0:00:09 / 0:00:00) Analyzing files... 100% [========================] 762/762 (0:00:09 / 0:00:00) 
2026-10-06T15:01:50.459+01:00  INFO 12809 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 32
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.22.json
версия 2.0.16.22: ru=8, fr=8, en=8, es=8
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ВзаиморасчётыСПокупателями.mdo
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ВзаиморасчётыСПоставщиками.mdo
 M src/cf/src/AccumulationRegisters/ДополнительныеРасходы/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ЗаказыПоставщикам/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/Продажи/ManagerModule.bsl
 M src/cf/src/Catalogs/ВидыЦен/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/ВидыЦен/ВидыЦен.mdo
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
 M src/cf/src/CommonModules/ОбщегоНазначенияВызовСервераПовтИсп/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиВызовСервера/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиКлиент/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиКлиентСервер/Module.bsl
 M src/cf/src/CommonModules/СерииИРазмещение/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/НалоговаяНакладная/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ManagerModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокументаМобильныйКлиент/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
 M src/cf/src/InformationRegisters/ЦеныНоменклатурыПоставщиков/ManagerModule.bsl
 M src/cf/src/Roles/MobileClient/Rights.rights
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/Клиент/Rights.rights
 M src/cf/src/Roles/ЛичныйКабинет/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Subsystems/Казначейство/Subsystems/Справочники/CommandInterface.cmi
 M src/cf/src/Subsystems/Казначейство/Subsystems/Справочники/Справочники.mdo
?? .ai/reports/multicurrency-final-check.md
?? .ai/reviews/multicurrency/
?? docs/plans/multicurrency.md
?? src/cf/src/CommonModules/РаботаСВалютами/
?? src/cf/src/CommonModules/РаботаСВалютамиКлиентСервер/
?? src/cf/src/InformationRegisters/КурсыВалют/
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
2.0.16.21 → 2.0.16.22

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
