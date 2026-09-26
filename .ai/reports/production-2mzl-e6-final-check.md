# Final check — production-2mzl-e6
_20260913T182730Z_


## Scope

```
.ai/plans/production-2mzl-e6.md
.ai/reports/production-2mzl-e6-final-check.md
.ai/reports/production-2mzl-e6.md
.ai/reviews/production-2mzl-e6/01b-architecture-critic.md
.ai/reviews/production-2mzl-e6/02-plan-review-claude.md
.ai/reviews/production-2mzl-e6/03-code-review-claude.md
.ai/reviews/production-2mzl-e6/04-database-review-claude.md
.ai/reviews/production-2mzl-e6/05-security-review-claude.md
docs/plans/production-2mzl-prompt.md
docs/plans/production-2mzl.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/ТехнологическиеКарты/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаВыбора/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
src/cf/src/Documents/ТехнологическаяКарта/ObjectModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-13T21:27:40.366+03:00  INFO 43810 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/736 (0:00:00 / ?) Analyzing files...   3% [                        ]  27/736 (0:00:01 / 0:00:26) Analyzing files...  15% [===                     ] 115/736 (0:00:02 / 0:00:10) Analyzing files...  25% [======                  ] 188/736 (0:00:03 / 0:00:08) Analyzing files...  42% [==========              ] 311/736 (0:00:04 / 0:00:05) Analyzing files...  50% [============            ] 374/736 (0:00:05 / 0:00:04) Analyzing files...  61% [==============          ] 452/736 (0:00:06 / 0:00:03) Analyzing files...  79% [===================     ] 588/736 (0:00:07 / 0:00:01) Analyzing files...  88% [=====================   ] 650/736 (0:00:08 / 0:00:01) Analyzing files...  99% [======================= ] 735/736 (0:00:09 / 0:00:00) Analyzing files... 100% [========================] 736/736 (0:00:09 / 0:00:00) Analyzing files... 100% [========================] 736/736 (0:00:09 / 0:00:00) 
2026-09-13T21:27:53.456+03:00  INFO 43810 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-08-26 14:06:31; изменённых модулей: 8
Documents/ЗаказПокупателя/ObjectModule.bsl: EventHandlerOutsideEventRegion +1 (было 5, стало 6)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    80: Метод "ПриКопировании" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    85: Метод "ПередЗаписью" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
Documents/ЗаказПокупателя/ObjectModule.bsl: SetPrivilegedMode +1 (было 0, стало 1)
    848: Проверьте установку привилегированного режима
Documents/ТехнологическаяКарта/ObjectModule.bsl: SetPrivilegedMode +1 (было 0, стало 1)
    34: Проверьте установку привилегированного режима
Documents/ТехнологическаяКарта/ObjectModule.bsl: YoLetterUsage +2 (было 0, стало 2)
    88: В текстах модулях не допускается использовать букву "Ё".
    47: В текстах модулях не допускается использовать букву "Ё".
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.14.json
версия 2.0.15.14: ru=7, fr=7, en=7, es=7
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
 M src/cf/src/CommonModules/ТехнологическиеКарты/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаВыбора/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
 M src/cf/src/Documents/ТехнологическаяКарта/ObjectModule.bsl
?? .ai/plans/production-2mzl-e6.md
?? .ai/reports/production-2mzl-e6-final-check.md
?? .ai/reports/production-2mzl-e6.md
?? .ai/reviews/production-2mzl-e6/
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
+// BSLLS:CyclomaticComplexity-off - та же причина: ветка на сценарий.
+// BSLLS:CyclomaticComplexity-on
+				// BSLLS:DeprecatedMethodCall-off
+				// BSLLS:DeprecatedMethodCall-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.15.13 → 2.0.15.14

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
