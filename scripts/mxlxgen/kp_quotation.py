#!/usr/bin/env python3
"""Генератор макета печатной формы коммерческого предложения (Template.mxlx).

Макет собирается из описания областей ниже, а не правится руками: формат .mxlx — XML-сериализация
табличного документа, где каждая ячейка ссылается на общий список форматов, шрифтов и линий по
индексу; ручная правка такого файла почти всегда ломает индексы. Порядок элементов взят по
работающим макетам конфигурации (DevisBL_A4, ЗаказПоставщику).

Запуск: python3 scripts/mxlxgen/kp_quotation.py  (перезаписывает макет документа).
После генерации — Refresh в EDT и смок «сформировать все печатные формы».
"""
import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'src/cf/src/Documents/КоммерческоеПредложение/Templates/КоммерческоеПредложение/Template.mxlx')

LANGS = ('ru', 'en', 'fr', 'es')

# Палитра
ACCENT = '#1F4E79'
MUTED = '#6B7280'
RULE = '#D0D7DE'
SOFT = '#EEF3F8'
WHITE = '#FFFFFF'

# Колонки: № | Наименование | Кол-во | Ед. | Цена | Скидка | Сумма
COLS = [30, 300, 62, 52, 84, 52, 100]
NCOLS = len(COLS)

fonts = []      # (size, bold, italic)
lines = []      # (width, style, kind)
formats = []    # dict -> index


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
    # Ссылки на форматы в mxlx считаются с единицы (f, formatIndex колонок, строк, рисунков, defaultFormatIndex),
    # а шрифты и линии - с нуля: сверено по макетам, которые печатаются (АктСверки). Ссылка с нуля даёт каждой ячейке
    # формат соседа - шаблонная ячейка «№ [Номер] от [Дата]» становилась параметром, печать падала на «Номер».
    key = tuple(sorted(kw.items()))
    for i, f in enumerate(formats):
        if tuple(sorted(f.items())) == key:
            return i + 1
    formats.append(dict(kw))
    return len(formats)


def ml(ru, en, fr, es):
    return {'ru': ru, 'en': en, 'fr': fr, 'es': es}


# ---------------------------------------------------------------------------------------------
# Модель листа: строки, ячейки, объединения, именованные области, рисунки


class Sheet:
    def __init__(self):
        self.rows = []          # [(height or None, {col: cell})]
        self.merges = []        # (r, c, w, h)
        self.areas = []         # (name, begin, end)
        self.drawings = []      # dict

    def row(self, height=None):
        self.rows.append((height, {}))
        return len(self.rows) - 1

    def cell(self, r, c, f, param=None, text=None, span=1, vspan=1):
        self.rows[r][1][c] = (f, param, text)
        if span > 1 or vspan > 1:
            self.merges.append((r, c, span - 1, vspan - 1))

    def area(self, name, begin, end):
        self.areas.append((name, begin, end))


S = Sheet()
L_RULE = line(1, 'Solid')
L_ACCENT = line(2, 'Solid')
L_NODRAW = line(1, 'None', 'Drawing')

F_BASE = font(9)
f_text = fmt(font=F_BASE, verticalAlignment='Center')
f_spacer = fmt(font=F_BASE)

# --- Шапка: логотип слева, реквизиты организации справа ---------------------------------------
top = S.row(8)
r_org = S.row(22)
S.cell(r_org, 2, fmt(font=font(14, True), horizontalAlignment='Right', verticalAlignment='Center',
                     textColor=ACCENT, fillType='Parameter'), 'ОрганизацияНаименование', span=5)
for name in ('ОрганизацияАдрес', 'ОрганизацияКонтакты', 'ОрганизацияКоды'):
    r = S.row(13)
    S.cell(r, 2, fmt(font=font(8), horizontalAlignment='Right', verticalAlignment='Center', textColor=MUTED,
                     fillType='Parameter'), name, span=5)
r_rule = S.row(10)
for c in range(NCOLS):
    S.cell(r_rule, c, fmt(font=F_BASE, bottomBorder=L_ACCENT, borderColor=ACCENT))
S.area('Шапка', top, r_rule)
S.drawings.append(dict(name='ЛоготипПредложения', r0=top, r0off=2, r1=r_rule - 1, r1off=10, c0=0, c0off=2,
                       c1=1, c1off=180, size='Proportionally'))

