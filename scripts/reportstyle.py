#!/usr/bin/env python3
"""Оформление отчётов: у каждого варианта схемы компоновки - макет оформления «Античный», у отчёта с выводом кодом -
процедура ОформитьОбласть с той же палитрой, у отчёта на табличном макете - функция ВАнтичном (тикет 2606453: новый отчёт без оформления не должен пройти сверку).

Использование: scripts/reportstyle.py [каталог src/cf]. Код возврата 1 - есть расхождения.
"""
import glob
import os
import re
import sys

root = sys.argv[1] if len(sys.argv) > 1 else 'src/cf'
problems = []
for schema in sorted(glob.glob(os.path.join(root, 'src', 'Reports', '*', 'Templates', '*', 'Template.dcs'))):
    text = open(schema, encoding='utf-8').read()
    for variant in re.findall(r'<settingsVariant>.*?</settingsVariant>', text, flags=re.S):
        name = re.search(r'<dcsset:name>([^<]*)</dcsset:name>', variant)
        styled = re.search(r'<dcscor:parameter>AppearanceTemplate</dcscor:parameter>\s*'
                           r'<dcscor:value xsi:type="xs:string">Античный</dcscor:value>', variant)
        if not styled:
            problems.append('%s: вариант «%s» без макета оформления «Античный»' % (schema, name.group(1) if name else '?'))
for module in sorted(glob.glob(os.path.join(root, 'src', 'Reports', '*', 'ObjectModule.bsl'))):
    text = open(module, encoding='utf-8').read()
    # Вывод кодом: стандартная обработка отключена, результат не выводит процессор компоновки в табличный документ.
    by_code = re.search(r'СтандартнаяОбработка\s*=\s*Ложь', text) and '.Область(' in text \
        and 'ПроцессорВыводаРезультатаКомпоновкиДанныхВТабличныйДокумент' not in text
    if by_code and 'Процедура ОформитьОбласть(' not in text:
        problems.append('%s: вывод кодом без процедуры ОформитьОбласть (палитра «Античного»)' % module)
# Отчёт на табличном макете (области макета выводит модуль формы): области красятся функцией ВАнтичном.
for form in sorted(glob.glob(os.path.join(root, 'src', 'Reports', '*', 'Forms', '*', 'Module.bsl'))):
    text = open(form, encoding='utf-8').read()
    areas = re.findall(r'[^\n]*\.ПолучитьОбласть\([^\n]*', text)
    if areas and 'Функция ВАнтичном(' not in text:
        problems.append('%s: области макета выводятся без функции ВАнтичном (палитра «Античного»)' % form)
    for line in areas:
        if 'ВАнтичном(' not in line and '"Отступ"' not in line:
            problems.append('%s: область без палитры «Античного»: %s' % (form, line.strip()))
for line in problems:
    print(line)
print('reportstyle: расхождений %d' % len(problems))
sys.exit(1 if problems else 0)
