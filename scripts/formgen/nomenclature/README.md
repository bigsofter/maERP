# Генератор формы списка товаров

`src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form` собирается скриптом `list.py` (этап 1 плана
`docs/plans/nomenclature-ui.md`, 2.0.16.60): исходная форма — из git (коммит `БАЗА` в скрипте), панель «Сведения» —
из формы списка реализаций (FORMS-STYLE, правило 6), флажок — из рабочего места закупок (урок tiny1C workflow-005).
Запрос динамического списка — текст `Справочники.Номенклатура.ТекстЗапросаСписка()` из модуля менеджера; форма при
создании ставит его же, генератор держит копию в Form.form, чтобы `listcheck.py` сверял колонки.

```bash
python3 scripts/formgen/nomenclature/list.py > /tmp/list.form && cp /tmp/list.form src/cf/src/Catalogs/Номенклатура/Forms/ФормаСписка/Form.form
```

Вывод — сначала во временный файл: при ошибке скрипта перенаправление прямо в Form.form оставит его пустым.
После — `scripts/listcheck.py`, `scripts/colfont.py`, Refresh в EDT, смок и снимок окна.
