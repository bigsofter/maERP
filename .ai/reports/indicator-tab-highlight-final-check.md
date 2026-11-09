# Final check — indicator-tab-highlight
_20261018T092515Z_


## Scope

```
.ai/reports/indicator-tab-highlight-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reviews/indicator-tab-highlight/03-code-review.json
.ai/reviews/indicator-tab-highlight/03b-code-review-verify.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonModules/РаботаСДокументамиКлиент/Module.bsl
src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Configuration/ManagedApplicationModule.bsl
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-18T10:25:22.894+01:00  INFO 44886 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/818 (0:00:00 / ?) Analyzing files...   3% [                        ]  32/818 (0:00:01 / 0:00:24) Analyzing files...  19% [====                    ] 158/818 (0:00:02 / 0:00:08) Analyzing files...  38% [=========               ] 314/818 (0:00:03 / 0:00:04) Analyzing files...  54% [=============           ] 446/818 (0:00:04 / 0:00:03) Analyzing files...  62% [===============         ] 515/818 (0:00:05 / 0:00:02) Analyzing files...  88% [=====================   ] 723/818 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 818/818 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 818/818 (0:00:06 / 0:00:00) 
2026-10-18T10:25:31.913+01:00  INFO 44886 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 8
CommonModules/ПроизводственныеЗаказы/Module.bsl: SetPrivilegedMode +1 (было 4, стало 5)
    19: Проверьте установку привилегированного режима
    40: Проверьте установку привилегированного режима
    61: Проверьте установку привилегированного режима
```
**FAIL**
### уровень 0.5: scripts/refcheck.py
```
Сверка ссылок: расхождений нет (известных — 50)
```
**PASS**
### уровень 0.7: scripts/listcheck.py
```
Проверка динамических списков: расхождений нет (известных — 0)
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.94.json
версия 2.0.16.94: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
 M src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиКлиент/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/Configuration/ManagedApplicationModule.bsl
 M src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
?? .ai/reports/indicator-tab-highlight-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reviews/indicator-tab-highlight/
?? .ai/reviews/machine-form/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/wo-techdebt2/
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
+	// BSLLS:StyleElementConstructors-off - в элементе стиля заменяется только гарнитура, и только для кружков.
+	// BSLLS:StyleElementConstructors-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.93 → 2.0.16.94

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
