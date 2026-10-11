# Final check — branded-print
_20261011T114828Z_


## Scope

```
.ai/reports/branded-print-final-check.md
.ai/reports/branded-print-phase1/kp-en-after.png
.ai/reports/branded-print-phase1/kp-en-before.png
.ai/reports/branded-print-phase1/kp-fr-v2-p1.png
.ai/reports/branded-print.md
.ai/reviews/branded-print/03-code-review.json
.ai/reviews/branded-print/03b-code-review-verify.json
.ai/reviews/branded-print/05-security-review.json
docs/plans/branded-print.md
docs/ROADMAP.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/mxlxgen/branded.py
scripts/print-preview.sh
scripts/print-preview/build_epf.py
scripts/print-preview/print.bsl
src/cf/src/CommonModules/ФирменнаяПечать/ФирменнаяПечать.mdo
src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonTemplates/ФирменныйДокумент/ФирменныйДокумент.mdo
src/cf/src/CommonTemplates/ФирменныйДокумент/Template.mxlx
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/Templates/КоммерческоеПредложение/Template.mxlx
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-11T12:48:37.699+01:00  INFO 42490 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/806 (0:00:00 / ?) Analyzing files...   6% [=                       ]  53/806 (0:00:01 / 0:00:14) Analyzing files...  23% [=====                   ] 191/806 (0:00:02 / 0:00:06) Analyzing files...  48% [===========             ] 390/806 (0:00:03 / 0:00:03) Analyzing files...  68% [================        ] 555/806 (0:00:04 / 0:00:01) Analyzing files...  88% [=====================   ] 710/806 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 806/806 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 806/806 (0:00:05 / 0:00:00) 
2026-10-11T12:48:46.191+01:00  INFO 42490 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 4
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.68.json
версия 2.0.16.68: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/branded-print.md
RM scripts/mxlxgen/kp_quotation.py -> scripts/mxlxgen/branded.py
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
D  src/cf/src/Documents/КоммерческоеПредложение/Templates/КоммерческоеПредложение/Template.mxlx
 M src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
?? .ai/reports/branded-print-final-check.md
?? .ai/reports/branded-print-phase1/
?? .ai/reports/branded-print.md
?? .ai/reviews/branded-print/03-code-review.json
?? .ai/reviews/branded-print/03b-code-review-verify.json
?? .ai/reviews/branded-print/05-security-review.json
?? scripts/print-preview.sh
?? scripts/print-preview/
?? src/cf/src/CommonModules/ФирменнаяПечать/
?? src/cf/src/CommonTemplates/ФирменныйДокумент/
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
none found

### Версия конфигурации
2.0.16.67 → 2.0.16.68

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
