# Final check — reports-dev-71
_20261011T181134Z_


## Scope

```
.ai/reports/reports-dev-71-final-check.md
.ai/reports/reports-dev-71.md
.ai/reviews/reports-dev-71/03-code-review.json
.ai/reviews/reports-dev-71/03b-code-review-verify.json
docs/plans/branded-print-s4-prompt.md
docs/TESTING.md
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/Reports/АнализСчета/Templates/СхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ОборотыСчета/Templates/СхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/КарточкаСчета/Templates/СхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/АнализСубконто/Templates/СхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/Затраты/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/КарточкаСубконто/Templates/СхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ИсторияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ДвиженияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ДеньгиПоСтанкам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьПоЧекам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ОтчетПоПересчетам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/МатериалыНаСтанках/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьПоПродажам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РасчетыСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/СебестоимостьПродукции/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьПоПоступлениям/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ОтчетПоНедостаткамТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ОборотноСальдоваяВедомостьПоСчету/Templates/СхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ПроданныйТоварБезНакладной/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьПоТоварамНаСкладах/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьПоДенежнымСредствам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/РеестрПоступленийТоваровУслуг/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьРасчётовСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьРасчётовСКонтрагентами/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ВедомостьРасчётовСПрочимиКонтрагентами/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
src/cf/src/Reports/ЕженедельноеПланированиеЗадолженностиПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
```

## Gates

(no src/cf/**.bsl changes — BSL LS skipped)
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
Языков: 4, пунктов изменений: 16
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.71.json
версия 2.0.16.71: ru=4, fr=4, en=4, es=4
```
**PASS**

## Git hygiene

### git status
```
 M docs/TESTING.md
 M docs/plans/branded-print-s4-prompt.md
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/Reports/АнализСубконто/Templates/СхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/АнализСчета/Templates/СхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьПоДенежнымСредствам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьПоПоступлениям/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьПоПродажам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьПоПродажамНалоговая/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьПоТоварамНаСкладах/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьПоЧекам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьРасчётовСКонтрагентами/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьРасчётовСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьРасчётовСПоставщиками/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВедомостьРасчётовСПрочимиКонтрагентами/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ВыработкаСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ДвижениеДенежныхСредств/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ДвиженияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ДеньгиПоСтанкам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ДолгиПокупателей/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ДолгиПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ЕженедельноеПланированиеЗадолженностиПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ЗагрузкаСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ЗанятостьСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/Затраты/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ИсторияИзмененияЦенПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ИсторияТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/КарточкаСубконто/Templates/СхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/КарточкаСчета/Templates/СхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/КассоваяКнига/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/МатериалыНаСтанках/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/НедостаточныеЗапасы/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/НеотгруженныеЗаказы/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОборотноСальдоваяВедомость/Templates/СхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОборотноСальдоваяВедомостьПоСчету/Templates/СхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОборотыСчета/Templates/СхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОтчетПоНедостаткамТовара/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОтчетПоПересчетам/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ОтчетПоПроводкам/Templates/СхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПланЗагрузкиСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПланированиеЗакупок/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПотребностиПроизводства/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПроданныйТоварБезНакладной/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПросроченныеДолгиПокупателей/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПросроченныеДолгиПоставщиков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ПростоиСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РасчетыСПокупателями/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РасчетыСПоставщиками/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РеестрНалоговыхНакладных/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РеестрНалоговыхНакладныхЗакупка/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РеестрПоступленийТоваровУслуг/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/РеестрРеализацийТоваровУслуг/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/СебестоимостьПродукции/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/СтатистикаДневныхПродаж/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/СтоимостьСклада/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыВНаличии/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыВПереработке/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ТоварыДляЗаказа/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ФинансовыйРезультат/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ЦеныНоменклатуры/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
 M src/cf/src/Reports/ЭффективностьСтанков/Templates/ОсновнаяСхемаКомпоновкиДанных/Template.dcs
?? .ai/reports/reports-dev-71-final-check.md
?? .ai/reports/reports-dev-71.md
?? .ai/reviews/reports-dev-71/
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
2.0.16.70 → 2.0.16.71

### Регламент тестов (docs/TESTING.md, п. 2) — напоминания, не FAIL
- уровни 1–3 проверяют build/ib, а её обновляет из EDT владелец: без Refresh и обновления базы смок гоняет код прошлой сборки

## Gates run

Запущено гейтов: 4 (PASS: 4, FAIL: 0)

Пропущены (по составу диффа или по месту запуска — сверь со «Scope» выше, пропуск НЕ равен «прошло»):
  - уровень 0 (BSL LS) — в диффе нет модулей src/cf/**.bsl
  - EDT: синтаксический контроль и ссылочная целостность метаданных — только у владельца после Refresh (CLAUDE.md), отсюда не запускается
  - уровни 1–3 (smoke.sh, doctests.sh) — без --db: проверяют build/ib, которую обновляет из EDT владелец; без обновления гоняли бы код прошлой сборки

## Verdict

**ALL GATES PASSED** — no hygiene issues flagged.
