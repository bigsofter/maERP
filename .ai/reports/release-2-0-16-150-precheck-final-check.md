# Final check — release-2-0-16-150-precheck
_20261109T100938Z_


## Scope

```
.ai/reports/arm-current-row-final-check.md
.ai/reports/arm-pf-output-final-check.md
.ai/reports/arm-production-print-final-check.md
.ai/reports/arm-props-from-gp-final-check.md
.ai/reports/arm-purch-tabs-final-check.md
.ai/reports/arm-purchasing-invoice-cols-final-check.md
.ai/reports/arm-purchasing-lines-columns-final-check.md
.ai/reports/arm-purchasing-receipt-lines-final-check.md
.ai/reports/arm-purchasing-receipts-final-check.md
.ai/reports/arm-purchasing-receipts-s2-final-check.md
.ai/reports/arm-receipt-lines-edit-final-check.md
.ai/reports/bulk-edit-platform-check-final-check.md
.ai/reports/calendar-country-choice-final-check.md
.ai/reports/card-crash-filters-final-check.md
.ai/reports/card-routing-crash-final-check.md
.ai/reports/currency-words-fill-final-check.md
.ai/reports/input-by-string-roles-final-check.md
.ai/reports/kp-print-terms-final-check.md
.ai/reports/lot-traceability-final-check.md
.ai/reports/machine-form-final-check.md
.ai/reports/machines-layout-final-check.md
.ai/reports/manual-output-from-stock-final-check.md
.ai/reports/nomenclature-card-layout-final-check.md
.ai/reports/operator-subcontract-print-final-check.md
.ai/reports/order-list-columns-final-check.md
.ai/reports/order-money-status-final-check.md
.ai/reports/order-stock-places-final-check.md
.ai/reports/print-preview-client-pdf-final-check.md
.ai/reports/processing-by-processor-final-check.md
.ai/reports/production-top-row-final-check.md
.ai/reports/recount-task-types-final-check.md
.ai/reports/release-2-0-16-150-precheck-final-check.md
.ai/reports/reports-console-final-check.md
.ai/reports/reports-variants-final-check.md
.ai/reports/role-print-commands-final-check.md
.ai/reports/sales-print-menu-final-check.md
.ai/reports/semi-finished-from-stock-final-check.md
.ai/reports/semi-finished-leaf-final-check.md
.ai/reports/semi-finished-subcontract-final-check.md
.ai/reports/shipments-tab-order-final-check.md
.ai/reports/startup-forms-warehouse-role-final-check.md
.ai/reports/subcontract-late-receipt-final-check.md
.ai/reports/subcontract-multi-order-final-check.md
.ai/reports/subcontract-partial-receipt-final-check.md
.ai/reports/subcontract-receipt-day-start-final-check.md
.ai/reports/tabs-handlers-final-check.md
.ai/reports/transfer-act-print-final-check.md
.ai/reports/transfer-row-product-field-final-check.md
.ai/reports/warehouse-orders-cost-f3-final-check.md
.ai/reports/warehouse-orders-cost-f4-final-check.md
.ai/reports/warehouse-orders-cost-f5-final-check.md
.ai/reports/warehouse-orders-option-final-check.md
.ai/reviews/arm-current-row/03-code-review.json
.ai/reviews/arm-current-row/03b-code-review-verify.json
.ai/reviews/arm-production-print/03-code-review.json
.ai/reviews/arm-production-print/03b-code-review-verify.json
.ai/reviews/arm-purchasing-receipt-lines/02-plan-review.json
.ai/reviews/arm-purchasing-receipt-lines/03-code-review.json
.ai/reviews/arm-purchasing-receipt-lines/03b-code-review-verify.json
.ai/reviews/card-crash-filters/03-code-review.json
.ai/reviews/machine-form/03-code-review.json
.ai/reviews/order-list-columns/03-code-review.json
.ai/reviews/order-list-columns/03b-code-review-verify.json
.ai/reviews/order-payment-state/02-plan-review.json
.ai/reviews/performance-vt/02-plan-review.json
.ai/reviews/performance-vt/04-database-review.json
.ai/reviews/production-top-row/03-code-review.json
.ai/reviews/production-top-row/03b-code-review-verify.json
.ai/reviews/subcontract-late-receipt/03-code-review.json
.ai/reviews/subcontract-late-receipt/03b-code-review-verify.json
.ai/reviews/subcontract-partial-receipt/03-code-review.json
.ai/reviews/uncommitted/03-code-review.json
.ai/reviews/verify/03-code-review.json
.ai/reviews/warehouse-orders-option/02-plan-review.json
.ai/reviews/warehouse-orders-option/03-code-review.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify-r1.json
.ai/reviews/warehouse-orders-option/03b-code-review-verify.json
.ai/reviews/warehouse-orders-option/04-database-review.json
.ai/reviews/wo-techdebt2/02-plan-review.json
CLAUDE.md
docs/drissotex-analysis/flycdi-2026-11-09.md
docs/drissotex-analysis/flycdi/area-A.md
docs/drissotex-analysis/flycdi/area-B.md
docs/drissotex-analysis/flycdi/area-C.md
docs/drissotex-analysis/flycdi/area-D.md
docs/drissotex-analysis/flycdi/objs-missing.txt
docs/drissotex-analysis/flycdi/scripts/attruuid.py
docs/drissotex-analysis/flycdi/scripts/classify.py
docs/drissotex-analysis/flycdi/scripts/cmp.py
docs/drissotex-analysis/flycdi/scripts/inv.py
docs/drissotex-analysis/flycdi/scripts/meth.py
docs/drissotex-analysis/flycdi/scripts/uuids.py
docs/plans/order-payment-state.md
docs/TECHDEBT.md
```

