#!/usr/bin/env python3
"""Приводит раскладку форм к стандарту docs/FORMS-STYLE.md.

Правит только свойства групп в Form.form, состав и порядок элементов не трогает:

  1. representation = None вместо WeakSeparation - рамок у групп-контейнеров нет.
     Исключения: группа со всплывающим поведением (behavior = PopUp) - рамка там и есть
     само окошко; последняя группа верхнего уровня - она работает подвалом формы.
  2. group = AutoScreenTypeSensitive вместо AlwaysHorizontal - на узком экране колонки
     перестраиваются в столбик.

Использование:
  scripts/forms-style.py <путь> [<путь> ...]      показать, что изменится
  scripts/forms-style.py --применить <путь> ...   записать изменения

Путь - каталог или файл Form.form. Каталоги обходятся рекурсивно, мобильные формы
пропускаются.
"""
import re
import sys
from pathlib import Path

ГРУППА = '<items xsi:type="form:FormGroup">'
EXTINFO = '<extInfo xsi:type="form:UsualGroupExtInfo">'


def блоки_групп(текст):
    """Границы всех групп формы: (начало, конец, глубина)."""
    найденные = []
    for m in re.finditer(re.escape(ГРУППА), текст):
        начало = m.start()
        глубина = текст.count('<items', 0, начало) - текст.count('</items>', 0, начало)
        уровень, позиция = 0, начало
        for tok in re.finditer(r'<items\b[^>]*>|</items>', текст[начало:]):
            уровень += 1 if tok.group(0).startswith('<items') else -1
            if уровень == 0:
                найденные.append((начало, начало + tok.end(), глубина))
                break
    return найденные


def собственный_extinfo(текст, начало, конец):
    """Свойства самой группы лежат последним extInfo её блока - после дочерних элементов."""
    позиции = [m.start() for m in re.finditer(re.escape(EXTINFO), текст[начало:конец])]
    if not позиции:
        return None
    s = начало + позиции[-1]
    return s, текст.index('</extInfo>', s) + len('</extInfo>')


def значение(фрагмент, тег):
    m = re.search(r'<' + тег + r'>([^<]*)</' + тег + r'>', фрагмент)
    return m.group(1) if m else None


def правки_формы(текст):
    """Список правок (позиция extInfo, тег, было, стало), от конца файла к началу."""
    группы = блоки_групп(текст)
    верхние = [g for g in группы if g[2] == 0]
    подвал = верхние[-1][0] if верхние else None

    правки = []
    for начало, конец, _ in группы:
        границы = собственный_extinfo(текст, начало, конец)
        if not границы:
            continue
        s, e = границы
        фрагмент = текст[s:e]

        if значение(фрагмент, 'representation') == 'WeakSeparation':
            всплывающая = значение(фрагмент, 'behavior') == 'PopUp'
            if not всплывающая and начало != подвал:
                правки.append((s, e, 'representation', 'WeakSeparation', 'None'))

        if значение(фрагмент, 'group') == 'AlwaysHorizontal':
            # Исключение стандарта: короткие пары фиксированной ширины (номер + дата)
            # остаются AlwaysHorizontal - см. docs/FORMS-STYLE.md, правило 3.
            имя_группы = re.search(r'<name>([^<]+)</name>', текст[начало:начало + 200])
            if имя_группы and 'НомерИДата' in имя_группы.group(1):
                continue
            правки.append((s, e, 'group', 'AlwaysHorizontal', 'AutoScreenTypeSensitive'))

    return sorted(правки, key=lambda p: -p[0])


def применить(путь, записывать):
    текст = путь.read_text(encoding='utf-8')
    правки = правки_формы(текст)
    if not правки:
        return 0

    новый = текст
    for s, e, тег, было, стало in правки:
        фрагмент = новый[s:e].replace(f'<{тег}>{было}</{тег}>', f'<{тег}>{стало}</{тег}>', 1)
        новый = новый[:s] + фрагмент + новый[e:]

    if записывать:
        путь.write_text(новый, encoding='utf-8')
    return len(правки)


def формы(пути):
    """Формы для правки. Мобильные пропускаются: стандарт описывает интерфейс 8.5 на
    компьютере, у мобильного клиента своя раскладка и проверить её владелец не может."""
    for сырой in пути:
        p = Path(сырой)
        найденные = sorted(p.rglob('Form.form')) if p.is_dir() else ([p] if p.name == 'Form.form' else [])
        for форма in найденные:
            if 'Мобильн' in форма.parent.name or 'MobileClient' in форма.parent.name:
                continue
            yield форма


def main():
    аргументы = sys.argv[1:]
    записывать = '--применить' in аргументы
    пути = [a for a in аргументы if not a.startswith('--')]
    if not пути:
        print(__doc__)
        return 1

    всего_форм = всего_правок = 0
    for форма in формы(пути):
        правок = применить(форма, записывать)
        if правок:
            всего_форм += 1
            всего_правок += правок
            print(f'{правок:3d}  {форма.parent.parent.parent.name}/{форма.parent.name}')

    действие = 'изменено' if записывать else 'будет изменено'
    print(f'\n{действие}: форм {всего_форм}, свойств групп {всего_правок}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
