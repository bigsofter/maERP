# Final check — branded-print-s3
_20261011T172135Z_


## Scope

```
.ai/bin/ai-lib.sh
.ai/README.md
.ai/reports/branded-print-phase3/facture-letterhead-tax-en-nologo.png
.ai/reports/branded-print-phase3/facture-purchase-fr.png
.ai/reports/branded-print-phase3/facture-sale-en-nologo-p1.png
.ai/reports/branded-print-phase3/facture-sale-es-p1.png
.ai/reports/branded-print-phase3/facture-sale-fr-logo-p1.png
.ai/reports/branded-print-phase3/facture-sale-fr-logo-p2.png
.ai/reports/branded-print-phase3/facture-sale-ru-nologo-p2.png
.ai/reports/branded-print-phase3/facture-services-fr-nologo.png
.ai/reports/branded-print-phase3/facture-tax-fr-nologo.png
.ai/reports/branded-print-phase3/old/НалоговаяНакладная-Счёт-fr-1.png
.ai/reports/branded-print-phase3/old/ЗаказПокупателя-Проформа-fr-1.png
.ai/reports/branded-print-phase3/old/РеализацияТоваровУслуг-Счёт-fr-1.png
.ai/reports/branded-print-phase3/old/НалоговаяНакладная-Facture-fr-1.png
.ai/reports/branded-print-phase3/old/РеализацияТоваровУслуг-Facture-fr-1.png
.ai/reports/branded-print-phase3/old/НалоговаяНакладная-FactureСФоном-fr-1.png
.ai/reports/branded-print-phase3/old/НалоговаяНакладнаяПокупка-Facture-fr-1.png
.ai/reports/branded-print-phase3/old/РеализацияТоваровУслуг-Facture-ru-1.png
.ai/reports/branded-print-phase3/proforma-order-fr-nologo.png
.ai/reports/branded-print-phase3/proforma-sale-fr-nologo.png
.ai/reports/branded-print-phase3/proforma-tax-es-nologo.png
.ai/reports/branded-print-s3-final-check.md
.ai/reports/branded-print.md
.ai/reviews/branded-print-s3/02-plan-review.json
.ai/reviews/branded-print-s3/03-code-review.json
.ai/reviews/branded-print-s3/03b-code-review-verify.json
.ai/reviews/branded-print-s3/04-database-review.json
docs/plans/branded-print.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/cf-dump.sh
scripts/mxlxgen/branded.py
src/cf/src/Catalogs/Валюты/ManagerModule.bsl
src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonTemplates/ФирменныйДокумент/Template.mxlx
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
src/cf/src/Documents/НалоговаяНакладная/ManagerModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
src/cf/src/Documents/НалоговаяНакладнаяПокупка/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-11T18:21:43.623+01:00  INFO 12966 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                        ]   1/802 (0:00:00 / 0:00:01) Analyzing files...   5% [=                       ]  47/802 (0:00:01 / 0:00:16) Analyzing files...  22% [=====                   ] 184/802 (0:00:02 / 0:00:06) Analyzing files...  40% [=========               ] 324/802 (0:00:03 / 0:00:04) Analyzing files...  56% [=============           ] 451/802 (0:00:04 / 0:00:03) Analyzing files...  63% [===============         ] 512/802 (0:00:05 / 0:00:02) Analyzing files...  84% [====================    ] 674/802 (0:00:06 / 0:00:01) Analyzing files... 100% [========================] 802/802 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 802/802 (0:00:06 / 0:00:00) 
2026-10-11T18:21:53.012+01:00  INFO 12966 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 10
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
Языков: 4, пунктов изменений: 20
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.70.json
версия 2.0.16.70: ru=5, fr=5, en=5, es=5
```
**PASS**

## Git hygiene

### git status
```
 M .ai/README.md
 M .ai/bin/ai-lib.sh
 M .ai/reports/branded-print.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/branded-print.md
 M scripts/cf-dump.sh
 M scripts/mxlxgen/branded.py
 M src/cf/src/Catalogs/Валюты/ManagerModule.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
 M src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/CommonTemplates/ФирменныйДокумент/Template.mxlx
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
 M src/cf/src/Documents/НалоговаяНакладная/ManagerModule.bsl
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/ManagerModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
?? .ai/reports/branded-print-phase3/
?? .ai/reports/branded-print-s3-final-check.md
?? .ai/reviews/branded-print-s3/
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
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-off - сумма из предпросмотра фазы 2, печаталась «279.000».
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - ставка НДС сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества, цены, скидка и НДС строк сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - цена с НДС 120, без НДС 100.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - цена 120 с НДС 20 - без НДС 100.
+	// BSLLS:MagicNumber-on
+// BSLLS:MethodSize-off
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.69 → 2.0.16.70

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