# --- Заголовок ------------------------------------------------------------------------------
r0 = S.row(14)
r_title = S.row(30)
S.cell(r_title, 0, fmt(font=font(18, True), verticalAlignment='Bottom', textColor=ACCENT),
       text=ml('КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ', 'QUOTATION', 'DEVIS', 'PRESUPUESTO'), span=4)
S.cell(r_title, 4, fmt(font=font(9, True), horizontalAlignment='Center', verticalAlignment='Center', textColor=WHITE,
                       backColor=ACCENT, fillType='Parameter'), 'ПлашкаРедакции', span=3)
r_num = S.row(18)
S.cell(r_num, 0, fmt(font=font(10), verticalAlignment='Center', textColor=MUTED, fillType='Template'),
       text=ml('№ [Номер] от [Дата]', 'No. [Номер] dated [Дата]', 'N° [Номер] du [Дата]', 'N.º [Номер] del [Дата]'), span=7)
S.area('Заголовок', r0, r_num)

# --- Стороны --------------------------------------------------------------------------------
r0 = S.row(14)
r_lbl = S.row(16)
f_lbl = fmt(font=font(7, True), verticalAlignment='Bottom', textColor=MUTED, bottomBorder=L_RULE, borderColor=RULE)
S.cell(r_lbl, 0, f_lbl, text=ml('КЛИЕНТ', 'CUSTOMER', 'CLIENT', 'CLIENTE'), span=2)
S.cell(r_lbl, 2, fmt(font=F_BASE, bottomBorder=L_RULE, borderColor=RULE))
S.cell(r_lbl, 3, f_lbl, text=ml('ВАШ МЕНЕДЖЕР', 'YOUR CONTACT', 'VOTRE CONTACT', 'SU CONTACTO'), span=4)
r_name = S.row(18)
f_party = fmt(font=font(10, True), verticalAlignment='Center', textPlacement='Wrap', fillType='Parameter')
S.cell(r_name, 0, f_party, 'КлиентНаименование', span=2)
S.cell(r_name, 3, f_party, 'Менеджер', span=4)
r_det = S.row(None)
f_det = fmt(font=font(8), verticalAlignment='Top', textColor=MUTED, textPlacement='Wrap', fillType='Parameter')
S.cell(r_det, 0, f_det, 'КлиентРеквизиты', span=2)
S.cell(r_det, 3, f_det, 'УсловияКратко', span=4)
S.area('Стороны', r0, r_det)

# --- Таблица --------------------------------------------------------------------------------
r0 = S.row(14)
r_head = S.row(22)
heads = [
    ml('№', 'No.', 'N°', 'N.º'),
    ml('Наименование', 'Description', 'Désignation', 'Descripción'),
    ml('Кол-во', 'Qty', 'Qté', 'Cant.'),
    ml('Ед.', 'Unit', 'Unité', 'Ud.'),
    ml('Цена', 'Price', 'Prix', 'Precio'),
    ml('Скидка', 'Disc.', 'Remise', 'Dto.'),
    ml('Сумма', 'Amount', 'Montant', 'Importe'),
]
aligns = ['Center', 'Left', 'Right', 'Center', 'Right', 'Right', 'Right']
for c, h in enumerate(heads):
    S.cell(r_head, c, fmt(font=font(8, True), horizontalAlignment=aligns[c], verticalAlignment='Center',
                          textColor=WHITE, backColor=ACCENT), text=h)
S.area('ШапкаТаблицы', r0, r_head)

r_line = S.row(18)
params = ['НомерСтроки', 'Наименование', 'Количество', 'Единица', 'Цена', 'Скидка', 'Сумма']
for c, p in enumerate(params):
    S.cell(r_line, c, fmt(font=font(9, c == 1), horizontalAlignment=aligns[c], verticalAlignment='Center',
                          textPlacement='Wrap', fillType='Parameter'), p)
S.area('Строка', r_line, r_line)

r_desc = S.row(None)
S.cell(r_desc, 1, fmt(font=font(8), verticalAlignment='Top', textColor=MUTED, textPlacement='Wrap',
                      fillType='Parameter'), 'Описание')
S.area('ОписаниеСтроки', r_desc, r_desc)

