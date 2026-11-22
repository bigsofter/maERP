# Final check — warehouse-orders-option
_20261028T073539Z_


## Scope

```
.ai/reports/arm-pf-output-final-check.md
.ai/reports/arm-production-print-final-check.md
.ai/reports/arm-purch-tabs-final-check.md
.ai/reports/arm-purchasing-receipts-final-check.md
.ai/reports/arm-purchasing-receipts-s2-final-check.md
.ai/reports/card-crash-filters-final-check.md
.ai/reports/card-routing-crash-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/order-stock-places-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/semi-finished-subcontract-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reports/tabs-handlers-final-check.md
.ai/reports/warehouse-orders-option-final-check.md
.ai/reviews/arm-production-print/03-code-review.json
.ai/reviews/arm-production-print/03b-code-review-verify.json
.ai/reviews/card-crash-filters/03-code-review.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/warehouse-orders-option/02-plan-review.json
.ai/reviews/warehouse-orders-option/03-code-review.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify.json
.ai/reviews/warehouse-orders-option/04-database-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/warehouse-orders-option.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/Catalogs/МестаХранения/ManagerModule.bsl
src/cf/src/Catalogs/МестаХранения/ObjectModule.bsl
src/cf/src/CommonForms/ФормаПервогоЗапуска/Form.form
src/cf/src/CommonModules/ОрдераСклада/Module.bsl
src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonModules/НачальноеЗаполнениеВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Constants/ИспользоватьОрдерныеСклады/ИспользоватьОрдерныеСклады.mdo
src/cf/src/Constants/ИспользоватьОрдерныеСклады/ValueManagerModule.bsl
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Склад/Form.form
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Склад/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ПриходныйОрдер/ObjectModule.bsl
src/cf/src/FunctionalOptions/ИспользоватьОрдерныеСклады/ИспользоватьОрдерныеСклады.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-28T08:35:46.953+01:00  INFO 18360 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/823 (0:00:00 / ?) Analyzing files...   2% [                        ]  18/823 (0:00:01 / 0:00:44) Analyzing files...  14% [===                     ] 120/823 (0:00:02 / 0:00:11) Analyzing files...  35% [========                ] 295/823 (0:00:03 / 0:00:05) Analyzing files...  56% [=============           ] 461/823 (0:00:04 / 0:00:03) Analyzing files...  69% [================        ] 570/823 (0:00:05 / 0:00:02) Analyzing files...  92% [======================  ] 758/823 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 823/823 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 823/823 (0:00:06 / 0:00:00) 
2026-10-28T08:35:56.959+01:00  INFO 18360 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 11
DataProcessors/ТестыДокументов/ManagerModule.bsl: DuplicateStringLiteral +1 (было 1, стало 2)
    2055: Необходимо избавиться от многократного использования строкового литерала "Номенклатура"
    19316: Необходимо избавиться от многократного использования строкового литерала "Номенклатура"
DataProcessors/ТестыДокументов/ManagerModule.bsl: MagicNumber +2 (было 0, стало 2)
    9256: Создайте константу с понятным названием, присвойте ей значение "2" и используйте эту константу вместо магического числа.
    9258: Создайте константу с понятным названием, присвойте ей значение "2" и используйте эту константу вместо магического числа.
DataProcessors/ТестыДокументов/ManagerModule.bsl: NestedFunctionInParameters +6 (было 1, стало 7)
    2054: Уберите инициализацию параметров метода "ПроверитьРавенство" вложенными методами
    5233: Уберите инициализацию параметров метода "ПроверитьРавенство" вложенными методами
    9134: Уберите инициализацию параметров метода "Проверить" вложенными методами
DataProcessors/ТестыДокументов/ManagerModule.bsl: UsingHardcodeNetworkAddress +4 (было 0, стало 4)
    2061: Используется хранение в коде ip-адреса
    2063: Используется хранение в коде ip-адреса
    2065: Используется хранение в коде ip-адреса
```
**FAIL**
### уровень 0.5: scripts/refcheck.py
```
Сверка ссылок: расхождений нет (известных — 51)
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.107.json
версия 2.0.16.107: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/Catalogs/МестаХранения/ManagerModule.bsl
 M src/cf/src/Catalogs/МестаХранения/ObjectModule.bsl
 M src/cf/src/CommonForms/ФормаПервогоЗапуска/Form.form
 M src/cf/src/CommonModules/НачальноеЗаполнениеВызовСервера/Module.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ОрдераСклада/Module.bsl
 M src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Склад/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Склад/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ПриходныйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РасходныйОрдер/ObjectModule.bsl
?? .ai/reports/arm-pf-output-final-check.md
?? .ai/reports/arm-production-print-final-check.md
?? .ai/reports/arm-purch-tabs-final-check.md
?? .ai/reports/arm-purchasing-receipts-final-check.md
?? .ai/reports/arm-purchasing-receipts-s2-final-check.md
?? .ai/reports/card-crash-filters-final-check.md
?? .ai/reports/card-routing-crash-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/order-stock-places-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/semi-finished-subcontract-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reports/tabs-handlers-final-check.md
?? .ai/reports/warehouse-orders-option-final-check.md
?? .ai/reviews/arm-production-print/
?? .ai/reviews/card-crash-filters/
?? .ai/reviews/machine-form/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/warehouse-orders-option/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/warehouse-orders-option.md
?? src/cf/src/Constants/ИспользоватьОрдерныеСклады/
?? src/cf/src/FunctionalOptions/ИспользоватьОрдерныеСклады/
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
+// BSLLS:SetPrivilegedMode-off - чтение одной константы опции, без записи.
+// BSLLS:SetPrivilegedMode-on
+// BSLLS:SetPrivilegedMode-off - проверка инварианта видит все склады и ордера, а не только доступные пользователю.
+// BSLLS:SelectTopWithoutOrderBy-off - ПЕРВЫЕ 1 - проверка существования, порядок не важен.
+// BSLLS:SelectTopWithoutOrderBy-on
+// BSLLS:SetPrivilegedMode-on
+// BSLLS:DataExchangeLoading-off
+// BSLLS:DataExchangeLoading-on
+// BSLLS:DataExchangeLoading-off
+// BSLLS:DataExchangeLoading-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.106 → 2.0.16.107

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 5, FAIL: 1)

Провалились:
  - уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**FAILURES ABOVE** — do not report the task done until resolved.
