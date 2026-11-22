# Final check — arm-purchasing-view-tab
_20261122T101215Z_


## Scope

```
.ai/reports/arm-purchasing-view-tab-acceptance.md
.ai/reports/arm-purchasing-view-tab-final-check.md
docs/.!95431!TESTS.xlsx
docs/plans/order-payment-state.md
docs/TESTING.md
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
tests/ui/core.bsl
tests/ui/scenarios.txt
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-11-22T11:12:27.959+01:00  INFO 9683 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/903 (0:00:00 / ?) Analyzing files...   0% [                        ]   9/903 (0:00:01 / 0:01:39) Analyzing files...   5% [=                       ]  52/903 (0:00:02 / 0:00:32) Analyzing files...  14% [===                     ] 129/903 (0:00:03 / 0:00:18) Analyzing files...  22% [=====                   ] 201/903 (0:00:04 / 0:00:13) Analyzing files...  33% [=======                 ] 300/903 (0:00:05 / 0:00:10) Analyzing files...  40% [=========               ] 366/903 (0:00:06 / 0:00:08) Analyzing files...  43% [==========              ] 390/903 (0:00:07 / 0:00:09) Analyzing files...  47% [===========             ] 430/903 (0:00:08 / 0:00:08) Analyzing files...  54% [=============           ] 493/903 (0:00:09 / 0:00:07) Analyzing files...  58% [==============          ] 529/903 (0:00:10 / 0:00:07) Analyzing files...  59% [==============          ] 540/903 (0:00:11 / 0:00:07) Analyzing files...  60% [==============          ] 548/903 (0:00:13 / 0:00:08) Analyzing files...  62% [===============         ] 568/903 (0:00:16 / 0:00:09) Analyzing files...  66% [===============         ] 596/903 (0:00:17 / 0:00:08) Analyzing files...  69% [================        ] 632/903 (0:00:18 / 0:00:07) Analyzing files...  71% [=================       ] 645/903 (0:00:19 / 0:00:07) Analyzing files...  75% [==================      ] 686/903 (0:00:20 / 0:00:06) Analyzing files...  80% [===================     ] 725/903 (0:00:21 / 0:00:05) Analyzing files...  84% [====================    ] 759/903 (0:00:22 / 0:00:04) Analyzing files...  89% [=====================   ] 809/903 (0:00:23 / 0:00:02) Analyzing files...  94% [======================  ] 850/903 (0:00:24 / 0:00:01) Analyzing files...  99% [======================= ] 901/903 (0:00:25 / 0:00:00) Analyzing files... 100% [========================] 903/903 (0:00:25 / 0:00:00) Analyzing files... 100% [========================] 903/903 (0:00:25 / 0:00:00) 
2026-11-22T11:12:58.932+01:00  INFO 9683 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 1
DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl: MissingParameterDescription +1 (было 0, стало 1)
    2811: Необходимо добавить описание всех параметров метода
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.18.3.json
версия 2.0.18.3: ru=5, fr=5, en=5, es=5
```
**PASS**
### приёмка: scripts/acceptcheck.py .ai/reports/arm-purchasing-view-tab-acceptance.md
```
Приёмка не закрыта (.ai/reports/arm-purchasing-view-tab-acceptance.md):
  - «Критерии приёмки»: «В панели справа рабочего места закупок две закладки: «Фильтры» и «Вид». На закладке «Потребность» поле «Группировка» стоит на «Вид», над таблицей его нет» - статус «не закрыт»
  - «Критерии приёмки»: «На закладке «Вид» при любой верхней закладке есть кнопка настройки колонок; она открывает штатное окно настройки формы, где меняются порядок и видимость колонок» - статус «не закрыт»
  - «Критерии приёмки»: «Выбранная группировка «Потребности» после закрытия и повторного открытия рабочего места та же» - статус «не закрыт»
  - «Критерии приёмки»: «Рабочее место открывается на той верхней закладке, на которой пользователь его закрыл, независимо от настройки пользователя «Товары / накладные»» - статус «не закрыт»
  - «Критерии приёмки»: «Вверху есть отдельная закладка «Поступившие товары» со строками товаров поступлений; ввод строки на ней работает как раньше в режиме «Товары» (единица подставляется после выбора товара)» - статус «не закрыт»
  - «Критерии приёмки»: «На закладке «Поступления» только список документов; переключателя «Документы / Товары» нет ни над таблицей, ни в панели» - статус «не закрыт»
  - «Критерии приёмки»: «В таблицах «Потребность» и «Заказы поставщикам» нет колонки-переключателя с пометкой; строки отмечаются штатным выделением платформы» - статус «не закрыт»
  - «Критерии приёмки»: «Кнопки «Заказать», «Создать поступление» и «Запросить предложения» стоят в командной панели таблицы «Потребность», а не отдельной строкой над ней, и остаются в панели, когда строки отмечены флажком выделения» - статус «не закрыт»
  - «Критерии приёмки»: ««Заказать» по двум выделенным строкам «Потребности» создаёт заказы поставщикам по обеим строкам; без выделенной строки с количеством «к заказу» ничего не создаётся» - статус «не закрыт»
  - «Критерии приёмки»: ««Создать поступление» на закладке «Заказы поставщикам» работает по выделенным заказам» - статус «не закрыт»
  - «Критерии приёмки»: «При выделении нескольких строк «Потребности» таблица не моргает, значения ячеек не меняются, нижние закладки не перечитываются» - статус «не закрыт»
  - «Однотипные объекты»: «Обработка.АРМЗакупки.Форма» - статус «не закрыт»
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
 M docs/TESTING.md
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Form.form
 M src/cf/src/DataProcessors/АРМЗакупки/Forms/Форма/Module.bsl
 M tests/ui/core.bsl
 M tests/ui/scenarios.txt
?? .ai/reports/arm-purchasing-view-tab-acceptance.md
?? .ai/reports/arm-purchasing-view-tab-final-check.md
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
none found

### Версия конфигурации
2.0.18.2 → 2.0.18.3

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 идут на базе гейта build/ib-gate через scripts/gate.sh; сборка сдаётся только со штампом на текущее дерево src/cf

## Gates run

Запущено гейтов: 12 (PASS: 9, FAIL: 3)

Провалились:
  - уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
  - приёмка: scripts/acceptcheck.py .ai/reports/arm-purchasing-view-tab-acceptance.md
  - карта архитектуры актуальна: scripts/archmap.py --check (обновить: python3 scripts/archmap.py)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (смок, тесты документов) — штампа scripts/gate.sh на текущее дерево src/cf нет: НА БАЗЕ НЕ ПРОВЕРЕНО

## Verdict

**FAILURES ABOVE** — do not report the task done until resolved.