r_sep = S.row(4)
for c in range(NCOLS):
    S.cell(r_sep, c, fmt(font=F_BASE, bottomBorder=L_RULE, borderColor=RULE))
S.area('РазделительСтрок', r_sep, r_sep)

# --- Итоги ----------------------------------------------------------------------------------
r0 = S.row(10)
f_tl = fmt(font=font(9), horizontalAlignment='Right', verticalAlignment='Center', textColor=MUTED, fillType='Parameter')
f_tv = fmt(font=font(9), horizontalAlignment='Right', verticalAlignment='Center', fillType='Parameter')
f_tl = fmt(font=font(9), horizontalAlignment='Right', verticalAlignment='Center', textColor=MUTED)
for lbl, val in ((ml('Итого без НДС', 'Total excl. VAT', 'Total HT', 'Total sin IVA'), 'СуммаБезНДС'),
                 (ml('НДС', 'VAT', 'TVA', 'IVA'), 'СуммаНДС')):
    r = S.row(17)
    S.cell(r, 3, f_tl, text=lbl, span=3)
    S.cell(r, 6, f_tv, val)
r_tot = S.row(24)
S.cell(r_tot, 3, fmt(font=font(10, True), horizontalAlignment='Right', verticalAlignment='Center', textColor=WHITE,
                     backColor=ACCENT), text=ml('ИТОГО', 'TOTAL', 'TOTAL TTC', 'TOTAL'), span=3)
S.cell(r_tot, 6, fmt(font=font(10, True), horizontalAlignment='Right', verticalAlignment='Center', textColor=WHITE,
                     backColor=ACCENT, fillType='Parameter'), 'Итого')
r_words = S.row(None)
S.cell(r_words, 0, fmt(font=font(8, False, True), verticalAlignment='Top', textColor=MUTED, textPlacement='Wrap',
                       fillType='Parameter'), 'СуммаПрописью', span=7)
S.area('Итоги', r0, r_words)

# --- Условия --------------------------------------------------------------------------------
r0 = S.row(12)
r_lbl = S.row(16)
for c in range(NCOLS):
    S.cell(r_lbl, c, fmt(font=F_BASE, bottomBorder=L_RULE, borderColor=RULE))
S.cell(r_lbl, 0, f_lbl, text=ml('УСЛОВИЯ', 'TERMS', 'CONDITIONS', 'CONDICIONES'), span=7)
r_cond = S.row(None)
S.cell(r_cond, 0, fmt(font=font(9), verticalAlignment='Top', textPlacement='Wrap', fillType='Parameter'),
       'Условия', span=7)
S.area('Условия', r0, r_cond)

# --- Подпись --------------------------------------------------------------------------------
r0 = S.row(16)
r_sig_lbl = S.row(14)
S.cell(r_sig_lbl, 0, fmt(font=font(8), verticalAlignment='Bottom', textColor=MUTED),
       text=ml('С уважением,', 'Kind regards,', 'Cordialement,', 'Atentamente,'), span=3)
r_sig = S.row(18)
S.cell(r_sig, 0, fmt(font=font(10, True), verticalAlignment='Center', fillType='Parameter'), 'ПодписьМенеджер', span=3)
r_sig2 = S.row(14)
S.cell(r_sig2, 0, fmt(font=font(8), verticalAlignment='Top', textColor=MUTED, fillType='Parameter'),
       'ПодписьОрганизация', span=3)
r_sig3 = S.row(30)
S.area('Подпись', r0, r_sig3)
S.drawings.append(dict(name='ПечатьПредложения', r0=r0, r0off=0, r1=r_sig3, r1off=30, c0=4, c0off=10,
                       c1=6, c1off=90, size='Proportionally'))

# --- Подвал реквизитов и пустая строка -----------------------------------------------------
r_foot0 = S.row(8)
for c in range(NCOLS):
    S.cell(r_foot0, c, fmt(font=F_BASE, bottomBorder=L_RULE, borderColor=RULE))
r_foot = S.row(26)
S.cell(r_foot, 0, fmt(font=font(7), horizontalAlignment='Center', verticalAlignment='Center', textColor=MUTED,
                      textPlacement='Wrap', fillType='Parameter'), 'ПодвалРеквизитов', span=7)
