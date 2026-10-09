# Final check — techdebt-fix
_20261009T125834Z_


## Scope

```
.ai/reports/techdebt-fix-final-check.md
.ai/reviews/techdebt-fix/02-plan-review.json
.ai/reviews/techdebt-fix/03-code-review.json
.ai/reviews/techdebt-fix/03b-code-review-verify.json
.ai/reviews/techdebt-fix/04-database-review.json
.ai/reviews/techdebt-fix/05-security-review.json
docs/plans/techdebt-codex-2026-10-09.md
docs/TECHDEBT.md
src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоcтавщикамиНалоговый/ManagerModule.bsl
src/cf/src/CommonModules/Производство/Module.bsl
src/cf/src/CommonModules/РаботаСВалютами/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/ОперацияБух/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПересчётТоваров/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеИзПереработки/ObjectModule.bsl
src/cf/src/Documents/НалоговаяНакладнаяПокупка/ObjectModule.bsl
src/cf/src/Roles/ЛичныйКабинет/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-09T13:58:43.980+01:00  INFO 47254 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/795 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/795 (0:00:01 / 0:01:28) Analyzing files...  16% [===                     ] 128/795 (0:00:02 / 0:00:10) Analyzing files...  28% [======                  ] 224/795 (0:00:03 / 0:00:07) Analyzing files...  50% [============            ] 401/795 (0:00:04 / 0:00:03) Analyzing files...  71% [=================       ] 570/795 (0:00:05 / 0:00:01) Analyzing files...  82% [===================     ] 656/795 (0:00:06 / 0:00:01) Analyzing files...  97% [======================= ] 778/795 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 795/795 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 795/795 (0:00:07 / 0:00:00) 
2026-10-09T13:58:55.537+01:00  INFO 47254 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 19
CommonModules/РаботаСДокументами/Module.bsl: SetPrivilegedMode +1 (было 4, стало 5)
    5: Проверьте установку привилегированного режима
    288: Проверьте установку привилегированного режима
    379: Проверьте установку привилегированного режима
CommonModules/ПроизводственныеЗаказы/Module.bsl: SetPrivilegedMode +1 (было 4, стало 5)
    19: Проверьте установку привилегированного режима
    40: Проверьте установку привилегированного режима
    61: Проверьте установку привилегированного режима
Documents/ЗаказПокупателя/ObjectModule.bsl: SetPrivilegedMode +1 (было 1, стало 2)
    244: Проверьте установку привилегированного режима
    1198: Проверьте установку привилегированного режима
Documents/РеализацияТоваровУслуг/ObjectModule.bsl: SetPrivilegedMode +1 (было 2, стало 3)
    3: Проверьте установку привилегированного режима
    46: Проверьте установку привилегированного режима
    215: Проверьте установку привилегированного режима
```
**FAIL**
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.41.json
версия 2.0.16.41: ru=5, fr=5, en=5, es=5
```
**PASS**

## Git hygiene

### git status
```
 M docs/TECHDEBT.md
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоcтавщикамиНалоговый/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
 M src/cf/src/CommonModules/Производство/Module.bsl
 M src/cf/src/CommonModules/РаботаСВалютами/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ЗаказПоставщику/ObjectModule.bsl
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/ObjectModule.bsl
 M src/cf/src/Documents/ОперацияБух/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПересчётТоваров/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Roles/ЛичныйКабинет/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
?? .ai/reports/techdebt-fix-final-check.md
?? .ai/reviews/techdebt-fix/
?? docs/plans/techdebt-codex-2026-10-09.md
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
+	// BSLLS:YoLetterUsage-off - имя регистра
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off - имя регистра
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off - имя регистра
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-off - автовыпуск на секунду раньше реализации, поступление - ещё раньше.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:YoLetterUsage-off - имя регистра
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.40 → 2.0.16.41

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
