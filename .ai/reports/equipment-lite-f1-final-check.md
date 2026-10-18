# Final check — equipment-lite-f1
_20261018T122521Z_


## Scope

```
.ai/reports/equipment-lite-f1-final-check.md
.ai/reports/equipment-lite-f1.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reviews/equipment-lite-f1/02-plan-review-r1.json
.ai/reviews/equipment-lite-f1/02-plan-review-r2.json
.ai/reviews/equipment-lite-f1/02-plan-review.json
.ai/reviews/equipment-lite-f1/03-code-review.json
.ai/reviews/equipment-lite-f1/03b-code-review-verify-r2.json
.ai/reviews/equipment-lite-f1/03b-code-review-verify-r3.json
.ai/reviews/equipment-lite-f1/03b-code-review-verify.json
.ai/reviews/equipment-lite-f1/03c-verify-note.md
.ai/reviews/equipment-lite-f1/04-database-review.json
.ai/reviews/equipment-lite-f1/05-security-review-r1.json
.ai/reviews/equipment-lite-f1/05-security-review-r2.json
.ai/reviews/equipment-lite-f1/05-security-review.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/equipment-lite-f1.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/Catalogs/РабочиеМеста/РабочиеМеста.mdo
src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаОбъединения/Form.form
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ФормаВыбораРабочегоМеста/Form.form
src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаСписка/Module.bsl
src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаЭлемента/Module.bsl
src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаОбъединения/Module.bsl
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ФормаВыбораРабочегоМеста/Module.bsl
src/cf/src/Catalogs/РабочиеМеста/ManagerModule.bsl
src/cf/src/Catalogs/ПодключаемоеОборудование/ObjectModule.bsl
src/cf/src/CommonModules/МенеджерОборудованияКлиент/Module.bsl
src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonModules/МенеджерОборудованияВызовСервера/Module.bsl
src/cf/src/CommonModules/ОперацииСПодключаемымОборудованиемКлиент/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Configuration/ManagedApplicationModule.bsl
src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Form.form
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
src/cf/src/InformationRegisters/ИдентификаторыРабочихМест/ИдентификаторыРабочихМест.mdo
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/ЛичныйКабинет/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Roles/MobileClient/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-18T13:25:29.355+01:00  INFO 1425 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/819 (0:00:00 / ?) Analyzing files...   3% [                        ]  30/819 (0:00:01 / 0:00:26) Analyzing files...  18% [====                    ] 152/819 (0:00:02 / 0:00:08) Analyzing files...  42% [==========              ] 345/819 (0:00:03 / 0:00:04) Analyzing files...  66% [================        ] 546/819 (0:00:04 / 0:00:02) Analyzing files...  83% [====================    ] 683/819 (0:00:05 / 0:00:00) Analyzing files...  99% [======================= ] 812/819 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 819/819 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 819/819 (0:00:06 / 0:00:00) 
2026-10-18T13:25:38.875+01:00  INFO 1425 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 15
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
Языков: 4, пунктов изменений: 24
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.95.json
версия 2.0.16.95: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 A docs/plans/equipment-lite-f1.md
 M src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ФормаВыбораРабочегоМеста/Form.form
 M src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ФормаВыбораРабочегоМеста/Module.bsl
 M src/cf/src/Catalogs/ПодключаемоеОборудование/ObjectModule.bsl
 A src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаОбъединения/Form.form
 A src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаОбъединения/Module.bsl
 M src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/РабочиеМеста/Forms/ФормаЭлемента/Module.bsl
 M src/cf/src/Catalogs/РабочиеМеста/ManagerModule.bsl
 M src/cf/src/Catalogs/РабочиеМеста/РабочиеМеста.mdo
 M src/cf/src/CommonModules/МенеджерОборудованияВызовСервера/Module.bsl
 M src/cf/src/CommonModules/МенеджерОборудованияКлиент/Module.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
 M src/cf/src/CommonModules/ОперацииСПодключаемымОборудованиемКлиент/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/Configuration/ManagedApplicationModule.bsl
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Form.form
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
 M src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 A src/cf/src/InformationRegisters/ИдентификаторыРабочихМест/ИдентификаторыРабочихМест.mdo
 M src/cf/src/Roles/MobileClient/Rights.rights
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/ЛичныйКабинет/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
?? .ai/reports/equipment-lite-f1-final-check.md
?? .ai/reports/equipment-lite-f1.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reviews/equipment-lite-f1/
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
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+// BSLLS:UnusedLocalVariable-off - BSL LS не разбирает выражения с Ждать и не видит использование переменных.
+// BSLLS:UnusedLocalVariable-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.94 → 2.0.16.95

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
