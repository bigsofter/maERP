# Final check — old-item-properties
_20261010T221301Z_


## Scope

```
.ai/reports/nomenclature-ui.md
.ai/reports/old-item-properties-final-check.md
.ai/reviews/old-item-properties/02-plan-review.json
.ai/reviews/old-item-properties/03-code-review.json
.ai/reviews/old-item-properties/03b-code-review-verify.json
.ai/reviews/old-item-properties/04-database-review.json
docs/plans/old-item-properties.md
docs/RELEASING.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-10T23:13:09.245+01:00  INFO 42723 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/805 (0:00:00 / ?) Analyzing files...   4% [=                       ]  34/805 (0:00:01 / 0:00:22) Analyzing files...  20% [====                    ] 161/805 (0:00:02 / 0:00:08) Analyzing files...  42% [==========              ] 341/805 (0:00:03 / 0:00:04) Analyzing files...  64% [===============         ] 516/805 (0:00:04 / 0:00:02) Analyzing files...  85% [====================    ] 690/805 (0:00:05 / 0:00:00) Analyzing files...  99% [======================= ] 804/805 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 805/805 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 805/805 (0:00:06 / 0:00:00) 
2026-10-10T23:13:18.508+01:00  INFO 42723 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 2
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
Языков: 4, пунктов изменений: 4
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.66.json
версия 2.0.16.66: ru=1, fr=1, en=1, es=1
```
**PASS**

## Git hygiene

### git status
```
 M .ai/reports/nomenclature-ui.md
 M docs/RELEASING.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
?? .ai/reports/old-item-properties-final-check.md
?? .ai/reviews/old-item-properties/
?? docs/plans/old-item-properties.md
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
+	// BSLLS:MagicNumber-off - размер порции.
+	// BSLLS:MagicNumber-on
+		// BSLLS:DeprecatedMethodCall-off
+		// BSLLS:DeprecatedMethodCall-on
+	// BSLLS:MagicNumber-off - квалификаторы типа плана видов характеристик ДополнительныеРеквизиты.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:UsingHardcodeNetworkAddress-off - номер версии конфигурации, а не адрес.
+	// BSLLS:UsingHardcodeNetworkAddress-on
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.65 → 2.0.16.66

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
