#!/usr/bin/env python3
"""Сравнивает два файла итогов tools/migration/reconcile.bsl (до перехода и после) по разделам и ключам.

Использование: reconcile.py <до.json> <после.json> [ожидаемое.json] > отчёт.txt
Ожидаемое (необязательно) - список {"Раздел", "Ключ" (точный ключ или "Склад:<uuid>" - все ключи раздела, начинающиеся
с этого uuid), "Количество", "Сумма" (ожидаемая дельта; "*" - любая), "Причина"}. Расхождение, не покрытое ожидаемым
точно, - строка РАСХОЖДЕНИЕ; итог - строка СВЕРКА;расхождений N (код возврата 1 при N > 0).
Файлы итогов содержат данные базы - держать в build/ (в git не попадают).
"""
import json
import sys

EPS = 0.005


def load(path):
    with open(path, encoding='utf-8-sig') as f:
        return json.load(f)


def match(rule, section, key):
    if rule['Раздел'] != section:
        return False
    k = rule['Ключ']
    if k.endswith('*'):
        return key.startswith(k[:-1])
    return key == k


def name(key, names):
    return ' / '.join(names.get(p, p) if p else '-' for p in key.split('/'))


def main():
    before, after = load(sys.argv[1]), load(sys.argv[2])
    expected = load(sys.argv[3]) if len(sys.argv) > 3 else []
    names = dict(before.get('Представления', {}))
    names.update(after.get('Представления', {}))
    bad = 0
    used = [dict(r, Факт_К=0.0, Факт_С=0.0, Ключей=0) for r in expected]
    for section in sorted(set(before['Итоги']) | set(after['Итоги'])):
        b, a = before['Итоги'].get(section), after['Итоги'].get(section)
        if not isinstance(b, dict) or not isinstance(a, dict):
            print(f'РАЗДЕЛ;{section};нет в одном из файлов (до: {type(b).__name__}, после: {type(a).__name__})')
            if section != 'Документы':
                bad += 1
            continue
        diffs = 0
        for key in sorted(set(b) | set(a)):
            vb = b.get(key, {'Количество': 0, 'Сумма': 0})
            va = a.get(key, {'Количество': 0, 'Сумма': 0})
            dq = va['Количество'] - vb['Количество']
            ds = va['Сумма'] - vb['Сумма']
            if abs(dq) < EPS and abs(ds) < EPS:
                continue
            rule = next((r for r in used if match(r, section, key)), None)
            if rule is not None:
                rule['Факт_К'] += dq
                rule['Факт_С'] += ds
                rule['Ключей'] += 1
                print(f'ОЖИДАЕМО;{section};{name(key, names)};кол {dq:+.3f};сумма {ds:+.2f};{rule["Причина"]}')
                continue
            diffs += 1
            print(f'РАСХОЖДЕНИЕ;{section};{name(key, names)};до {vb["Количество"]:.3f}/{vb["Сумма"]:.2f};'
                  f'после {va["Количество"]:.3f}/{va["Сумма"]:.2f};дельта {dq:+.3f}/{ds:+.2f}')
        if section != 'Документы':
            bad += diffs
        print(f'РАЗДЕЛ;{section};ключей до {len(b)};после {len(a)};расхождений {diffs}')
    for r in used:
        ok = True
        for field, fact in (('Количество', r['Факт_К']), ('Сумма', r['Факт_С'])):
            want = r.get(field, '*')
            if want != '*' and abs(fact - want) >= EPS:
                ok = False
        if not ok:
            bad += 1
        print(f'{"ОЖИДАНИЕ" if ok else "РАСХОЖДЕНИЕ"};{r["Раздел"]};{r["Ключ"]};ожидалось {r.get("Количество", "*")}/'
              f'{r.get("Сумма", "*")};факт {r["Факт_К"]:+.3f}/{r["Факт_С"]:+.2f};ключей {r["Ключей"]};{r["Причина"]}')
    print(f'СВЕРКА;расхождений {bad}')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
