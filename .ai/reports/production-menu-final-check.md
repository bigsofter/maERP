# Final check — production-menu
_20260917T164748Z_


## Scope

```
.ai/reports/production-menu-final-check.md
.ai/reviews/production-menu/02-plan-review-claude.md
docs/plans/production-menu.md
docs/ROADMAP.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
src/cf/src/Documents/ВыпускПродукции/Commands/ВыпускПродукции/CommandModule.bsl
src/cf/src/Reports/СебестоимостьПродукции/СебестоимостьПродукции.mdo
src/cf/src/Reports/СебестоимостьПродукции/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Subsystems/Производство/Производство.mdo
src/cf/src/Subsystems/Производство/CommandInterface.cmi
src/cf/src/Subsystems/Производство/Subsystems/Нормативы/Нормативы.mdo
src/cf/src/Subsystems/Производство/Subsystems/Переработка/Переработка.mdo
src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
src/cf/src/Subsystems/Производство/Subsystems/Переработка/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-17T17:47:57.021+01:00  INFO 98530 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/740 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/740 (0:00:01 / 0:01:21) Analyzing files...   3% [                        ]  26/740 (0:00:02 / 0:00:55) Analyzing files...  18% [====                    ] 137/740 (0:00:03 / 0:00:13) Analyzing files...  27% [======                  ] 205/740 (0:00:04 / 0:00:10) Analyzing files...  43% [==========              ] 323/740 (0:00:05 / 0:00:06) Analyzing files...  60% [==============          ] 451/740 (0:00:06 / 0:00:03) Analyzing files...  74% [=================       ] 551/740 (0:00:07 / 0:00:02) Analyzing files...  83% [====================    ] 618/740 (0:00:08 / 0:00:01) Analyzing files... 100% [========================] 740/740 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 740/740 (0:00:08 / 0:00:00) 
2026-09-17T17:48:10.816+01:00  INFO 98530 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-08-26 14:06:31; изменённых модулей: 2
DataProcessors/ТестыДокументов/ManagerModule.bsl: DuplicateStringLiteral +1 (было 0, стало 1)
    4291: Необходимо избавиться от многократного использования строкового литерала "Заказ"
DataProcessors/ТестыДокументов/ManagerModule.bsl: NestedFunctionInParameters +1 (было 0, стало 1)
    4370: Уберите инициализацию параметров метода "Проверить" вложенными методами
DataProcessors/ТестыДокументов/ManagerModule.bsl: YoLetterUsage +1 (было 0, стало 1)
    2994: В текстах модулях не допускается использовать букву "Ё".
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
Языков: 4, пунктов изменений: 20
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.36.json
версия 2.0.15.36: ru=5, fr=5, en=5, es=5
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
D  src/cf/src/Documents/ВыпускПродукции/Commands/ВыпускПродукции/CommandModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Subsystems/Производство/CommandInterface.cmi
RM src/cf/src/Subsystems/Производство/Subsystems/Справочники/CommandInterface.cmi -> src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
RM src/cf/src/Subsystems/Производство/Subsystems/Справочники/Справочники.mdo -> src/cf/src/Subsystems/Производство/Subsystems/Нормативы/Нормативы.mdo
RM src/cf/src/Subsystems/Производство/Subsystems/ПроизводственныеОперации/CommandInterface.cmi -> src/cf/src/Subsystems/Производство/Subsystems/Переработка/CommandInterface.cmi
RM src/cf/src/Subsystems/Производство/Subsystems/ПроизводственныеОперации/ПроизводственныеОперации.mdo -> src/cf/src/Subsystems/Производство/Subsystems/Переработка/Переработка.mdo
 M src/cf/src/Subsystems/Производство/Производство.mdo
?? .ai/reports/production-menu-final-check.md
?? .ai/reviews/production-menu/
?? docs/plans/production-menu.md
?? src/cf/src/Reports/СебестоимостьПродукции/
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
+	// BSLLS:MagicNumber-off - сырьё 10 по 12 со ставкой 20%: приход продукции 120, в нём НДС 20, продукции 5 штук.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.15.35 → 2.0.15.36

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
