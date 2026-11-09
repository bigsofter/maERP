# Final check — menu-restructure-2
_20261002T234102Z_


## Scope

```
.ai/reports/menu-restructure-2-final-check.md
.ai/reports/menu-restructure-2.md
.ai/reviews/menu-restructure/03-stage2-plan-review-claude.md
.ai/reviews/menu-restructure/04-stage2-code-review-claude.md
docs/plans/menu-restructure-stage2.md
docs/plans/menu-restructure.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/menucheck-baseline.txt
scripts/titlecheck-baseline.txt
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ManagerModule.bsl
src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
src/cf/src/Catalogs/ДоговорыСКонтрагентами/ДоговорыСКонтрагентами.mdo
src/cf/src/Catalogs/Номенклатура/Commands/ЗакупаемыеТовары/CommandModule.bsl
src/cf/src/Catalogs/ДоговорыСКонтрагентами/Commands/ДоговорыСПоставщиками/CommandModule.bsl
src/cf/src/Catalogs/ДоговорыСКонтрагентами/Commands/ДоговорыСКонтрагентами/CommandModule.bsl
src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/ДоговорыСКонтрагентами/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Module.bsl
src/cf/src/Catalogs/ДоговорыСКонтрагентами/Forms/ФормаСписка/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/ФормированиеЗаказовПоставщику.mdo
src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/FunctionalOptions/Производство/Производство.mdo
src/cf/src/FunctionalOptions/ИспользоватьИмпорт/ИспользоватьИмпорт.mdo
src/cf/src/InformationRegisters/МинимальныйОстатокПоСкладам/МинимальныйОстатокПоСкладам.mdo
src/cf/src/Reports/ПросроченныеДолгиПоставщиков/ПросроченныеДолгиПоставщиков.mdo
src/cf/src/Reports/РеестрПоступленийТоваровУслуг/РеестрПоступленийТоваровУслуг.mdo
src/cf/src/Reports/ЕженедельноеПланированиеЗадолженностиПоставщиков/ЕженедельноеПланированиеЗадолженностиПоставщиков.mdo
src/cf/src/Reports/ПросроченныеДолгиПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Логист/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Subsystems/Закупки/Закупки.mdo
src/cf/src/Subsystems/Казначейство/Казначейство.mdo
src/cf/src/Subsystems/Закупки/CommandInterface.cmi
src/cf/src/Subsystems/Казначейство/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/Subsystems/Импорт/Импорт.mdo
src/cf/src/Subsystems/Закупки/Subsystems/Справочники/Справочники.mdo
src/cf/src/Subsystems/Закупки/Subsystems/Планирование/Планирование.mdo
src/cf/src/Subsystems/Закупки/Subsystems/ПоставщикиИЦены/ПоставщикиИЦены.mdo
src/cf/src/Subsystems/Закупки/Subsystems/РаботаСПоставщиками/РаботаСПоставщиками.mdo
src/cf/src/Subsystems/Закупки/Subsystems/Импорт/CommandInterface.cmi
src/cf/src/Subsystems/Склад/Subsystems/Справочники/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/Subsystems/Справочники/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/Subsystems/Планирование/CommandInterface.cmi
src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/Subsystems/ПоставщикиИЦены/CommandInterface.cmi
src/cf/src/Subsystems/Казначейство/Subsystems/Справочники/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/Subsystems/РаботаСПоставщиками/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-03T00:41:12.761+01:00  INFO 54793 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/751 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/751 (0:00:01 / 0:01:23) Analyzing files...   6% [=                       ]  47/751 (0:00:02 / 0:00:30) Analyzing files...  13% [===                     ] 105/751 (0:00:03 / 0:00:18) Analyzing files...  36% [========                ] 271/751 (0:00:04 / 0:00:07) Analyzing files...  46% [===========             ] 351/751 (0:00:05 / 0:00:05) Analyzing files...  61% [==============          ] 459/751 (0:00:06 / 0:00:03) Analyzing files...  89% [=====================   ] 673/751 (0:00:07 / 0:00:00) Analyzing files...  99% [======================= ] 749/751 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 751/751 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 751/751 (0:00:08 / 0:00:00) 
2026-10-03T00:41:24.323+01:00  INFO 54793 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 8
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
Языков: 4, пунктов изменений: 36
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.6.json
версия 2.0.16.6: ru=9, fr=9, en=9, es=9
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
 M scripts/menucheck-baseline.txt
 M scripts/titlecheck-baseline.txt
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ManagerModule.bsl
 M src/cf/src/Catalogs/ДоговорыСКонтрагентами/Commands/ДоговорыСКонтрагентами/CommandModule.bsl
 M src/cf/src/Catalogs/ДоговорыСКонтрагентами/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ДоговорыСКонтрагентами/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Catalogs/ДоговорыСКонтрагентами/ДоговорыСКонтрагентами.mdo
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/ФормированиеЗаказовПоставщику.mdo
 M src/cf/src/FunctionalOptions/ИспользоватьИмпорт/ИспользоватьИмпорт.mdo
 M src/cf/src/FunctionalOptions/Производство/Производство.mdo
 M src/cf/src/InformationRegisters/МинимальныйОстатокПоСкладам/МинимальныйОстатокПоСкладам.mdo
 M src/cf/src/Reports/ЕженедельноеПланированиеЗадолженностиПоставщиков/ЕженедельноеПланированиеЗадолженностиПоставщиков.mdo
 M src/cf/src/Reports/ПросроченныеДолгиПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПросроченныеДолгиПоставщиков/ПросроченныеДолгиПоставщиков.mdo
 M src/cf/src/Reports/РеестрПоступленийТоваровУслуг/РеестрПоступленийТоваровУслуг.mdo
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Subsystems/Закупки/CommandInterface.cmi
RM src/cf/src/Subsystems/Закупки/Subsystems/ЦеныПоставщиков/CommandInterface.cmi -> src/cf/src/Subsystems/Закупки/Subsystems/Импорт/CommandInterface.cmi
RM src/cf/src/Subsystems/Закупки/Subsystems/ЦеныПоставщиков/ЦеныПоставщиков.mdo -> src/cf/src/Subsystems/Закупки/Subsystems/Импорт/Импорт.mdo
 M src/cf/src/Subsystems/Закупки/Subsystems/Планирование/CommandInterface.cmi
 M src/cf/src/Subsystems/Закупки/Subsystems/Планирование/Планирование.mdo
RM src/cf/src/Subsystems/Закупки/Subsystems/РаботаСПоставщиками/CommandInterface.cmi -> src/cf/src/Subsystems/Закупки/Subsystems/ПоставщикиИЦены/CommandInterface.cmi
RM src/cf/src/Subsystems/Закупки/Subsystems/РаботаСПоставщиками/РаботаСПоставщиками.mdo -> src/cf/src/Subsystems/Закупки/Subsystems/ПоставщикиИЦены/ПоставщикиИЦены.mdo
 M src/cf/src/Subsystems/Закупки/Subsystems/Справочники/CommandInterface.cmi
 M src/cf/src/Subsystems/Закупки/Subsystems/Справочники/Справочники.mdo
 M src/cf/src/Subsystems/Закупки/Закупки.mdo
 M src/cf/src/Subsystems/Казначейство/CommandInterface.cmi
 M src/cf/src/Subsystems/Казначейство/Subsystems/Справочники/CommandInterface.cmi
 M src/cf/src/Subsystems/Казначейство/Казначейство.mdo
 M src/cf/src/Subsystems/Продажи/Subsystems/Справочники/CommandInterface.cmi
 M src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
 M src/cf/src/Subsystems/Склад/Subsystems/Справочники/CommandInterface.cmi
?? .ai/reports/menu-restructure-2-final-check.md
?? .ai/reports/menu-restructure-2.md
?? .ai/reviews/menu-restructure/03-stage2-plan-review-claude.md
?? .ai/reviews/menu-restructure/04-stage2-code-review-claude.md
?? docs/plans/menu-restructure-stage2.md
?? src/cf/src/Catalogs/ДоговорыСКонтрагентами/Commands/ДоговорыСПоставщиками/
?? src/cf/src/Catalogs/Номенклатура/Commands/ЗакупаемыеТовары/
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
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.5 → 2.0.16.6

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
