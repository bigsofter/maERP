# Final check — arm-purchasing
_20261007T154511Z_


## Scope

```
.ai/reports/arm-purchasing-final-check.md
.ai/reviews/arm-purchasing/02-plan-review.json
.ai/reviews/arm-purchasing/02b-plan-review-round2.json
.ai/reviews/arm-purchasing/02c-plan-review-round3.json
.ai/reviews/arm-purchasing/03-plan-review-claude.md
.ai/reviews/arm-purchasing/04-code-review-claude.md
.ai/reviews/arm-purchasing/05-database-security-claude.md
docs/plans/arm-purchasing.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/formgen/zakupki/gen.py
scripts/formgen/zakupki/README.md
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМЗакупки/АРМЗакупки.mdo
src/cf/src/DataProcessors/АРМЗакупки/Commands/АРМЗакупки/CommandModule.bsl
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаДокумента/Module.bsl
src/cf/src/Enums/СтатусыЗаказовПоставщику/СтатусыЗаказовПоставщику.mdo
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Subsystems/Закупки/Закупки.mdo
src/cf/src/Subsystems/Закупки/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-07T16:45:19.420+01:00  INFO 21704 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/766 (0:00:00 / ?) Analyzing files...   9% [==                      ]  73/766 (0:00:01 / 0:00:09) Analyzing files...  25% [======                  ] 193/766 (0:00:02 / 0:00:05) Analyzing files...  46% [===========             ] 354/766 (0:00:03 / 0:00:03) Analyzing files...  69% [================        ] 532/766 (0:00:04 / 0:00:01) Analyzing files...  87% [====================    ] 668/766 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 766/766 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 766/766 (0:00:05 / 0:00:00) 
2026-10-07T16:45:27.439+01:00  INFO 21704 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.28.json
версия 2.0.16.28: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Subsystems/Закупки/CommandInterface.cmi
 M src/cf/src/Subsystems/Закупки/Закупки.mdo
?? .ai/reports/arm-purchasing-final-check.md
?? .ai/reviews/arm-purchasing/
?? docs/plans/arm-purchasing.md
?? scripts/formgen/zakupki/
?? src/cf/src/DataProcessors/АРМЗакупки/
?? src/cf/src/Enums/СтатусыЗаказовПоставщику/
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
+	// BSLLS:MagicNumber-off - количества и суммы сценария: заказы по 10, поступления 4 и 6, возврат 1, перенос 3.
+	// BSLLS:MagicNumber-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-off - страница с запасом на все заказы сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - заказ 4 единицы, оплата накладной половиной суммы.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - перенос 3 единиц.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - пять непредварительных заказов сценария по два на странице: три страницы.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - заказано 10, пришло 10 - 1 возврат.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.27 → 2.0.16.28

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
