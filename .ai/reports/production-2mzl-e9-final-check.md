# Final check — production-2mzl-e9
_20260914T120447Z_


## Scope

```
.ai/plans/production-2mzl-e9.md
.ai/reports/production-2mzl-e9-final-check.md
.ai/reviews/production-2mzl-e9/01-architecture-critic.md
.ai/reviews/production-2mzl-e9/02-plan-review-astra.md
.ai/reviews/production-2mzl-e9/03-code-review.md
.ai/reviews/production-2mzl-e9/03b-code-review-verify-astra.md
.ai/reviews/production-2mzl-e9/03c-code-review-verify2-astra.md
.ai/reviews/production-2mzl-e9/04-database-review-claude.md
.ai/reviews/production-2mzl-e9/04-database-review.md
.ai/reviews/production-2mzl-e9/05-security-review-claude.md
.ai/reviews/production-2mzl-e9/05-security-review.md
docs/plans/production-2mzl-prompt.md
docs/plans/production-2mzl.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
src/cf/src/CommonModules/Производство/Производство.mdo
src/cf/src/CommonModules/Производство/Module.bsl
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Constants/ИспользоватьВыпускПродукцииПриПродаже/ИспользоватьВыпускПродукцииПриПродаже.mdo
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Form.form
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
src/cf/src/Documents/ВыпускПродукции/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВыпускПродукции/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
src/cf/src/Reports/ПотребностиПроизводства/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-14T15:04:55.171+03:00  INFO 41434 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/739 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/739 (0:00:01 / 0:01:21) Analyzing files...  12% [===                     ]  96/739 (0:00:02 / 0:00:13) Analyzing files...  26% [======                  ] 195/739 (0:00:03 / 0:00:08) Analyzing files...  41% [=========               ] 303/739 (0:00:04 / 0:00:05) Analyzing files...  56% [=============           ] 421/739 (0:00:05 / 0:00:03) Analyzing files...  83% [====================    ] 619/739 (0:00:06 / 0:00:01) Analyzing files... 100% [========================] 739/739 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 739/739 (0:00:06 / 0:00:00) 
2026-09-14T15:05:05.395+03:00  INFO 41434 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-08-26 14:06:31; изменённых модулей: 10
CommonModules/Производство/Module.bsl: SetPrivilegedMode +6 (было 0, стало 6)
    21: Проверьте установку привилегированного режима
    96: Проверьте установку привилегированного режима
    154: Проверьте установку привилегированного режима
CommonModules/ПроизводственныеЗаказы/Module.bsl: LogicalOrInTheWhereSectionOfQuery +1 (было 0, стало 1)
    416: Не следует использовать логическое "ИЛИ" в секции "ГДЕ" запроса
CommonModules/ПроизводственныеЗаказы/Module.bsl: SetPrivilegedMode +4 (было 0, стало 4)
    19: Проверьте установку привилегированного режима
    40: Проверьте установку привилегированного режима
    61: Проверьте установку привилегированного режима
CommonModules/ПроизводственныеЗаказы/Module.bsl: YoLetterUsage +54 (было 0, стало 54)
    572: В текстах модулях не допускается использовать букву "Ё".
    563: В текстах модулях не допускается использовать букву "Ё".
    597: В текстах модулях не допускается использовать букву "Ё".
DataProcessors/ТестыДокументов/ManagerModule.bsl: YoLetterUsage +1 (было 0, стало 1)
    2946: В текстах модулях не допускается использовать букву "Ё".
Documents/РеализацияТоваровУслуг/ObjectModule.bsl: EventHandlerOutsideEventRegion +1 (было 6, стало 7)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    41: Метод "ОбработкаПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    74: Метод "ОбработкаУдаленияПроведения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
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
Языков: 4, пунктов изменений: 24
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.21.json
версия 2.0.15.21: ru=6, fr=6, en=6, es=6
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
 M src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
 M src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
 A src/cf/src/CommonModules/Производство/Module.bsl
 A src/cf/src/CommonModules/Производство/Производство.mdo
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/Constants/ИспользоватьВыпускПродукцииПриПродаже/ИспользоватьВыпускПродукцииПриПродаже.mdo
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/Производство/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Reports/ПотребностиПроизводства/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
?? .ai/plans/production-2mzl-e9.md
?? .ai/reports/production-2mzl-e9-final-check.md
?? .ai/reviews/production-2mzl-e9/
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
+		// BSLLS:MagicNumber-off - точность количества определяемого типа.
+		// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - остатки: товар 3 по 50, M1 50 по 40, M2 10 по 30; заказ P1 10, P2 3; под заказ M1 12.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - P1 6 из 10; M1 12 партией под заказ по 10, M2 3 по 30, товар 3 по 50.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - ручной выпуск 2 (M1 4 по 40), реализация 4: автовыпуск 2 (M1 4 по 40).
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - заказ P1 10: отгрузки 6 и 4 в одну секунду.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - остаток сырья с серией 5, на единицу продукции 2.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - остаток M3 3, нужно 10.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.15.20 → 2.0.15.21

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
