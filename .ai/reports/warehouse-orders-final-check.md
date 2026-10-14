# Final check — warehouse-orders
_20261014T195822Z_


## Scope

```
.ai/reports/warehouse-orders-final-check.md
.ai/reviews/warehouse-orders/01-explore-phase2-claude.md
.ai/reviews/warehouse-orders/02-plan-review-p1-r1.json
.ai/reviews/warehouse-orders/02-plan-review-p1-r2.json
.ai/reviews/warehouse-orders/02-plan-review-p1-r3.json
.ai/reviews/warehouse-orders/02-plan-review.json
.ai/reviews/warehouse-orders/03-code-review.json
.ai/reviews/warehouse-orders/03b-code-review-verify-r2.json
.ai/reviews/warehouse-orders/03b-code-review-verify.json
.ai/reviews/warehouse-orders/04-database-review.json
.ai/reviews/warehouse-orders/05-security-review-r1.json
.ai/reviews/warehouse-orders/05-security-review-r2.json
.ai/reviews/warehouse-orders/05-security-review-r3.json
.ai/reviews/warehouse-orders/05-security-review.json
docs/plans/warehouse-orders.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
docs/TESTS.xlsx
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ТоварыНаСкладах.mdo
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыВНаличии/RecordSetModule.bsl
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/RecordSetModule.bsl
src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
src/cf/src/Catalogs/СерииНоменклатуры/Forms/ВыборСерииПоОстаткам/Form.form
src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock/Module.bsl
src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
src/cf/src/CommonModules/Производство/Module.bsl
src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
src/cf/src/CommonModules/СерииИРазмещение/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммы/Module.bsl
src/cf/src/CommonModules/ТехнологическиеКарты/Module.bsl
src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ПечатьЭтикеток/Forms/ВыборСерииПоОстаткам/Form.form
src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Form.form
src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/Forms/Форма/Module.bsl
src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/АктРазбора/АктРазбора.mdo
src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
src/cf/src/Documents/КорректировкаРегистров/КорректировкаРегистров.mdo
src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаВыбораРегистра/Module.bsl
src/cf/src/Documents/ПересчётТоваров/ManagerModule.bsl
src/cf/src/Documents/КорректировкаРегистров/ObjectModule.bsl
src/cf/src/Reports/ТоварыДляЗаказа/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/НедостаточныеЗапасы/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ОтчетПоНедостаткамТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Roles/Логист/Rights.rights
src/cf/src/Roles/Казначей/Rights.rights
src/cf/src/Roles/Кладовщик/Rights.rights
src/cf/src/Roles/Руководитель/Rights.rights
src/cf/src/Roles/ЛичныйКабинет/Rights.rights
src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
src/cf/src/Roles/ОператорПроизводства/Rights.rights
src/cf/src/Roles/MobileClient/Rights.rights
src/cf/src/Roles/PDV/Rights.rights
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-14T20:58:30.743+01:00  INFO 51291 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/805 (0:00:00 / ?) Analyzing files...   1% [                        ]   9/805 (0:00:01 / 0:01:28) Analyzing files...   5% [=                       ]  46/805 (0:00:02 / 0:00:33) Analyzing files...  19% [====                    ] 155/805 (0:00:03 / 0:00:12) Analyzing files...  34% [========                ] 280/805 (0:00:04 / 0:00:07) Analyzing files...  48% [===========             ] 391/805 (0:00:05 / 0:00:05) Analyzing files...  67% [================        ] 544/805 (0:00:06 / 0:00:02) Analyzing files...  81% [===================     ] 658/805 (0:00:07 / 0:00:01) Analyzing files... 100% [========================] 805/805 (0:00:07 / 0:00:00) Analyzing files... 100% [========================] 805/805 (0:00:07 / 0:00:00) 
2026-10-14T20:58:42.357+01:00  INFO 51291 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-02 16:05:23; изменённых модулей: 27
CommonModules/РаботаСДокументами/Module.bsl: SetPrivilegedMode +1 (было 4, стало 5)
    5: Проверьте установку привилегированного режима
    297: Проверьте установку привилегированного режима
    388: Проверьте установку привилегированного режима
CommonModules/ПроизводственныеЗаказы/Module.bsl: SetPrivilegedMode +1 (было 4, стало 5)
    19: Проверьте установку привилегированного режима
    40: Проверьте установку привилегированного режима
    61: Проверьте установку привилегированного режима
CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl: CognitiveComplexity +1 (было 2, стало 3)
    230: Уменьшите когнитивную сложность "ПолучитьДанныеНоменклатуры" с 16 до 15
    317: Уменьшите когнитивную сложность "ПолучитьЦенуНоменклатуры" с 18 до 15
    695: Уменьшите когнитивную сложность "УстановитьНастройкиОтчёта" с 26 до 15
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
Языков: 4, пунктов изменений: 16
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.76.json
версия 2.0.16.76: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M .ai/reviews/warehouse-orders/02-plan-review.json
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M docs/TESTS.xlsx
 M docs/plans/warehouse-orders.md
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/RecordSetModule.bsl
 A src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
 A src/cf/src/AccumulationRegisters/ТоварыНаСкладах/RecordSetModule.bsl
 A src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ТоварыНаСкладах.mdo
 M src/cf/src/Catalogs/Номенклатура/Forms/FormProduitsOnStock/Module.bsl
 M src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
 M src/cf/src/Catalogs/Номенклатура/ManagerModule.bsl
 M src/cf/src/Catalogs/СерииНоменклатуры/Forms/ВыборСерииПоОстаткам/Form.form
 M src/cf/src/CommonModules/ЗагрузкаСтанков/Module.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммы/Module.bsl
 M src/cf/src/CommonModules/ОбновлениеПрограммыОбработчики/Module.bsl
 M src/cf/src/CommonModules/ОбщегоНазначенияВызовСервера/Module.bsl
 M src/cf/src/CommonModules/ПроизводственныеЗаказы/Module.bsl
 M src/cf/src/CommonModules/Производство/Module.bsl
 M src/cf/src/CommonModules/ПроцедурыРегламентныхЗаданий/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonModules/СерииИРазмещение/Module.bsl
 M src/cf/src/CommonModules/ТехнологическиеКарты/Module.bsl
 M src/cf/src/CommonModules/ТребованияНакладные/Module.bsl
 M src/cf/src/CommonModules/УправляемыеБлокировки/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/АРМЗакупки/ManagerModule.bsl
 M src/cf/src/DataProcessors/ЛичныйКабинетПартнера/Forms/ФормаНоменклатура/Form.form
 M src/cf/src/DataProcessors/ПечатьЭтикеток/Forms/ВыборСерииПоОстаткам/Form.form
 M src/cf/src/DataProcessors/ТестовыеДанные/ManagerModule.bsl
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/DataProcessors/ФормированиеЗаказовПоставщику/Forms/Форма/Module.bsl
 M src/cf/src/Documents/АктРазбора/АктРазбора.mdo
 M src/cf/src/Documents/ВозвратОтПокупателя/ВозвратОтПокупателя.mdo
 M src/cf/src/Documents/ВозвратОтПокупателяНалоговый/ВозвратОтПокупателяНалоговый.mdo
 M src/cf/src/Documents/ВозвратПоставщику/ВозвратПоставщику.mdo
 M src/cf/src/Documents/ВозвратПоставщикуНалоговый/ВозвратПоставщикуНалоговый.mdo
 M src/cf/src/Documents/ВыпускПродукции/ВыпускПродукции.mdo
 M src/cf/src/Documents/ЗаказПокупателя/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ЗаказПоставщику/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаВыбораРегистра/Module.bsl
 M src/cf/src/Documents/КорректировкаРегистров/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/КорректировкаРегистров/ObjectModule.bsl
 M src/cf/src/Documents/КорректировкаРегистров/КорректировкаРегистров.mdo
 M src/cf/src/Documents/НалоговаяНакладная/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/НалоговаяНакладная/НалоговаяНакладная.mdo
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/НалоговаяНакладнаяПокупка.mdo
 M src/cf/src/Documents/ОприходованиеТоваров/ОприходованиеТоваров.mdo
 M src/cf/src/Documents/ПередачаВПереработку/ПередачаВПереработку.mdo
 M src/cf/src/Documents/ПеремещениеТоваров/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПеремещениеТоваров/ПеремещениеТоваров.mdo
 M src/cf/src/Documents/ПересортицаТоваров/ПересортицаТоваров.mdo
 M src/cf/src/Documents/ПересчётТоваров/ManagerModule.bsl
 M src/cf/src/Documents/ПоступлениеИзПереработки/ПоступлениеИзПереработки.mdo
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Documents/СписаниеТоваров/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/СписаниеТоваров/СписаниеТоваров.mdo
 M src/cf/src/Documents/ТребованиеНакладная/ТребованиеНакладная.mdo
 M src/cf/src/Reports/НедостаточныеЗапасы/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОтчетПоНедостаткамТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыДляЗаказа/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Roles/MobileClient/Rights.rights
 M src/cf/src/Roles/PDV/Rights.rights
 M src/cf/src/Roles/БухгалтерПоЗарплате/Rights.rights
 M src/cf/src/Roles/Казначей/Rights.rights
 M src/cf/src/Roles/Кладовщик/Rights.rights
 M src/cf/src/Roles/ЛичныйКабинет/Rights.rights
 M src/cf/src/Roles/Логист/Rights.rights
 M src/cf/src/Roles/МенеджерПоЗакупкам/Rights.rights
 M src/cf/src/Roles/МенеджерПоПродажам/Rights.rights
 M src/cf/src/Roles/Оператор/Rights.rights
 M src/cf/src/Roles/ОператорПроизводства/Rights.rights
 M src/cf/src/Roles/Руководитель/Rights.rights
?? .ai/reports/warehouse-orders-final-check.md
?? .ai/reviews/warehouse-orders/01-explore-phase2-claude.md
?? .ai/reviews/warehouse-orders/02-plan-review-p1-r1.json
?? .ai/reviews/warehouse-orders/02-plan-review-p1-r2.json
?? .ai/reviews/warehouse-orders/02-plan-review-p1-r3.json
?? .ai/reviews/warehouse-orders/03-code-review.json
?? .ai/reviews/warehouse-orders/03b-code-review-verify-r2.json
?? .ai/reviews/warehouse-orders/03b-code-review-verify.json
?? .ai/reviews/warehouse-orders/04-database-review.json
?? .ai/reviews/warehouse-orders/05-security-review-r1.json
?? .ai/reviews/warehouse-orders/05-security-review-r2.json
?? .ai/reviews/warehouse-orders/05-security-review-r3.json
?? .ai/reviews/warehouse-orders/05-security-review.json
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
+// выдаются (ворота - право записи ТоварыВНаличии). BSLLS:SetPrivilegedMode-off
+// независимо от прав роли. BSLLS:SetPrivilegedMode-off
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - количества сценария.
+	// BSLLS:MagicNumber-on
+	// BSLLS:MagicNumber-off - минимум 5, остатки сценария.
+	// BSLLS:MagicNumber-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.75 → 2.0.16.76

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
