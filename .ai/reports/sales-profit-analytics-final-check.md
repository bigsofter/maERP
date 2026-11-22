# Final check — sales-profit-analytics
_20261122T144651Z_


## Scope

```
.ai/reports/sales-profit-analytics-acceptance.md
.ai/reports/sales-profit-analytics-final-check.md
.ai/reviews/sales-profit-analytics/02-plan-review.json
.ai/reviews/sales-profit-analytics/03-code-review.json
docs/.!95431!TESTS.xlsx
docs/ARCHITECTURE.md
docs/plans/order-payment-state.md
docs/plans/sales-profit-analytics.md
docs/ROADMAP.md
docs/TECHDEBT.md
scripts/smoke-floor.txt
src/cf/src/AccumulationRegisters/СебестоимостьПродаж/ManagerModule.bsl
src/cf/src/CommonModules/КонтрольЦенПродажи/Module.bsl
src/cf/src/CommonModules/РаботаСДокументамиВызовСервера/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/Дашборд/Forms/ДашбордПродаж/Module.bsl
src/cf/src/DataProcessors/Дашборд/Forms/БазовыйДашборд/Module.bsl
src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Reports/ВедомостьПоПродажам/ВедомостьПоПродажам.mdo
src/cf/src/Reports/ВедомостьПоПродажам/Commands/ПрибыльПоДокументам/CommandModule.bsl
src/cf/src/Reports/ВедомостьПоПродажам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-22T15:46:57.614+01:00  INFO 38093 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/904 (0:00:00 / ?) Analyzing files...   6% [=                       ]  55/904 (0:00:01 / 0:00:15) Analyzing files...  20% [====                    ] 183/904 (0:00:02 / 0:00:07) Analyzing files...  35% [========                ] 319/904 (0:00:03 / 0:00:05) Analyzing files...  52% [============            ] 471/904 (0:00:04 / 0:00:03) Analyzing files...  65% [===============         ] 593/904 (0:00:05 / 0:00:02) Analyzing files...  82% [===================     ] 744/904 (0:00:06 / 0:00:01) Analyzing files...  91% [=====================   ] 828/904 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 904/904 (0:00:08 / 0:00:00) Analyzing files... 100% [========================] 904/904 (0:00:08 / 0:00:00) 
2026-11-22T15:47:08.437+01:00  INFO 38093 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 10
DataProcessors/ТестыДокументов/ManagerModule.bsl: UnusedLocalVariable +1 (было 0, стало 1)
    23931: Удалите неиспользуемую переменную Номер
```
**FAIL**
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
### уровень 0.85: scripts/navcheck.py
```
Сверка навигации форм: ссылка «Файлы» скрыта во всех формах документов (форм — 50)
```
**PASS**
### уровень 0.9: scripts/colfont.py (шрифт шапки колонок)
```
Колонки без шрифта шапки: 0 (в формах 0); с titleFont: 2767
```
**PASS**
### уровень 0.95: scripts/menucheck.py (фактическое меню разделов)
```

Сверка меню: подсистем 45, расхождений сверх базы 0, протухших строк базы 0
```
**PASS**
### ОписаниеИзменений: секция текущей версии на ru/fr/en/es
```
Языков: 4, пунктов изменений: 20
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.18.4.json
версия 2.0.18.4: ru=5, fr=5, en=5, es=5
```
**PASS**
### приёмка: scripts/acceptcheck.py .ai/reports/sales-profit-analytics-acceptance.md
```
Приёмка не закрыта (.ai/reports/sales-profit-analytics-acceptance.md):
  - «Критерии приёмки»: «В списке реализаций в шапке формы есть подменю «Отчёты» с командой «Прибыль по документам»; по выделенной реализации открывается отчёт по этому документу с разбивкой по товарам: количество, выручка без НДС, себестоимость, прибыль, наценка» - статус «не закрыт»
  - «Критерии приёмки»: «Та же команда по нескольким отмеченным реализациям открывает отчёт по всем отмеченным; команда остаётся доступной, когда строки отмечены флажком» - статус «не закрыт»
  - «Критерии приёмки»: «В форме реализации та же команда в подменю «Отчёты» открывает отчёт по текущему документу» - статус «не закрыт»
  - «Критерии приёмки»: «В списке и в форме налоговой накладной команда открывает отчёт по продажам этой накладной (основание и отгрузки строк)» - статус «не закрыт»
  - «Критерии приёмки»: «Прибыль документа в отчёте равна прибыли, которую до сборки показывал итог внизу формы реализации (выручка без НДС минус себестоимость)» - статус «не закрыт»
  - «Критерии приёмки»: «В формах реализации и налоговой накладной внизу нет полей «Себестоимость», «Выручка (без НДС)», «Прибыль», «Наценка, %»; суммы документа (без НДС, НДС, всего) на месте» - статус «не закрыт»
  - «Критерии приёмки»: «В разделе «Продажи» у отчёта «Ведомость по продажам» есть варианты «Прибыль по документам» и «Продажи в минус»; вариант «Продажи в минус» показывает убыточный товар документа и не показывает прибыльный» - статус «не закрыт»
  - «Критерии приёмки»: «Пользователь без права на себестоимость продаж (личный кабинет, оператор производства) команды «Прибыль по документам» не видит» - статус «не закрыт»
  - «Критерии приёмки»: «На дашборде есть плитка «Продажи в минус за 7 дней» с числом и суммой; щелчок открывает вариант «Продажи в минус» за этот период; без права на себестоимость - прочерк» - статус «не закрыт»
  - «Критерии приёмки»: «В форме реализации на складе с контролем «не ниже себестоимости» строка с ценой ниже порога подсвечена до проведения; после исправления цены подсветка уходит» - статус «не закрыт»
  - «Критерии приёмки»: «Подсветка пересчитывается при изменении количества, скидки, суммы, склада, валюты и курса, после загрузки строк из Excel и пересчёта цен» - статус «не закрыт»
  - «Критерии приёмки»: «На складе без контроля минимальной цены строки не подсвечиваются; проведение реализации работает как раньше» - статус «не закрыт»
  - «Критерии приёмки»: «Колонки последних цен в строках реализации (закупка, продажа, наценка %) на месте и работают» - статус «не закрыт»
  - «Однотипные объекты»: «Документ.РеализацияТоваровУслуг.ФормаДокумента (итог, команда, подсветка)» - статус «не закрыт»
  - «Однотипные объекты»: «Документ.РеализацияТоваровУслуг.ФормаСписка (команда)» - статус «не закрыт»
  - «Однотипные объекты»: «Документ.НалоговаяНакладная.ФормаДокумента (итог, команда)» - статус «не закрыт»
  - «Однотипные объекты»: «Документ.НалоговаяНакладная.ФормаСписка (команда)» - статус «не закрыт»
  - «Однотипные объекты»: «Отчёт.ВедомостьПоПродажам (варианты)» - статус «не закрыт»
  - «Однотипные объекты»: «Обработка.Дашборд: стоковый дашборд и дашборд продаж (плитка)» - статус «не закрыт»
```
**FAIL**
### карта архитектуры актуальна: scripts/archmap.py --check (обновить: python3 scripts/archmap.py)
```
archmap: docs/ARCHITECTURE.md отстал от src/cf/src - запустите scripts/archmap.py
```
**FAIL**
### неслитые ветки с правками конфигурации: scripts/branchcheck.sh
```
Сверка веток: неслитых правок конфигурации нет (проверено веток: 18)
```
**PASS**

