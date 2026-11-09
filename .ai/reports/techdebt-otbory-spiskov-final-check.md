# Final check — techdebt-otbory-spiskov
_20261010T215638Z_


## Scope

```
.ai/reports/techdebt-otbory-spiskov-final-check.md
.ai/reviews/old-item-properties/02-plan-review.json
.ai/reviews/techdebt-otbory-spiskov/03-code-review.json
.ai/reviews/techdebt-otbory-spiskov/03b-code-review-verify.json
docs/plans/old-item-properties.md
docs/ROADMAP.md
docs/TECHDEBT.md
src/cf/src/CommonModules/ОтборыСписков/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
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
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Module.bsl
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
2026-10-10T22:56:46.426+01:00  INFO 97080 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/805 (0:00:00 / ?) Analyzing files...   9% [==                      ]  80/805 (0:00:01 / 0:00:09) Analyzing files...  25% [======                  ] 205/805 (0:00:02 / 0:00:05) Analyzing files...  53% [============            ] 433/805 (0:00:03 / 0:00:02) Analyzing files...  69% [================        ] 562/805 (0:00:04 / 0:00:01) Analyzing files...  89% [=====================   ] 720/805 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 805/805 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 805/805 (0:00:05 / 0:00:00) 
2026-10-10T22:56:55.068+01:00  INFO 97080 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 22
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.65.json
версия 2.0.16.65: ru=1, fr=1, en=1, es=1
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M src/cf/src/CommonModules/ОтборыСписков/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/АктРазбора/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВозвратПоставщику/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВыплатаЗарплаты/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ВыпускПродукции/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаданиеНаПересчет/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/КадровыйПриказ/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/КорректировкаДолга/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/НачислениеЗарплаты/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ОприходованиеТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПередачаВПереработку/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПеремещениеТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПересортицаТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПересчётТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПлатёжнаяВедомостьНаАванс/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеДополнительныхРасходов/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПравилоЦенообразования/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПредложениеПоставщика/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПриказНаНачислениеУдержание/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПриходныйКассовыйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПрочиеРасходы/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ПрочиеРасходыВозврат/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РасходныйКассовыйОрдер/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СверкаВзаиморасчётов/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СертификатНаОплату/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СписаниеБезналичныхДенежныхСредств/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ТабельУчётаРабочегоВремени/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/УстановкаПлановыхПоказателей/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/УстановкаЦенНоменклатуры/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/УстановкаЦенНоменклатурыВручную/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/УценкаТоваров/Forms/ФормаСписка/Module.bsl
?? .ai/reports/techdebt-otbory-spiskov-final-check.md
?? .ai/reviews/old-item-properties/
?? .ai/reviews/techdebt-otbory-spiskov/
?? docs/plans/old-item-properties.md
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
2.0.16.64 → 2.0.16.65

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
