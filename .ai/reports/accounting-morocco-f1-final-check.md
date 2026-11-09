# Final check — accounting-morocco-f1
_20261018T200637Z_


## Scope

```
.ai/reports/accounting-morocco-f1-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reviews/accounting-morocco-f1/03-code-review.json
.ai/reviews/accounting-morocco-f1/03b-code-review-verify-r1.json
.ai/reviews/accounting-morocco-f1/03b-code-review-verify.json
.ai/reviews/accounting-morocco-f1/03c-verify-note.md
.ai/reviews/accounting-morocco-f1/04-database-review.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/Продажи/Продажи.mdo
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ТоварыВНаличии.mdo
src/cf/src/AccumulationRegisters/ДвиженияДенежныхСредств/ДвиженияДенежныхСредств.mdo
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ВзаиморасчётыСПокупателями.mdo
src/cf/src/AccumulationRegisters/ДенежныеСредстваОрганизаций/ДенежныеСредстваОрганизаций.mdo
src/cf/src/ChartsOfCharacteristicTypes/ВидыНастроекПользователей/ВидыНастроекПользователей.mdo
src/cf/src/CommonForms/ФормаПервогоЗапуска/Form.form
src/cf/src/CommonModules/НалоговыйУчет/НалоговыйУчет.mdo
src/cf/src/CommonModules/НалоговыйУчет/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/НачальноеЗаполнениеВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Constants/РаздельныйУчет/РаздельныйУчет.mdo
src/cf/src/Constants/РаздельныйУчет/ValueManagerModule.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Бухгалтерия/Form.form
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Form.form
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
src/cf/src/Documents/СписаниеТоваров/СписаниеТоваров.mdo
src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/СписаниеТоваров/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/СписаниеТоваров/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/СписаниеТоваров/ObjectModule.bsl
src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
src/cf/src/FunctionalOptions/РаздельныйУчет/РаздельныйУчет.mdo
src/cf/src/InformationRegisters/НастройкиПользователей/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-18T21:06:45.363+01:00  INFO 70117 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/821 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/821 (0:00:01 / 0:01:30) Analyzing files...  14% [===                     ] 116/821 (0:00:02 / 0:00:12) Analyzing files...  35% [========                ] 292/821 (0:00:03 / 0:00:05) Analyzing files...  57% [=============           ] 468/821 (0:00:04 / 0:00:03) Analyzing files...  70% [================        ] 578/821 (0:00:05 / 0:00:02) Analyzing files...  86% [====================    ] 714/821 (0:00:06 / 0:00:00) Analyzing files...  99% [======================= ] 819/821 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 821/821 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 821/821 (0:00:07 / 0:00:00) 
2026-10-18T21:06:56.336+01:00  INFO 70117 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 19
новых замечаний нет
```
**PASS**
### уровень 0.5: scripts/refcheck.py
```
Сверка ссылок: расхождений нет (известных — 50)
```
**PASS**
### уровень 0.7: scripts/listcheck.py
```
Проверка динамических списков: расхождений нет (известных — 0)
```
**PASS**
### уровень 0.8: scripts/queryfields.py
```
Сверка полей запросов: расхождений нет (известных — 4)
```
**PASS**
### ОписаниеИзменений: секция текущей версии на ru/fr/en/es
```
Языков: 4, пунктов изменений: 16
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.96.json
версия 2.0.16.96: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ВзаиморасчётыСПокупателями.mdo
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ВзаиморасчётыСПоставщиками.mdo
 M src/cf/src/AccumulationRegisters/ДвиженияДенежныхСредств/ДвиженияДенежныхСредств.mdo
 M src/cf/src/AccumulationRegisters/ДенежныеСредстваОрганизаций/ДенежныеСредстваОрганизаций.mdo
 M src/cf/src/AccumulationRegisters/Продажи/Продажи.mdo
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ТоварыВНаличии.mdo
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыНастроекПользователей/ВидыНастроекПользователей.mdo
 M src/cf/src/CommonForms/ФормаПервогоЗапуска/Form.form
 A src/cf/src/CommonModules/НалоговыйУчет/Module.bsl
 A src/cf/src/CommonModules/НалоговыйУчет/НалоговыйУчет.mdo
 M src/cf/src/CommonModules/НачальноеЗаполнениеВызовСервера/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 A src/cf/src/Constants/РаздельныйУчет/ValueManagerModule.bsl
 A src/cf/src/Constants/РаздельныйУчет/РаздельныйУчет.mdo
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Form.form
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Бухгалтерия/Form.form
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
 M src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
 M src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/РасходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/СписаниеТоваров/ObjectModule.bsl
 M src/cf/src/Documents/СписаниеТоваров/СписаниеТоваров.mdo
 A src/cf/src/FunctionalOptions/РаздельныйУчет/РаздельныйУчет.mdo
 M src/cf/src/InformationRegisters/НастройкиПользователей/ManagerModule.bsl
?? .ai/reports/accounting-morocco-f1-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reviews/accounting-morocco-f1/03-code-review.json
?? .ai/reviews/accounting-morocco-f1/03b-code-review-verify-r1.json
?? .ai/reviews/accounting-morocco-f1/03b-code-review-verify.json
?? .ai/reviews/accounting-morocco-f1/03c-verify-note.md
?? .ai/reviews/accounting-morocco-f1/04-database-review.json
?? .ai/reviews/machine-form/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/wo-techdebt2/
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
+	// BSLLS:SetPrivilegedMode-off - значение настройки базы читает каждый пользователь
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off - проверка данных всей базы при записи настройки, права пользователя на регистры не важны
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.95 → 2.0.16.96

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
