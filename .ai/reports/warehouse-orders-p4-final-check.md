# Final check — warehouse-orders-p4
_20261015T075358Z_


## Scope

```
.ai/reports/warehouse-orders-p4-final-check.md
.ai/reviews/warehouse-orders-p4/03-code-review.json
.ai/reviews/warehouse-orders-p4/03b-code-review-verify.json
.ai/reviews/warehouse-orders-p4/04-database-review-r1.json
.ai/reviews/warehouse-orders-p4/04-database-review.json
.ai/reviews/warehouse-orders-p4/05-security-review.json
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/formgen/warehouse-orders/gen_report.py
scripts/formgen/warehouse-orders/queue.py
src/cf/src/CommonModules/ОрдераСклада/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Module.bsl
src/cf/src/Reports/ОстаткиНаСкладах/ОстаткиНаСкладах.mdo
src/cf/src/Reports/ОстаткиНаСкладах/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Логист/Rights.rights
src/cf/src/Roles/Оператор/Rights.rights
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Subsystems/Склад/Склад.mdo
src/cf/src/Subsystems/Закупки/Закупки.mdo
src/cf/src/Subsystems/Склад/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/CommandInterface.cmi
src/cf/src/Subsystems/Продажи/Subsystems/Опт/Опт.mdo
src/cf/src/Subsystems/Продажи/Subsystems/Опт/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-15T08:54:05.660+01:00  INFO 84312 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/817 (0:00:00 / ?) Analyzing files...   5% [=                       ]  41/817 (0:00:01 / 0:00:19) Analyzing files...  25% [======                  ] 207/817 (0:00:02 / 0:00:05) Analyzing files...  47% [===========             ] 385/817 (0:00:03 / 0:00:03) Analyzing files...  63% [===============         ] 520/817 (0:00:04 / 0:00:02) Analyzing files...  82% [===================     ] 672/817 (0:00:05 / 0:00:01) Analyzing files...  99% [======================= ] 809/817 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:06 / 0:00:00) 
2026-10-15T08:54:14.803+01:00  INFO 84312 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.79.json
версия 2.0.16.79: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/CommonModules/ОрдераСклада/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РасходныйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РасходныйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Subsystems/Закупки/CommandInterface.cmi
 M src/cf/src/Subsystems/Закупки/Закупки.mdo
 M src/cf/src/Subsystems/Продажи/CommandInterface.cmi
 M src/cf/src/Subsystems/Продажи/Subsystems/Опт/CommandInterface.cmi
 M src/cf/src/Subsystems/Продажи/Subsystems/Опт/Опт.mdo
 M src/cf/src/Subsystems/Продажи/Продажи.mdo
 M src/cf/src/Subsystems/Склад/CommandInterface.cmi
 M src/cf/src/Subsystems/Склад/Склад.mdo
?? .ai/reports/warehouse-orders-p4-final-check.md
?? .ai/reviews/warehouse-orders-p4/
?? scripts/formgen/warehouse-orders/gen_report.py
?? scripts/formgen/warehouse-orders/queue.py
?? src/cf/src/Reports/ОстаткиНаСкладах/
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
2.0.16.78 → 2.0.16.79

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
