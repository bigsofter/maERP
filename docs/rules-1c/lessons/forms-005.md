---
id: forms-005
категория: формы-xml
серьёзность: важно
заголовок: "Сворачиваемой группе - collapsedRepresentationTitle на всех языках"
ключи: [Collapsible, collapsedRepresentationTitle, сворачивание, многоязычность]
---

# Сворачиваемой группе - collapsedRepresentationTitle на всех языках

## Правило

Группа с `behavior = Collapsible` показывает в свёрнутом виде текст из
`collapsedRepresentationTitle` - заполнять на всех языках конфигурации (в maERP -
ru/fr/en/es). Убирая сворачивание, убрать и `collapsedRepresentationTitle` с
`controlRepresentation`, иначе останется мёртвый заголовок вида «Шапка (Развернуть)».

## История

maERP 2026-09-01: после отмены сворачивания шапки реализации заголовок
«En-tête (réduire)» остался на форме - убран вместе со свойствами сворачивания.