## Git hygiene

### git status
```
 A .ai/reports/sales-profit-analytics-acceptance.md
 M docs/ARCHITECTURE.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 A docs/plans/sales-profit-analytics.md
 M scripts/smoke-floor.txt
 M src/cf/src/AccumulationRegisters/СебестоимостьПродаж/ManagerModule.bsl
 M src/cf/src/CommonModules/КонтрольЦенПродажи/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументамиВызовСервера/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/Дашборд/Forms/БазовыйДашборд/Module.bsl
 M src/cf/src/DataProcessors/Дашборд/Forms/ДашбордПродаж/Module.bsl
 M src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 A src/cf/src/Reports/ВедомостьПоПродажам/Commands/ПрибыльПоДокументам/CommandModule.bsl
 M src/cf/src/Reports/ВедомостьПоПродажам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьПоПродажам/ВедомостьПоПродажам.mdo
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
?? .ai/reports/sales-profit-analytics-final-check.md
?? .ai/reviews/sales-profit-analytics/
?? docs/.!95431!TESTS.xlsx
?? docs/plans/order-payment-state.md
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
+	// BSLLS:SetPrivilegedMode-off
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:MagicNumber-off
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.18.3 → 2.0.18.4

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 идут на базе гейта build/ib-gate через scripts/gate.sh; сборка сдаётся только со штампом на текущее дерево src/cf

## Gates run

Запущено гейтов: 12 (PASS: 9, FAIL: 3)

Провалились:
  - уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
  - приёмка: scripts/acceptcheck.py .ai/reports/sales-profit-analytics-acceptance.md
  - карта архитектуры актуальна: scripts/archmap.py --check (обновить: python3 scripts/archmap.py)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (смок, тесты документов) — штампа scripts/gate.sh на текущее дерево src/cf нет: НА БАЗЕ НЕ ПРОВЕРЕНО

## Verdict

**FAILURES ABOVE** — do not report the task done until resolved.
