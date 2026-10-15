# Final check — performance-vt
_20261015T195403Z_


## Scope

```
.ai/reports/performance-vt-final-check.md
.ai/reports/performance-vt.md
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/Продажи/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ЗаказыПоставщикам/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ДополнительныеРасходы/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
src/cf/src/Catalogs/ДоговорыСКонтрагентами/ManagerModule.bsl
src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/ManagerModule.bsl
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
src/cf/src/Documents/УстановкаЦенНоменклатуры/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ТабельУчётаРабочегоВремени/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/КассоваяСмена/ManagerModule.bsl
src/cf/src/Documents/ВыплатаЗарплаты/ManagerModule.bsl
src/cf/src/InformationRegisters/ПравилаЦенообразования/ManagerModule.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-15T20:54:11.033+01:00  INFO 73310 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/818 (0:00:00 / ?) Analyzing files...   3% [                        ]  31/818 (0:00:01 / 0:00:25) Analyzing files...  16% [===                     ] 134/818 (0:00:02 / 0:00:10) Analyzing files...  27% [======                  ] 223/818 (0:00:03 / 0:00:08) Analyzing files...  48% [===========             ] 394/818 (0:00:04 / 0:00:04) Analyzing files...  62% [===============         ] 512/818 (0:00:05 / 0:00:02) Analyzing files...  91% [======================  ] 752/818 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 818/818 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 818/818 (0:00:06 / 0:00:00) 
2026-10-15T20:54:20.337+01:00  INFO 73310 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 17
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.83.json
версия 2.0.16.83: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ДополнительныеРасходы/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ЗаказыПоставщикам/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/Продажи/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 M src/cf/src/Catalogs/ДоговорыСКонтрагентами/ManagerModule.bsl
 M src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
 M src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
 M src/cf/src/CommonModules/ПроцедурыРегламентныхЗаданий/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/Forms/Форма/Module.bsl
 M src/cf/src/Documents/ВыплатаЗарплаты/ManagerModule.bsl
 M src/cf/src/Documents/КассоваяСмена/ManagerModule.bsl
 M src/cf/src/Documents/ТабельУчётаРабочегоВремени/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/УстановкаЦенНоменклатуры/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/InformationRegisters/ПравилаЦенообразования/ManagerModule.bsl
?? .ai/reports/performance-vt-final-check.md
?? .ai/reports/performance-vt.md
?? .ai/reviews/performance-vt/
?? .ai/reviews/uncommitted/
?? .ai/reviews/wo-techdebt2/
?? src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/ManagerModule.bsl
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
+	// BSLLS:MagicNumber-off - заказ 10, два поступления по 3.
+	// BSLLS:MagicNumber-on
+	// BSLLS:YoLetterUsage-off - имя регистра в метаданных.
+	// BSLLS:YoLetterUsage-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.82 → 2.0.16.83

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
