#!/usr/bin/env python3
"""Генератор макета печати инвентаризации Документ.ПересчётТоваров.ИнвентаризационнаяОпись (Template.mxlx).

Один макет на две формы (docs/plans/inventory-print.md): «Инвентаризационная опись» (все строки) и «Сличительная
ведомость» (строки с расхождением); заголовок формы — параметр. Вариант БезЦен — только количества.

Формат и порядок элементов — как в scripts/mxlxgen/branded.py: ссылки на форматы считаются с единицы, шрифты и линии с
нуля; руками файл не правится. Числа приходят в параметры строками, отформатированными модулем менеджера.

Запуск: python3 scripts/mxlxgen/inventory.py  (перезаписывает макет). После — Refresh в EDT и смок печати.
"""
import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'src/cf/src/Documents/ПересчётТоваров/Templates/ИнвентаризационнаяОпись/Template.mxlx')

LANGS = ('ru', 'en', 'fr', 'es')
ACCENT = '#1F4E79'
MUTED = '#6B7280'
RULE = '#D0D7DE'
SOFT = '#EEF3F8'
WHITE = '#FFFFFF'
PT = 4

# Альбомный лист, ширина 960: № | Арт. | Товар | Ед. | С/с | Учёт кол-во | Учёт сумма | Факт кол-во | Факт сумма |
# Разница кол-во | Разница сумма
WIDTH = 960
TB = [0, 28, 98, 388, 428, 498, 558, 638, 698, 778, 838, 960]
# Без цен: № | Арт. | Товар | Ед. | Учёт | Факт | Разница
NB = [0, 28, 98, 598, 648, 752, 856, 960]

fonts, lines, formats = [], [], []


def font(size, bold=False, italic=False):
    key = (size, bold, italic)
    if key not in fonts:
        fonts.append(key)
    return fonts.index(key)


def line(width=1, style='Solid', kind='Cell'):
    key = (width, style, kind)
    if key not in lines:
        lines.append(key)
    return lines.index(key)


def fmt(**kw):
    key = tuple(sorted(kw.items()))
    for i, f in enumerate(formats):
        if tuple(sorted(f.items())) == key:
            return i + 1
    formats.append(dict(kw))
    return len(formats)


def ml(ru, en, fr, es):
    return {'ru': ru, 'en': en, 'fr': fr, 'es': es}


class Sheet:
    def __init__(self):
        self.rows = []
        self.areas = []

    def row(self, height=None):
        self.rows.append((height, []))
        return len(self.rows) - 1

    def cell(self, r, x, f, param=None, text=None):
        self.rows[r][1].append((x[0], x[1], f, param, text))

    def area(self, name, begin, end):
        self.areas.append((name, begin, end))


S = Sheet()
L_RULE = line(1, 'Solid')
L_ACCENT = line(2, 'Solid')
F_BASE = font(9)


def p(size=9, bold=False, align='Left', color=None, wrap=False, border=False, back=None):
    kw = dict(font=font(size, bold), horizontalAlignment=align, verticalAlignment='Center', fillType='Parameter')
    if color:
        kw['textColor'] = color
    if wrap:
        kw['textPlacement'] = 'Wrap'
    if border:
        kw.update(leftBorder=L_RULE, topBorder=L_RULE, rightBorder=L_RULE, bottomBorder=L_RULE, borderColor=RULE)
    if back:
        kw['backColor'] = back
    return fmt(**kw)


def t(size=8, bold=True, align='Center', border=True):
    kw = dict(font=font(size, bold), horizontalAlignment=align, verticalAlignment='Center', textPlacement='Wrap',
              textColor=WHITE, backColor=ACCENT)
    if border:
        kw.update(leftBorder=L_RULE, topBorder=L_RULE, rightBorder=L_RULE, bottomBorder=L_RULE, borderColor=RULE)
    return fmt(**kw)


