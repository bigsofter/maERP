# Final check — production-2mzl-e12-3a
_20260915T163505Z_


## Scope

```
.ai/reports/production-2mzl-e12-3a-final-check.md
.ai/reports/production-2mzl-e12-3a.md
.ai/reviews/production-2mzl-e12-3a/03-code-review.md
.ai/reviews/production-2mzl-e12-3a/04-code-review-claude.md
.ai/reviews/production-2mzl-e12-3a/05-database-security-review-claude.md
.ai/reviews/production-2mzl-e12-3a/06-verify-claude.md
docs/plans/production-2mzl-e12-arm.md
docs/plans/production-2mzl.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/formgen/arm/gen5.py
scripts/formgen/arm/README.md
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
src/cf/src/Documents/ВыпускПродукции/ManagerModule.bsl
src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-15T19:35:13.301+03:00  INFO 46260 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/741 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/741 (0:00:01 / 0:01:22) Analyzing files...  12% [===                     ]  93/741 (0:00:02 / 0:00:14) Analyzing files...  36% [========                ] 273/741 (0:00:03 / 0:00:05) Analyzing files...  62% [==============          ] 462/741 (0:00:04 / 0:00:02) Analyzing files...  85% [====================    ] 637/741 (0:00:05 / 0:00:00) Analyzing files...  99% [======================= ] 739/741 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 741/741 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 741/741 (0:00:06 / 0:00:00) 
2026-09-15T19:35:21.803+03:00  INFO 46260 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-08-26 14:06:31; изменённых модулей: 5
CommonModules/ПроизводственныеЗаказы/Module.bsl: LogicalOrInTheWhereSectionOfQuery +1 (было 0, стало 1)
    445: Не следует использовать логическое "ИЛИ" в секции "ГДЕ" запроса
CommonModules/ПроизводственныеЗаказы/Module.bsl: SetPrivilegedMode +4 (было 0, стало 4)
    19: Проверьте установку привилегированного режима
    40: Проверьте установку привилегированного режима
    61: Проверьте установку привилегированного режима
CommonModules/ПроизводственныеЗаказы/Module.bsl: YoLetterUsage +54 (было 0, стало 54)
    601: В текстах модулях не допускается использовать букву "Ё".
    592: В текстах модулях не допускается использовать букву "Ё".
    626: В текстах модулях не допускается использовать букву "Ё".
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
### уровень 0.8: scripts/queryfields.py
```
Сверка полей запросов: расхождений нет (известных — 4)
```
**PASS**
### ОписаниеИзменений: секция текущей версии на ru/fr/en/es
```
Языков: 4, пунктов изменений: 24
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.33.json
версия 2.0.15.33: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/production-2mzl-e12-arm.md
 M docs/plans/production-2mzl.md
 M scripts/formgen/arm/README.md
 M src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ManagerModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ObjectModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
?? .ai/reports/production-2mzl-e12-3a-final-check.md
?? .ai/reports/production-2mzl-e12-3a.md
?? .ai/reviews/production-2mzl-e12-3a/03-code-review.md
?? .ai/reviews/production-2mzl-e12-3a/04-code-review-claude.md
?? .ai/reviews/production-2mzl-e12-3a/05-database-security-review-claude.md
?? .ai/reviews/production-2mzl-e12-3a/06-verify-claude.md
?? scripts/formgen/arm/gen5.py
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
+	// BSLLS:YoLetterUsage-off - имя параметра общего текста запроса расчета стадии.
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:SetPrivilegedMode-off - налоговые накладные читаются служебно, наружу - только переданные реализации.
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:YoLetterUsage-off - имя табличной части в метаданных.
+	// BSLLS:YoLetterUsage-on
+		// BSLLS:MagicNumber-off - процент в долю.
+		// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - процент в долю.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария: заказ 10 и 1, расход 2, сырьё 30 по 10.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария: выпуск 4, правка до 5, расход 2.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария: отгрузка 3 и 4 при выпущенных 5, автовыпуск 2.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - выпущено 5 вручную и 7 с автовыпуском.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - выпуск 1 на минуту позже реализации.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - заказано 10, выпущено 7 (5 и автовыпуск 2), расход 2.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - отгрузка 20 при заказанных 10.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.15.32 → 2.0.15.33

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
