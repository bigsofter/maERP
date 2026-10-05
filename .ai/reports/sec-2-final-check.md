# Final check — sec-2
_20261005T203904Z_


## Scope

```
.ai/reports/sec-2-final-check.md
.ai/reviews/sec-2/02-plan-review-claude.md
.ai/reviews/sec-2/03-review-claude.md
.ai/reviews/sec-2/04-security-claude.md
docs/plans/sec-2-user-access-settings.md
docs/ROADMAP.md
docs/TECHDEBT.md
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/InformationRegisters/НастройкиПользователей/Forms/ФормаЗаписи/Form.form
src/cf/src/InformationRegisters/НастройкиПользователей/Forms/ФормаЗаписи/Module.bsl
src/cf/src/InformationRegisters/НастройкиПользователей/ManagerModule.bsl
src/cf/src/InformationRegisters/НастройкиПользователей/RecordSetModule.bsl
src/cf/src/Roles/ОбменМобильнаяДоставка/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-05T21:39:14.918+01:00  INFO 57171 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/759 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/759 (0:00:01 / 0:01:24) Analyzing files...  10% [==                      ]  81/759 (0:00:02 / 0:00:16) Analyzing files...  21% [=====                   ] 163/759 (0:00:03 / 0:00:10) Analyzing files...  34% [========                ] 262/759 (0:00:04 / 0:00:07) Analyzing files...  46% [===========             ] 353/759 (0:00:05 / 0:00:05) Analyzing files...  63% [===============         ] 485/759 (0:00:06 / 0:00:03) Analyzing files...  79% [==================      ] 600/759 (0:00:07 / 0:00:01) Analyzing files...  95% [======================  ] 723/759 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 759/759 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 759/759 (0:00:08 / 0:00:00) 
2026-10-05T21:39:28.060+01:00  INFO 57171 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.15.json
версия 2.0.16.15: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/InformationRegisters/НастройкиПользователей/Forms/ФормаЗаписи/Form.form
 M src/cf/src/InformationRegisters/НастройкиПользователей/ManagerModule.bsl
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/ОбменМобильнаяДоставка/Rights.rights
?? .ai/reports/sec-2-final-check.md
?? .ai/reviews/sec-2/
?? docs/plans/sec-2-user-access-settings.md
?? src/cf/src/InformationRegisters/НастройкиПользователей/Forms/ФормаЗаписи/Module.bsl
?? src/cf/src/InformationRegisters/НастройкиПользователей/RecordSetModule.bsl
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
+	// BSLLS:SetPrivilegedMode-off - родителей видов и строки базы читает проверка прав, а не пишущий пользователь
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off - чтение ролей текущего пользователя ИБ, решение от режима не зависит
+	// BSLLS:SetPrivilegedMode-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.14 → 2.0.16.15

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
