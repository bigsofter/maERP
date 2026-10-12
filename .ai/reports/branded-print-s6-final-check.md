# Final check — branded-print-s6
_20261012T001618Z_


## Scope

```
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗаказПоставщику-en-00000000008-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-en-00000000008-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-en-00000000008-2.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-en-00000000008-3.png
.ai/reports/branded-print-phase6/ПредложениеПоставщика-ЗапросЦен-en-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗаказПоставщику-es-00000000008-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-es-00000000008-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-es-00000000008-2.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-es-00000000008-3.png
.ai/reports/branded-print-phase6/ПредложениеПоставщика-ЗапросЦен-es-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗаказПоставщику-fr-00000000008-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-fr-00000000008-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-fr-00000000008-2.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-fr-00000000008-3.png
.ai/reports/branded-print-phase6/ПредложениеПоставщика-ЗапросЦен-fr-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗаказПоставщику-ru-00000000008-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-ru-00000000008-1.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-ru-00000000008-2.png
.ai/reports/branded-print-phase6/ЗаказПоставщику-ЗапросКотировокСФото-ru-00000000008-3.png
.ai/reports/branded-print-phase6/ПредложениеПоставщика-ЗапросЦен-ru-1.png
.ai/reports/branded-print-phase6/РасходныйКассовыйОрдер-LettreDePaiement-en-1.png
.ai/reports/branded-print-phase6/РасходныйКассовыйОрдер-LettreDePaiement-es-1.png
.ai/reports/branded-print-phase6/РасходныйКассовыйОрдер-LettreDePaiement-fr-1.png
.ai/reports/branded-print-phase6/РасходныйКассовыйОрдер-LettreDePaiement-ru-1.png
.ai/reports/branded-print-phase6/old/ЗаказПоставщику-ЗаказПоставщику-fr-1.png
.ai/reports/branded-print-phase6/old/ЗаказПоставщику-ЗапросКотировокСФото-fr-1.png
.ai/reports/branded-print-phase6/old/РасходныйКассовыйОрдер-LettreDePaiement-fr-1.png
.ai/reports/branded-print-s6-final-check.md
.ai/reviews/branded-print-s6/02-plan-review.json
.ai/reviews/branded-print-s6/03-code-review.json
.ai/reviews/branded-print-s6/03b-code-review-verify.json
.ai/reviews/branded-print-s6/04-database-review.json
.ai/reviews/branded-print-s6/05-security-review.json
docs/plans/branded-print.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/mxlxgen/branded.py
src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonTemplates/ФирменныйДокумент/Template.mxlx
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ЗаказПоставщику/ManagerModule.bsl
src/cf/src/Documents/ПредложениеПоставщика/ManagerModule.bsl
src/cf/src/Documents/РасходныйКассовыйОрдер/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-12T01:16:25.563+01:00  INFO 97864 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/803 (0:00:00 / ?) Analyzing files...   3% [                        ]  29/803 (0:00:01 / 0:00:26) Analyzing files...  20% [====                    ] 161/803 (0:00:02 / 0:00:08) Analyzing files...  38% [=========               ] 307/803 (0:00:03 / 0:00:04) Analyzing files...  57% [=============           ] 464/803 (0:00:04 / 0:00:02) Analyzing files...  78% [==================      ] 634/803 (0:00:05 / 0:00:01) Analyzing files... 100% [========================] 803/803 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 803/803 (0:00:05 / 0:00:00) 
2026-10-12T01:16:33.634+01:00  INFO 97864 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 6
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
Языков: 4, пунктов изменений: 32
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.74.json
версия 2.0.16.74: ru=8, fr=8, en=8, es=8
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/branded-print.md
 M scripts/mxlxgen/branded.py
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/CommonTemplates/ФирменныйДокумент/Template.mxlx
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПоставщику/ManagerModule.bsl
 M src/cf/src/Documents/ПредложениеПоставщика/ManagerModule.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/ManagerModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
?? .ai/reports/branded-print-phase6/
?? .ai/reports/branded-print-s6-final-check.md
?? .ai/reviews/branded-print-s6/
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
+	// BSLLS:YoLetterUsage-off - имя регистра в метаданных.
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-off - количества и цены строк.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количество и цена строки.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - суммы ордера и оснований.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.73 → 2.0.16.74

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
