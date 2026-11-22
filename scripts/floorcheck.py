#!/usr/bin/env python3
"""Порог числа проверок: сверяет строку «ИТОГ;» отчёта с scripts/smoke-floor.txt.

Использование: scripts/floorcheck.py <отчёт> [ключ,ключ,...]
Без списка ключей сверяются все ключи порога, которые есть в строке итога.
Код 1 - значение ниже порога или в отчёте нет строки итога. «Пропущено» больше нуля - тоже провал.
"""
import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
floor = {}
for line in open(os.path.join(root, 'smoke-floor.txt'), encoding='utf-8'):
    line = line.strip()
    if line and not line.startswith('#'):
        k, v = line.split('=')
        floor[k] = int(v)

text = open(sys.argv[1], encoding='utf-8-sig', errors='replace').read()
total = [l for l in text.splitlines() if l.startswith('ИТОГ;')]
if not total:
    sys.exit('ПОРОГ: в отчёте нет строки ИТОГ')
values = dict(p.split('=') for p in total[-1].split(';')[1:] if '=' in p)
keys = sys.argv[2].split(',') if len(sys.argv) > 2 else [k for k in floor if k in values]
bad = []
if not keys:
    bad.append('в строке итога нет ни одного ключа порога')
for k in keys:
    if k not in values:
        bad.append('%s: нет в строке итога' % k)
    elif int(values[k]) < floor[k]:
        bad.append('%s=%s при пороге %d' % (k, values[k], floor[k]))
if int(values.get('Пропущено', 0)) > 0:
    bad.append('Пропущено=%s: пропущенный сценарий на базе гейта - провал' % values['Пропущено'])
if bad:
    sys.exit('ПОРОГ не выдержан: ' + '; '.join(bad))
print('Порог выдержан: ' + ', '.join('%s=%s' % (k, values[k]) for k in keys))
