# Final check — choice-history
_20261017T114420Z_


## Scope

```
.ai/reports/choice-history-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reviews/choice-history/03-code-review.json
.ai/reviews/choice-history/03b-code-review-verify.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/Catalogs/Банки/Банки.mdo
src/cf/src/Catalogs/Валюты/Валюты.mdo
src/cf/src/Catalogs/ВидыЦен/ВидыЦен.mdo
src/cf/src/Catalogs/Должности/Должности.mdo
src/cf/src/Catalogs/СтраныМира/СтраныМира.mdo
src/cf/src/Catalogs/ВидыЗаданий/ВидыЗаданий.mdo
src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
src/cf/src/Catalogs/НаборыУпаковок/НаборыУпаковок.mdo
src/cf/src/Catalogs/БанковскиеСчета/БанковскиеСчета.mdo
src/cf/src/Catalogs/СерииНоменклатуры/СерииНоменклатуры.mdo
src/cf/src/Catalogs/СтруктураПредприятия/СтруктураПредприятия.mdo
src/cf/src/Catalogs/ВариантыВыходаНаРаботу/ВариантыВыходаНаРаботу.mdo
src/cf/src/Catalogs/НоменклатураКонтрагентов/НоменклатураКонтрагентов.mdo
src/cf/src/Catalogs/ХарактеристикиНоменклатуры/ХарактеристикиНоменклатуры.mdo
src/cf/src/Catalogs/ВидыДокументовФизическихЛиц/ВидыДокументовФизическихЛиц.mdo
src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/СтатьиДвиженияДенежныхСредств.mdo
src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
src/cf/src/ChartsOfCharacteristicTypes/ВидыРеквизитовКонтрагентов/ВидыРеквизитовКонтрагентов.mdo
src/cf/src/CommonModules/РаботаСДокументамиКлиент/Module.bsl
src/cf/src/CommonModules/РаботаСДокументамиВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/АктРазбора/АктРазбора.mdo
src/cf/src/Documents/ОперацияБух/ОперацияБух.mdo
src/cf/src/Documents/УценкаТоваров/УценкаТоваров.mdo
src/cf/src/Documents/КадровыйПриказ/КадровыйПриказ.mdo
src/cf/src/Documents/ВыплатаЗарплаты/ВыплатаЗарплаты.mdo
src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
src/cf/src/Documents/КорректировкаДолга/КорректировкаДолга.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
src/cf/src/Documents/ПлатёжнаяВедомостьНаАванс/ПлатёжнаяВедомостьНаАванс.mdo
src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
src/cf/src/Documents/ПриказНаНачислениеУдержание/ПриказНаНачислениеУдержание.mdo
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаДокументаМобильныйКлиент/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
src/cf/src/Enums/Месяца/Месяца.mdo
src/cf/src/Enums/ХозяйственныеОперации/ХозяйственныеОперации.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-17T12:44:29.498+01:00  INFO 83852 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/818 (0:00:00 / ?) Analyzing files...   8% [==                      ]  73/818 (0:00:01 / 0:00:10) Analyzing files...  19% [====                    ] 157/818 (0:00:02 / 0:00:08) Analyzing files...  37% [========                ] 306/818 (0:00:03 / 0:00:05) Analyzing files...  56% [=============           ] 463/818 (0:00:04 / 0:00:03) Analyzing files...  70% [================        ] 574/818 (0:00:05 / 0:00:02) Analyzing files...  85% [====================    ] 703/818 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 818/818 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 818/818 (0:00:06 / 0:00:00) 
2026-10-17T12:44:38.887+01:00  INFO 83852 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.90.json
версия 2.0.16.90: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/Catalogs/Банки/Банки.mdo
 M src/cf/src/Catalogs/БанковскиеСчета/БанковскиеСчета.mdo
 M src/cf/src/Catalogs/Валюты/Валюты.mdo
 M src/cf/src/Catalogs/ВариантыВыходаНаРаботу/ВариантыВыходаНаРаботу.mdo
 M src/cf/src/Catalogs/ВидыДокументовФизическихЛиц/ВидыДокументовФизическихЛиц.mdo
 M src/cf/src/Catalogs/ВидыЗаданий/ВидыЗаданий.mdo
 M src/cf/src/Catalogs/ВидыЦен/ВидыЦен.mdo
 M src/cf/src/Catalogs/ДоговорыСКонтрагентами/ДоговорыСКонтрагентами.mdo
 M src/cf/src/Catalogs/ДокументыФизическихЛиц/ДокументыФизическихЛиц.mdo
 M src/cf/src/Catalogs/Должности/Должности.mdo
 M src/cf/src/Catalogs/Контрагенты/Контрагенты.mdo
 M src/cf/src/Catalogs/НаборыУпаковок/НаборыУпаковок.mdo
 M src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
 M src/cf/src/Catalogs/Номенклатура/Номенклатура.mdo
 M src/cf/src/Catalogs/НоменклатураКонтрагентов/НоменклатураКонтрагентов.mdo
 M src/cf/src/Catalogs/НомераГТД/НомераГТД.mdo
 M src/cf/src/Catalogs/Организации/Организации.mdo
 M src/cf/src/Catalogs/Пользователи/Пользователи.mdo
 M src/cf/src/Catalogs/СерииНоменклатуры/СерииНоменклатуры.mdo
 M src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/СтатьиДвиженияДенежныхСредств.mdo
 M src/cf/src/Catalogs/СтраныМира/СтраныМира.mdo
 M src/cf/src/Catalogs/СтруктураПредприятия/СтруктураПредприятия.mdo
 M src/cf/src/Catalogs/ТоварныеГруппы/ТоварныеГруппы.mdo
 M src/cf/src/Catalogs/УпаковкиЕдиницыИзмерения/УпаковкиЕдиницыИзмерения.mdo
 M src/cf/src/Catalogs/УчётныеЗаписиЭлектроннойПочты/УчётныеЗаписиЭлектроннойПочты.mdo
 M src/cf/src/Catalogs/ФизическиеЛица/ФизическиеЛица.mdo
 M src/cf/src/Catalogs/ХарактеристикиНоменклатуры/ХарактеристикиНоменклатуры.mdo
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыРеквизитовКонтрагентов/ВидыРеквизитовКонтрагентов.mdo
 M src/cf/src/CommonModules/РаботаСДокументамиВызовСервера/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиКлиент/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиКлиентСервер/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/РегистрацияИзмененийДляОбменаДанными/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/АктРазбора/АктРазбора.mdo
 M src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
 M src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
 M src/cf/src/Documents/ВыплатаЗарплаты/ВыплатаЗарплаты.mdo
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
 M src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаДокументаМобильныйКлиент/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
 M src/cf/src/Documents/КадровыйПриказ/КадровыйПриказ.mdo
 M src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
 M src/cf/src/Documents/КорректировкаДолга/КорректировкаДолга.mdo
 M src/cf/src/Documents/НачислениеЗарплаты/НачислениеЗарплаты.mdo
 M src/cf/src/Documents/ОбслуживаниеСтанка/ОбслуживаниеСтанка.mdo
 M src/cf/src/Documents/ОперацияБух/ОперацияБух.mdo
 M src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПередачаВПереработку/ПередачаВПереработку.mdo
 M src/cf/src/Documents/ПеремещениеТоваров/ПеремещениеТоваров.mdo
 M src/cf/src/Documents/ПересчётТоваров/ПересчётТоваров.mdo
 M src/cf/src/Documents/ПлатёжнаяВедомостьНаАванс/ПлатёжнаяВедомостьНаАванс.mdo
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
 M src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
 M src/cf/src/Documents/ПриказНаНачислениеУдержание/ПриказНаНачислениеУдержание.mdo
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/ПриходныйОрдер/ПриходныйОрдер.mdo
 M src/cf/src/Documents/РасходныйКассовыйОрдер/РасходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/РасходныйОрдер/РасходныйОрдер.mdo
 M src/cf/src/Documents/СверкаВзаиморасчётов/СверкаВзаиморасчётов.mdo
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
 M src/cf/src/Documents/СписаниеТоваров/СписаниеТоваров.mdo
 M src/cf/src/Documents/ТехнологическаяКарта/ТехнологическаяКарта.mdo
 M src/cf/src/Documents/ТребованиеНакладная/ТребованиеНакладная.mdo
 M src/cf/src/Documents/УценкаТоваров/УценкаТоваров.mdo
 M src/cf/src/Enums/Месяца/Месяца.mdo
 M src/cf/src/Enums/ХозяйственныеОперации/ХозяйственныеОперации.mdo
?? .ai/reports/choice-history-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reviews/choice-history/
?? .ai/reviews/machine-form/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
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
none found

### Версия конфигурации
2.0.16.89 → 2.0.16.90

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
