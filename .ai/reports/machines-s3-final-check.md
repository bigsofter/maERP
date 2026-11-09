# Final check — machines-s3
_20261008T182836Z_


## Scope

```
.ai/reports/machines-s3-final-check.md
.ai/reviews/machines-s3/02-plan-review.json
.ai/reviews/machines-s3/03-code-review.json
.ai/reviews/machines-s3/03b-code-review-verify.json
docs/plans/machines.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-08T19:28:43.923+01:00  INFO 51298 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/782 (0:00:00 / ?) Analyzing files...   3% [                        ]  27/782 (0:00:01 / 0:00:28) Analyzing files...  18% [====                    ] 144/782 (0:00:02 / 0:00:08) Analyzing files...  33% [========                ] 264/782 (0:00:03 / 0:00:05) Analyzing files...  60% [==============          ] 473/782 (0:00:04 / 0:00:02) Analyzing files...  75% [==================      ] 593/782 (0:00:05 / 0:00:01) Analyzing files...  92% [======================  ] 722/782 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 782/782 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 782/782 (0:00:06 / 0:00:00) 
2026-10-08T19:28:54.194+01:00  INFO 51298 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 3
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.34.json
версия 2.0.16.34: ru=5, fr=5, en=5, es=5
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/machines.md
 M src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
?? .ai/reports/machines-s3-final-check.md
?? .ai/reviews/machines-s3/
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
+	// BSLLS:MagicNumber-off - заказ 10 продукции x 2 сырья по 6 кг; станки 120 кг/ч, 15 мин на смену заказа, 8-20.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.33 → 2.0.16.34

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
