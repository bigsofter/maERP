# Final check — menu-restructure-1a
_20261002T140837Z_


## Scope

```
.ai/reports/menu-restructure-1a-final-check.md
docs/plans/menu-restructure-stage1-prompt.md
docs/plans/menu-restructure.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/titlecheck-baseline.txt
src/cf/src/AccumulationRegisters/ДвиженияПоКассе/ДвиженияПоКассе.mdo
src/cf/src/AccumulationRegisters/ДенежныеСредстваОрганизаций/ДенежныеСредстваОрганизаций.mdo
src/cf/src/Catalogs/Кассы/Кассы.mdo
src/cf/src/Catalogs/КодыТНВЭД/КодыТНВЭД.mdo
src/cf/src/ChartsOfCharacteristicTypes/ВидыСубконтоХозрасчетные/ВидыСубконтоХозрасчетные.mdo
src/cf/src/CommonModules/МенеджерОборудованияКлиент/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/CommandInterface.cmi
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Form.form
src/cf/src/DocumentJournals/КассовыеДокументы/КассовыеДокументы.mdo
src/cf/src/Documents/АктРазбора/АктРазбора.mdo
src/cf/src/Documents/КассоваяСмена/КассоваяСмена.mdo
src/cf/src/Documents/КадровыйПриказ/КадровыйПриказ.mdo
src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Form.form
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Form.form
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ManagerModule.bsl
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ManagerModule.bsl
src/cf/src/InformationRegisters/НумерацияЧековККТ/НумерацияЧековККТ.mdo
src/cf/src/Reports/КассоваяКнига/КассоваяКнига.mdo
src/cf/src/Reports/ОтчетПоНедостаткамТовара/ОтчетПоНедостаткамТовара.mdo
src/cf/src/Reports/КассоваяКнига/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РеестрНалоговыхНакладных/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РеестрНалоговыхНакладныхЗакупка/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/ScheduledJobs/АвтозакрытиеСмены/АвтозакрытиеСмены.mdo
src/cf/src/Subsystems/Сервис/Subsystems/НастройкиПрограммы/НастройкиПрограммы.mdo
src/cf/src/Subsystems/ECommerce/ECommerce.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-02T15:08:45.906+01:00  INFO 38973 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/741 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/741 (0:00:01 / 0:01:22) Analyzing files...  18% [====                    ] 140/741 (0:00:02 / 0:00:08) Analyzing files...  41% [=========               ] 305/741 (0:00:03 / 0:00:04) Analyzing files...  58% [=============           ] 430/741 (0:00:04 / 0:00:02) Analyzing files...  74% [=================       ] 553/741 (0:00:05 / 0:00:01) Analyzing files...  93% [======================  ] 693/741 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 741/741 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 741/741 (0:00:06 / 0:00:00) 
2026-10-02T15:08:54.979+01:00  INFO 38973 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-09-25 23:18:19; изменённых модулей: 8
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
Языков: 4, пунктов изменений: 16
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.4.json
версия 2.0.16.4: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/menu-restructure-stage1-prompt.md
 M docs/plans/menu-restructure.md
 M scripts/titlecheck-baseline.txt
 M src/cf/src/AccumulationRegisters/ДвиженияПоКассе/ДвиженияПоКассе.mdo
 M src/cf/src/AccumulationRegisters/ДенежныеСредстваОрганизаций/ДенежныеСредстваОрганизаций.mdo
 M src/cf/src/Catalogs/Кассы/Кассы.mdo
 M src/cf/src/Catalogs/КодыТНВЭД/КодыТНВЭД.mdo
 M src/cf/src/Catalogs/НомераГТД/НомераГТД.mdo
 M src/cf/src/ChartsOfCharacteristicTypes/ВидыСубконтоХозрасчетные/ВидыСубконтоХозрасчетные.mdo
 M src/cf/src/CommonModules/МенеджерОборудованияКлиент/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/CommandInterface.cmi
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Form.form
 M src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
 M src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
 M src/cf/src/DocumentJournals/КассовыеДокументы/КассовыеДокументы.mdo
 M src/cf/src/Documents/АктРазбора/АктРазбора.mdo
 M src/cf/src/Documents/ВозвратОтПокупателя/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
 M src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
 M src/cf/src/Documents/КадровыйПриказ/КадровыйПриказ.mdo
 M src/cf/src/Documents/КассоваяСмена/КассоваяСмена.mdo
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/ПоступлениеБезналичныхДенежныхСредств.mdo
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/ПриходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/РасходныйКассовыйОрдер/РасходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Documents/СертификатНаОплату/СертификатНаОплату.mdo
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/СписаниеБезналичныхДенежныхСредств.mdo
 M src/cf/src/InformationRegisters/НумерацияЧековККТ/НумерацияЧековККТ.mdo
 M src/cf/src/Reports/КассоваяКнига/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/КассоваяКнига/КассоваяКнига.mdo
 M src/cf/src/Reports/ОтчетПоНедостаткамТовара/ОтчетПоНедостаткамТовара.mdo
 M src/cf/src/Reports/РеестрНалоговыхНакладных/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РеестрНалоговыхНакладныхЗакупка/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/ScheduledJobs/АвтозакрытиеСмены/АвтозакрытиеСмены.mdo
 M src/cf/src/Subsystems/ECommerce/ECommerce.mdo
 M src/cf/src/Subsystems/Сервис/Subsystems/НастройкиПрограммы/НастройкиПрограммы.mdo
?? .ai/reports/menu-restructure-1a-final-check.md
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
2.0.16.3 → 2.0.16.4

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