S.area('ПодвалРеквизитов', r_foot0, r_foot)

r_empty = S.row(14)
S.area('ПустаяСтрока', r_empty, r_empty)

# ---------------------------------------------------------------------------------------------
# Сериализация

col_fmt = [fmt(width=w) for w in COLS]
row_fmt = {}
f_draw = fmt(drawingBorder=L_NODRAW)
f_default = fmt(font=F_BASE)

ORDER = ['drawingBorder', 'font', 'border', 'leftBorder', 'topBorder', 'rightBorder', 'bottomBorder', 'borderColor',
         'height', 'width', 'horizontalAlignment', 'verticalAlignment', 'textColor', 'backColor', 'textPlacement',
         'fillType']


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

for idx, (height, cells) in enumerate(S.rows):
    out += ['\t<rowsItem>', f'\t\t<index>{idx}</index>', '\t\t<row>']
    if height is not None:
        out.append(f'\t\t\t<formatIndex>{fmt(height=height)}</formatIndex>')
    if not cells:
        out.append('\t\t\t<empty>true</empty>')
    for c in sorted(cells):
        f, param, text = cells[c]
        out += ['\t\t\t<c>', f'\t\t\t\t<i>{c}</i>', '\t\t\t\t<c>', f'\t\t\t\t\t<f>{f}</f>']
        if param:
            out.append(f'\t\t\t\t\t<parameter>{param}</parameter>')
        if text:
            out += tl(text, '\t\t\t\t\t')
        out += ['\t\t\t\t</c>', '\t\t\t</c>']
    out += ['\t\t</row>', '\t</rowsItem>']

for n, d in enumerate(S.drawings, start=1):
    out += ['\t<drawing>', '\t\t<drawingType>Picture</drawingType>', f'\t\t<id>{n}</id>',
            f'\t\t<formatIndex>{f_draw}</formatIndex>',
            f'\t\t<beginRow>{d["r0"]}</beginRow>', f'\t\t<beginRowOffset>{d["r0off"]}</beginRowOffset>',
            f'\t\t<endRow>{d["r1"]}</endRow>', f'\t\t<endRowOffset>{d["r1off"]}</endRowOffset>',
            f'\t\t<beginColumn>{d["c0"]}</beginColumn>', f'\t\t<beginColumnOffset>{d["c0off"]}</beginColumnOffset>',
            f'\t\t<endColumn>{d["c1"]}</endColumn>', f'\t\t<endColumnOffset>{d["c1off"]}</endColumnOffset>',
            '\t\t<autoSize>false</autoSize>', f'\t\t<pictureSize>{d["size"]}</pictureSize>',
            f'\t\t<zOrder>{n}</zOrder>', '\t\t<pictureIndex>1</pictureIndex>', '\t</drawing>']

out += ['\t<templateMode>true</templateMode>', f'\t<defaultFormatIndex>{f_default}</defaultFormatIndex>',
        f'\t<height>{len(S.rows)}</height>']
for r, c, w, h in S.merges:
    out += ['\t<merge>', f'\t\t<r>{r}</r>', f'\t\t<c>{c}</c>']
    if w:
        out.append(f'\t\t<w>{w}</w>')
    if h:
        out.append(f'\t\t<h>{h}</h>')
    out.append('\t</merge>')
for name, b, e in S.areas:
    out += ['\t<namedItem xsi:type="NamedItemCells">', f'\t\t<name>{name}</name>', '\t\t<area>', '\t\t\t<type>Rows</type>',
            f'\t\t\t<beginRow>{b}</beginRow>', f'\t\t\t<endRow>{e}</endRow>', '\t\t\t<beginColumn>-1</beginColumn>',
            '\t\t\t<endColumn>-1</endColumn>', '\t\t</area>', '\t</namedItem>']
for n, d in enumerate(S.drawings, start=1):
    out += ['\t<namedItem xsi:type="NamedItemDrawing">', f'\t\t<name>{d["name"]}</name>',
            f'\t\t<drawingID>{n}</drawingID>', '\t</namedItem>']
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
out += ['\t<picture>', '\t\t<index>0</index>', '\t\t<picture/>', '\t</picture>', '</document>']

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out) + '\n')
print(OUT, len(S.rows), 'rows', len(formats), 'formats')
