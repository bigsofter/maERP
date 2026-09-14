# Final check — production-2mzl-e11-demo
_20260914T164659Z_


## Scope

```
.ai/plans/production-2mzl-e11-demo.md
.ai/reports/production-2mzl-e11-demo-final-check.md
.ai/reviews/production-2mzl-e11-demo/01-architecture-critic.md
.ai/reviews/production-2mzl-e11-demo/02-plan-review-astra.md
.ai/reviews/production-2mzl-e11-demo/02b-plan-review-verify-astra.md
.ai/reviews/production-2mzl-e11-demo/03-code-review.md
.ai/reviews/production-2mzl-e11-demo/04-database-review-claude.md
.ai/reviews/production-2mzl-e11-demo/04-database-review.md
docs/plans/production-2mzl-e11-demo.md
docs/plans/production-2mzl-prompt.md
docs/plans/production-2mzl.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/fixtures.sh
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-14T19:47:08.485+03:00  INFO 59104 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/740 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/740 (0:00:01 / 0:01:21) Analyzing files...  15% [===                     ] 117/740 (0:00:02 / 0:00:10) Analyzing files...  34% [========                ] 255/740 (0:00:03 / 0:00:05) Analyzing files...  48% [===========             ] 362/740 (0:00:04 / 0:00:04) Analyzing files...  64% [===============         ] 480/740 (0:00:05 / 0:00:02) Analyzing files...  86% [====================    ] 643/740 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 740/740 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 740/740 (0:00:06 / 0:00:00) 
2026-09-14T19:47:18.358+03:00  INFO 59104 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-08-26 14:06:31; изменённых модулей: 3
DataProcessors/ТестыДокументов/ManagerModule.bsl: YoLetterUsage +1 (было 0, стало 1)
    2954: В текстах модулях не допускается использовать букву "Ё".
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.24.json
версия 2.0.15.24: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
A  .ai/plans/production-2mzl-e11-demo.md
A  .ai/reviews/production-2mzl-e11-demo/01-architecture-critic.md
A  .ai/reviews/production-2mzl-e11-demo/02-plan-review-astra.md
A  .ai/reviews/production-2mzl-e11-demo/02b-plan-review-verify-astra.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
A  docs/plans/production-2mzl-e11-demo.md
 M docs/plans/production-2mzl-prompt.md
 M docs/plans/production-2mzl.md
 M scripts/fixtures.sh
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
?? .ai/reports/production-2mzl-e11-demo-final-check.md
?? .ai/reviews/production-2mzl-e11-demo/03-code-review.md
?? .ai/reviews/production-2mzl-e11-demo/04-database-review-claude.md
?? .ai/reviews/production-2mzl-e11-demo/04-database-review.md
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
+	// BSLLS:MagicNumber-off - две секунды между документами контура (E9): автовыпуск датируется на секунду раньше реализации.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - 15 минут: около сотни документов по две секунды с запасом.
+	// BSLLS:MagicNumber-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-off - цены и нормы демо-набора (план .ai/plans/production-2mzl-e11-demo.md, §2).
+	// BSLLS:MagicNumber-on
+	// BSLLS:YoLetterUsage-off - имя реквизита в метаданных.
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-off - Table 6.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - остаток материалов на складе (план, §3).
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - Chaise 8.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - оплачена половина.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - Table 4.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - Planche 6, Tissu 3, Mousse 3 на изделие.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - Chaise 10, поступление половины.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - Table 2.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - Lampe 2, аванс за одну.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.15.23 → 2.0.15.24

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
