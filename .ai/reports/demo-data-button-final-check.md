# Final check — demo-data-button
_20261009T205613Z_


## Scope

```
.ai/reports/demo-data-button-final-check.md
.ai/reports/demo-data-button.md
.ai/reviews/demo-data-button/02-plan-review.json
.ai/reviews/demo-data-button/03-code-review.json
.ai/reviews/demo-data-button/03b-code-review-verify.json
.ai/reviews/demo-data-button/04-database-review.json
.ai/reviews/demo-data-button/05-security-review.json
docs/plans/demo-data-button.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/fixtures.sh
src/cf/src/CommonModules/ПроцедурыРегламентныхЗаданий/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Form.form
src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Module.bsl
src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-09T21:56:21.821+01:00  INFO 57870 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/797 (0:00:00 / ?) Analyzing files...   2% [                        ]  18/797 (0:00:01 / 0:00:43) Analyzing files...  16% [===                     ] 132/797 (0:00:02 / 0:00:10) Analyzing files...  35% [========                ] 279/797 (0:00:03 / 0:00:05) Analyzing files...  55% [=============           ] 442/797 (0:00:04 / 0:00:03) Analyzing files...  77% [==================      ] 619/797 (0:00:05 / 0:00:01) Analyzing files...  99% [======================= ] 790/797 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 797/797 (0:00:06 / 0:00:00) 
2026-10-09T21:56:31.558+01:00  INFO 57870 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 5
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
Языков: 4, пунктов изменений: 16
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.47.json
версия 2.0.16.47: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M scripts/fixtures.sh
 M src/cf/src/CommonModules/ПроцедурыРегламентныхЗаданий/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Form.form
 M src/cf/src/DataProcessors/НастройкиПрограммы/Forms/КомпанияИУчёт/Module.bsl
 M src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
?? .ai/reports/demo-data-button-final-check.md
?? .ai/reports/demo-data-button.md
?? .ai/reviews/demo-data-button/
?? docs/plans/demo-data-button.md
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
+		// BSLLS:DeprecatedMethodCall-off
+		// BSLLS:DeprecatedMethodCall-on
+		// BSLLS:DeprecatedMethodCall-off
+		// BSLLS:DeprecatedMethodCall-on
+	// BSLLS:DeprecatedMethodCall-off
+	// BSLLS:DeprecatedMethodCall-on
+// BSLLS:CognitiveComplexity-off - линейная таблица описаний: ветка на кейс.
+// BSLLS:CyclomaticComplexity-off - та же причина.
+// BSLLS:MagicNumber-off - число документов кейса.
+// BSLLS:MagicNumber-on
+// BSLLS:CyclomaticComplexity-on
+// BSLLS:CognitiveComplexity-on
+// BSLLS:CognitiveComplexity-off - линейная таблица описаний: ветка на кейс.
+// BSLLS:CyclomaticComplexity-off - та же причина.
+// BSLLS:MagicNumber-off - число документов кейса.
+// BSLLS:MagicNumber-on
+// BSLLS:CyclomaticComplexity-on
+// BSLLS:CognitiveComplexity-on
+	// BSLLS:QueryParseError-off - шаблон с подстановкой таблицы и поля.
+	// BSLLS:QueryParseError-on
+	// BSLLS:MagicNumber-off - две секунды между документами контура (E9): автовыпуск датируется на секунду раньше реализации.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - 15 минут: около сотни документов по две секунды с запасом.
+	// BSLLS:MagicNumber-on
+		// BSLLS:YoLetterUsage-off
+		// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-off - цены и нормы демо-набора (план .ai/plans/production-2mzl-e11-demo.md, §2).
+	// BSLLS:MagicNumber-on
+	// BSLLS:QueryParseError-off - текст собирается из имени справочника и полей отбора.
+	// BSLLS:QueryParseError-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.46 → 2.0.16.47

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
