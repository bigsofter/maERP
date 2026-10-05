# Final check — synonyms-fin-terms
_20261005T173323Z_


## Scope

```
.ai/reports/synonyms-fin-terms-final-check.md
src/cf/src/AccumulationRegisters/Убытки/Убытки.mdo
src/cf/src/AccumulationRegisters/Зарплата/Зарплата.mdo
src/cf/src/AccumulationRegisters/ДополнительныеРасходы/ДополнительныеРасходы.mdo
src/cf/src/AccumulationRegisters/ДвиженияДенежныхСредств/ДвиженияДенежныхСредств.mdo
src/cf/src/AccumulationRegisters/ВзаиморасчётыСКонтрагентамиПрочие/ВзаиморасчётыСКонтрагентамиПрочие.mdo
src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/СтатьиДвиженияДенежныхСредств.mdo
src/cf/src/ChartsOfCharacteristicTypes/ВидыСубконтоХозрасчетные/ВидыСубконтоХозрасчетные.mdo
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Documents/ПрочиеРасходы/ПрочиеРасходы.mdo
src/cf/src/Documents/СписаниеТоваров/СписаниеТоваров.mdo
src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
src/cf/src/Documents/ПрочиеРасходыВозврат/ПрочиеРасходыВозврат.mdo
src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
src/cf/src/Documents/ПриказНаНачислениеУдержание/ПриказНаНачислениеУдержание.mdo
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/ПоступлениеДополнительныхРасходов.mdo
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
src/cf/src/Enums/ТипыДвиженияДенежныхСредств/ТипыДвиженияДенежныхСредств.mdo
src/cf/src/Reports/Затраты/Затраты.mdo
src/cf/src/Reports/АнализСчета/АнализСчета.mdo
src/cf/src/Reports/ОборотыСчета/ОборотыСчета.mdo
src/cf/src/Reports/КарточкаСчета/КарточкаСчета.mdo
src/cf/src/Reports/ДвижениеДенежныхСредств/ДвижениеДенежныхСредств.mdo
src/cf/src/Reports/ОборотноСальдоваяВедомость/ОборотноСальдоваяВедомость.mdo
src/cf/src/Reports/ОборотноСальдоваяВедомостьПоСчету/ОборотноСальдоваяВедомостьПоСчету.mdo
src/cf/src/Reports/ДвижениеДенежныхСредств/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-05T18:33:30.273+01:00  INFO 27897 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/757 (0:00:00 / ?) Analyzing files...   8% [=                       ]  62/757 (0:00:01 / 0:00:11) Analyzing files...  25% [======                  ] 196/757 (0:00:02 / 0:00:05) Analyzing files...  44% [==========              ] 338/757 (0:00:03 / 0:00:03) Analyzing files...  63% [===============         ] 483/757 (0:00:04 / 0:00:02) Analyzing files...  84% [====================    ] 640/757 (0:00:05 / 0:00:00) Analyzing files...  98% [======================= ] 747/757 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 757/757 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 757/757 (0:00:06 / 0:00:00) 
2026-10-05T18:33:39.582+01:00  INFO 27897 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 7
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.13.json
версия 2.0.16.13: ru=1, fr=1, en=1, es=1
```
**PASS**

## Git hygiene

### git status
```
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСКонтрагентамиПрочие/ВзаиморасчётыСКонтрагентамиПрочие.mdo
 M src/cf/src/AccumulationRegisters/ДвиженияДенежныхСредств/ДвиженияДенежныхСредств.mdo
 M src/cf/src/AccumulationRegisters/ДополнительныеРасходы/ДополнительныеРасходы.mdo
 M src/cf/src/AccumulationRegisters/Зарплата/Зарплата.mdo
 M src/cf/src/AccumulationRegisters/Убытки/Убытки.mdo
 M src/cf/src/Catalogs/СтатьиДвиженияДенежныхСредств/СтатьиДвиженияДенежныхСредств.mdo
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыСубконтоХозрасчетные/ВидыСубконтоХозрасчетные.mdo
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/ПоступлениеДополнительныхРасходов.mdo
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
 M src/cf/src/Documents/ПриказНаНачислениеУдержание/ПриказНаНачислениеУдержание.mdo
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПрочиеРасходы/ПрочиеРасходы.mdo
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПрочиеРасходыВозврат/ПрочиеРасходыВозврат.mdo
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/РасходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СписаниеТоваров/СписаниеТоваров.mdo
 M src/cf/src/Enums/ТипыДвиженияДенежныхСредств/ТипыДвиженияДенежныхСредств.mdo
 M src/cf/src/Reports/АнализСчета/АнализСчета.mdo
 M src/cf/src/Reports/ДвижениеДенежныхСредств/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ДвижениеДенежныхСредств/ДвижениеДенежныхСредств.mdo
 M src/cf/src/Reports/Затраты/Затраты.mdo
 M src/cf/src/Reports/КарточкаСчета/КарточкаСчета.mdo
 M src/cf/src/Reports/ОборотноСальдоваяВедомость/ОборотноСальдоваяВедомость.mdo
 M src/cf/src/Reports/ОборотноСальдоваяВедомостьПоСчету/ОборотноСальдоваяВедомостьПоСчету.mdo
 M src/cf/src/Reports/ОборотыСчета/ОборотыСчета.mdo
?? .ai/reports/synonyms-fin-terms-final-check.md
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
2.0.16.12 → 2.0.16.13

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
