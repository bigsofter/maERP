# Final check — supplier-order-roles
_20261125T144908Z_


## Scope

```
.ai/bin/ai-final-check
.ai/reports/doc-numbering-acceptance.md
.ai/reports/supplier-order-roles-acceptance.md
.ai/reports/supplier-order-roles-final-check.md
.ai/reports/supplier-order-roles.md
.ai/reviews/doc-numbering/02-plan-review.json
.ai/reviews/supplier-order-roles/02-plan-review.json
.ai/reviews/supplier-order-roles/03-code-review.json
.ai/reviews/supplier-order-roles/03b-code-review-verify.json
CLAUDE.md
docs/ARCHITECTURE.md
docs/plans/doc-numbering.md
docs/plans/order-payment-state.md
docs/plans/supplier-order-roles.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/testing/doc-scenarios.md
scripts/env.sh
scripts/ib-sync.sh
scripts/reportstyle.py
scripts/rolecheck.py
scripts/roles-run.sh
scripts/smoke-floor.txt
scripts/uitest.sh
scripts/vm-gate.sh
scripts/vm-run.sh
scripts/xmlsum.sh
src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
src/cf/src/CommonModules/ОрдераСклада/Module.bsl
src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
src/cf/src/Reports/ДвиженияДокумента/Forms/ФормаОтчета/Module.bsl
src/cf/src/Reports/ЗарплатаСотрудника/Forms/ФормаОтчета/Module.bsl
src/cf/src/Reports/ПрослеживаемостьПартий/ObjectModule.bsl
src/cf/src/Reports/ИсторияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ДвиженияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ОстаткиНаСкладах/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ТоварыВПереработке/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ПланЗагрузкиСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РасчетыСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ПрослеживаемостьПартий/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ПереработкаПоПереработчикам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/ЧтениеЗаказаПоставщику/ЧтениеЗаказаПоставщику.mdo
src/cf/src/Roles/ИзменениеЗаказаПоставщику/ИзменениеЗаказаПоставщику.mdo
src/cf/src/Roles/Логист/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Roles/ЧтениеЗаказаПоставщику/Rights.rights
src/cf/src/Roles/ИзменениеЗаказаПоставщику/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
tests/ui/core.bsl
tests/ui/role-scenarios-orders.txt
tests/ui/role-scenarios.txt
tests/ui/role-users.bsl
tests/ui/scenarios.txt
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-25T15:49:19.135+01:00  INFO 7571 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/904 (0:00:00 / ?) Analyzing files...   0% [                        ]   9/904 (0:00:01 / 0:01:39) Analyzing files...   4% [=                       ]  45/904 (0:00:02 / 0:00:38) Analyzing files...  11% [==                      ] 108/904 (0:00:03 / 0:00:22) Analyzing files...  20% [====                    ] 188/904 (0:00:04 / 0:00:15) Analyzing files...  25% [======                  ] 231/904 (0:00:05 / 0:00:14) Analyzing files...  31% [=======                 ] 288/904 (0:00:06 / 0:00:12) Analyzing files...  45% [==========              ] 408/904 (0:00:07 / 0:00:08) Analyzing files...  58% [=============           ] 527/904 (0:00:08 / 0:00:05) Analyzing files...  71% [=================       ] 642/904 (0:00:09 / 0:00:03) Analyzing files...  87% [====================    ] 788/904 (0:00:10 / 0:00:01) Analyzing files...  94% [======================  ] 850/904 (0:00:11 / 0:00:00) Analyzing files...  98% [======================= ] 891/904 (0:00:12 / 0:00:00) Analyzing files... 100% [========================] 904/904 (0:00:13 / 0:00:00) Analyzing files... 100% [========================] 904/904 (0:00:13 / 0:00:00) 
2026-11-25T15:49:37.018+01:00  INFO 7571 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 15
новых замечаний нет
```
**PASS**
### уровень 0.5: scripts/refcheck.py
```
Сверка ссылок: расхождений нет (известных — 48)
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
### уровень 0.85: scripts/navcheck.py
```
Сверка навигации форм: ссылка «Файлы» скрыта во всех формах документов (форм — 50)
```
**PASS**
### уровень 0.9: scripts/colfont.py (шрифт шапки колонок)
```
Колонки без шрифта шапки: 0 (в формах 0); с titleFont: 2767
```
**PASS**
### уровень 0.93: scripts/reportstyle.py (оформление отчётов)
```
reportstyle: расхождений 0
```
**PASS**
### уровень 0.95: scripts/menucheck.py (фактическое меню разделов)
```

