# Final check — branded-print-s2
_20261011T144701Z_


## Scope

```
.ai/reports/branded-print-phase2/kp-sale-goods-ru.png
.ai/reports/branded-print-phase2/kp-sale-mixed-es.png
.ai/reports/branded-print-phase2/kp-sale-mixed-fr.png
.ai/reports/branded-print-phase2/kp-sale-services-en.png
.ai/reports/branded-print-s2-final-check.md
.ai/reports/branded-print.md
.ai/reviews/branded-print-s2/02-plan-review-r1.json
.ai/reviews/branded-print-s2/02-plan-review-r2.json
.ai/reviews/branded-print-s2/02-plan-review-r3.json
.ai/reviews/branded-print-s2/02-plan-review.json
.ai/reviews/branded-print-s2/03-code-review.json
.ai/reviews/branded-print-s2/03b-code-review-verify.json
.ai/reviews/branded-print-s2/04-database-review.json
.ai/reviews/branded-print-s2/05-security-review.json
docs/plans/branded-print.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/kp-concurrency.sh
scripts/kp-concurrency/run.bsl
scripts/print-preview.sh
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
src/cf/src/Documents/ЗаказПокупателя/Commands/ПечатьКоммерческоеПредложение/CommandModule.bsl
src/cf/src/Documents/ЗаказПокупателя/Commands/ПечатьКоммерческоеПредложениеА4/CommandModule.bsl
src/cf/src/Documents/ЗаказПокупателя/Commands/ПечатьКоммерческоеПредложениеА4БезНДС/CommandModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Form.form
src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Form.form
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/КоммерческоеПредложение/ObjectModule.bsl
src/cf/src/FilterCriteria/СвязанныеДокументы/Forms/ФормаОтчета/Module.bsl
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-11T15:47:10.491+01:00  INFO 16972 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/802 (0:00:00 / ?) Analyzing files...   4% [=                       ]  34/802 (0:00:01 / 0:00:22) Analyzing files...  19% [====                    ] 155/802 (0:00:02 / 0:00:08) Analyzing files...  37% [========                ] 298/802 (0:00:03 / 0:00:05) Analyzing files...  56% [=============           ] 452/802 (0:00:04 / 0:00:03) Analyzing files...  76% [==================      ] 610/802 (0:00:05 / 0:00:01) Analyzing files...  98% [======================= ] 792/802 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 802/802 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 802/802 (0:00:06 / 0:00:00) 
2026-10-11T15:47:20.038+01:00  INFO 16972 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 16
Documents/ЗаказПокупателя/ObjectModule.bsl: SetPrivilegedMode +1 (было 1, стало 2)
    244: Проверьте установку привилегированного режима
    1209: Проверьте установку привилегированного режима
Documents/РеализацияТоваровУслуг/ObjectModule.bsl: SetPrivilegedMode +1 (было 2, стало 3)
    3: Проверьте установку привилегированного режима
    46: Проверьте установку привилегированного режима
    232: Проверьте установку привилегированного режима
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
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.69.json
версия 2.0.16.69: ru=6, fr=6, en=6, es=6
```
**PASS**

## Git hygiene

### git status
```
 M .ai/reports/branded-print.md
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/branded-print.md
 M scripts/print-preview.sh
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/СмокТест/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
D  src/cf/src/Documents/ЗаказПокупателя/Commands/ПечатьКоммерческоеПредложение/CommandModule.bsl
D  src/cf/src/Documents/ЗаказПокупателя/Commands/ПечатьКоммерческоеПредложениеА4/CommandModule.bsl
D  src/cf/src/Documents/ЗаказПокупателя/Commands/ПечатьКоммерческоеПредложениеА4БезНДС/CommandModule.bsl
D  src/cf/src/Documents/ЗаказПокупателя/Commands/ПечатьКоммерческоеПредложениеА4БезЦен/CommandModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ManagerModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ЗаказПокупателя/ЗаказПокупателя.mdo
 M src/cf/src/Documents/КоммерческоеПредложение/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/КоммерческоеПредложение/ManagerModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/ObjectModule.bsl
 M src/cf/src/Documents/КоммерческоеПредложение/КоммерческоеПредложение.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаСписка/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ManagerModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/FilterCriteria/СвязанныеДокументы/Forms/ФормаОтчета/Module.bsl
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/Казначей/Rights.rights
?? .ai/reports/branded-print-phase2/
?? .ai/reports/branded-print-s2-final-check.md
?? .ai/reviews/branded-print-s2/
?? scripts/kp-concurrency.sh
?? scripts/kp-concurrency/
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
+	// BSLLS:PairingBrokenTransaction-off
+	// BSLLS:WrongUseOfRollbackTransactionMethod-off
+		// BSLLS:WrongUseOfRollbackTransactionMethod-on
+		// BSLLS:PairingBrokenTransaction-on
+		// BSLLS:DeprecatedMethodCall-off
+		// BSLLS:DeprecatedMethodCall-on
+	// BSLLS:MagicNumber-off - длины текстов: вместе больше прежнего предела строки КП в 1024 знака.
+	// BSLLS:MagicNumber-on
+		// BSLLS:MagicNumber-off
+		// BSLLS:MagicNumber-on
+		// BSLLS:MagicNumber-off - количества и цены строк сценария.
+		// BSLLS:MagicNumber-on
+		// BSLLS:MagicNumber-off
+		// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - шесть цифр от миллисекунд: номер уникален в прогоне и короче 11 знаков.
+	// BSLLS:MagicNumber-on
+	// BSLLS:SetPrivilegedMode-off - читается только значение константы опции, наружу - Булево.
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:SetPrivilegedMode-off - протокол целиком (3.3, круг 3): реализацию пишут роли без прав на КП; вход -
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:MagicNumber-off - номера запросов пакета.
+	// BSLLS:MagicNumber-on
+	// BSLLS:SetPrivilegedMode-off - номер сверяется со всеми КП года, в том числе недоступными пользователю.
+	// BSLLS:SetPrivilegedMode-on
+	// BSLLS:IsInRoleMethod-off - то же ограничение, что скрывает суммы в форме реализации: привязано к роли.
+	// BSLLS:IsInRoleMethod-on
+	// BSLLS:SetPrivilegedMode-off - читаются только КП, найденные протоколом по реализациям, доступным пользователю.
+	// BSLLS:SetPrivilegedMode-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.68 → 2.0.16.69

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
