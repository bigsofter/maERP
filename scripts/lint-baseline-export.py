#!/usr/bin/env python3
"""Сжатая копия базового снимка BSL LS для git: scripts/bsl-baseline-counts.json.

Полный снимок build/bsl-json-baseline.json (15 МБ) лежит вне git; гейт «нет новых замечаний» в
.ai/bin/ai-final-check сравнивает только счётчики по парам (модуль, код замечания). Эта копия хранит ровно
их: на свежем клоне или после потери build/ гейт продолжает работать. Запускать после каждого обновления
базового снимка: python3 scripts/lint-baseline-export.py
"""
import collections
import json
import os
import unicodedata
import urllib.parse

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(root, 'build', 'bsl-json-baseline.json')
dst = os.path.join(root, 'scripts', 'bsl-baseline-counts.json')
MARK = '/src/cf/src/'


def key(p):
    p = unicodedata.normalize('NFC', urllib.parse.unquote(p))
    i = p.find(MARK)
    return p[i + len(MARK):] if i >= 0 else p


data = json.load(open(src, encoding='utf-8'))
counts = collections.Counter()
for fi in data['fileinfos']:
    k = key(fi['path'])
    for d in fi.get('diagnostics') or []:
        counts[k + '\t' + d['code']] += 1
out = {'date': data.get('date', '?'), 'counts': dict(sorted(counts.items()))}
with open(dst, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=0, sort_keys=True)
    f.write('\n')
print('записано пар: %d, файл %s' % (len(counts), dst))
