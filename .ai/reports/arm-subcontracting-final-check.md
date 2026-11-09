# Final check — arm-subcontracting
_20261005T214311Z_


## Scope

```
.ai/reports/arm-subcontracting-final-check.md
.ai/reviews/arm-subcontracting/02-plan-review-claude.md
.ai/reviews/arm-subcontracting/03-review-claude.md
.ai/reviews/arm-subcontracting/04-database-security-claude.md
docs/DEPLOY.md
docs/plans/arm-subcontracting-properties.md
docs/TECHDEBT.md
scripts/formgen/arm/gen10_columns.py
scripts/formgen/arm/gen10_panel.py
scripts/formgen/arm/gen10.py
scripts/formgen/arm/README.md
src/cf/src/CommonForms/ФормаПервогоЗапуска/Module.bsl
src/cf/src/CommonModules/УправлениеСвойствами/Module.bsl
src/cf/src/CommonModules/НачальноеЗаполнениеВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/ПередачаВПереработку/ПередачаВПереработку.mdo
src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПередачаВПереработку/ManagerModule.bsl
src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
src/cf/src/Enums/Отрасли/Отрасли.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-05T22:43:20.584+01:00  INFO 1111 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/759 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/759 (0:00:01 / 0:01:23) Analyzing files...  10% [==                      ]  79/759 (0:00:02 / 0:00:17) Analyzing files...  26% [======                  ] 198/759 (0:00:03 / 0:00:08) Analyzing files...  42% [==========              ] 319/759 (0:00:04 / 0:00:05) Analyzing files...  53% [============            ] 406/759 (0:00:05 / 0:00:04) Analyzing files...  70% [================        ] 533/759 (0:00:06 / 0:00:02) Analyzing files...  88% [=====================   ] 673/759 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 759/759 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 759/759 (0:00:07 / 0:00:00) 
2026-10-05T22:43:31.904+01:00  INFO 1111 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 20
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.16.json
версия 2.0.16.16: ru=5, fr=5, en=5, es=5
```
**PASS**

## Git hygiene

### git status
```
 M docs/DEPLOY.md
 M docs/TECHDEBT.md
 M scripts/formgen/arm/README.md
 M src/cf/src/CommonForms/ФормаПервогоЗапуска/Module.bsl
 M src/cf/src/CommonModules/НачальноеЗаполнениеВызовСервера/Module.bsl
 M src/cf/src/CommonModules/УправлениеСвойствами/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ManagerModule.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ПередачаВПереработку.mdo
 M src/cf/src/Enums/Отрасли/Отрасли.mdo
?? .ai/reports/arm-subcontracting-final-check.md
?? .ai/reviews/arm-subcontracting/
?? docs/plans/arm-subcontracting-properties.md
?? scripts/formgen/arm/gen10.py
?? scripts/formgen/arm/gen10_columns.py
?? scripts/formgen/arm/gen10_panel.py
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
+	// BSLLS:PrivilegedModuleMethodCall-off - вызов собственного метода внутри привилегированного модуля
+	// BSLLS:PrivilegedModuleMethodCall-on
+		// BSLLS:PrivilegedModuleMethodCall-off - вызов собственного метода внутри привилегированного модуля
+		// BSLLS:PrivilegedModuleMethodCall-on
+	// BSLLS:PrivilegedModuleMethodCall-off - вызов собственного метода внутри привилегированного модуля
+	// BSLLS:PrivilegedModuleMethodCall-on
+	// BSLLS:MagicNumber-off - порядок полей задан прямо в описании реквизитов.
+	// BSLLS:PrivilegedModuleMethodCall-off - вызов собственного метода внутри привилегированного модуля
+	// BSLLS:PrivilegedModuleMethodCall-on
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - пауза перед перечитыванием свойств, секунды.
+	// BSLLS:MagicNumber-on
+	// BSLLS:SetPrivilegedMode-off - узкая запись свойства ПФ/ГП после проверок выше (решение владельца 2026-10-05)
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:PrivilegedModuleMethodCall-off - текст предупреждения, без записи данных
+	// BSLLS:PrivilegedModuleMethodCall-on
+	// BSLLS:MagicNumber-off - передано 6 сырья при норме 2: ожидается 3; в заказе 10.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - строки 99 в передаче нет, число 5 - не строка.
+	// BSLLS:MagicNumber-on
+	// BSLLS:SetPrivilegedMode-off - наличие поступления проверяется и у пользователя без права их читать
+	// BSLLS:SetPrivilegedMode-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.15 → 2.0.16.16

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