## Gates

(no src/cf/**.bsl changes — BSL LS skipped)
### уровни 1–2: scripts/smoke.sh (CheckConfig + смок)
```
== Шаг 1. Проверка конфигурации (CheckConfig) ==
CheckConfig: ошибок нет
== Шаг 1б. Расширенная проверка модулей ==
Расширенная проверка: новых замечаний нет
== Шаг 2. Смок-тест «открыть все формы» ==
ИТОГ;Всего=422;Ошибок=0;НаОбразцах=112;ОшибокНаОбразцах=0;ПечатныхФорм=51;ОшибокПечати=0;ВариантовОтчетов=69;ОшибокОтчетов=0
Пропущено проверок: 11; пустых печатных форм: 0 (подробности в /Users/ivan-gurkin/Dev/maERP/build/smoke-report.txt)
ТЕСТЫ ПРОЙДЕНЫ
```
**PASS**
### уровень 3: scripts/doctests.sh
```
ОК;ОрдерныйСкладСтараяСхема;ордер старой схемы (без своих партий) вне пересчёта не оформляется
ОК;ОрдерныйСкладПереводГруппы;перепроведение одного ордера переводит и второй ордер того же поступления, партии равны
ОК;ОрдерныйСкладПереводРасходных;перепроведение раннего расходного ордера переводит оба ордера реализации, списание по
ОК;ОрдерныйСкладПереводПотребителя;списание партии-поступления до перевода переходит на партию ордера
ОК;ОрдерныйСкладОбновлениеФазы5;обработчик перевода ордеров фазы 5 переводит ордера без партий, повтор ничего не меняет
ОК;ДокументПервыйПриход;поступление без ордера ждёт приёмки, ордера на основании - партии по доле строки, смена цены поступления пересчитывает партии
ОК;ДокументПервыйДоли;три приёмки строки 10,00 - доли положительны, в сумме 10,00
ОК;ДокументПервыйОтменаПоступления;поступление, принятое ордером, не отменяется
ОК;ДокументПервыйРасход;реализация без ордера: себестоимость - по отгрузкам расходных ордеров на её основании
ОК;ДокументПервыйВозвратСверх;возврат по реализации ордерного склада сверх отгруженного - отказ
ОК;ДокументПервыйОтменаОрдераСВозвратом;отмена расходного ордера, отгрузку которого вернули, - отказ
ОК;ДокументПервыйМомент;ордер на основании документа - только позже документа
ОК;ДокументПервыйДопрасходы;допрасход по поступлению до приёмки - по мере приёмки, остаток ждёт ордера
ОК;ДокументПервыйСерии;строка без ордера на ордерном складе - одна серия
ОК;ОпцияОрдерныхСкладовОтказСклада;признак «Ордерный склад» при выключенной опции не записывается
ОК;ОпцияОрдерныхСкладовОтказОрдера;ордер при выключенной опции не записывается
ОК;ОпцияОрдерныхСкладовОтказЗагрузки;РасходныйОрдер и в режиме загрузки при выключенной опции не записывается
ОК;ОпцияОрдерныхСкладовОтказЗагрузкиПрихода;ПриходныйОрдер и в режиме загрузки при выключенной опции не записывается
ОК;ОпцияОрдерныхСкладовВключение;при включённой опции ордерный склад записывается, выключение запрещено
ОК;ОпцияОрдерныхСкладовОтказВыключения;опция не выключается, пока есть ордерный склад
ОК;ОпцияОрдерныхСкладовЧерновик;непроведённый ордер запрещает выключение опции, без него - разрешено
ОК;ОпцияОрдерныхСкладовОбновление;обработчик обновления не включает опцию в базе без ордеров, повтор безопасен
ОК;ПоступленияТоварамиАРМ;строки «Товаров»: по открытому заказу, без заказа, в выбранный документ, правка и удаление,
ОК;ПоступленияТоварамиАРМДваКода;две строки заказа одного товара: вторая - к свободному коду, третья - отказ
ОК;ПоступленияТоварамиАРМОрдер;ордерный склад: строки «Товаров» по заказу и без заказа - приходные ордера; склад строки выбирает поступление или приходный ордер, единица и заказ новой строки - по товару
ОК;ПроизводительностьЗапросов;формирование заказов: заказано 4; кредитный контроль без контрагента: долг 300 только по реализации; автоподбор: цена вида одной строкой, без вида цены - без цены
ОК;АвтоподборПоУмолчанию;пустая строка автоподбора - последние созданные: 31 позиций, без групп и помеченных
ОК;РабочиеМеста;место по регистру и однозначному коду, кандидаты по имени компьютера без привязки, неоднозначный код - выбор, занятый идентификатор не перепривязывается, выбор на сеанс, помеченное место, объединение с переносом и пометкой совпадающего, отказ устаревшего списка, повторного и встречного объединения, перенос идентификатора, миграция кодов и её повтор
ОК;РаздельныйУчет;без опции признак не действует, физический остаток - все движения, белый и чёрный остатки раздельно, признак в товарах, долгах, продажах и кассе, банк белый, запрет выключения опции
ОК;НалоговыйДокументНаОсновании;полное покрытие двух оснований, физический остаток и фактические долг и выручка не меняются, белые - по налоговому документу, оплаты до и после документа, перенос и отмена распределения, запреты покрытия и изменения, возврат по налоговому документу, поступление на основании
ОК;ТехдолгРевьюПоступлениеДоАвтовыпуска;T12: поступление из переработки по заказу датой раньше реализации с автовыпуском той же продукции не проводится, в сообщениях - текст запрета по дате
ОК;ТехдолгРевьюОбнуленныйРасход;T13: положительная норма материала, расход которой на отгрузку округляется до нуля, - ошибка расчёта автовыпуска с материалом и продукцией, продукция не выпускается, проведение реализации отклоняется этой ошибкой
ОК;ТехдолгРевьюСтадииБезИстории;T28: обработчик стадий заказов без истории пишет проведённому заказу на производство без истории запись с индикатором, повторный запуск её не дублирует
ОК;ТехдолгРевьюПраваРолей;T7, T8: ЛичныйКабинет только читает взаиморасчёты, продажи, товары в наличии, заказы поставщикам и историю статусов заказов; ОператорПроизводства только читает историю статусов
ОК;КарточкаНоменклатуры;минимумы нового товара по обоим измерениям, артикул, штрихкоды трёх веток и серии, последняя строка свойства, цены карточки, независимые группы отбора; минимумов с пустой номенклатурой в базе: 2
ОК;СписокНоменклатуры;запрос списка: две партии - одна строка с суммой остатка склада, другой склад - 0, закупаемые без продукции, без права на минимумы складов - минимум карточки; сведения панели - остаток и свободно по складу, товар и движение; иерархия: последняя строка свойства, «<не задано>», сведение, пересечение узла и панели, свойство панели в любом режиме, контекст в счётчиках, текст без сведений
ОК;ПереносСтарыхСвойств;свойство на каждый вид с фактическими типами, последняя строка, заданное не перезаписано, повтор без изменений, старая ТЧ цела, регистрация 2.0.16.66, ошибка товара собрана
ОК;ПоследовательностьСостав;регистраторы стоимостных регистров в последовательности (исключения: корректировка регистров и налоговые документы), ТоварыВПереработке в ее движениях, задание пересчета включено
ОК;ВыпускВПоследовательности;поступление задним числом сдвигает границу назад, пересчет: выпуск и продажа продукции по FIFO с новой партией, повторный пересчет - те же движения
ОК;АвтовыпускВПоследовательности;пересчет перепроводит автовыпуск без отказа правки: состав, «ИзОстатка» и стадия - прежние
ОК;ТребованиеВПоследовательности;завершенное требование и его выпуск в пересчете: выпуск не задваивается, загрузка и закрепление станка прежние, перемещение - те же партии
ОК;ПереработкаВПоследовательности;передача и поступление из переработки в пересчете: долг переработчику и стоимость продукции прежние
ОК;ОбновлениеГраницыПоследовательности;обработчик обновления: запись последовательности истории, граница раньше передачи и прежней, повтор - та же граница
ОК;КорректировкаРегистровГраница;корректировка регистров: граница на период записи раньше даты документа - при записи и при удалении
ОК;СебестоимостьПродажРеализации;себестоимость продаж реализации = ее списание склада построчно, продажи - без партий и себестоимости, прибыль - единой формулой
ОК;ВозвратИзСебестоимостиПродаж;возврат из себестоимости продаж: партии FIFO основания, второй возврат - оставшиеся партии, итог продажи с возвратами нулевой, перепроведение не меняет записи
ОК;ВозвратДвумяСтроками;две строки одного товара в возврате восстанавливают каждую партию один раз
ОК;СебестоимостьНалоговогоНаОснованиях;налоговый на основаниях: черная и белая стороны себестоимости, возврат из белой; пересчет перепроводит основание с возвратом, налоговый документ и возврат, без заморозки
ОК;ПереносСебестоимостиПродаж;перенос истории: детализация движениями склада, поправка исторического возврата, построчная корректировка, сверка, повтор; компенсация поправки завершающим возвратом; излишек - остановка
ОК;МаржаОтчетов;ведомость по продажам: прибыль из себестоимости продаж совпадает с единой функцией
ОК;РаскладкаКопеек;раскладка до копейки: сумма частей = итогу, знак и предел каждого источника
ОК;ПраваСебестоимостиПродаж;чтение себестоимости продаж у ролей, читающих продажи, кроме личного кабинета; изменения нет
ОК;ФормыПриЗапуске;флажок пишет и снимает запись текущего пользователя, порядок форм - белого списка, имя вне списка - отказ; карточка удаляет только переданные виды
ОК;РольСкладскиеОрдера;роль: рабочее место закупок без раздела «Закупки» и без чтения заказов, ордера и печать; с оператором производства - режим приёмки без оплат; объекты оплат совпадают с запросами
ОК;ПриемкаАРМЗакупок;данные заказа без оплат - пустые оплаты, документы и сальдо; «только ордер»: склад не ордерный - отказ, ордерный - приходный ордер по заказу
ОК;ВводПоСтрокеРолей;у объектов с просмотром есть ввод по строке (580 пар роль-объект)
ОК;ПечатьПереработкиОператора;у оператора производства доступны команды печати закладок (4)
ОК;КомандыПечатиРолей;видимые документы - с командами печати (255 пар роль-команда), у роли без цен - только формы без цен
ОК;ПечатьБезЦенСкладскихФорм;оприходование и списание: с суммами - сумма прописью, без цен - без сумм и итогов
ТЕСТЫ ПРОЙДЕНЫ
```
**PASS**

## Git hygiene

### git status
```
 M CLAUDE.md
 M docs/TECHDEBT.md
?? .ai/reports/arm-current-row-final-check.md
?? .ai/reports/arm-pf-output-final-check.md
?? .ai/reports/arm-production-print-final-check.md
?? .ai/reports/arm-props-from-gp-final-check.md
?? .ai/reports/arm-purch-tabs-final-check.md
?? .ai/reports/arm-purchasing-invoice-cols-final-check.md
?? .ai/reports/arm-purchasing-lines-columns-final-check.md
?? .ai/reports/arm-purchasing-receipt-lines-final-check.md
?? .ai/reports/arm-purchasing-receipts-final-check.md
?? .ai/reports/arm-purchasing-receipts-s2-final-check.md
?? .ai/reports/arm-receipt-lines-edit-final-check.md
?? .ai/reports/bulk-edit-platform-check-final-check.md
?? .ai/reports/calendar-country-choice-final-check.md
?? .ai/reports/card-crash-filters-final-check.md
?? .ai/reports/card-routing-crash-final-check.md
?? .ai/reports/currency-words-fill-final-check.md
?? .ai/reports/input-by-string-roles-final-check.md
?? .ai/reports/kp-print-terms-final-check.md
?? .ai/reports/lot-traceability-final-check.md
?? .ai/reports/machine-form-final-check.md
?? .ai/reports/machines-layout-final-check.md
?? .ai/reports/manual-output-from-stock-final-check.md
?? .ai/reports/nomenclature-card-layout-final-check.md
?? .ai/reports/operator-subcontract-print-final-check.md
?? .ai/reports/order-list-columns-final-check.md
?? .ai/reports/order-money-status-final-check.md
?? .ai/reports/order-stock-places-final-check.md
?? .ai/reports/print-preview-client-pdf-final-check.md
?? .ai/reports/processing-by-processor-final-check.md
?? .ai/reports/production-top-row-final-check.md
?? .ai/reports/recount-task-types-final-check.md
?? .ai/reports/release-2-0-16-150-precheck-final-check.md
?? .ai/reports/reports-console-final-check.md
?? .ai/reports/reports-variants-final-check.md
?? .ai/reports/role-print-commands-final-check.md
?? .ai/reports/sales-print-menu-final-check.md
?? .ai/reports/semi-finished-from-stock-final-check.md
?? .ai/reports/semi-finished-leaf-final-check.md
?? .ai/reports/semi-finished-subcontract-final-check.md
?? .ai/reports/shipments-tab-order-final-check.md
?? .ai/reports/startup-forms-warehouse-role-final-check.md
?? .ai/reports/subcontract-late-receipt-final-check.md
?? .ai/reports/subcontract-multi-order-final-check.md
?? .ai/reports/subcontract-partial-receipt-final-check.md
?? .ai/reports/subcontract-receipt-day-start-final-check.md
?? .ai/reports/tabs-handlers-final-check.md
?? .ai/reports/transfer-act-print-final-check.md
?? .ai/reports/transfer-row-product-field-final-check.md
?? .ai/reports/warehouse-orders-cost-f3-final-check.md
?? .ai/reports/warehouse-orders-cost-f4-final-check.md
?? .ai/reports/warehouse-orders-cost-f5-final-check.md
?? .ai/reports/warehouse-orders-option-final-check.md
?? .ai/reviews/arm-current-row/
?? .ai/reviews/arm-production-print/
?? .ai/reviews/arm-purchasing-receipt-lines/
?? .ai/reviews/card-crash-filters/
?? .ai/reviews/machine-form/
?? .ai/reviews/order-list-columns/
?? .ai/reviews/order-payment-state/
?? .ai/reviews/performance-vt/
?? .ai/reviews/production-top-row/
?? .ai/reviews/subcontract-late-receipt/
?? .ai/reviews/subcontract-partial-receipt/
?? .ai/reviews/uncommitted/
?? .ai/reviews/verify/
?? .ai/reviews/warehouse-orders-option/
?? .ai/reviews/wo-techdebt2/
?? docs/drissotex-analysis/flycdi-2026-11-09.md
?? docs/drissotex-analysis/flycdi/
?? docs/plans/order-payment-state.md
?? docs/plans/retail-chain.md
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

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
замечаний нет

## Gates run

Запущено гейтов: 2 (PASS: 2, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - уровень 0 (BSL LS) — в диффе нет модулей src/cf/**.bsl
  - уровень 0.5 (refcheck) — в диффе нет src/cf/** и scripts/refcheck*
  - уровень 0.7 (listcheck) — в диффе нет src/cf/** и scripts/listcheck*
  - уровень 0.8 (queryfields) — в диффе нет src/cf/** и scripts/queryfields*
  - секция ОписаниеИзменений — в диффе нет src/cf/**

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
