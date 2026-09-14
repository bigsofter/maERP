# Final check — production-2mzl-e8
_20260914T074234Z_


## Scope

```
.ai/plans/production-2mzl-e8.md
.ai/reports/production-2mzl-e8-final-check.md
.ai/reviews/production-2mzl-e8/01-architecture-critic.md
.ai/reviews/production-2mzl-e8/02-plan-review-claude.md
.ai/reviews/production-2mzl-e8/03-code-review-claude.md
.ai/reviews/production-2mzl-e8/04-database-review-claude.md
.ai/reviews/production-2mzl-e8/05-security-review-claude.md
docs/plans/production-2mzl-prompt.md
docs/plans/production-2mzl.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/CommonModules/ПроизводственныеЗаказы/ПроизводственныеЗаказы.mdo
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Module.bsl
src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/ConditionalAppearance.dcssca
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
src/cf/src/Documents/КорректировкаДолга/ObjectModule.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
src/cf/src/Enums/СтатусыЗаказовПокупателя/СтатусыЗаказовПокупателя.mdo
src/cf/src/InformationRegisters/ИсторияЗаказовПокупателейПоСтатусам/ИсторияЗаказовПокупателейПоСтатусам.mdo
src/cf/src/Roles/Логист/Rights.rights
src/cf/src/Roles/Оператор/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/ECommerce/Rights.rights
src/cf/src/Roles/MobileClient/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-14T10:42:43.560+03:00  INFO 84544 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/738 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/738 (0:00:01 / 0:01:21) Analyzing files...   5% [=                       ]  40/738 (0:00:02 / 0:00:34) Analyzing files...  19% [====                    ] 145/738 (0:00:03 / 0:00:12) Analyzing files...  34% [========                ] 257/738 (0:00:04 / 0:00:07) Analyzing files...  42% [==========              ] 316/738 (0:00:05 / 0:00:06) Analyzing files...  57% [=============           ] 426/738 (0:00:06 / 0:00:04) Analyzing files...  81% [===================     ] 598/738 (0:00:07 / 0:00:01) Analyzing files... 100% [========================] 738/738 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 738/738 (0:00:07 / 0:00:00) 
2026-09-14T10:42:54.540+03:00  INFO 84544 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-08-26 14:06:31; изменённых модулей: 17
CommonModules/ПроизводственныеЗаказы/Module.bsl: LogicalOrInTheWhereSectionOfQuery +1 (было 0, стало 1)
    401: Не следует использовать логическое "ИЛИ" в секции "ГДЕ" запроса
CommonModules/ПроизводственныеЗаказы/Module.bsl: SetPrivilegedMode +4 (было 0, стало 4)
    19: Проверьте установку привилегированного режима
    40: Проверьте установку привилегированного режима
    61: Проверьте установку привилегированного режима
CommonModules/ПроизводственныеЗаказы/Module.bsl: YoLetterUsage +54 (было 0, стало 54)
    557: В текстах модулях не допускается использовать букву "Ё".
    548: В текстах модулях не допускается использовать букву "Ё".
    582: В текстах модулях не допускается использовать букву "Ё".
DataProcessors/ТестыДокументов/ManagerModule.bsl: YoLetterUsage +1 (было 0, стало 1)
    2940: В текстах модулях не допускается использовать букву "Ё".
Documents/ВозвратПоставщику/ObjectModule.bsl: EventHandlerOutsideEventRegion +2 (было 4, стало 6)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    23: Метод "ОбработкаПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    54: Метод "ОбработкаУдаленияПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
Documents/КорректировкаДолга/ObjectModule.bsl: EventHandlerOutsideEventRegion +2 (было 4, стало 6)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    6: Метод "ОбработкаПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    59: Метод "ОбработкаУдаленияПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
Documents/ВозвратОтПокупателя/ObjectModule.bsl: EventHandlerOutsideEventRegion +2 (было 4, стало 6)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    32: Метод "ОбработкаПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    59: Метод "ОбработкаУдаленияПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl: EventHandlerOutsideEventRegion +2 (было 5, стало 7)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    72: Метод "ОбработкаПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    99: Метод "ОбработкаУдаленияПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl: EventHandlerOutsideEventRegion +2 (было 5, стало 7)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    87: Метод "ОбработкаПроверкиЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    101: Метод "ОбработкаПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl: EventHandlerOutsideEventRegion +2 (было 5, стало 7)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    78: Метод "ОбработкаПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    107: Метод "ОбработкаУдаленияПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl: EventHandlerOutsideEventRegion +2 (было 5, стало 7)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    63: Метод "ОбработкаПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    90: Метод "ОбработкаУдаленияПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
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
Языков: 4, пунктов изменений: 32
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.20.json
версия 2.0.15.20: ru=8, fr=8, en=8, es=8
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/production-2mzl-prompt.md
 M docs/plans/production-2mzl.md
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
 M src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
 M src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/ConditionalAppearance.dcssca
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ЗаказПоставщику/ObjectModule.bsl
 M src/cf/src/Documents/КорректировкаДолга/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Documents/СертификатНаОплату/ObjectModule.bsl
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/ObjectModule.bsl
 M src/cf/src/Enums/СтатусыЗаказовПокупателя/СтатусыЗаказовПокупателя.mdo
 M src/cf/src/InformationRegisters/ИсторияЗаказовПокупателейПоСтатусам/ИсторияЗаказовПокупателейПоСтатусам.mdo
 M src/cf/src/Roles/ECommerce/Rights.rights
 M src/cf/src/Roles/MobileClient/Rights.rights
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
?? .ai/plans/production-2mzl-e8.md
?? .ai/reports/production-2mzl-e8-final-check.md
?? .ai/reviews/production-2mzl-e8/
?? src/cf/src/CommonModules/ПроизводственныеЗаказы/
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
+	// BSLLS:MagicNumber-off - количества сценария: товар 3 + 3 + 1, продукция на склад 1.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - продукция 10, записей истории 1 и 2.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - поступления 12 и 8 из потребности 20.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - выпуски 4 и 6 из 10.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - отгрузки: товар 3 и продукция 4, затем продукция 6; возврат 1.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - оплаты 700 (первая реализация) и 600 (аванс под вторую).
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.15.19 → 2.0.15.20

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
