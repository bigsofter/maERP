# Final check — forms-unification
_20260925T090114Z_


## Scope

```
.ai/reports/forms-unification-final-check.md
docs/FORMS-STYLE.md
docs/plans/forms-layout-unification.md
scripts/forms-layout.py
scripts/synonyms-dict.json
scripts/synonyms.py
scripts/titlecheck-baseline.txt
scripts/titlecheck.py
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/АктРазбора/АктРазбора.mdo
src/cf/src/Documents/КассоваяСмена/КассоваяСмена.mdo
src/cf/src/Documents/ВыплатаЗарплаты/ВыплатаЗарплаты.mdo
src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
src/cf/src/Documents/КорректировкаДолга/КорректировкаДолга.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
src/cf/src/Documents/ПредложениеПоставщика/ПредложениеПоставщика.mdo
src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/ПоступлениеДополнительныхРасходов.mdo
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаСписка/Form.form
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
src/cf/src/Reports/ГлавнаяКнига/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ИсторияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ИсторияКлиента/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ТоварыДляЗаказа/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьПоПродажам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РасчетыСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/СтатистикаДневныхПродаж/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ОтчетПоНедостаткамТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ПроданныйТоварБезНакладной/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РеестрРеализацийТоваровУслуг/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ИсторияИзмененияЦенПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьРасчётовСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьРасчётовСКонтрагентами/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьРасчётовСПрочимиКонтрагентами/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-25T10:01:24.865+01:00  INFO 70257 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/741 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/741 (0:00:01 / 0:01:21) Analyzing files...   7% [=                       ]  52/741 (0:00:02 / 0:00:26) Analyzing files...  18% [====                    ] 138/741 (0:00:03 / 0:00:13) Analyzing files...  33% [=======                 ] 245/741 (0:00:04 / 0:00:08) Analyzing files...  39% [=========               ] 293/741 (0:00:05 / 0:00:07) Analyzing files...  54% [=============           ] 403/741 (0:00:06 / 0:00:05) Analyzing files...  74% [=================       ] 549/741 (0:00:07 / 0:00:02) Analyzing files...  88% [=====================   ] 657/741 (0:00:08 / 0:00:01) Analyzing files... 100% [========================] 741/741 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 741/741 (0:00:08 / 0:00:00) 
2026-09-25T10:01:38.773+01:00  INFO 70257 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-09-19 09:10:00; изменённых модулей: 2
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
Языков: 4, пунктов изменений: 4
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.64.json
версия 2.0.15.64: ru=1, fr=1, en=1, es=1
```
**PASS**

## Git hygiene

### git status
```
 M docs/FORMS-STYLE.md
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/Documents/АктРазбора/АктРазбора.mdo
 M src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
 M src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
 M src/cf/src/Documents/ВыплатаЗарплаты/ВыплатаЗарплаты.mdo
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
 M src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
 M src/cf/src/Documents/ЗаказПоставщику/ЗаказПоставщику.mdo
 M src/cf/src/Documents/ЗаявкаНаПоискТовара/ЗаявкаНаПоискТовара.mdo
 M src/cf/src/Documents/КассоваяСмена/КассоваяСмена.mdo
 M src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
 M src/cf/src/Documents/КорректировкаДолга/КорректировкаДолга.mdo
 M src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
 M src/cf/src/Documents/НачислениеЗарплаты/НачислениеЗарплаты.mdo
 M src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
 M src/cf/src/Documents/ПередачаВПереработку/ObjectModule.bsl
 M src/cf/src/Documents/ПеремещениеТоваров/ПеремещениеТоваров.mdo
 M src/cf/src/Documents/ПересчётТоваров/ПересчётТоваров.mdo
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/ПоступлениеДополнительныхРасходов.mdo
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
 M src/cf/src/Documents/ПредложениеПоставщика/ПредложениеПоставщика.mdo
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПрочиеРасходы/ПрочиеРасходы.mdo
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/ПрочиеРасходыВозврат/ПрочиеРасходыВозврат.mdo
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РасходныйКассовыйОрдер/РасходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Documents/СверкаВзаиморасчётов/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
 M src/cf/src/Documents/СписаниеТоваров/СписаниеТоваров.mdo
 M src/cf/src/Reports/ВедомостьПоПродажам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьРасчётовСКонтрагентами/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьРасчётовСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьРасчётовСПоставщиками/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьРасчётовСПрочимиКонтрагентами/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ГлавнаяКнига/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ИсторияИзмененияЦенПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ИсторияКлиента/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ИсторияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/НеоплаченныеПродажи/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/НеотгруженныеЗаказы/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОтчетПоНедостаткамТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПланированиеЗакупок/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПроданныйТоварБезНакладной/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РасчетыСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РасчетыСПоставщиками/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РеестрНалоговыхНакладных/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РеестрНалоговыхНакладныхЗакупка/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РеестрРеализацийТоваровУслуг/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/СтатистикаДневныхПродаж/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыДляЗаказа/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ФинансовыйРезультат/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
?? .ai/reports/forms-unification-final-check.md
?? docs/plans/forms-layout-unification.md
?? scripts/forms-layout.py
?? scripts/synonyms-dict.json
?? scripts/synonyms.py
?? scripts/titlecheck-baseline.txt
?? scripts/titlecheck.py
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
версия 2.0.15.64 не поднималась относительно HEAD — если это передача владельцу на тест, подними Y и заведи секцию (CLAUDE.md «Версия и список изменений»)

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
