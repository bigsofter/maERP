# Final check — menu-machines
_20261009T170934Z_


## Scope

```
.ai/reports/menu-machines-final-check.md
.ai/reviews/menu-machines/03-code-review.json
.ai/reviews/menu-machines/03b-code-review-verify.json
docs/plans/menu-restructure.md
src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
src/cf/src/Configuration/Configuration.mdo
src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
src/cf/src/Subsystems/Производство/Производство.mdo
src/cf/src/Subsystems/Производство/CommandInterface.cmi
src/cf/src/Subsystems/Продажи/Subsystems/Опт/Опт.mdo
src/cf/src/Subsystems/Склад/Subsystems/Товары/Товары.mdo
src/cf/src/Subsystems/Закупки/Subsystems/Импорт/Импорт.mdo
src/cf/src/Subsystems/Казначейство/Subsystems/Банк/Банк.mdo
src/cf/src/Subsystems/Склад/Subsystems/Хранение/Хранение.mdo
src/cf/src/Subsystems/Казначейство/Subsystems/Касса/Касса.mdo
src/cf/src/Subsystems/Производство/Subsystems/Станки/Станки.mdo
src/cf/src/Subsystems/Производство/Subsystems/Нормативы/Нормативы.mdo
src/cf/src/Subsystems/Закупки/Subsystems/Планирование/Планирование.mdo
src/cf/src/Subsystems/Продажи/Subsystems/Опт/CommandInterface.cmi
src/cf/src/Subsystems/Склад/Subsystems/Товары/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/Subsystems/Импорт/CommandInterface.cmi
src/cf/src/Subsystems/Казначейство/Subsystems/Банк/CommandInterface.cmi
src/cf/src/Subsystems/Казначейство/Subsystems/Касса/CommandInterface.cmi
src/cf/src/Subsystems/Производство/Subsystems/Станки/CommandInterface.cmi
src/cf/src/Subsystems/Закупки/Subsystems/Планирование/CommandInterface.cmi
src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
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
Языков: 4, пунктов изменений: 12
Описание изменений: /Users/ivan-gurkin/Dev/maERP/build/changelog-2.0.16.44.json
версия 2.0.16.44: ru=3, fr=3, en=3, es=3
```
**PASS**

## Git hygiene

### git status
```
 M docs/plans/menu-restructure.md
 M src/cf/src/CommonTemplates/ОписаниеИзменений/Template.txt
 M src/cf/src/Configuration/Configuration.mdo
 M src/cf/src/FunctionalOptions/ИспользоватьУчетСтанков/ИспользоватьУчетСтанков.mdo
 M src/cf/src/Subsystems/Закупки/Subsystems/Импорт/CommandInterface.cmi
 M src/cf/src/Subsystems/Закупки/Subsystems/Импорт/Импорт.mdo
 M src/cf/src/Subsystems/Закупки/Subsystems/Планирование/CommandInterface.cmi
 M src/cf/src/Subsystems/Закупки/Subsystems/Планирование/Планирование.mdo
 M src/cf/src/Subsystems/Казначейство/Subsystems/Банк/CommandInterface.cmi
 M src/cf/src/Subsystems/Казначейство/Subsystems/Банк/Банк.mdo
 M src/cf/src/Subsystems/Казначейство/Subsystems/Касса/CommandInterface.cmi
 M src/cf/src/Subsystems/Казначейство/Subsystems/Касса/Касса.mdo
 M src/cf/src/Subsystems/Продажи/Subsystems/Опт/CommandInterface.cmi
 M src/cf/src/Subsystems/Продажи/Subsystems/Опт/Опт.mdo
 M src/cf/src/Subsystems/Производство/CommandInterface.cmi
 M src/cf/src/Subsystems/Производство/Subsystems/Нормативы/CommandInterface.cmi
 M src/cf/src/Subsystems/Производство/Subsystems/Нормативы/Нормативы.mdo
 M src/cf/src/Subsystems/Производство/Subsystems/Станки/CommandInterface.cmi
 M src/cf/src/Subsystems/Производство/Subsystems/Станки/Станки.mdo
 M src/cf/src/Subsystems/Производство/Производство.mdo
 M src/cf/src/Subsystems/Склад/Subsystems/Товары/CommandInterface.cmi
 M src/cf/src/Subsystems/Склад/Subsystems/Товары/Товары.mdo
 M src/cf/src/Subsystems/Склад/Subsystems/Хранение/CommandInterface.cmi
 M src/cf/src/Subsystems/Склад/Subsystems/Хранение/Хранение.mdo
?? .ai/reports/menu-machines-final-check.md
?? .ai/reviews/menu-machines/
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
2.0.16.43 → 2.0.16.44

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
