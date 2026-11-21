#!/usr/bin/env python3
"""Полный список форм списков для обхода на клиенте: tests/ui/forms-all.txt.

В гейт базы входит короткий список tests/ui/forms.txt (рабочие места и ходовые списки). Полный обход - все
документы, справочники и журналы документов - идёт около часа и запускается перед релизом и после массовых
правок форм списков:  python3 tests/ui/gen_forms_all.py && UITEST_ROLES=Администратор \\
    UITEST_FORMS=tests/ui/forms-all.txt scripts/uitest.sh
"""
import os
import unicodedata

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src = os.path.join(root, 'src', 'cf', 'src')
kinds = [('Documents', 'Document', 'Документ'), ('Catalogs', 'Catalog', 'Справочник'),
         ('DocumentJournals', 'DocumentJournal', 'ЖурналДокументов')]
lines = ['# Генерируется tests/ui/gen_forms_all.py - руками не править.']
for folder, meta, ru in kinds:
    base = os.path.join(src, folder)
    for name in sorted(unicodedata.normalize('NFC', n) for n in os.listdir(base)):
        if name.startswith('.'):
            continue
        lines.append('%s.%s;e1cib/list/%s.%s;%s.%s.' % (meta, name, ru, name, ru, name))
out = os.path.join(root, 'tests', 'ui', 'forms-all.txt')
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print('форм: %d, файл %s' % (len(lines) - 1, out))
