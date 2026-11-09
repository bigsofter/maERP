# Final check — menu-restructure-1b
_20261002T151246Z_


## Scope

```
.ai/reports/menu-restructure-1b-final-check.md
docs/plans/menu-restructure.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/Catalogs/СерииНоменклатуры/ObjectModule.bsl
src/cf/src/CommonForms/ФормаПервогоЗапуска/Form.form
src/cf/src/CommonForms/ФормаПервогоЗапуска/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonModules/НачальноеЗаполнениеВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Constants/ИспользоватьЛиды/ИспользоватьЛиды.mdo
src/cf/src/Constants/ИспользоватьИмпорт/ИспользоватьИмпорт.mdo
src/cf/src/Constants/ИспользоватьПересчеты/ИспользоватьПересчеты.mdo
src/cf/src/Constants/ИспользоватьПереработку/ИспользоватьПереработку.mdo
src/cf/src/Constants/ИспользоватьКомплектацию/ИспользоватьКомплектацию.mdo
src/cf/src/Constants/ИспользоватьЗадачиЗаказов/ИспользоватьЗадачиЗаказов.mdo
src/cf/src/Constants/ИспользоватьРозничныеПродажи/ИспользоватьРозничныеПродажи.mdo
src/cf/src/Constants/ИспользоватьСерииНоменклатуры/ИспользоватьСерииНоменклатуры.mdo
src/cf/src/Constants/ИспользоватьЗаявкиНаПоискТовара/ИспользоватьЗаявкиНаПоискТовара.mdo
src/cf/src/Constants/ИспользоватьАльтернативныеОплаты/ИспользоватьАльтернативныеОплаты.mdo
src/cf/src/Constants/ИспользоватьПравилаЦенообразования/ИспользоватьПравилаЦенообразования.mdo
src/cf/src/Constants/ИспользоватьКоммерческиеПредложения/ИспользоватьКоммерческиеПредложения.mdo
src/cf/src/Constants/ИспользоватьХарактеристикиНоменклатуры/ИспользоватьХарактеристикиНоменклатуры.mdo
src/cf/src/DataProcessors/НастройкиПрограммы/НастройкиПрограммы.mdo
src/cf/src/DataProcessors/НастройкиПрограммы/Commands/Склад/CommandModule.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Commands/Бухгалтерия/CommandModule.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Commands/Казначейство/CommandModule.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Commands/CRM/CommandModule.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Склад/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Закупки/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Бухгалтерия/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Склад/Module.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Закупки/Module.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Бухгалтерия/Module.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Module.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/CRM/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/CRM/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/FunctionalOptions/Бухгалтерия/Бухгалтерия.mdo
src/cf/src/FunctionalOptions/Производство/Производство.mdo
src/cf/src/FunctionalOptions/ИспользоватьЛиды/ИспользоватьЛиды.mdo
src/cf/src/FunctionalOptions/ИспользоватьИмпорт/ИспользоватьИмпорт.mdo
src/cf/src/FunctionalOptions/ИспользоватьПересчеты/ИспользоватьПересчеты.mdo
src/cf/src/FunctionalOptions/ИспользоватьПереработку/ИспользоватьПереработку.mdo
src/cf/src/FunctionalOptions/ИспользоватьКомплектацию/ИспользоватьКомплектацию.mdo
src/cf/src/FunctionalOptions/ИспользоватьЗадачиЗаказов/ИспользоватьЗадачиЗаказов.mdo
src/cf/src/FunctionalOptions/ИспользоватьРозничныеПродажи/ИспользоватьРозничныеПродажи.mdo
src/cf/src/FunctionalOptions/ИспользоватьСерииНоменклатуры/ИспользоватьСерииНоменклатуры.mdo
src/cf/src/FunctionalOptions/ИспользоватьЗаявкиНаПоискТовара/ИспользоватьЗаявкиНаПоискТовара.mdo
src/cf/src/FunctionalOptions/ИспользоватьАльтернативныеОплаты/ИспользоватьАльтернативныеОплаты.mdo
src/cf/src/FunctionalOptions/ИспользоватьПравилаЦенообразования/ИспользоватьПравилаЦенообразования.mdo
src/cf/src/FunctionalOptions/ИспользоватьКоммерческиеПредложения/ИспользоватьКоммерческиеПредложения.mdo
src/cf/src/FunctionalOptions/ИспользоватьХарактеристикиНоменклатуры/ИспользоватьХарактеристикиНоменклатуры.mdo
src/cf/src/Subsystems/Сервис/Subsystems/НастройкиПрограммы/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-02T16:12:55.738+01:00  INFO 40026 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/749 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/749 (0:00:01 / 0:01:22) Analyzing files...   7% [=                       ]  57/749 (0:00:02 / 0:00:24) Analyzing files...  16% [===                     ] 123/749 (0:00:03 / 0:00:15) Analyzing files...  28% [======                  ] 217/749 (0:00:04 / 0:00:09) Analyzing files...  43% [==========              ] 323/749 (0:00:05 / 0:00:06) Analyzing files...  62% [===============         ] 469/749 (0:00:06 / 0:00:03) Analyzing files...  85% [====================    ] 640/749 (0:00:07 / 0:00:01) Analyzing files... 100% [========================] 749/749 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 749/749 (0:00:07 / 0:00:00) 
2026-10-02T16:13:06.633+01:00  INFO 40026 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 14
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.5.json
версия 2.0.16.5: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/menu-restructure.md
 M src/cf/src/Catalogs/СерииНоменклатуры/ObjectModule.bsl
 M src/cf/src/CommonForms/ФормаПервогоЗапуска/Form.form
 M src/cf/src/CommonForms/ФормаПервогоЗапуска/Module.bsl
 M src/cf/src/CommonModules/НачальноеЗаполнениеВызовСервера/Module.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/Constants/ИспользоватьСерииНоменклатуры/ИспользоватьСерииНоменклатуры.mdo
 M src/cf/src/Constants/ИспользоватьХарактеристикиНоменклатуры/ИспользоватьХарактеристикиНоменклатуры.mdo
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Закупки/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Закупки/Module.bsl
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Продажи/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Module.bsl
 M src/cf/src/DataProcessors/НастройкиПрограммы/НастройкиПрограммы.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/FunctionalOptions/Бухгалтерия/Бухгалтерия.mdo
 M src/cf/src/FunctionalOptions/ИспользоватьСерииНоменклатуры/ИспользоватьСерииНоменклатуры.mdo
 M src/cf/src/FunctionalOptions/ИспользоватьХарактеристикиНоменклатуры/ИспользоватьХарактеристикиНоменклатуры.mdo
 M src/cf/src/FunctionalOptions/Производство/Производство.mdo
 M src/cf/src/Subsystems/Сервис/Subsystems/НастройкиПрограммы/CommandInterface.cmi
?? .ai/reports/menu-restructure-1b-final-check.md
?? src/cf/src/Constants/ИспользоватьАльтернативныеОплаты/
?? src/cf/src/Constants/ИспользоватьЗадачиЗаказов/
?? src/cf/src/Constants/ИспользоватьЗаказыПокупателей/
?? src/cf/src/Constants/ИспользоватьЗаявкиНаПоискТовара/
?? src/cf/src/Constants/ИспользоватьИмпорт/
?? src/cf/src/Constants/ИспользоватьКоммерческиеПредложения/
?? src/cf/src/Constants/ИспользоватьКомплектацию/
?? src/cf/src/Constants/ИспользоватьЛиды/
?? src/cf/src/Constants/ИспользоватьЛичныйКабинет/
?? src/cf/src/Constants/ИспользоватьПереработку/
?? src/cf/src/Constants/ИспользоватьПересчеты/
?? src/cf/src/Constants/ИспользоватьПравилаЦенообразования/
?? src/cf/src/Constants/ИспользоватьРегламентированныйУчет/
?? src/cf/src/Constants/ИспользоватьРозничныеПродажи/
?? src/cf/src/Constants/ИспользоватьЯчейки/
?? src/cf/src/DataProcessors/НастройкиПрограммы/Commands/CRM/
?? src/cf/src/DataProcessors/НастройкиПрограммы/Commands/Бухгалтерия/
?? src/cf/src/DataProcessors/НастройкиПрограммы/Commands/Казначейство/
?? src/cf/src/DataProcessors/НастройкиПрограммы/Commands/Склад/
?? src/cf/src/DataProcessors/НастройкиПрограммы/Forms/CRM/
?? src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Бухгалтерия/
?? src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Казначейство/
?? src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Склад/
?? src/cf/src/FunctionalOptions/ИспользоватьАльтернативныеОплаты/
?? src/cf/src/FunctionalOptions/ИспользоватьЗадачиЗаказов/
?? src/cf/src/FunctionalOptions/ИспользоватьЗаказыПокупателей/
?? src/cf/src/FunctionalOptions/ИспользоватьЗаявкиНаПоискТовара/
?? src/cf/src/FunctionalOptions/ИспользоватьИмпорт/
?? src/cf/src/FunctionalOptions/ИспользоватьКоммерческиеПредложения/
?? src/cf/src/FunctionalOptions/ИспользоватьКомплектацию/
?? src/cf/src/FunctionalOptions/ИспользоватьЛиды/
?? src/cf/src/FunctionalOptions/ИспользоватьЛичныйКабинет/
?? src/cf/src/FunctionalOptions/ИспользоватьПереработку/
?? src/cf/src/FunctionalOptions/ИспользоватьПересчеты/
?? src/cf/src/FunctionalOptions/ИспользоватьПравилаЦенообразования/
?? src/cf/src/FunctionalOptions/ИспользоватьРегламентированныйУчет/
?? src/cf/src/FunctionalOptions/ИспользоватьРозничныеПродажи/
?? src/cf/src/FunctionalOptions/ИспользоватьЯчейки/
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
2.0.16.4 → 2.0.16.5

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
