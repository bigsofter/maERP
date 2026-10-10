# Final check — nomenclature-ui-s1
_20261010T173315Z_


## Scope

```
.ai/reports/nomenclature-ui-s1-final-check.md
.ai/reports/nomenclature-ui.md
.ai/reviews/nomenclature-ui-s1/03-code-review.json
.ai/reviews/nomenclature-ui-s1/03b-code-review-verify.json
docs/FORMS-STYLE.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/formgen/nomenclature/list.py
scripts/formgen/nomenclature/README.md
src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Module.bsl
src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-10T18:33:22.352+01:00  INFO 13289 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/805 (0:00:00 / ?) Analyzing files...   8% [=                       ]  67/805 (0:00:01 / 0:00:11) Analyzing files...  27% [======                  ] 221/805 (0:00:02 / 0:00:05) Analyzing files...  51% [============            ] 412/805 (0:00:03 / 0:00:02) Analyzing files...  73% [=================       ] 592/805 (0:00:04 / 0:00:01) Analyzing files...  93% [======================  ] 755/805 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 805/805 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 805/805 (0:00:05 / 0:00:00) 
2026-10-10T18:33:30.538+01:00  INFO 13289 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.60.json
версия 2.0.16.60: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M .ai/reports/nomenclature-ui.md
 M docs/FORMS-STYLE.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 A scripts/formgen/nomenclature/README.md
 A scripts/formgen/nomenclature/list.py
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
?? .ai/reports/nomenclature-ui-s1-final-check.md
?? .ai/reviews/nomenclature-ui-s1/
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
+	// BSLLS:MagicNumber-off - треть секунды, константа имени не добавит.
+	// BSLLS:MagicNumber-on
+	// BSLLS:IsInRoleMethod-off
+	// BSLLS:IsInRoleMethod-on
+	// BSLLS:LogicalOrInTheWhereSectionOfQuery-off
+	// BSLLS:JoinWithVirtualTable-off
+	// BSLLS:JoinWithSubQuery-off
+	// BSLLS:JoinWithSubQuery-on
+	// BSLLS:JoinWithVirtualTable-on
+	// BSLLS:LogicalOrInTheWhereSectionOfQuery-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
+	// BSLLS:JoinWithVirtualTable-off
+	// BSLLS:JoinWithVirtualTable-on
+		// BSLLS:MagicNumber-off - двенадцать месяцев.
+		// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.59 → 2.0.16.60

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
