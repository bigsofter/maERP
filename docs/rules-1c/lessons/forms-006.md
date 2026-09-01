---
id: forms-006
категория: формы-xml
серьёзность: справка
заголовок: "Тумблер: RadioButtonField + choiceList; значения перечислений - ReferenceValue"
ключи: [Tumbler, RadioButtonField, choiceList, перечисление, EnumValue]
---

# Тумблер: RadioButtonField + choiceList; значения перечислений - ReferenceValue

## Рецепт

Переключатель-тумблер (вид операции, фильтр списка):

```xml
<type>RadioButtonField</type>
<extInfo xsi:type="form:RadioButtonsFieldExtInfo">
  <radioButtonsType>Tumbler</radioButtonsType>
  <equalElementsWidth>true</equalElementsWidth>
  <choiceList>
    <presentation><key>ru</key><value>Продажа</value></presentation>
    ...
    <value xsi:type="core:ReferenceValue">
      <value>Enum.ХозяйственныеОперации.EnumValue.РеализацияКлиенту</value>
    </value>
  </choiceList>
</extInfo>
```

Числовые значения - `core:NumberValue`, строковые - `core:StringValue`.
`<titleLocation>None</titleLocation>` убирает подпись поля.

Для фильтра списка: реквизит формы + обработчик OnChange, отбор ставить программно
элементом отбора динамического списка (не пользовательскими настройками) - тогда
тумблер и настройки пользователя не спорят за один элемент отбора.

## Образцы в maERP

Журнал БезналичныеПлатежи (ФормаСписка, поле ВариантОтображения); формы реализации
после 2026-08-31.
