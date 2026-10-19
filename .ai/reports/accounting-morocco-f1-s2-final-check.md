# Final check — accounting-morocco-f1-s2
_20261019T013312Z_


## Scope

```
.ai/reports/accounting-morocco-f1-s2-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r1.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r10.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r11.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r12.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r13.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r14.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r15.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r16.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r17.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r2.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r3.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r4.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r5.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r6.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r7.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r8.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review-r9.json
.ai/reviews/accounting-morocco-f1-s2/02-plan-review.json
.ai/reviews/accounting-morocco-f1-s2/03-code-review.json
.ai/reviews/accounting-morocco-f1-s2/03b-code-review-verify-r1.json
.ai/reviews/accounting-morocco-f1-s2/03b-code-review-verify.json
.ai/reviews/accounting-morocco-f1-s2/03c-verify-note.md
.ai/reviews/accounting-morocco-f1-s2/04-database-review.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
docs/plans/accounting-morocco-f1-s2.md
docs/ROADMAP.md
docs/TECHDEBT.md
docs/TESTING.md
src/cf/src/AccumulationRegisters/Продажи/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/НалоговыеДокументыНаОснованиях.mdo
src/cf/src/CommonModules/НалоговыйУчет/Module.bsl
src/cf/src/CommonModules/ПодпискиНаСобытия/Module.bsl
src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/Module.bsl
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Form.form
src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ManagerModule.bsl
src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
src/cf/src/Documents/КорректировкаДолга/ObjectModule.bsl
src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
src/cf/src/Documents/НалоговаяНакладнаяПокупка/ObjectModule.bsl
src/cf/src/EventSubscriptions/ПлатежПередУдалением/ПлатежПередУдалением.mdo
src/cf/src/EventSubscriptions/ПрежниеОснованияОплатыПередЗаписью/ПрежниеОснованияОплатыПередЗаписью.mdo
```

## Gates

### уровень 0: scripts/lint.sh (BSL LS)
```
line 1:0 token recognition error at: '﻿'
line 1:0 token recognition error at: '﻿'
2026-10-19T02:33:20.152+01:00  INFO 66639 --- [BSL Language Server] [-types-warmup-1] _.b.l.t.r.PlatformContextProviderFactory : Loaded 2614 platform contexts from 1C syntax helper
Analyzing files...   0% [                              ]   0/822 (0:00:00 / ?) Analyzing files...   2% [                        ]  19/822 (0:00:01 / 0:00:42) Analyzing files...  14% [===                     ] 116/822 (0:00:02 / 0:00:12) Analyzing files...  32% [=======                 ] 266/822 (0:00:03 / 0:00:06) Analyzing files...  51% [============            ] 420/822 (0:00:04 / 0:00:03) Analyzing files...  78% [==================      ] 648/822 (0:00:05 / 0:00:01) Analyzing files...  98% [======================= ] 808/822 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 822/822 (0:00:06 / 0:00:00) Analyzing files... 100% [========================] 822/822 (0:00:06 / 0:00:00) 
2026-10-19T02:33:29.898+01:00  INFO 66639 --- [BSL Language Server] [           main] c.g._.b.l.reporters.JsonReporter         : JSON report saved to /Users/ivan-gurkin/Dev/maERP/build/./bsl-json.json
Отчёт: /Users/ivan-gurkin/Dev/maERP/build/bsl-json.json
```
**PASS**
### уровень 0: нет новых замечаний BSL LS против baseline в изменённых модулях
```
baseline: 2026-10-18 20:37:12; изменённых модулей: 18
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
Проверка динамических списков: расхождений нет (известных — 0)
```
**PASS**
### уровень 0.8: scripts/queryfields.py
```
Сверка полей запросов: расхождений нет (известных — 4)
```
**PASS**
### ОписаниеИзменений: секция текущей версии на ru/fr/en/es
```
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.97.json
версия 2.0.16.97: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/ROADMAP.md
 M docs/TECHDEBT.md
 M docs/TESTING.md
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПокупателями/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ВзаиморасчётыСПоставщиками/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/Продажи/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыВНаличии/ManagerModule.bsl
 M src/cf/src/AccumulationRegisters/ТоварыНаСкладах/ManagerModule.bsl
 M src/cf/src/CommonModules/НалоговыйУчет/Module.bsl
 M src/cf/src/CommonModules/ПодпискиНаСобытия/Module.bsl
 M src/cf/src/CommonModules/РаботаСДокументами/Module.bsl
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/DataProcessors/ТестыДокументов/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ManagerModule.bsl
 M src/cf/src/Documents/ВозвратОтПокупателя/ObjectModule.bsl
 M src/cf/src/Documents/ВозвратПоставщику/ObjectModule.bsl
 M src/cf/src/Documents/КорректировкаДолга/ObjectModule.bsl
 M src/cf/src/Documents/НалоговаяНакладная/ObjectModule.bsl
 M src/cf/src/Documents/НалоговаяНакладнаяПокупка/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/ПоступлениеТоваровУслуг/ПоступлениеТоваровУслуг.mdo
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Form.form
 M src/cf/src/Documents/РеализацияТоваровУслуг/Forms/ФормаДокумента/Module.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/ObjectModule.bsl
 M src/cf/src/Documents/РеализацияТоваровУслуг/РеализацияТоваровУслуг.mdo
 M src/cf/src/Documents/СертификатНаОплату/ObjectModule.bsl
?? .ai/reports/accounting-morocco-f1-s2-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reviews/accounting-morocco-f1-s2/
?? .ai/reviews/machine-form/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/wo-techdebt2/
?? docs/plans/accounting-morocco-f1-s2.md
?? src/cf/src/CommonModules/НалоговыеДокументыНаОснованиях/
?? src/cf/src/EventSubscriptions/ПлатежПередУдалением/
?? src/cf/src/EventSubscriptions/ПрежниеОснованияОплатыПередЗаписью/
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
+	// BSLLS:JoinWithVirtualTable-off
+	// BSLLS:JoinWithSubQuery-off
+	// BSLLS:JoinWithVirtualTable-on
+	// BSLLS:JoinWithSubQuery-on
+	// BSLLS:JoinWithVirtualTable-off
+	// BSLLS:JoinWithSubQuery-off
+	// BSLLS:JoinWithVirtualTable-on
+	// BSLLS:JoinWithSubQuery-on
+	// BSLLS:JoinWithVirtualTable-off
+	// BSLLS:JoinWithSubQuery-off
+	// BSLLS:JoinWithVirtualTable-on
+	// BSLLS:JoinWithSubQuery-on
+				// BSLLS:YoLetterUsage-off - имя измерения
+				// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off - имя измерения
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:MagicNumber-off - количества и надбавка цены сценария
+	// BSLLS:MagicNumber-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
+	// BSLLS:YoLetterUsage-off
+	// BSLLS:YoLetterUsage-on
```
Каждое подавление — осознанное: проверь, что оно не прячет настоящую ошибку.

### Версия конфигурации
2.0.16.96 → 2.0.16.97

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- новые объекты/формы (3 файлов), а реестр docs/TESTS.xlsx не менялся — изменение состава тестов фиксируется в реестре
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 6 (PASS: 6, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
