#!/usr/bin/env python3
"""Форма рабочего места производства, редакция 11 (2.0.16.17, замечания владельца 2026-10-05).

Поверх редакции 10 (gen10.py) текстовыми преобразованиями её вывода:
- gen11_panel.py - дополнения таблицы «Заказы» (штатная навигация не показывается), колонка «Кол-во ПФ/ГП» и порядок
  колонок передачи, выбор материала и ПФ/ГП без выпадающего списка ввода по строке.

Проверка: python3 gen11.py | diff - ../../../src/cf/src/DataProcessors/АРМПроизводство/Forms/Форма/Form.form
"""
import os
import re
import sys

import gen10

ЗДЕСЬ = os.path.dirname(os.path.abspath(__file__))


def применить(имя, s):
    среда = {'s': s, 're': re}
    with open(os.path.join(ЗДЕСЬ, имя), encoding='utf-8') as f:
        exec(compile(f.read(), имя, 'exec'), среда)
    return среда['s']


def build():
    return применить('gen11_panel.py', gen10.build())


if __name__ == '__main__':
    sys.stdout.write(build())
