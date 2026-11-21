#!/usr/bin/env python3
"""Гейт полноты: сверка сдачи с постановкой по файлу приёмки .ai/reports/<slug>-acceptance.md.

Зачем (разбор качества 2026-11-21): критериев приёмки не было ни в одном плане, ревьюер видел дифф и
авторский текст «Что нового», а постановку владельца и тикет - нет. Тикет закрывался по зелёным гейтам,
а не по исходному замечанию: сортировка рабочих мест сдавалась шесть сборок подряд.

Файл приёмки (шаблон - docs/plans/_ACCEPTANCE-TEMPLATE.md):
  ## Постановка          - текст тикета или сообщения владельца ДОСЛОВНО, не пересказ
  ## Критерии приёмки    - таблица | № | Критерий | Статус | Доказательство |
  ## Однотипные объекты  - таблица | Объект | Затронут | Статус | Доказательство | (все формы/списки/роли того же класса)
Статусы: «закрыт», «не закрыт», «вне объёма» (только с решением владельца в доказательстве).
Доказательство - чем проверено: имя сценария теста, путь к снимку окна, строка отчёта прогона.
«Код написан», «гейты зелёные», «проверено» без указания чем - не доказательство.

Использование: scripts/acceptcheck.py <файл>     код 1 - файла нет, критерий не закрыт или без доказательства
"""
import os
import re
import sys

path = sys.argv[1]
if not os.path.isfile(path):
    sys.exit('нет файла приёмки %s - завести по docs/plans/_ACCEPTANCE-TEMPLATE.md' % path)
text = open(path, encoding='utf-8').read()

sections = {}
name = None
for line in text.splitlines():
    m = re.match(r'^##\s+(.+?)\s*$', line)
    if m:
        name = m.group(1).lower()
        sections[name] = []
    elif name is not None:
        sections[name].append(line)

def section(prefix):
    for k, v in sections.items():
        if k.startswith(prefix):
            return v
    return None

errors = []
task = section('постановка')
if task is None or len(' '.join(task).strip()) < 40:
    errors.append('раздел «Постановка» пуст или короче 40 знаков: нужен дословный текст тикета или сообщения владельца')

EMPTY = {'', '-', '—', '…', '...', 'нет'}
WEAK = re.compile(r'^(проверено|готово|сделано|код написан|гейты зел[её]ные|работает|ок|ok)[.!]*$', re.I)

def rows(lines):
    out = []
    for l in lines:
        if not l.strip().startswith('|'):
            continue
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if all(set(c) <= set('-: ') for c in cells):
            continue
        out.append(cells)
    return out[1:] if out else []

def check(title, prefix, required, status_col, evidence_col, name_col):
    lines = section(prefix)
    if lines is None:
        if required:
            errors.append('нет раздела «%s»' % title)
        return 0
    table = rows(lines)
    if required and not table:
        errors.append('в разделе «%s» нет ни одной строки' % title)
    for cells in table:
        if len(cells) <= max(status_col, evidence_col):
            errors.append('«%s»: строка без статуса или доказательства: %s' % (title, ' | '.join(cells)))
            continue
        label, status, evidence = cells[name_col], cells[status_col].lower(), cells[evidence_col]
        if status not in ('закрыт', 'вне объёма', 'не затронут'):
            errors.append('«%s»: «%s» - статус «%s»' % (title, label, cells[status_col] or 'пусто'))
        elif evidence.lower() in EMPTY or WEAK.match(evidence):
            errors.append('«%s»: «%s» - нет доказательства (чем проверено)' % (title, label))
        elif status == 'вне объёма' and 'владел' not in evidence.lower():
            errors.append('«%s»: «%s» - «вне объёма» без решения владельца в доказательстве' % (title, label))
    return len(table)

n = check('Критерии приёмки', 'критерии', True, 2, 3, 1)
m = check('Однотипные объекты', 'однотипные', True, 2, 3, 0)
if errors:
    print('Приёмка не закрыта (%s):' % path)
    for e in errors:
        print('  - ' + e)
    sys.exit(1)
print('Приёмка закрыта: критериев %d, однотипных объектов %d' % (n, m))
