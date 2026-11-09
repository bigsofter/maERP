# Final check — warehouse-orders-p2
_20261015T000819Z_


## Scope

```
.ai/reports/warehouse-orders-p2-final-check.md
.ai/reviews/warehouse-orders-p2/03-code-review.json
.ai/reviews/warehouse-orders-p2/03b-code-review-verify.json
.ai/reviews/warehouse-orders-p2/04-database-review-r1.json
.ai/reviews/warehouse-orders-p2/04-database-review-r2.json
.ai/reviews/warehouse-orders-p2/04-database-review-r3.json
.ai/reviews/warehouse-orders-p2/04-database-review-r4.json
.ai/reviews/warehouse-orders-p2/04-database-review-r5.json
.ai/reviews/warehouse-orders-p2/04-database-review-r6.json
.ai/reviews/warehouse-orders-p2/04-database-review-r7.json
.ai/reviews/warehouse-orders-p2/04-database-review-r8.json
.ai/reviews/warehouse-orders-p2/04-database-review-r9.json
.ai/reviews/warehouse-orders-p2/04-database-review.json
.ai/reviews/warehouse-orders-p2/05-security-review-r1.json
.ai/reviews/warehouse-orders-p2/05-security-review.json
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
scripts/formgen/warehouse-orders/gen_forms.py
scripts/formgen/warehouse-orders/gen_mdo.py
scripts/formgen/warehouse-orders/pages.py
src/cf/src/AccumulationRegisters/ТоварыКОформлению/ТоварыКОформлению.mdo
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ЗаказыПоставщикам/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
src/cf/src/Catalogs/МестаХранения/МестаХранения.mdo
src/cf/src/Catalogs/МестаХранения/Forms/ФормаЭлемента/Form.form
src/cf/src/Catalogs/МестаХранения/Forms/ФормаЭлемента/Module.bsl
src/cf/src/Catalogs/МестаХранения/ManagerModule.bsl
src/cf/src/Catalogs/МестаХранения/ObjectModule.bsl
src/cf/src/Catalogs/ПроизводственноеОборудование/ObjectModule.bsl
src/cf/src/CommonModules/ОрдераСклада/ОрдераСклада.mdo
src/cf/src/CommonModules/ОрдераСклада/Module.bsl
src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
src/cf/src/Documents/ПриходныйОрдер/ПриходныйОрдер.mdo
src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
src/cf/src/Documents/ПриходныйОрдер/Commands/ПечатьПриходныйОрдер/CommandModule.bsl
src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Form.form
src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Module.bsl
src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПриходныйОрдер/ManagerModule.bsl
src/cf/src/Documents/ПриходныйОрдер/ObjectModule.bsl
src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/Руководитель/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Subsystems/Склад/Склад.mdo
src/cf/src/Subsystems/Склад/CommandInterface.cmi
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-15T01:08:25.990+01:00  INFO 55538 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/817 (0:00:00 / ?) Analyzing files...   6% [=                       ]  53/817 (0:00:01 / 0:00:14) Analyzing files...  17% [====                    ] 145/817 (0:00:02 / 0:00:09) Analyzing files...  34% [========                ] 283/817 (0:00:03 / 0:00:05) Analyzing files...  50% [============            ] 411/817 (0:00:04 / 0:00:03) Analyzing files...  69% [================        ] 570/817 (0:00:05 / 0:00:02) Analyzing files... 100% [========================] 817/817 (0:00:05 / 0:00:00) Analyzing files... 100% [========================] 817/817 (0:00:05 / 0:00:00) 
2026-10-15T01:08:34.469+01:00  INFO 55538 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 27
CommonModules/ПроизводственныеЗаказы/Module.bsl: SetPrivilegedMode +1 (было 4, стало 5)
    19: Проверьте установку привилегированного режима
    40: Проверьте установку привилегированного режима
    61: Проверьте установку привилегированного режима
Documents/РеализацияТоваровУслуг/ObjectModule.bsl: SetPrivilegedMode +1 (было 2, стало 3)
    3: Проверьте установку привилегированного режима
    65: Проверьте установку привилегированного режима
    300: Проверьте установку привилегированного режима
```
**FAIL**
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
Языков: 4, пунктов изменений: 40
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.77.json
версия 2.0.16.77: ru=10, fr=10, en=10, es=10
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M src/cf/src/AccumulationRegisters/ЗаказыПоставщикам/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ПотребностиПроизводства/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 A src/cf/src/AccumulationRegisters/ТоварыКОформлению/ManagerModule.bsl
 A src/cf/src/AccumulationRegisters/ТоварыКОформлению/ТоварыКОформлению.mdo
 M src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
 M src/cf/src/Catalogs/МестаХранения/Forms/ФормаЭлемента/Form.form
 M src/cf/src/Catalogs/МестаХранения/Forms/ФормаЭлемента/Module.bsl
 M src/cf/src/Catalogs/МестаХранения/ManagerModule.bsl
 M src/cf/src/Catalogs/МестаХранения/ObjectModule.bsl
 M src/cf/src/Catalogs/МестаХранения/МестаХранения.mdo
 M src/cf/src/Catalogs/ПроизводственноеОборудование/ObjectModule.bsl
 A src/cf/src/CommonModules/ОрдераСклада/Module.bsl
 A src/cf/src/CommonModules/ОрдераСклада/ОрдераСклада.mdo
 M src/cf/src/CommonModules/ПечатныеФормы/Module.bsl
 M src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
 M src/cf/src/CommonModules/Производство/Module.bsl
 M src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
 M src/cf/src/CommonModules/ФирменнаяПечать/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/VentesEnDetail/Forms/Form/Module.bsl
 M src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
 M src/cf/src/DataProcessors/Дашборд/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
 A src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаДокумента/Form.form
 A src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаДокумента/Module.bsl
 A src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Form.form
 A src/cf/src/Documents/ПриходныйОрдер/Forms/ФормаСписка/Module.bsl
 A src/cf/src/Documents/ПриходныйОрдер/ManagerModule.bsl
 A src/cf/src/Documents/ПриходныйОрдер/ObjectModule.bsl
 A src/cf/src/Documents/ПриходныйОрдер/ПриходныйОрдер.mdo
 A src/cf/src/Documents/РасходныйОрдер/Forms/ФормаДокумента/Form.form
 A src/cf/src/Documents/РасходныйОрдер/Forms/ФормаДокумента/Module.bsl
 A src/cf/src/Documents/РасходныйОрдер/Forms/ФормаСписка/Form.form
 A src/cf/src/Documents/РасходныйОрдер/Forms/ФормаСписка/Module.bsl
 A src/cf/src/Documents/РасходныйОрдер/ManagerModule.bsl
 A src/cf/src/Documents/РасходныйОрдер/ObjectModule.bsl
 A src/cf/src/Documents/РасходныйОрдер/РасходныйОрдер.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Roles/Руководитель/Rights.rights
 M src/cf/src/Subsystems/Склад/CommandInterface.cmi
 M src/cf/src/Subsystems/Склад/Склад.mdo
?? .ai/reports/warehouse-orders-p2-final-check.md
?? .ai/reviews/warehouse-orders-p2/
?? scripts/formgen/warehouse-orders/
?? src/cf/src/Documents/ПриходныйОрдер/Commands/
?? src/cf/src/Documents/РасходныйОрдер/Commands/
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
+// BSLLS:SetPrivilegedMode-off
+// BSLLS:DataExchangeLoading-off
+// BSLLS:SetPrivilegedMode-off
+// BSLLS:SetPrivilegedMode-on
+// BSLLS:DataExchangeLoading-on
+// пользователь. BSLLS:SetPrivilegedMode-off
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+// BSLLS:SetPrivilegedMode-off
+// BSLLS:EventHandlerOutsideEventRegion-off
+// BSLLS:EventHandlerOutsideEventRegion-on
+// BSLLS:SetPrivilegedMode-on
+	// BSLLS:MagicNumber-off - треть секунды, константа имени не добавит.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - размер страницы, используется только здесь.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - треть секунды, константа имени не добавит.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.76 → 2.0.16.77

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
