# Final check — kp-print-revisions
_20261010T113757Z_


## Scope

```
.ai/reports/kp-print-revisions-final-check.md
.ai/reviews/kp-print-revisions/02-plan-review.json
.ai/reviews/kp-print-revisions/03-code-review.json
.ai/reviews/kp-print-revisions/03b-code-review-verify.json
.ai/reviews/kp-print-revisions/04-database-review.json
.ai/reviews/kp-print-revisions/05-security-review.json
.ai/reviews/machines-analytics/02-plan-review.json
.ai/reviews/machines-analytics/02b-plan-review-round2.json
.ai/reviews/machines-analytics/02c-plan-review-round3.json
.ai/reviews/machines-analytics/02d-plan-review-round4.json
.ai/reviews/machines-analytics/02e-plan-review-round5.json
.ai/reviews/machines-analytics/02f-plan-review-round6.json
.ai/reviews/machines-analytics/02g-plan-review-round7.json
.ai/reviews/machines-analytics/02h-plan-review-round8.json
docs/plans/kp-print-revisions.md
docs/plans/machines-analytics.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/mxlxgen/kp_quotation.py
src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
src/cf/src/Documents/КоммерческоеПредложение/Commands/ПечатьКоммерческоеПредложение/CommandModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаРедакции/Form.form
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаРедакции/Module.bsl
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/ObjectModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/Templates/КоммерческоеПредложение/Template.mxlx
src/cf/src/InformationRegisters/РедакцииКоммерческихПредложений/РедакцииКоммерческихПредложений.mdo
src/cf/src/InformationRegisters/РедакцииКоммерческихПредложений/RecordSetModule.bsl
src/cf/src/Roles/Оператор/Rights.rights
src/cf/src/Roles/Руководитель/Rights.rights
src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-10T12:38:05.260+01:00  INFO 28132 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/803 (0:00:00 / ?) Analyzing files...   1% [                        ]  13/803 (0:00:01 / 0:01:01) Analyzing files...  14% [===                     ] 120/803 (0:00:02 / 0:00:11) Analyzing files...  29% [======                  ] 234/803 (0:00:03 / 0:00:07) Analyzing files...  54% [=============           ] 437/803 (0:00:04 / 0:00:03) Analyzing files...  80% [===================     ] 644/803 (0:00:05 / 0:00:01) Analyzing files...  99% [======================= ] 801/803 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 803/803 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 803/803 (0:00:06 / 0:00:00) 
2026-10-10T12:38:14.129+01:00  INFO 28132 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 9
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.51.json
версия 2.0.16.51: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/ObjectModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Roles/Руководитель/Rights.rights
?? .ai/reports/kp-print-revisions-final-check.md
?? .ai/reviews/kp-print-revisions/
?? .ai/reviews/machines-analytics/
?? docs/plans/kp-print-revisions.md
?? docs/plans/machines-analytics.md
?? scripts/mxlxgen/
?? src/cf/src/Documents/КоммерческоеПредложение/Commands/
?? src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаРедакции/
?? src/cf/src/Documents/КоммерческоеПредложение/Templates/
?? src/cf/src/InformationRegisters/РедакцииКоммерческихПредложений/
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
+// BSLLS:DataExchangeLoading-off - редакции удаляются и при загрузке обмена: иначе удаление документа упрётся в защиту архива
+// BSLLS:DataExchangeLoading-on
+		// BSLLS:SetPrivilegedMode-off - пишется только снимок этого документа, сформированный в ПередЗаписью; права на
+		// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off - удаляются только редакции этого документа, флаг ЗаписьРедакцииКП - как при записи.
+	// BSLLS:SetPrivilegedMode-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.49 → 2.0.16.51

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