# --- Заголовок и реквизиты ------------------------------------------------------------------------------------------
r = S.row(26)
S.cell(r, (0, WIDTH), p(14, True, color=ACCENT), 'ТекстЗаголовка')
S.area('Заголовок', r, r)
r0 = S.row(15)
S.cell(r0, (0, 160), fmt(font=font(9, True), verticalAlignment='Center'),
       text=ml('Организация:', 'Company:', 'Société :', 'Empresa:'))
S.cell(r0, (160, WIDTH), p(9), 'Организация')
r1 = S.row(15)
S.cell(r1, (0, 160), fmt(font=font(9, True), verticalAlignment='Center'),
       text=ml('Место хранения:', 'Storage location:', 'Lieu de stockage :', 'Lugar de almacenamiento:'))
S.cell(r1, (160, WIDTH), p(9), 'МестоХранения')
r2 = S.row(15)
S.cell(r2, (0, 160), fmt(font=font(9, True), verticalAlignment='Center'),
       text=ml('Себестоимость:', 'Cost:', 'Coût de revient :', 'Coste:'))
S.cell(r2, (160, WIDTH), p(9, color=MUTED), 'ПояснениеЦены')
r3 = S.row(8)
S.area('Реквизиты', r0, r3)

HEAD = [
    ml('№', 'No.', 'N°', 'N.º'), ml('Артикул', 'Ref.', 'Réf.', 'Ref.'),
    ml('Товар', 'Item', 'Article', 'Artículo'), ml('Ед.', 'Unit', 'Unité', 'Ud.'),
]
GROUPS = [ml('По учёту', 'Book', 'Théorique', 'Contable'), ml('Фактически', 'Actual', 'Réel', 'Real'),
          ml('Разница', 'Difference', 'Écart', 'Diferencia')]
QTY = ml('Кол-во', 'Qty', 'Qté', 'Cant.')
SUM = ml('Сумма', 'Amount', 'Montant', 'Importe')
COST = ml('С/с за ед.', 'Unit cost', 'Coût unit.', 'Coste ud.')
LINE_PARAMS = ['НомерСтроки', 'Артикул', 'Товар', 'Единица']

# --- Таблица с ценами -----------------------------------------------------------------------------------------------
h1 = S.row(16)
h2 = S.row(16)
for i in range(4):
    S.cell(h1, (TB[i], TB[i + 1]), t(), text=HEAD[i])
    S.cell(h2, (TB[i], TB[i + 1]), t())
S.cell(h1, (TB[4], TB[5]), t(), text=COST)
S.cell(h2, (TB[4], TB[5]), t())
for g in range(3):
    c = 5 + g * 2
    S.cell(h1, (TB[c], TB[c + 2]), t(), text=GROUPS[g])
    S.cell(h2, (TB[c], TB[c + 1]), t(), text=QTY)
    S.cell(h2, (TB[c + 1], TB[c + 2]), t(), text=SUM)
S.area('ШапкаТаблицы', h1, h2)
rl = S.row(None)
for i, name in enumerate(LINE_PARAMS):
    S.cell(rl, (TB[i], TB[i + 1]), p(9, align='Center' if i in (0, 3) else 'Left', wrap=True, border=True), name)
for i, name in enumerate(['Цена', 'Количество', 'Сумма', 'КоличествоФакт', 'СуммаФакт', 'РазницаКоличество',
                          'РазницаСумма'], start=4):
    S.cell(rl, (TB[i], TB[i + 1]), p(9, bold=i >= 9, align='Right', border=True), name)
S.area('Строка', rl, rl)
ri = S.row(18)
S.cell(ri, (TB[0], TB[5]), p(9, True, align='Right', border=True, back=SOFT), 'ПодписьИтога')
for i, name in ((5, None), (6, 'ИтогСумма'), (7, None), (8, 'ИтогСуммаФакт'), (9, None), (10, 'ИтогРазница')):
    S.cell(ri, (TB[i], TB[i + 1]), p(9, True, align='Right', border=True, back=SOFT), name)
