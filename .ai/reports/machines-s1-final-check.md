# Final check — machines-s1
_20261008T070859Z_


## Scope

```
.ai/reports/machines-s1-final-check.md
.ai/reviews/machines-s1/02-plan-review-claude.md
.ai/reviews/machines-s1/03-code-review-claude.md
.ai/reviews/machines-s1/04-database-review-claude.md
.ai/reviews/machines/02-plan-review-claude.md
docs/plans/machines.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/Catalogs/ПроизводственноеОборудование/ПроизводственноеОборудование.mdo
src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаВыбора/Module.bsl
src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаЭлемента/Module.bsl
src/cf/src/Catalogs/ПроизводственноеОборудование/ManagerModule.bsl
src/cf/src/Catalogs/ПроизводственноеОборудование/ObjectModule.bsl
src/cf/src/CommonModules/ЗагрузкаСтанков/ЗагрузкаСтанков.mdo
src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Constants/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
src/cf/src/Constants/СписыватьМатериалыНаСтанокПриРазмещении/СписыватьМатериалыНаСтанокПриРазмещении.mdo
src/cf/src/Constants/ИспользоватьУчетСтанков/ValueManagerModule.bsl
src/cf/src/DataProcessors/ЗагрузкаСтанков/ЗагрузкаСтанков.mdo
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Form.form
src/cf/src/DataProcessors/ЗагрузкаСтанков/Forms/ПробаПланировщика/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Module.bsl
src/cf/src/DataProcessors/ЗагрузкаСтанков/Forms/ПробаПланировщика/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ОбслуживаниеСтанка/ОбслуживаниеСтанка.mdo
src/cf/src/Documents/ОбслуживаниеСтанка/Forms/ФормаСписка/Attributes/Список/ExtInfo/ListSettings.dcss
src/cf/src/Documents/ОбслуживаниеСтанка/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ОбслуживаниеСтанка/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ОбслуживаниеСтанка/ObjectModule.bsl
src/cf/src/Enums/ВидыЗагрузкиСтанков/ВидыЗагрузкиСтанков.mdo
src/cf/src/Enums/ВидыОбслуживанияСтанков/ВидыОбслуживанияСтанков.mdo
src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
src/cf/src/InformationRegisters/ЗагрузкаСтанков/ЗагрузкаСтанков.mdo
src/cf/src/Reports/ПростоиСтанков/ПростоиСтанков.mdo
src/cf/src/Reports/ПростоиСтанков/ManagerModule.bsl
src/cf/src/Reports/ПростоиСтанков/ObjectModule.bsl
src/cf/src/Reports/ПростоиСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Subsystems/Производство/Производство.mdo
src/cf/src/Subsystems/Производство/CommandInterface.cmi
src/cf/src/Subsystems/Производство/Subsystems/Нормативы/Нормативы.mdo
src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-08T08:09:06.384+01:00  INFO 67209 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/777 (0:00:00 / ?) Analyzing files...   6% [=                       ]  52/777 (0:00:01 / 0:00:14) Analyzing files...  23% [=====                   ] 179/777 (0:00:02 / 0:00:06) Analyzing files...  44% [==========              ] 347/777 (0:00:03 / 0:00:03) Analyzing files...  64% [===============         ] 503/777 (0:00:04 / 0:00:02) Analyzing files...  88% [=====================   ] 690/777 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 777/777 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 777/777 (0:00:05 / 0:00:00) 
2026-10-08T08:09:14.677+01:00  INFO 67209 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 13
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.32.json
версия 2.0.16.32: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/machines.md
 M src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/ПроизводственноеОборудование/ПроизводственноеОборудование.mdo
 M src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Subsystems/Производство/CommandInterface.cmi
 M src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
 M src/cf/src/Subsystems/Производство/Subsystems/Нормативы/Нормативы.mdo
 M src/cf/src/Subsystems/Производство/Производство.mdo
?? .ai/reports/machines-s1-final-check.md
?? .ai/reviews/machines-s1/
?? .ai/reviews/machines/02-plan-review-claude.md
?? src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаВыбора/Module.bsl
?? src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаСписка/Module.bsl
?? src/cf/src/Catalogs/ПроизводственноеОборудование/Forms/ФормаЭлемента/Module.bsl
?? src/cf/src/Catalogs/ПроизводственноеОборудование/ManagerModule.bsl
?? src/cf/src/Catalogs/ПроизводственноеОборудование/ObjectModule.bsl
?? src/cf/src/CommonModules/ЗагрузкаСтанков/
?? src/cf/src/Constants/ИспользоватьУчетСтанков/
?? src/cf/src/Constants/СписыватьМатериалыНаСтанокПриРазмещении/
?? src/cf/src/DataProcessors/ЗагрузкаСтанков/
?? src/cf/src/Documents/ОбслуживаниеСтанка/
?? src/cf/src/Enums/ВидыЗагрузкиСтанков/
?? src/cf/src/Enums/ВидыОбслуживанияСтанков/
?? src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/
?? src/cf/src/InformationRegisters/ЗагрузкаСтанков/
?? src/cf/src/Reports/ПростоиСтанков/
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
+	// BSLLS:MagicNumber-off - часы смен и интервалов сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.31 → 2.0.16.32

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
