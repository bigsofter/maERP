# Final check — machines-s2
_20261008T115802Z_


## Scope

```
.ai/reports/machines-s2-final-check.md
.ai/reviews/machines-s2/04-code-review-claude.md
.ai/reviews/machines-s2/05-database-review-claude.md
.ai/reviews/machines-s2/06-security-review-claude.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/МатериалыНаСтанках/МатериалыНаСтанках.mdo
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыВНаличии/RecordSetModule.bsl
src/cf/src/Catalogs/ПроизводственноеОборудование/ObjectModule.bsl
src/cf/src/CommonModules/ТребованияНакладные/ТребованияНакладные.mdo
src/cf/src/CommonModules/Производство/Module.bsl
src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Constants/ИспользоватьПроизводство/ValueManagerModule.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
src/cf/src/Documents/ТребованиеНакладная/ТребованиеНакладная.mdo
src/cf/src/Documents/ТребованиеНакладная/Forms/ФормаСписка/Attributes/Список/ExtInfo/ListSettings.dcss
src/cf/src/Documents/ВыпускПродукции/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ТребованиеНакладная/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ТребованиеНакладная/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ТребованиеНакладная/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ТребованиеНакладная/ManagerModule.bsl
src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
src/cf/src/Documents/ТребованиеНакладная/ObjectModule.bsl
src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
src/cf/src/Enums/СтатусыТребованийНакладных/СтатусыТребованийНакладных.mdo
src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
src/cf/src/InformationRegisters/ЗагрузкаСтанков/ЗагрузкаСтанков.mdo
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Subsystems/Производство/Производство.mdo
src/cf/src/Subsystems/Производство/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-08T12:58:11.353+01:00  INFO 12100 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/782 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/782 (0:00:01 / 0:01:26) Analyzing files...  15% [===                     ] 124/782 (0:00:02 / 0:00:10) Analyzing files...  28% [======                  ] 222/782 (0:00:03 / 0:00:07) Analyzing files...  46% [===========             ] 365/782 (0:00:04 / 0:00:04) Analyzing files...  68% [================        ] 534/782 (0:00:05 / 0:00:02) Analyzing files...  82% [===================     ] 642/782 (0:00:06 / 0:00:01) Analyzing files...  96% [======================= ] 755/782 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 782/782 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 782/782 (0:00:07 / 0:00:00) 
2026-10-08T12:58:22.744+01:00  INFO 12100 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.33.json
версия 2.0.16.33: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/RecordSetModule.bsl
 M src/cf/src/Catalogs/ПроизводственноеОборудование/ObjectModule.bsl
 M src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
 M src/cf/src/CommonModules/Производство/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
 M src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
 M src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
 M src/cf/src/InformationRegisters/ЗагрузкаСтанков/ЗагрузкаСтанков.mdo
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Subsystems/Производство/CommandInterface.cmi
 M src/cf/src/Subsystems/Производство/Производство.mdo
?? .ai/reports/machines-s2-final-check.md
?? .ai/reviews/machines-s2/04-code-review-claude.md
?? .ai/reviews/machines-s2/05-database-review-claude.md
?? .ai/reviews/machines-s2/06-security-review-claude.md
?? src/cf/src/AccumulationRegisters/МатериалыНаСтанках/
?? src/cf/src/CommonModules/ТребованияНакладные/
?? src/cf/src/Constants/ИспользоватьПроизводство/ValueManagerModule.bsl
?? src/cf/src/Documents/ТребованиеНакладная/
?? src/cf/src/Enums/СтатусыТребованийНакладных/
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
+	// BSLLS:SetPrivilegedMode-off - запрет проверяется у любого, кто пишет константу (мастер, настройки), по всем требованиям.
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:MagicNumber-off - сырьё по 6 кг; заказ 10 продукции x 2 сырья; закупки 15 по 10 и 15 по 12.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - заказ 20 продукции x 2 сырья; партии P1 15 по 10 и P2 15 по 12.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
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
2.0.16.32 → 2.0.16.33

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
