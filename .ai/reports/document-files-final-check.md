# Final check — document-files
_20261110T203402Z_


## Scope

```
.ai/reports/document-files-final-check.md
.ai/reviews/document-files/02-plan-review.json
.ai/reviews/document-files/03-code-review.json
.ai/reviews/document-files/03b-code-review-verify.json
docs/plans/document-files.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
src/cf/src/CommonCommands/ФайлыДокумента/ФайлыДокумента.mdo
src/cf/src/CommonCommands/ФайлыДокумента/CommandModule.bsl
src/cf/src/CommonModules/ПраваНаФайлы/Module.bsl
src/cf/src/CommonModules/ПрисоединённыеФайлыВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/DefinedTypes/ВладельцыПрисоединенныхФайлов/ВладельцыПрисоединенныхФайлов.mdo
src/cf/src/InformationRegisters/ПрисоединённыеФайлы/Forms/ФормаСписка/Module.bsl
src/cf/src/Roles/Логист/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/Руководитель/Rights.rights
src/cf/src/Roles/ЛичныйКабинет/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-10T21:34:11.979+01:00  INFO 32250 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/860 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/860 (0:00:01 / 0:01:35) Analyzing files...  10% [==                      ]  90/860 (0:00:02 / 0:00:17) Analyzing files...  22% [=====                   ] 190/860 (0:00:03 / 0:00:10) Analyzing files...  31% [=======                 ] 272/860 (0:00:04 / 0:00:08) Analyzing files...  49% [===========             ] 423/860 (0:00:05 / 0:00:05) Analyzing files...  66% [===============         ] 572/860 (0:00:06 / 0:00:03) Analyzing files...  88% [=====================   ] 759/860 (0:00:07 / 0:00:00) Analyzing files...  97% [======================= ] 839/860 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 860/860 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 860/860 (0:00:08 / 0:00:00) 
2026-11-10T21:34:24.413+01:00  INFO 32250 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-11-10 19:03:41; изменённых модулей: 6
новых замечаний нет
```
**PASS**
### уровень 0.5: scripts/refcheck.py
```
Сверка ссылок: расхождений нет (известных — 48)
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
Описание изменений: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/changelog-2.0.17.9.json
версия 2.0.17.9: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
 M src/cf/src/CommonModules/ПраваНаФайлы/Module.bsl
 M src/cf/src/CommonModules/ПрисоединённыеФайлыВызовСервера/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/DefinedTypes/ВладельцыПрисоединенныхФайлов/ВладельцыПрисоединенныхФайлов.mdo
 M src/cf/src/InformationRegisters/ПрисоединённыеФайлы/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/ЛичныйКабинет/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Roles/Руководитель/Rights.rights
?? .ai/reports/document-files-final-check.md
?? .ai/reviews/document-files/
?? docs/plans/document-files.md
?? src/cf/src/CommonCommands/ФайлыДокумента/
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
+	// BSLLS:YoLetterUsage-off - имя регистра в метаданных.
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off - имя регистра в метаданных.
+	// BSLLS:YoLetterUsage-on
+// BSLLS:PrivilegedModuleMethodCall-off - вызовы служебных методов внутри самого привилегированного модуля.
+// BSLLS:YoLetterUsage-off - имена объектов метаданных ПрисоединённыеФайлы.
+	// BSLLS:YoLetterUsage-off - имя регистра в метаданных.
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off - имена регистра и модуля файлов в метаданных.
+	// BSLLS:PrivilegedModuleMethodCall-off - сценарий теста проверяет сам привилегированный метод.
+	// BSLLS:PrivilegedModuleMethodCall-on
+	// BSLLS:YoLetterUsage-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.17.8 → 2.0.17.9

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- новые объекты/формы (1 файлов), а реестр docs/TESTS.xlsx не менялся — изменение состава тестов фиксируется в реестре
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