S.area('Итого', ri, ri)

# --- Таблица без цен ------------------------------------------------------------------------------------------------
b1 = S.row(22)
for i in range(4):
    S.cell(b1, (NB[i], NB[i + 1]), t(), text=HEAD[i])
for g in range(3):
    S.cell(b1, (NB[4 + g], NB[5 + g]), t(), text=GROUPS[g])
S.area('ШапкаТаблицыБезЦен', b1, b1)
bl = S.row(None)
for i, name in enumerate(LINE_PARAMS):
    S.cell(bl, (NB[i], NB[i + 1]), p(9, align='Center' if i in (0, 3) else 'Left', wrap=True, border=True), name)
for i, name in enumerate(['Количество', 'КоличествоФакт', 'РазницаКоличество'], start=4):
    S.cell(bl, (NB[i], NB[i + 1]), p(9, bold=i == 6, align='Right', border=True), name)
S.area('СтрокаБезЦен', bl, bl)

# --- Нет расхождений, подписи ---------------------------------------------------------------------------------------
rn = S.row(22)
S.cell(rn, (0, WIDTH), p(10, True, color=MUTED), 'ТекстНетРасхождений')
S.area('НетРасхождений', rn, rn)
s0 = S.row(24)
s1 = S.row(18)
S.cell(s1, (0, 160), fmt(font=font(9, True), verticalAlignment='Center'),
       text=ml('Ответственный:', 'Responsible:', 'Responsable :', 'Responsable:'))
S.cell(s1, (160, 440), p(9, border=False), 'Ответственный')
S.cell(s1, (440, 640), fmt(font=F_BASE, bottomBorder=L_RULE, borderColor=RULE))
s2 = S.row(18)
S.cell(s2, (0, 160), fmt(font=font(9, True), verticalAlignment='Center'),
       text=ml('Исполнитель:', 'Counted by:', 'Compté par :', 'Contado por:'))
S.cell(s2, (160, 440), p(9), 'Исполнитель')
S.cell(s2, (440, 640), fmt(font=F_BASE, bottomBorder=L_RULE, borderColor=RULE))
S.area('Подписи', s0, s2)

# --- Сериализация ---------------------------------------------------------------------------------------------------
GRID = sorted({0, WIDTH} | set(TB) | set(NB) | {x for _, cells in S.rows for c in cells for x in c[:2]})
COLS = [b - a for a, b in zip(GRID, GRID[1:])]
NCOLS = len(COLS)
col_fmt = [fmt(width=w) for w in COLS]
f_default = fmt(font=F_BASE)
ORDER = ['font', 'border', 'leftBorder', 'topBorder', 'rightBorder', 'bottomBorder', 'borderColor', 'height', 'width',
         'horizontalAlignment', 'verticalAlignment', 'textColor', 'backColor', 'textPlacement', 'fillType']


def tl(text, ind):
    out = [f'{ind}<tl>']
    for lang in LANGS:
        out += [f'{ind}\t<v8:item>', f'{ind}\t\t<v8:lang>{lang}</v8:lang>',
                f'{ind}\t\t<v8:content>{escape(text[lang])}</v8:content>', f'{ind}\t</v8:item>']
    out.append(f'{ind}</tl>')
    return out


out = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<document xmlns="http://v8.1c.ru/8.2/data/spreadsheet" xmlns:pal="http://v8.1c.ru/8.1/data/ui/colors/palette" '
       'xmlns:style="http://v8.1c.ru/8.1/data/ui/style" xmlns:v8="http://v8.1c.ru/8.1/data/core" '
       'xmlns:v8ui="http://v8.1c.ru/8.1/data/ui" xmlns:xs="http://www.w3.org/2001/XMLSchema" '
       'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">',
       '\t<languageSettings>', '\t\t<currentLanguage>ru</currentLanguage>', '\t\t<defaultLanguage>ru</defaultLanguage>']
