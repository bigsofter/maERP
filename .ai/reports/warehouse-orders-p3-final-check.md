# Final check — warehouse-orders-p3
_20261015T013219Z_


## Scope

```
.ai/reports/warehouse-orders-p3-final-check.md
.ai/reviews/warehouse-orders-p3/03-code-review.json
.ai/reviews/warehouse-orders-p3/03b-code-review-verify.json
.ai/reviews/warehouse-orders-p3/04-database-review-r1.json
.ai/reviews/warehouse-orders-p3/04-database-review.json
.ai/reviews/warehouse-orders-p3/05-security-review.json
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/CommonModules/ОрдераСклада/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/РасходныйОрдер/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-15T02:32:25.834+01:00  INFO 87182 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/817 (0:00:00 / ?) Analyzing files...   3% [                        ]  31/817 (0:00:01 / 0:00:25) Analyzing files...  17% [====                    ] 140/817 (0:00:02 / 0:00:09) Analyzing files...  38% [=========               ] 313/817 (0:00:03 / 0:00:04) Analyzing files...  49% [===========             ] 405/817 (0:00:04 / 0:00:04) Analyzing files...  54% [=============           ] 449/817 (0:00:05 / 0:00:04) Analyzing files...  61% [==============          ] 501/817 (0:00:06 / 0:00:03) Analyzing files...  64% [===============         ] 529/817 (0:00:07 / 0:00:03) Analyzing files...  72% [=================       ] 593/817 (0:00:08 / 0:00:03) Analyzing files...  87% [=====================   ] 718/817 (0:00:09 / 0:00:01) Analyzing files...  96% [======================= ] 789/817 (0:00:10 / 0:00:00) Analyzing files...  99% [======================= ] 813/817 (0:00:11 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:11 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:11 / 0:00:00) 
2026-10-15T02:32:39.850+01:00  INFO 87182 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Сверка ссылок: расхождений нет (известных — 50)
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.78.json
версия 2.0.16.78: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/CommonModules/ОрдераСклада/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/РасходныйОрдер/ManagerModule.bsl
?? .ai/reports/warehouse-orders-p3-final-check.md
?? .ai/reviews/warehouse-orders-p3/
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
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.77 → 2.0.16.78

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
