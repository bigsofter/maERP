# Final check — branded-print-s7
_20261012T074848Z_


## Scope

```
.ai/reports/branded-print-s7-final-check.md
.ai/reviews/branded-print-s7/02-plan-review.json
.ai/reviews/branded-print-s7/03-code-review.json
.ai/reviews/branded-print-s7/04-database-review.json
docs/plans/branded-print.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/refcheck-known.txt
src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonTemplates/АктОбОказанииУслуг/АктОбОказанииУслуг.mdo
src/cf/src/CommonTemplates/АктОбОказанииУслуг/Template.mxlx
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ЗаказПоставщику/ЗаказПоставщику.mdo
src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
src/cf/src/Documents/СверкаВзаиморасчётов/СверкаВзаиморасчётов.mdo
src/cf/src/Documents/РасходныйКассовыйОрдер/РасходныйКассовыйОрдер.mdo
src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
src/cf/src/Documents/НалоговаяНакладная/ManagerModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
src/cf/src/Documents/НалоговаяНакладнаяПокупка/ManagerModule.bsl
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ManagerModule.bsl
src/cf/src/Documents/НалоговаяНакладная/Templates/Чек/Template.mxlx
src/cf/src/Documents/НалоговаяНакладная/Templates/Счёт/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/Счёт/Template.mxlx
src/cf/src/Documents/СверкаВзаиморасчётов/Templates/АктСверки/Template.mxlx
src/cf/src/Documents/ЗаказПоставщику/Templates/ЗаказПоставщику/Template.mxlx
src/cf/src/Documents/СверкаВзаиморасчётов/Templates/АктСверкиБезНДС/Template.mxlx
src/cf/src/Documents/НалоговаяНакладная/Templates/РасходнаяНакладная/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/РасходнаяНакладная/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/DevisBL_A4/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/DevisBL/Template.mxlx
src/cf/src/Documents/НалоговаяНакладная/Templates/Facture/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/Facture/Template.mxlx
src/cf/src/Documents/НалоговаяНакладнаяПокупка/Templates/Facture/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/FactureModel/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/FactureModelEnTete/Template.mxlx
src/cf/src/Documents/РеализацияТоваровУслуг/Templates/FactureOld/Template.mxlx
src/cf/src/Documents/РасходныйКассовыйОрдер/Templates/LettreDePaiement/Template.mxlx
src/cf/src/InformationRegisters/ПользовательскиеМакетыПечати/Forms/МакетыПечатныхФорм/Module.bsl
src/cf/src/InformationRegisters/ПользовательскиеМакетыПечати/Forms/РедактированиеМакета/Module.bsl
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-12T08:48:56.247+01:00  INFO 87671 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/803 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/803 (0:00:01 / 0:01:28) Analyzing files...   8% [==                      ]  68/803 (0:00:02 / 0:00:21) Analyzing files...  21% [=====                   ] 171/803 (0:00:03 / 0:00:11) Analyzing files...  44% [==========              ] 361/803 (0:00:04 / 0:00:04) Analyzing files...  67% [================        ] 541/803 (0:00:05 / 0:00:02) Analyzing files...  87% [=====================   ] 705/803 (0:00:06 / 0:00:00) Analyzing files...  99% [======================= ] 802/803 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 803/803 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 803/803 (0:00:07 / 0:00:00) 
2026-10-12T08:49:06.456+01:00  INFO 87671 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 10
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
Языков: 4, пунктов изменений: 8
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.75.json
версия 2.0.16.75: ru=2, fr=2, en=2, es=2
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/branded-print.md
 M scripts/refcheck-known.txt
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
 D src/cf/src/CommonTemplates/АктОбОказанииУслуг/Template.mxlx
 D src/cf/src/CommonTemplates/АктОбОказанииУслуг/АктОбОказанииУслуг.mdo
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/СмокТест/Forms/Форма/Module.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ManagerModule.bsl
 D src/cf/src/Documents/ЗаказПоставщику/Templates/ЗаказПоставщику/Template.mxlx
 D src/cf/src/Documents/ЗаказПоставщику/Templates/ЗапросКотировок/Template.mxlx
 M src/cf/src/Documents/ЗаказПоставщику/ЗаказПоставщику.mdo
 M src/cf/src/Documents/НалоговаяНакладная/ManagerModule.bsl
 D src/cf/src/Documents/НалоговаяНакладная/Templates/Facture/Template.mxlx
 D src/cf/src/Documents/НалоговаяНакладная/Templates/РасходнаяНакладная/Template.mxlx
 D src/cf/src/Documents/НалоговаяНакладная/Templates/Счёт/Template.mxlx
 D src/cf/src/Documents/НалоговаяНакладная/Templates/Чек/Template.mxlx
 M src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/ManagerModule.bsl
 D src/cf/src/Documents/НалоговаяНакладнаяПокупка/Templates/Facture/Template.mxlx
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
 D src/cf/src/Documents/РасходныйКассовыйОрдер/Templates/LettreDePaiement/Template.mxlx
 M src/cf/src/Documents/РасходныйКассовыйОрдер/РасходныйКассовыйОрдер.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
 D src/cf/src/Documents/РеализацияТоваровУслуг/Templates/DevisBL/Template.mxlx
 D src/cf/src/Documents/РеализацияТоваровУслуг/Templates/DevisBL_A4/Template.mxlx
 D src/cf/src/Documents/РеализацияТоваровУслуг/Templates/Facture/Template.mxlx
 D src/cf/src/Documents/РеализацияТоваровУслуг/Templates/FactureModel/Template.mxlx
 D src/cf/src/Documents/РеализацияТоваровУслуг/Templates/FactureModelEnTete/Template.mxlx
 D src/cf/src/Documents/РеализацияТоваровУслуг/Templates/FactureOld/Template.mxlx
 D src/cf/src/Documents/РеализацияТоваровУслуг/Templates/РасходнаяНакладная/Template.mxlx
 D src/cf/src/Documents/РеализацияТоваровУслуг/Templates/Счёт/Template.mxlx
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 D src/cf/src/Documents/СверкаВзаиморасчётов/Templates/АктСверки/Template.mxlx
 D src/cf/src/Documents/СверкаВзаиморасчётов/Templates/АктСверкиБезНДС/Template.mxlx
 M src/cf/src/Documents/СверкаВзаиморасчётов/СверкаВзаиморасчётов.mdo
 M src/cf/src/InformationRegisters/ПользовательскиеМакетыПечати/Forms/МакетыПечатныхФорм/Module.bsl
 M src/cf/src/InformationRegisters/ПользовательскиеМакетыПечати/Forms/РедактированиеМакета/Module.bsl
?? .ai/reports/branded-print-s7-final-check.md
?? .ai/reviews/branded-print-s7/
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
2.0.16.74 → 2.0.16.75

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