Сверка меню: подсистем 45, расхождений сверх базы 0, протухших строк базы 0
```
**PASS**
### ОписаниеИзменений: секция текущей версии на ru/fr/en/es
```
Языков: 4, пунктов изменений: 64
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.18.5.json
версия 2.0.18.5: ru=16, fr=16, en=16, es=16
```
**PASS**
### уровни 1–3: штамп гейта базы на текущее дерево src/cf
```
PASS 5b879ae13772fdf10194d365204f7ee7511781a7 2.0.18.5 2026-11-25T14:49:06
```
**PASS**
### приёмка: scripts/acceptcheck.py .ai/reports/supplier-order-roles-acceptance.md
```
Приёмка закрыта: критериев 18, однотипных объектов 31
```
**PASS**
### карта архитектуры актуальна: scripts/archmap.py --check (обновить: python3 scripts/archmap.py)
```
archmap: docs/ARCHITECTURE.md актуален
```
**PASS**
### неслитые ветки с правками конфигурации: scripts/branchcheck.sh
```
Сверка веток: неслитых правок конфигурации нет (проверено веток: 18)
```
**PASS**

## Git hygiene

### git status
```
 M .ai/bin/ai-final-check
 A .ai/reports/supplier-order-roles-acceptance.md
 M CLAUDE.md
 M docs/ARCHITECTURE.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 A docs/plans/supplier-order-roles.md
 M docs/testing/doc-scenarios.md
 M scripts/env.sh
 M scripts/ib-sync.sh
 M scripts/rolecheck.py
 M scripts/smoke-floor.txt
 M scripts/uitest.sh
 M src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
 M src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/Module.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ОрдераСклада/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Reports/ДвиженияДокумента/Forms/ФормаОтчета/Module.bsl
 M src/cf/src/Reports/ДвиженияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ЗарплатаСотрудника/Forms/ФормаОтчета/Module.bsl
 M src/cf/src/Reports/ИсторияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОстаткиНаСкладах/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПереработкаПоПереработчикам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПланЗагрузкиСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПрослеживаемостьПартий/ObjectModule.bsl
 M src/cf/src/Reports/ПрослеживаемостьПартий/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РасчетыСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыВПереработке/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
 A src/cf/src/Roles/ИзменениеЗаказаПоставщику/Rights.rights
 A src/cf/src/Roles/ИзменениеЗаказаПоставщику/ИзменениеЗаказаПоставщику.mdo
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 A src/cf/src/Roles/ЧтениеЗаказаПоставщику/Rights.rights
 A src/cf/src/Roles/ЧтениеЗаказаПоставщику/ЧтениеЗаказаПоставщику.mdo
 M tests/ui/core.bsl
 A tests/ui/role-scenarios.txt
 M tests/ui/role-users.bsl
 M tests/ui/scenarios.txt
?? .ai/reports/doc-numbering-acceptance.md
?? .ai/reports/supplier-order-roles-final-check.md
?? .ai/reports/supplier-order-roles.md
?? .ai/reviews/doc-numbering/
?? .ai/reviews/supplier-order-roles/
?? docs/plans/doc-numbering.md
?? docs/plans/order-payment-state.md
?? scripts/reportstyle.py
?? scripts/roles-run.sh
?? scripts/vm-gate.sh
?? scripts/vm-run.sh
?? scripts/xmlsum.sh
?? tests/ui/role-scenarios-orders.txt
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
+		// BSLLS:SetPrivilegedMode-off - читается только ссылка/признак, наружу данные заказа поставщику не выходят
+		// BSLLS:SetPrivilegedMode-on
+		// BSLLS:SetPrivilegedMode-off
+		// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off - читаются только номер и дата основания, наружу данные заказа не выходят
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off - читается только ссылка/признак, наружу данные заказа поставщику не выходят
+	// BSLLS:SetPrivilegedMode-on
+		// BSLLS:SetPrivilegedMode-off - читается только ссылка/признак, наружу данные заказа поставщику не выходят
+		// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off - читается только ссылка/признак, наружу данные заказа поставщику не выходят
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:MagicNumber-off - количества сценария и сутки в секундах.
+	// BSLLS:MagicNumber-on
+	// BSLLS:StyleElementConstructors-off - палитра макета оформления «Античный», в стилях конфигурации её нет
+	// BSLLS:MagicNumber-off - составляющие цветов той же палитры
+	// BSLLS:MagicNumber-on
+	// BSLLS:StyleElementConstructors-on
+	// BSLLS:StyleElementConstructors-off - палитра макета оформления «Античный», в стилях конфигурации её нет
+	// BSLLS:MagicNumber-off - составляющие цветов той же палитры
+	// BSLLS:MagicNumber-on
+	// BSLLS:StyleElementConstructors-on
+// BSLLS:StyleElementConstructors-off - палитра макета оформления «Античный» платформы: в стиле конфигурации её нет.
+// BSLLS:StyleElementConstructors-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.18.4 → 2.0.18.5

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- новые объекты/формы (2 файлов), а реестр docs/TESTS.xlsx не менялся — изменение состава тестов фиксируется в реестре
- уровни 1–3 идут на базе гейта build/ib-gate через scripts/gate.sh; сборка сдаётся только со штампом на текущее дерево src/cf

## Gates run

Запущено гейтов: 14 (PASS: 14, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
