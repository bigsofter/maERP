# Final check — nomenclature-ui-s5
_20261010T184350Z_


## Scope

```
.ai/reports/nomenclature-ui-s5-final-check.md
.ai/reports/nomenclature-ui.md
.ai/reviews/nomenclature-ui-s5/03-code-review.json
.ai/reviews/nomenclature-ui-s5/03b-code-review-verify.json
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/formgen/nomenclature/card.py
scripts/formgen/nomenclature/choice.py
scripts/formgen/nomenclature/list.py
src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбораУпаковок/Attributes/Список/ExtInfo/ListSettings.dcss
src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаПодбора/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбораУпаковок/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбора/Module.bsl
src/cf/src/Catalogs/Номенклатура/Forms/ФормаПодбора/Module.bsl
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock1/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock1/Module.bsl
src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
src/cf/src/CommonModules/НавигаторНоменклатуры/НавигаторНоменклатуры.mdo
src/cf/src/CommonModules/НавигаторНоменклатуры/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-10T19:43:58.432+01:00  INFO 12992 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/805 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/805 (0:00:01 / 0:01:28) Analyzing files...  13% [===                     ] 110/805 (0:00:02 / 0:00:12) Analyzing files...  23% [=====                   ] 191/805 (0:00:03 / 0:00:09) Analyzing files...  42% [==========              ] 343/805 (0:00:04 / 0:00:05) Analyzing files...  68% [================        ] 549/805 (0:00:05 / 0:00:02) Analyzing files...  79% [===================     ] 643/805 (0:00:06 / 0:00:01) Analyzing files...  87% [=====================   ] 707/805 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 805/805 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 805/805 (0:00:07 / 0:00:00) 
2026-10-10T19:44:09.259+01:00  INFO 12992 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 8
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
Языков: 4, пунктов изменений: 8
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.64.json
версия 2.0.16.64: ru=2, fr=2, en=2, es=2
```
**PASS**

## Git hygiene

### git status
```
 M .ai/reports/nomenclature-ui.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M scripts/formgen/nomenclature/card.py
 A scripts/formgen/nomenclature/choice.py
 M scripts/formgen/nomenclature/list.py
D  src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock1/Form.form
D  src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock1/Module.bsl
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбора/Module.bsl
D  src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбораУпаковок/Attributes/Список/ExtInfo/ListSettings.dcss
D  src/cf/src/Catalogs/Номенклатура/Forms/ФормаВыбораУпаковок/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаПодбора/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаПодбора/Module.bsl
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
 M src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
 M src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
 A src/cf/src/CommonModules/НавигаторНоменклатуры/Module.bsl
 A src/cf/src/CommonModules/НавигаторНоменклатуры/НавигаторНоменклатуры.mdo
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
?? .ai/reports/nomenclature-ui-s5-final-check.md
?? .ai/reviews/nomenclature-ui-s5/
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
+	// BSLLS:MagicNumber-off - пятая доля секунды: листание узлов стрелками не дёргает сервер на каждый узел.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - пятая доля секунды: листание узлов стрелками не дёргает сервер на каждый узел.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - проценты.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - проценты.
+	// BSLLS:MagicNumber-on
+	// BSLLS:LogicalOrInTheWhereSectionOfQuery-off
+	// BSLLS:JoinWithSubQuery-off
+	// BSLLS:JoinWithSubQuery-on
+	// BSLLS:LogicalOrInTheWhereSectionOfQuery-on
+			// BSLLS:GetFormMethod-off
+			// BSLLS:GetFormMethod-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.63 → 2.0.16.64

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
