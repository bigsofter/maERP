# Final check — machines-w5
_20261009T000131Z_


## Scope

```
.ai/reports/machines-s4.md
.ai/reports/machines-w5-final-check.md
.ai/reviews/machines-s4-fix/03-code-review.json
.ai/reviews/machines-s4/02-plan-review.json
.ai/reviews/machines-s4/03-code-review.json
.ai/reviews/machines-w5/01-plan-review-claude.md
.ai/reviews/machines-w5/03-code-review-claude.md
.ai/reviews/machines-w5/04-database-claude.md
.ai/reviews/machines-w5/05-verify-claude.md
docs/plans/machines-w5.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
src/cf/src/CommonCommands/СписаниеМатериалов/СписаниеМатериалов.mdo
src/cf/src/CommonCommands/ИнвентаризацияСтанков/ИнвентаризацияСтанков.mdo
src/cf/src/CommonCommands/ОприходованиеМатериалов/ОприходованиеМатериалов.mdo
src/cf/src/CommonCommands/СписаниеМатериалов/CommandModule.bsl
src/cf/src/CommonCommands/ИнвентаризацияСтанков/CommandModule.bsl
src/cf/src/CommonCommands/ОприходованиеМатериалов/CommandModule.bsl
src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ПересчётТоваров/ПересчётТоваров.mdo
src/cf/src/Documents/ОбслуживаниеСтанка/ОбслуживаниеСтанка.mdo
src/cf/src/Documents/ТребованиеНакладная/ТребованиеНакладная.mdo
src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
src/cf/src/Documents/ПересчётТоваров/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПересчётТоваров/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ОбслуживаниеСтанка/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ТребованиеНакладная/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПересчётТоваров/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПересчётТоваров/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПересчётТоваров/ObjectModule.bsl
src/cf/src/Documents/ОбслуживаниеСтанка/ObjectModule.bsl
src/cf/src/Documents/ТребованиеНакладная/ObjectModule.bsl
src/cf/src/Documents/ОприходованиеТоваров/ObjectModule.bsl
src/cf/src/Enums/ВидыСкладскихОпераций/ВидыСкладскихОпераций.mdo
src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
src/cf/src/Reports/ЭффективностьСтанков/ЭффективностьСтанков.mdo
src/cf/src/Reports/ПростоиСтанков/ManagerModule.bsl
src/cf/src/Reports/МатериалыНаСтанках/ManagerModule.bsl
src/cf/src/Reports/ЭффективностьСтанков/ManagerModule.bsl
src/cf/src/Reports/ЭффективностьСтанков/ObjectModule.bsl
src/cf/src/Reports/ПростоиСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ДеньгиПоСтанкам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВыработкаСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/МатериалыНаСтанках/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ЭффективностьСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Subsystems/Производство/Производство.mdo
src/cf/src/Subsystems/Производство/CommandInterface.cmi
src/cf/src/Subsystems/Производство/Subsystems/Станки/Станки.mdo
src/cf/src/Subsystems/Производство/Subsystems/Станки/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-09T01:01:40.304+01:00  INFO 23944 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/795 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/795 (0:00:01 / 0:01:27) Analyzing files...  10% [==                      ]  82/795 (0:00:02 / 0:00:17) Analyzing files...  21% [=====                   ] 172/795 (0:00:03 / 0:00:10) Analyzing files...  40% [=========               ] 319/795 (0:00:04 / 0:00:05) Analyzing files...  60% [==============          ] 477/795 (0:00:05 / 0:00:03) Analyzing files...  76% [==================      ] 605/795 (0:00:06 / 0:00:01) Analyzing files...  92% [======================  ] 732/795 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 795/795 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 795/795 (0:00:07 / 0:00:00) 
2026-10-09T01:01:50.924+01:00  INFO 23944 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.40.json
версия 2.0.16.40: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
A  .ai/reviews/machines-s4-fix/03-code-review.json
A  .ai/reviews/machines-s4/02-plan-review.json
A  .ai/reviews/machines-s4/03-code-review.json
A  .ai/reviews/machines-w5/01-plan-review-claude.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
A  docs/plans/machines-w5.md
M  src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
M  src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
M  src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
A  src/cf/src/CommonCommands/ИнвентаризацияСтанков/CommandModule.bsl
A  src/cf/src/CommonCommands/ИнвентаризацияСтанков/ИнвентаризацияСтанков.mdo
A  src/cf/src/CommonCommands/ОприходованиеМатериалов/CommandModule.bsl
A  src/cf/src/CommonCommands/ОприходованиеМатериалов/ОприходованиеМатериалов.mdo
A  src/cf/src/CommonCommands/СписаниеМатериалов/CommandModule.bsl
A  src/cf/src/CommonCommands/СписаниеМатериалов/СписаниеМатериалов.mdo
M  src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
M  src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
M  src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
M  src/cf/src/Configuration/Configuration.mdo
M  src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
M  src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
M  src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
M  src/cf/src/Documents/ОбслуживаниеСтанка/Forms/ФормаДокумента/Form.form
M  src/cf/src/Documents/ОбслуживаниеСтанка/ObjectModule.bsl
M  src/cf/src/Documents/ОбслуживаниеСтанка/ОбслуживаниеСтанка.mdo
M  src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаДокумента/Form.form
M  src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаДокумента/Module.bsl
M  src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Form.form
M  src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Module.bsl
M  src/cf/src/Documents/ОприходованиеТоваров/ObjectModule.bsl
M  src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
M  src/cf/src/Documents/ПересчётТоваров/Forms/ФормаДокумента/Form.form
M  src/cf/src/Documents/ПересчётТоваров/Forms/ФормаДокумента/Module.bsl
M  src/cf/src/Documents/ПересчётТоваров/Forms/ФормаСписка/Form.form
M  src/cf/src/Documents/ПересчётТоваров/Forms/ФормаСписка/Module.bsl
M  src/cf/src/Documents/ПересчётТоваров/ObjectModule.bsl
M  src/cf/src/Documents/ПересчётТоваров/ПересчётТоваров.mdo
M  src/cf/src/Documents/СписаниеТоваров/Forms/ФормаДокумента/Form.form
M  src/cf/src/Documents/СписаниеТоваров/Forms/ФормаДокумента/Module.bsl
M  src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Form.form
M  src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Module.bsl
M  src/cf/src/Documents/СписаниеТоваров/ObjectModule.bsl
M  src/cf/src/Documents/СписаниеТоваров/СписаниеТоваров.mdo
M  src/cf/src/Documents/ТребованиеНакладная/Forms/ФормаДокумента/Form.form
M  src/cf/src/Documents/ТребованиеНакладная/ObjectModule.bsl
M  src/cf/src/Documents/ТребованиеНакладная/ТребованиеНакладная.mdo
A  src/cf/src/Enums/ВидыСкладскихОпераций/ВидыСкладскихОпераций.mdo
M  src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
M  src/cf/src/Reports/ВыработкаСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
M  src/cf/src/Reports/ДеньгиПоСтанкам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
M  src/cf/src/Reports/ЗагрузкаСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
M  src/cf/src/Reports/МатериалыНаСтанках/ManagerModule.bsl
M  src/cf/src/Reports/МатериалыНаСтанках/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
M  src/cf/src/Reports/ПростоиСтанков/ManagerModule.bsl
M  src/cf/src/Reports/ПростоиСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
A  src/cf/src/Reports/ЭффективностьСтанков/ManagerModule.bsl
A  src/cf/src/Reports/ЭффективностьСтанков/ObjectModule.bsl
A  src/cf/src/Reports/ЭффективностьСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
A  src/cf/src/Reports/ЭффективностьСтанков/ЭффективностьСтанков.mdo
M  src/cf/src/Roles/Кладовщик/Rights.rights
M  src/cf/src/Roles/ОператорПроизводства/Rights.rights
M  src/cf/src/Subsystems/Производство/CommandInterface.cmi
A  src/cf/src/Subsystems/Производство/Subsystems/Станки/CommandInterface.cmi
A  src/cf/src/Subsystems/Производство/Subsystems/Станки/Станки.mdo
M  src/cf/src/Subsystems/Производство/Производство.mdo
?? .ai/reports/machines-s4.md
?? .ai/reports/machines-w5-final-check.md
?? .ai/reviews/machines-w5/03-code-review-claude.md
?? .ai/reviews/machines-w5/04-database-claude.md
?? .ai/reviews/machines-w5/05-verify-claude.md
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
+	// BSLLS:MagicNumber-off - заказ 10 продукции x 2 сырья по 6 кг; станок 120 кг/ч, 15 мин на смену заказа, 8-20.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - заказ 10 продукции x 2 сырья по 6 кг; станки 120 кг/ч, 15 мин на смену заказа, 8-20.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - заказ 10 продукции x 2 сырья по 6 кг; станки 120 кг/ч, 15 мин на смену заказа, 8-20.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - заказ 10 продукции x 2 сырья; закупки сырья 30.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.35 → 2.0.16.40

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
