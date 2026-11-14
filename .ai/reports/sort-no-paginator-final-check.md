# Final check — sort-no-paginator
_20261110T180421Z_


## Scope

```
.ai/reports/sort-no-paginator-final-check.md
.ai/reviews/sort-no-paginator/03-code-review.json
.ai/reviews/sort-no-paginator/03b-code-review-verify.json
docs/FORMS-STYLE.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/list-panel.py
src/cf/src/AccumulationRegisters/ТоварыВНаличии/Forms/ВыборПартииПоОстаткам/Attributes/Список/ExtInfo/ListSettings.dcss
src/cf/src/CommonModules/РаботаСДокументамиКлиентСервер/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Attributes/Заказы/ExtInfo/ListSettings.dcss
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Attributes/Список/ExtInfo/ListSettings.dcss
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Attributes/Список/ExtInfo/ListSettings.dcss
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Attributes/СписокПродаж/ExtInfo/ListSettings.dcss
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Attributes/СписокЗаказы/ExtInfo/ListSettings.dcss
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Attributes/СписокЗаказы/ExtInfo/ListSettings.dcss
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Attributes/СписокПоступлений/ExtInfo/ListSettings.dcss
src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Form.form
src/cf/src/Documents/КадровыйПриказ/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Form.form
src/cf/src/Documents/КорректировкаДолга/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПравилоЦенообразования/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Form.form
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПриказНаНачислениеУдержание/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаСписка/Form.form
src/cf/src/Documents/УстановкаЦенНоменклатурыВручную/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Form.form
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/КадровыйПриказ/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/КорректировкаДолга/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПравилоЦенообразования/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПриказНаНачислениеУдержание/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/УстановкаЦенНоменклатурыВручную/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-10T19:04:28.952+01:00  INFO 19706 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/859 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/859 (0:00:01 / 0:01:35) Analyzing files...  10% [==                      ]  92/859 (0:00:02 / 0:00:16) Analyzing files...  21% [=====                   ] 182/859 (0:00:03 / 0:00:11) Analyzing files...  29% [=======                 ] 257/859 (0:00:04 / 0:00:09) Analyzing files...  46% [===========             ] 402/859 (0:00:05 / 0:00:05) Analyzing files...  53% [============            ] 460/859 (0:00:06 / 0:00:05) Analyzing files...  77% [==================      ] 666/859 (0:00:07 / 0:00:02) Analyzing files... 100% [========================] 859/859 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 859/859 (0:00:07 / 0:00:00) 
2026-11-10T19:04:39.926+01:00  INFO 19706 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-11-10 19:03:41; изменённых модулей: 25
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
Языков: 4, пунктов изменений: 20
Описание изменений: /Users/ivan-gurkin/orca/workspaces/maERP/Второй-поток-Саппорт/build/changelog-2.0.17.8.json
версия 2.0.17.8: ru=5, fr=5, en=5, es=5
```
**PASS**

## Git hygiene

### git status
```
 M docs/FORMS-STYLE.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M scripts/list-panel.py
 M src/cf/src/CommonModules/РаботаСДокументамиКлиентСервер/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
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
 M src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/КадровыйПриказ/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/КадровыйПриказ/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/КорректировкаДолга/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/КорректировкаДолга/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НачислениеЗарплаты/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НачислениеЗарплаты/Forms/ФормаСписка/Module.bsl
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
 M src/cf/src/Documents/ПлатёжнаяВедомостьНаАванс/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПлатёжнаяВедомостьНаАванс/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПравилоЦенообразования/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПравилоЦенообразования/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПриказНаНачислениеУдержание/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПриказНаНачислениеУдержание/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РасходныйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РасходныйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СверкаВзаиморасчётов/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СверкаВзаиморасчётов/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СертификатНаОплату/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СертификатНаОплату/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ТабельУчётаРабочегоВремени/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ТабельУчётаРабочегоВремени/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/УстановкаПлановыхПоказателей/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/УстановкаПлановыхПоказателей/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/УстановкаЦенНоменклатуры/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/УстановкаЦенНоменклатуры/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/УстановкаЦенНоменклатурыВручную/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/УстановкаЦенНоменклатурыВручную/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/УценкаТоваров/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/УценкаТоваров/Forms/ФормаСписка/Module.bsl
?? .ai/reports/sort-no-paginator-final-check.md
?? .ai/reviews/sort-no-paginator/
?? src/cf/src/AccumulationRegisters/ТоварыВНаличии/Forms/ВыборПартииПоОстаткам/Attributes/
?? src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Attributes/
?? src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Attributes/
?? src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Attributes/СписокПродаж/
?? src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Attributes/СписокПоступлений/
?? src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Attributes/СписокЗаказы/
?? src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Attributes/
?? src/cf/src/Documents/РасходныйОрдер/Forms/ФормаСписка/Attributes/
?? src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Attributes/СписокЗаказы/
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
+	// BSLLS:MagicNumber-off - пять непредварительных заказов сценария.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.17.7 → 2.0.17.8

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
