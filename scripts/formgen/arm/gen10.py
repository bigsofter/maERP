#!/usr/bin/env python3
"""Форма рабочего места производства, редакция 10 (2.0.16.16, замечания владельца 2026-10-05).

Поверх редакции 9 (gen9.py) текстовыми преобразованиями её вывода:
- gen10_columns.py - количественные колонки всех таблиц документов уже, заголовки короче, полное имя - в подсказке;
- gen10_panel.py - закладка «Передача в переработку», колонка ПФ/ГП строки передачи, таблица свойств ПФ/ГП справа
  от таблицы передач (реквизиты СвойстваПродукции, ПродукцияСвойств).

Проверка: python3 gen10.py | diff - ../../../src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
"""
import os
import re
import sys

import gen9

ЗДЕСЬ = os.path.dirname(os.path.abspath(__file__))


def применить(имя, s):
    среда = {'s': s, 're': re}
    with open(os.path.join(ЗДЕСЬ, имя), encoding='utf-8') as f:
        exec(compile(f.read(), имя, 'exec'), среда)
    return среда['s']


def build():
    s = gen9.build()
    s = применить('gen10_columns.py', s)
    return применить('gen10_panel.py', s)


if __name__ == '__main__':
    sys.stdout.write(build())
