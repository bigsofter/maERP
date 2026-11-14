# Final check — tovar-filter
_20261112T073216Z_


## Scope

```
.ai/reports/tovar-filter-final-check.md
.ai/reviews/tovar-filter/03-code-review.json
.ai/reviews/tovar-filter/03b-code-review-verify-round1.json
.ai/reviews/tovar-filter/03b-code-review-verify.json
docs/TESTING.md
docs/TESTS.xlsx
scripts/listcheck.py
src/cf/src/CommonModules/ОтборыСписков/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Form.form
src/cf/src/Documents/УценкаТоваров/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Form.form
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Form.form
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Form.form
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Form.form
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Form.form
src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/УценкаТоваров/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Module.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-12T08:32:23.282+01:00  INFO 21158 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/860 (0:00:00 / ?) Analyzing files...   5% [=                       ]  44/860 (0:00:01 / 0:00:18) Analyzing files...  11% [==                      ] 102/860 (0:00:02 / 0:00:14) Analyzing files...  28% [======                  ] 245/860 (0:00:03 / 0:00:07) Analyzing files...  48% [===========             ] 417/860 (0:00:04 / 0:00:04) Analyzing files...  67% [================        ] 581/860 (0:00:05 / 0:00:02) Analyzing files...  84% [====================    ] 730/860 (0:00:06 / 0:00:01) Analyzing files...  94% [======================  ] 809/860 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 860/860 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 860/860 (0:00:07 / 0:00:00) 
2026-11-12T08:32:34.147+01:00  INFO 21158 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-11-10 19:03:41; изменённых модулей: 18
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
Описание изменений: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/changelog-2.0.17.18.json
версия 2.0.17.18: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M scripts/listcheck.py
 M src/cf/src/CommonModules/ОтборыСписков/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПеремещениеТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПеремещениеТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПересортицаТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПересортицаТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПересчётТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПересчётТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РасходныйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РасходныйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/УценкаТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/УценкаТоваров/Forms/ФормаСписка/Module.bsl
?? .ai/reports/tovar-filter-final-check.md
?? .ai/reviews/tovar-filter/
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
none found

### Версия конфигурации
2.0.17.11 → 2.0.17.18

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