for lid, code, desc in (('ru', 'Русский', 'Русский'), ('en', 'English', 'English'), ('fr', 'Francais', 'Français'),
                        ('es', 'Испанский', 'Испанский')):
    out += ['\t\t<languageInfo>', f'\t\t\t<id>{lid}</id>', f'\t\t\t<code>{code}</code>',
            f'\t\t\t<description>{desc}</description>', '\t\t</languageInfo>']
out += ['\t</languageSettings>', '\t<columns>', f'\t\t<size>{NCOLS}</size>']
for i, f in enumerate(col_fmt):
    out += ['\t\t<columnsItem>', f'\t\t\t<index>{i}</index>', '\t\t\t<column>', f'\t\t\t\t<formatIndex>{f}</formatIndex>',
            '\t\t\t</column>', '\t\t</columnsItem>']
out.append('\t</columns>')
merges = []
for idx, (height, cells) in enumerate(S.rows):
    out += ['\t<rowsItem>', f'\t\t<index>{idx}</index>', '\t\t<row>']
    if height is not None:
        out.append(f'\t\t\t<formatIndex>{fmt(height=height * PT)}</formatIndex>')
    placed = {}
    for x0, x1, f, param, text in cells:
        c0, c1 = GRID.index(x0), GRID.index(x1)
        placed[c0] = (f, param, text)
        for c in range(c0 + 1, c1):
            placed[c] = (f, None, None)
        if c1 - c0 > 1:
            merges.append((idx, c0, c1 - c0 - 1))
    if not placed:
        out.append('\t\t\t<empty>true</empty>')
    for c in sorted(placed):
        f, param, text = placed[c]
        out += ['\t\t\t<c>', f'\t\t\t\t<i>{c}</i>', '\t\t\t\t<c>', f'\t\t\t\t\t<f>{f}</f>']
        if param:
            out.append(f'\t\t\t\t\t<parameter>{param}</parameter>')
        if text:
            out += tl(text, '\t\t\t\t\t')
        out += ['\t\t\t\t</c>', '\t\t\t</c>']
    out += ['\t\t</row>', '\t</rowsItem>']
out += ['\t<templateMode>true</templateMode>', f'\t<defaultFormatIndex>{f_default}</defaultFormatIndex>',
        f'\t<height>{len(S.rows)}</height>']
for r, c, w in merges:
    out += ['\t<merge>', f'\t\t<r>{r}</r>', f'\t\t<c>{c}</c>', f'\t\t<w>{w}</w>', '\t</merge>']
for name, b, e in S.areas:
    out += ['\t<namedItem xsi:type="NamedItemCells">', f'\t\t<name>{name}</name>', '\t\t<area>', '\t\t\t<type>Rows</type>',
            f'\t\t\t<beginRow>{b}</beginRow>', f'\t\t\t<endRow>{e}</endRow>', '\t\t\t<beginColumn>-1</beginColumn>',
            '\t\t\t<endColumn>-1</endColumn>', '\t\t</area>', '\t</namedItem>']
for width, style, kind in lines:
    out += [f'\t<line width="{width}" gap="false">',
            f'\t\t<v8ui:style xsi:type="v8ui:SpreadsheetDocument{kind}LineType">{style}</v8ui:style>', '\t</line>']
for size, bold, italic in fonts:
    out.append(f'\t<font faceName="Arial" height="{size}" bold="{str(bold).lower()}" italic="{str(italic).lower()}" '
               'underline="false" strikeout="false" kind="Absolute" scale="100"/>')
for f in formats:
    out.append('\t<format>')
    for k in ORDER:
        if k in f:
            out.append(f'\t\t<{k}>{f[k]}</{k}>')
    out.append('\t</format>')
out.append('</document>')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out) + '\n')
print(OUT, len(S.rows), 'rows', len(formats), 'formats')
