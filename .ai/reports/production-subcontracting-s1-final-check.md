# Final check — production-subcontracting-s1
_20260919T005112Z_


## Scope

```
.ai/reports/production-subcontracting-s1-final-check.md
.ai/reviews/production-subcontracting-s1/02-plan-review-claude.md
.ai/reviews/production-subcontracting-s1/03-code-review-claude.md
.ai/reviews/production-subcontracting-s1/04-database-review-claude.md
docs/MERGE-DRISSOTEX.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
src/cf/src/CommonModules/ТехнологическиеКарты/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
src/cf/src/Documents/ТехнологическаяКарта/ТехнологическаяКарта.mdo
src/cf/src/Documents/ТехнологическаяКарта/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
src/cf/src/Documents/ТехнологическаяКарта/ObjectModule.bsl
src/cf/src/Enums/СпособыИзготовления/СпособыИзготовления.mdo
src/cf/src/InformationRegisters/СоставТехКарты/СоставТехКарты.mdo
src/cf/src/InformationRegisters/СоставТехКарты/Forms/ФормаСписка/Form.form
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-09-19T01:51:21.136+01:00  INFO 43765 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/740 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/740 (0:00:01 / 0:01:22) Analyzing files...  15% [===                     ] 115/740 (0:00:02 / 0:00:10) Analyzing files...  43% [==========              ] 323/740 (0:00:03 / 0:00:03) Analyzing files...  70% [================        ] 521/740 (0:00:04 / 0:00:01) Analyzing files...  88% [=====================   ] 657/740 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 740/740 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 740/740 (0:00:05 / 0:00:00) 
2026-09-19T01:51:29.661+01:00  INFO 43765 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-08-26 14:06:31; изменённых модулей: 7
Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl: TransferringParametersBetweenClientAndServer +1 (было 1, стало 2)
    86: Установите модификатор "Знач" для параметра ТипНоменклатуры метода СпособПополненияПоУмолчаниюНаСервере
    312: Установите модификатор "Знач" для параметра ID метода УдалитьИзображениеНаСервере
Documents/ЗаказПокупателя/ObjectModule.bsl: EventHandlerOutsideEventRegion +2 (было 5, стало 7)
    2: Метод "ОбработкаЗаполнения" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    62: Метод "ПриКопировании" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
    67: Метод "ПередЗаписью" — обработчик платформенного события и должен находиться в стандартной области «Обработчики событий»
Documents/ЗаказПокупателя/ObjectModule.bsl: SetPrivilegedMode +1 (было 0, стало 1)
    956: Проверьте установку привилегированного режима
Documents/ТехнологическаяКарта/ObjectModule.bsl: SetPrivilegedMode +1 (было 0, стало 1)
    42: Проверьте установку привилегированного режима
Documents/ТехнологическаяКарта/ObjectModule.bsl: YoLetterUsage +2 (было 0, стало 2)
    109: В текстах модулях не допускается использовать букву "Ё".
    55: В текстах модулях не допускается использовать букву "Ё".
```
**FAIL**
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
Языков: 4, пунктов изменений: 24
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.15.39.json
версия 2.0.15.39: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
A  .ai/reviews/production-subcontracting-s1/02-plan-review-claude.md
A  .ai/reviews/production-subcontracting-s1/03-code-review-claude.md
A  .ai/reviews/production-subcontracting-s1/04-database-review-claude.md
M  docs/MERGE-DRISSOTEX.md
M  docs/TESTING.md
M  docs/TESTS.xlsx
M  src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Form.form
M  src/cf/src/Catalogs/Номенклатура/Forms/ФормаЭлемента/Module.bsl
M  src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
M  src/cf/src/CommonModules/ТехнологическиеКарты/Module.bsl
M  src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
M  src/cf/src/Configuration/Configuration.mdo
M  src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
M  src/cf/src/DataProcessors/АРМПроизводство/ManagerModule.bsl
M  src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
M  src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
M  src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
M  src/cf/src/Documents/ТехнологическаяКарта/Forms/ФормаДокумента/Form.form
M  src/cf/src/Documents/ТехнологическаяКарта/ObjectModule.bsl
M  src/cf/src/Documents/ТехнологическаяКарта/ТехнологическаяКарта.mdo
A  src/cf/src/Enums/СпособыИзготовления/СпособыИзготовления.mdo
M  src/cf/src/InformationRegisters/СоставТехКарты/Forms/ФормаСписка/Form.form
M  src/cf/src/InformationRegisters/СоставТехКарты/СоставТехКарты.mdo
?? .ai/reports/production-subcontracting-s1-final-check.md
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
2.0.15.38 → 2.0.15.39

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 5, FAIL: 1)

Провалились:
  - уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**FAILURES ABOVE** — do not report the task done until resolved.
