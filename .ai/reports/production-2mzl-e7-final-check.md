# Final check — production-2mzl-e7
_20260913T195347Z_


## Scope

```
.ai/plans/production-2mzl-e7.md
.ai/reports/production-2mzl-e7-final-check.md
.ai/reviews/production-2mzl-e7/01b-architecture-critic.md
.ai/reviews/production-2mzl-e7/02-plan-review-claude.md
.ai/reviews/production-2mzl-e7/03-code-review-claude.md
.ai/reviews/production-2mzl-e7/04-database-review-claude.md
.ai/reviews/production-2mzl-e7/05-security-review-claude.md
docs/plans/production-2mzl-prompt.md
docs/plans/production-2mzl.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ПотребностиПроизводства.mdo
src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ЗаказПоставщику/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
src/cf/src/Reports/ПотребностиПроизводства/ПотребностиПроизводства.mdo
src/cf/src/Reports/ПотребностиПроизводства/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Логист/Rights.rights
src/cf/src/Roles/Оператор/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Subsystems/Закупки/Закупки.mdo
src/cf/src/Subsystems/Производство/Производство.mdo
src/cf/src/Subsystems/Закупки/CommandInterface.cmi
src/cf/src/Subsystems/Производство/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-13T22:53:53.615+03:00  INFO 62153 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/737 (0:00:00 / ?) Analyzing files...   9% [==                      ]  72/737 (0:00:01 / 0:00:09) Analyzing files...  35% [========                ] 261/737 (0:00:02 / 0:00:03) Analyzing files...  60% [==============          ] 444/737 (0:00:03 / 0:00:01) Analyzing files...  84% [====================    ] 623/737 (0:00:04 / 0:00:00) Analyzing files... 100% [========================] 737/737 (0:00:04 / 0:00:00) Analyzing files... 100% [========================] 737/737 (0:00:04 / 0:00:00) 
2026-09-13T22:53:59.978+03:00  INFO 62153 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-08-26 14:06:31; изменённых модулей: 9
Documents/ЗаказПокупателя/ObjectModule.bsl: EventHandlerOutsideEventRegion +1 (было 5, стало 6)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    80: Метод "ПриКопировании" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    85: Метод "ПередЗаписью" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
Documents/ЗаказПокупателя/ObjectModule.bsl: SetPrivilegedMode +1 (было 0, стало 1)
    896: Проверьте установку привилегированного режима
```
**FAIL**
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
### ОписаниеИзменений: секция текущей версии на ru/fr/en/es
```
Языков: 4, пунктов изменений: 28
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.15.json
версия 2.0.15.15: ru=7, fr=7, en=7, es=7
```
**PASS**

## Git hygiene

### git status
```
 A .ai/plans/production-2mzl-e7.md
 A .ai/reviews/production-2mzl-e7/01b-architecture-critic.md
 A .ai/reviews/production-2mzl-e7/02-plan-review-claude.md
 A .ai/reviews/production-2mzl-e7/03-code-review-claude.md
 A .ai/reviews/production-2mzl-e7/04-database-review-claude.md
 A .ai/reviews/production-2mzl-e7/05-security-review-claude.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/production-2mzl-prompt.md
 M docs/plans/production-2mzl.md
 A src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
 A src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ПотребностиПроизводства.mdo
 M src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
 M src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
 M src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ЗаказПоставщику/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПоставщику/ObjectModule.bsl
 M src/cf/src/Documents/ЗаказПоставщику/ЗаказПоставщику.mdo
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
 A src/cf/src/Reports/ПотребностиПроизводства/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 A src/cf/src/Reports/ПотребностиПроизводства/ПотребностиПроизводства.mdo
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Subsystems/Закупки/CommandInterface.cmi
 M src/cf/src/Subsystems/Закупки/Закупки.mdo
 M src/cf/src/Subsystems/Производство/CommandInterface.cmi
 M src/cf/src/Subsystems/Производство/Производство.mdo
?? .ai/reports/production-2mzl-e7-final-check.md
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
+	// BSLLS:MagicNumber-off - количества сценария из плана E7, п. 12.7.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количество строки закупки без движений.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария из плана E7, п. 12.7.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария из плана E7, п. 12.7.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария из плана E7, п. 12.7.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - три строки потребности заказа.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - новое количество продукции P1.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.15.14 → 2.0.15.15

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 5 (PASS: 4, FAIL: 1)

Провалились:
  - уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**FAILURES ABOVE** — do not report the task done until resolved.
