# Final check — multicurrency-payments
_20261006T161234Z_


## Scope

```
.ai/reports/multicurrency-payments-final-check.md
.ai/reviews/multicurrency-payments/01-plan-review-claude.md
.ai/reviews/multicurrency-payments/02-code-review-claude.md
.ai/reviews/multicurrency-payments/03-database-review-claude.md
.ai/reviews/multicurrency-payments/04-security-review-claude.md
.ai/reviews/multicurrency-payments/05-verify-claude.md
.ai/reviews/multicurrency-payments/06-verify-claude.md
docs/plans/multicurrency-payments.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ДенежныеСредстваОрганизаций/ДенежныеСредстваОрганизаций.mdo
src/cf/src/AccumulationRegisters/Убытки/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ДвиженияПоКассе/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ДенежныеСредстваОрганизаций/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателямиНалоговый/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоcтавщикамиНалоговый/ManagerModule.bsl
src/cf/src/Catalogs/СтатьиФинансовогоРезультата/СтатьиФинансовогоРезультата.mdo
src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/СтатьиДвиженияДенежныхСредств.mdo
src/cf/src/CommonModules/РаботаСВалютами/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/РаботаСВалютамиКлиентСервер/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПриходныйКассовыйОрдер/ManagerModule.bsl
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ManagerModule.bsl
src/cf/src/Documents/КассоваяСмена/ObjectModule.bsl
src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
src/cf/src/Reports/ФинансовыйРезультат/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-06T17:12:42.945+01:00  INFO 16571 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/763 (0:00:00 / ?) Analyzing files...   1% [                        ]  11/763 (0:00:01 / 0:01:08) Analyzing files...  12% [==                      ]  95/763 (0:00:02 / 0:00:14) Analyzing files...  27% [======                  ] 210/763 (0:00:03 / 0:00:07) Analyzing files...  40% [=========               ] 311/763 (0:00:04 / 0:00:05) Analyzing files...  55% [=============           ] 424/763 (0:00:05 / 0:00:04) Analyzing files...  81% [===================     ] 621/763 (0:00:06 / 0:00:01) Analyzing files...  99% [======================= ] 759/763 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 763/763 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 763/763 (0:00:07 / 0:00:00) 
2026-10-06T17:12:53.536+01:00  INFO 16571 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 28
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.23.json
версия 2.0.16.23: ru=7, fr=7, en=7, es=7
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоcтавщикамиНалоговый/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателямиНалоговый/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ДвиженияПоКассе/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ДенежныеСредстваОрганизаций/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ДенежныеСредстваОрганизаций/ДенежныеСредстваОрганизаций.mdo
 M src/cf/src/AccumulationRegisters/Убытки/ManagerModule.bsl
 M src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/СтатьиДвиженияДенежныхСредств.mdo
 M src/cf/src/Catalogs/СтатьиФинансовогоРезультата/СтатьиФинансовогоРезультата.mdo
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/РаботаСВалютами/Module.bsl
 M src/cf/src/CommonModules/РаботаСВалютамиКлиентСервер/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиВызовСервера/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиКлиентСервер/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ManagerModule.bsl
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/ManagerModule.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/РасходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ManagerModule.bsl
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
 M src/cf/src/Reports/ФинансовыйРезультат/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
?? .ai/reports/multicurrency-payments-final-check.md
?? .ai/reviews/multicurrency-payments/
?? docs/plans/multicurrency-payments.md
?? src/cf/src/Documents/КассоваяСмена/ObjectModule.bsl
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
+	// BSLLS:YoLetterUsage-off - имя реквизита метаданных
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off - имена существующих функций
+	// BSLLS:YoLetterUsage-on
+			// BSLLS:YoLetterUsage-off - имя колонки по измерению регистра
+			// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+		// BSLLS:YoLetterUsage-off - имя существующей функции
+		// BSLLS:YoLetterUsage-on
+		// BSLLS:YoLetterUsage-off - имя существующей функции
+		// BSLLS:YoLetterUsage-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.22 → 2.0.16.23

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
