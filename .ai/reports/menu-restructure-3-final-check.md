# Final check — menu-restructure-3
_20261003T092857Z_


## Scope

```
.ai/reports/menu-restructure-3-final-check.md
.ai/reviews/menu-restructure/05-stage3-plan-review-claude.md
.ai/reviews/menu-restructure/06-stage3-code-review-claude.md
docs/plans/menu-restructure-stage3.md
docs/plans/menu-restructure.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/menucheck-baseline.txt
scripts/titlecheck-baseline.txt
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
src/cf/src/Catalogs/ДоговорыСКонтрагентами/ДоговорыСКонтрагентами.mdo
src/cf/src/Catalogs/Номенклатура/Commands/ТоварыДляПродажи/CommandModule.bsl
src/cf/src/Catalogs/ДоговорыСКонтрагентами/Commands/ДоговорыСПокупателями/CommandModule.bsl
src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Module.bsl
src/cf/src/CommonForms/ИнтерфейсКлиент/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Продажи/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Продажи/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/FunctionalOptions/ИспользоватьЗадачиЗаказов/ИспользоватьЗадачиЗаказов.mdo
src/cf/src/FunctionalOptions/ИспользоватьЗаявкиНаПоискТовара/ИспользоватьЗаявкиНаПоискТовара.mdo
src/cf/src/FunctionalOptions/ИспользоватьАльтернативныеОплаты/ИспользоватьАльтернативныеОплаты.mdo
src/cf/src/FunctionalOptions/ИспользоватьКоммерческиеПредложения/ИспользоватьКоммерческиеПредложения.mdo
src/cf/src/InformationRegisters/КураторыДоговоров/КураторыДоговоров.mdo
src/cf/src/Reports/СтатистикаДневныхПродаж/СтатистикаДневныхПродаж.mdo
src/cf/src/Reports/ПросроченныеДолгиПокупателей/ПросроченныеДолгиПокупателей.mdo
src/cf/src/Reports/ПросроченныеДолгиПоставщиков/ObjectModule.bsl
src/cf/src/Reports/ПросроченныеДолгиПокупателей/ObjectModule.bsl
src/cf/src/Reports/ПросроченныеДолгиПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ПросроченныеДолгиПокупателей/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ABCАнализПродаж/ABCАнализПродаж.mdo
src/cf/src/Reports/ABCАнализПродаж/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Оператор/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
src/cf/src/Subsystems/Продажи/Продажи.mdo
src/cf/src/Subsystems/Бухгалтерия/Бухгалтерия.mdo
src/cf/src/Subsystems/Казначейство/Казначейство.mdo
src/cf/src/Subsystems/Продажи/CommandInterface.cmi
src/cf/src/Subsystems/Бухгалтерия/CommandInterface.cmi
src/cf/src/Subsystems/Казначейство/CommandInterface.cmi
src/cf/src/Subsystems/Продажи/Subsystems/Опт/Опт.mdo
src/cf/src/Subsystems/Продажи/Subsystems/Цены/Цены.mdo
src/cf/src/Subsystems/Продажи/Subsystems/Клиенты/Клиенты.mdo
src/cf/src/Subsystems/Продажи/Subsystems/Справочники/Справочники.mdo
src/cf/src/Subsystems/Продажи/Subsystems/РозничныеПродажи/РозничныеПродажи.mdo
src/cf/src/Subsystems/Продажи/Subsystems/Опт/CommandInterface.cmi
src/cf/src/Subsystems/Продажи/Subsystems/Цены/CommandInterface.cmi
src/cf/src/Subsystems/Продажи/Subsystems/Клиенты/CommandInterface.cmi
src/cf/src/Subsystems/Склад/Subsystems/Справочники/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/Subsystems/Справочники/CommandInterface.cmi
src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/Subsystems/ПоставщикиИЦены/CommandInterface.cmi
src/cf/src/Subsystems/Казначейство/Subsystems/Справочники/CommandInterface.cmi
src/cf/src/Subsystems/Продажи/Subsystems/РаботаСПокупателями/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-03T10:29:07.720+01:00  INFO 73329 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/753 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/753 (0:00:01 / 0:01:22) Analyzing files...  11% [==                      ]  84/753 (0:00:03 / 0:00:23) Analyzing files...  23% [=====                   ] 180/753 (0:00:04 / 0:00:12) Analyzing files...  44% [==========              ] 332/753 (0:00:05 / 0:00:06) Analyzing files...  62% [===============         ] 474/753 (0:00:06 / 0:00:03) Analyzing files...  79% [==================      ] 595/753 (0:00:07 / 0:00:01) Analyzing files...  92% [======================  ] 695/753 (0:00:08 / 0:00:00) Analyzing files...  96% [======================= ] 726/753 (0:00:09 / 0:00:00) Analyzing files...  99% [======================= ] 748/753 (0:00:10 / 0:00:00) Analyzing files... 100% [========================] 753/753 (0:00:10 / 0:00:00) Analyzing files... 100% [========================] 753/753 (0:00:10 / 0:00:00) 
2026-10-03T10:29:22.665+01:00  INFO 73329 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 9
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.7.json
версия 2.0.16.7: ru=9, fr=9, en=9, es=9
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/menu-restructure-stage3.md
 M docs/plans/menu-restructure.md
 M scripts/menucheck-baseline.txt
 M scripts/titlecheck-baseline.txt
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
 M src/cf/src/Catalogs/ДоговорыСКонтрагентами/ДоговорыСКонтрагентами.mdo
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
 M src/cf/src/CommonForms/ИнтерфейсКлиент/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Продажи/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Продажи/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/FunctionalOptions/ИспользоватьАльтернативныеОплаты/ИспользоватьАльтернативныеОплаты.mdo
 M src/cf/src/FunctionalOptions/ИспользоватьЗадачиЗаказов/ИспользоватьЗадачиЗаказов.mdo
 M src/cf/src/FunctionalOptions/ИспользоватьЗаявкиНаПоискТовара/ИспользоватьЗаявкиНаПоискТовара.mdo
 M src/cf/src/FunctionalOptions/ИспользоватьКоммерческиеПредложения/ИспользоватьКоммерческиеПредложения.mdo
 M src/cf/src/FunctionalOptions/ИспользоватьЛичныйКабинет/ИспользоватьЛичныйКабинет.mdo
 M src/cf/src/InformationRegisters/КураторыДоговоров/КураторыДоговоров.mdo
 M src/cf/src/Reports/ABCАнализПродаж/ABCАнализПродаж.mdo
 M src/cf/src/Reports/ABCАнализПродаж/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПросроченныеДолгиПокупателей/ObjectModule.bsl
 M src/cf/src/Reports/ПросроченныеДолгиПокупателей/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПросроченныеДолгиПокупателей/ПросроченныеДолгиПокупателей.mdo
 M src/cf/src/Reports/ПросроченныеДолгиПоставщиков/ObjectModule.bsl
 M src/cf/src/Reports/ПросроченныеДолгиПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/СтатистикаДневныхПродаж/СтатистикаДневныхПродаж.mdo
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Subsystems/Бухгалтерия/CommandInterface.cmi
 M src/cf/src/Subsystems/Бухгалтерия/Бухгалтерия.mdo
 M src/cf/src/Subsystems/Закупки/Subsystems/ПоставщикиИЦены/CommandInterface.cmi
 M src/cf/src/Subsystems/Закупки/Subsystems/Справочники/CommandInterface.cmi
 M src/cf/src/Subsystems/Казначейство/CommandInterface.cmi
 M src/cf/src/Subsystems/Казначейство/Subsystems/Справочники/CommandInterface.cmi
 M src/cf/src/Subsystems/Казначейство/Казначейство.mdo
 M src/cf/src/Subsystems/Продажи/CommandInterface.cmi
RM src/cf/src/Subsystems/Продажи/Subsystems/РаботаСПокупателями/CommandInterface.cmi -> src/cf/src/Subsystems/Продажи/Subsystems/Опт/CommandInterface.cmi
RM src/cf/src/Subsystems/Продажи/Subsystems/РаботаСПокупателями/РаботаСПокупателями.mdo -> src/cf/src/Subsystems/Продажи/Subsystems/Опт/Опт.mdo
 M src/cf/src/Subsystems/Продажи/Subsystems/РозничныеПродажи/CommandInterface.cmi
 M src/cf/src/Subsystems/Продажи/Subsystems/РозничныеПродажи/РозничныеПродажи.mdo
 M src/cf/src/Subsystems/Продажи/Subsystems/Справочники/CommandInterface.cmi
 M src/cf/src/Subsystems/Продажи/Subsystems/Справочники/Справочники.mdo
RM src/cf/src/Subsystems/Продажи/Subsystems/Ценообразование/CommandInterface.cmi -> src/cf/src/Subsystems/Продажи/Subsystems/Цены/CommandInterface.cmi
RM src/cf/src/Subsystems/Продажи/Subsystems/Ценообразование/Ценообразование.mdo -> src/cf/src/Subsystems/Продажи/Subsystems/Цены/Цены.mdo
 M src/cf/src/Subsystems/Продажи/Продажи.mdo
 M src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
 M src/cf/src/Subsystems/Склад/Subsystems/Справочники/CommandInterface.cmi
?? .ai/reports/menu-restructure-3-final-check.md
?? .ai/reviews/menu-restructure/05-stage3-plan-review-claude.md
?? .ai/reviews/menu-restructure/06-stage3-code-review-claude.md
?? src/cf/src/Catalogs/ДоговорыСКонтрагентами/Commands/ДоговорыСПокупателями/
?? src/cf/src/Catalogs/Номенклатура/Commands/ТоварыДляПродажи/
?? src/cf/src/Subsystems/Продажи/Subsystems/Клиенты/
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
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.6 → 2.0.16.7

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
