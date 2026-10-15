# Final check — test-coverage
_20261015T180621Z_


## Scope

```
.ai/reports/test-coverage-final-check.md
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/listcheck-known.txt
src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбора/Form.form
src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораРозница/Form.form
src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ПодключениеИНастройкаОборудования/Form.form
src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораECommerce/Form.form
src/cf/src/ChartsOfAccounts/Хозрасчетный/Forms/ФормаСписка/Form.form
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/Форма/Form.form
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/DocumentJournals/БезналичныеПлатежи/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаВыбора/Form.form
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСпискаМобильныйКлиент/Form.form
src/cf/src/InformationRegisters/ПрисоединённыеФайлы/Forms/ФормаСписка/Form.form
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-15T19:06:32.481+01:00  INFO 36100 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/817 (0:00:00 / ?) Analyzing files...   5% [=                       ]  45/817 (0:00:01 / 0:00:17) Analyzing files...  17% [====                    ] 144/817 (0:00:02 / 0:00:09) Analyzing files...  34% [========                ] 279/817 (0:00:03 / 0:00:05) Analyzing files...  41% [=========               ] 336/817 (0:00:04 / 0:00:05) Analyzing files...  58% [==============          ] 482/817 (0:00:05 / 0:00:03) Analyzing files...  66% [===============         ] 543/817 (0:00:06 / 0:00:03) Analyzing files...  84% [====================    ] 687/817 (0:00:07 / 0:00:01) Analyzing files...  99% [======================= ] 813/817 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:08 / 0:00:00) 
2026-10-15T19:06:44.873+01:00  INFO 36100 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 1
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
Языков: 4, пунктов изменений: 8
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.82.json
версия 2.0.16.82: ru=2, fr=2, en=2, es=2
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M scripts/listcheck-known.txt
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбора/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораECommerce/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаВыбораРозница/Form.form
 M src/cf/src/Catalogs/Контрагенты/Forms/ФормаСпискаECommerce/Form.form
 M src/cf/src/Catalogs/ПодключаемоеОборудование/Forms/ПодключениеИНастройкаОборудования/Form.form
 M src/cf/src/ChartsOfAccounts/Хозрасчетный/Forms/ФормаСписка/Form.form
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/DocumentJournals/БезналичныеПлатежи/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСпискаМобильныйКлиент/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаВыбора/Form.form
 M src/cf/src/InformationRegisters/ПрисоединённыеФайлы/Forms/ФормаСписка/Form.form
?? .ai/reports/test-coverage-final-check.md
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
+	// BSLLS:MagicNumber-off - P1 6 из 10, как первая отгрузка сценария АвтовыпускПриОтгрузке; автовыпуск на секунду
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - продукция 8 с нормой 0,000000125: материал заказа 0,000001 (разрядность количества),
+	// BSLLS:MagicNumber-on
+	// BSLLS:YoLetterUsage-off - имена регистров
+	// BSLLS:YoLetterUsage-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.81 → 2.0.16.82

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
