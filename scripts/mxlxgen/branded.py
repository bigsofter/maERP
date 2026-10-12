#!/usr/bin/env python3
"""Генератор общего макета фирменных печатных форм ФирменныйДокумент (Template.mxlx).

Один макет на все фирменные формы (docs/plans/branded-print.md): КП, а в следующих фазах Facture, BL, Avoir и
другие. Выводит его общий модуль ФирменнаяПечать; тексты, зависящие от вида формы (заголовок, подписи сторон), -
параметры, а не тексты ячеек. Варианты таблицы - отдельные именованные области ШапкаТаблицы<Вариант> и
Строка<Вариант> (пусто - все колонки, БезСкидки, БезЦен; Фактура; Накладная, НакладнаяБезЦен; Сверка, СверкаБезНДС).

Макет собирается из описания областей ниже, а не правится руками: формат .mxlx — XML-сериализация
табличного документа, где каждая ячейка ссылается на общий список форматов, шрифтов и линий по
индексу; ручная правка такого файла почти всегда ломает индексы. Порядок элементов взят по
работающим макетам конфигурации (DevisBL_A4, ЗаказПоставщику).

Запуск: python3 scripts/mxlxgen/branded.py  (перезаписывает общий макет).
После генерации — Refresh в EDT, scripts/print-preview.sh по каждой затронутой форме (вид проверяется только
глазами, tiny1C tmpl-004) и смок «сформировать все печатные формы».
"""
import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'src/cf/src/CommonTemplates/ФирменныйДокумент/Template.mxlx')

LANGS = ('ru', 'en', 'fr', 'es')

# Палитра
ACCENT = '#1F4E79'
MUTED = '#6B7280'
RULE = '#D0D7DE'
SOFT = '#EEF3F8'
WHITE = '#FFFFFF'

# Сетка колонок - по позициям (единицы ширины колонки mxlx, вся ширина 680): области задаются отрезками [x0, x1),
# а общая сетка листа строится из всех границ. Так у КП и Facture свои колонки в одном макете: КП - прежние 7 колонок
# (ширины 30, 300, 62, 52, 84, 52, 100), Facture - 8 своих.
WIDTH = 680
KP = [0, 30, 330, 392, 444, 528, 580, 680]          # границы колонок КП
FA = [0, 24, 76, 246, 290, 340, 420, 468, 548, 680]  # № | Réf | Désignation | Qté | Ед. | Prix | TVA % | TVA | Montant
BL = [0, 24, 370, 430, 490, 570, 680]                 # BL, Avoir, акт: № | Désignation | Qté | U | Prix | Montant
BN = [0, 24, 500, 580, 680]                           # они же без цен: № | Désignation | Qté | U
SV = [0, 76, 338, 452, 566, 680]                      # акт сверки: Дата | Документ | Дебет | Кредит | НДС
SB = [0, 76, 452, 566, 680]                           # акт сверки без НДС: Дата | Документ | Дебет | Кредит
QT = [0, 24, 300, 370, 450, 530, 590, 680]            # запрос котировок: № | Наименование | Арт. | Код пост. | Код произв. | Ед. | Кол-во
QF = [0, 24, 250, 310, 380, 450, 500, 560, 680]       # запрос котировок с фото: те же колонки уже и Фото
LT = [0, 30, 250, 380, 530, 680]                      # письмо о платеже: № | Документ | Дата BL | № BL | Сумма
PHOTO_ROW = 56                                        # ряд под фото строки, пт: рисунок высоту строки не задаёт
PT = 4  # единиц высоты строки mxlx в одном пункте

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


def kp(c, span=1):
    # Отрезок колонок КП: c - индекс колонки, span - число колонок.
    return KP[c], KP[c + span]


# ---------------------------------------------------------------------------------------------
# Модель листа: строки, ячейки по позициям, именованные области, рисунки


class Sheet:
    def __init__(self):
        self.rows = []          # [(height or None, [(x0, x1, f, param, text)])]
        self.areas = []         # (name, begin, end)
        self.drawings = []      # dict

    def row(self, height=None):
        self.rows.append((height, []))
        return len(self.rows) - 1

    def cell(self, r, x, f, param=None, text=None, vspan=1):
        x0, x1 = x
        self.rows[r][1].append((x0, x1, f, param, text, vspan))

    def rule(self, r, f):
        # Строка-линейка: формат на каждой колонке общей сетки (заполняется при сериализации).
        self.rows[r][1].append((None, None, f, None, None, 1))

    def area(self, name, begin, end):
        self.areas.append((name, begin, end))


S = Sheet()
L_RULE = line(1, 'Solid')
L_ACCENT = line(2, 'Solid')
L_NODRAW = line(1, 'None', 'Drawing')

F_BASE = font(9)
f_text = fmt(font=F_BASE, verticalAlignment='Center')
f_spacer = fmt(font=F_BASE)
f_rule = fmt(font=F_BASE, bottomBorder=L_RULE, borderColor=RULE)

# --- Шапка: логотип слева, реквизиты организации справа ---------------------------------------
top = S.row(8)
r_org = S.row(22)
S.cell(r_org, kp(2, 5), fmt(font=font(14, True), horizontalAlignment='Right', verticalAlignment='Center',
                            textColor=ACCENT, fillType='Parameter'), 'ОрганизацияНаименование')
for name in ('ОрганизацияАдрес', 'ОрганизацияКонтакты', 'ОрганизацияКоды'):
    r = S.row(13)
    S.cell(r, kp(2, 5), fmt(font=font(8), horizontalAlignment='Right', verticalAlignment='Center', textColor=MUTED,
                            fillType='Parameter'), name)
r_rule = S.row(10)
S.rule(r_rule, fmt(font=F_BASE, bottomBorder=L_ACCENT, borderColor=ACCENT))
S.area('Шапка', top, r_rule)
# Имена рисунков - не «Логотип»/«ПечатьОрганизации»: в них ПечатныеФормы.СформироватьПечатныеФормы после вывода
# подставляет текущие картинки организации, а снимок редакции КП печатает свои, сохранённые.
S.drawings.append(dict(name='ЛоготипДокумента', r0=top, r0off=2, r1=r_rule - 1, r1off=10, x0=2, x1=210,
                       size='Proportionally'))

# --- Заголовок ------------------------------------------------------------------------------
r0 = S.row(14)
r_title = S.row(30)
# Заголовок - параметр: его текст на языке печати задаёт вид формы (ФирменнаяПечать.ОписаниеВида).
S.cell(r_title, (0, WIDTH), fmt(font=font(18, True), verticalAlignment='Bottom', textColor=ACCENT,
                                fillType='Parameter'), 'Заголовок')
# Плашка редакции - в строке номера, а не рядом с заголовком: русский заголовок в 18 пт занимает почти всю ширину.
# Без плашки заливку снимает ФирменнаяПечать.Вывести (ячейку находит по параметру «Плашка»).
r_num = S.row(18)
S.cell(r_num, kp(0, 4), fmt(font=font(10), verticalAlignment='Center', textColor=MUTED, fillType='Template'),
       text=ml('№ [Номер] от [Дата]', 'No. [Номер] dated [Дата]', 'N° [Номер] du [Дата]', 'N.º [Номер] del [Дата]'))
S.cell(r_num, kp(4, 3), fmt(font=font(9, True), horizontalAlignment='Center', verticalAlignment='Center',
                            textColor=WHITE, backColor=ACCENT, fillType='Parameter'), 'Плашка')
S.area('Заголовок', r0, r_num)

# --- Стороны КП -----------------------------------------------------------------------------
r0 = S.row(14)
r_lbl = S.row(16)
f_lbl = fmt(font=font(7, True), verticalAlignment='Bottom', textColor=MUTED, bottomBorder=L_RULE, borderColor=RULE)
# Подписи сторон - параметры: у документа поставщику слева поставщик, у акта сверки - контрагент.
f_lbl_p = fmt(font=font(7, True), verticalAlignment='Bottom', textColor=MUTED, bottomBorder=L_RULE, borderColor=RULE,
              fillType='Parameter')
S.cell(r_lbl, kp(0, 2), f_lbl_p, 'ПодписьСтороны')
S.cell(r_lbl, kp(2), f_rule)
S.cell(r_lbl, kp(3, 4), f_lbl_p, 'ПодписьКонтакта')
r_name = S.row(18)
f_party = fmt(font=font(10, True), verticalAlignment='Center', textPlacement='Wrap', fillType='Parameter')
S.cell(r_name, kp(0, 2), f_party, 'КлиентНаименование')
S.cell(r_name, kp(3, 4), f_party, 'Менеджер')
r_det = S.row(None)
f_det = fmt(font=font(8), verticalAlignment='Top', textColor=MUTED, textPlacement='Wrap', fillType='Parameter')
S.cell(r_det, kp(0, 2), f_det, 'КлиентРеквизиты')
S.cell(r_det, kp(3, 4), f_det, 'УсловияКратко')
S.area('Стороны', r0, r_det)

# --- Стороны Facture и Proforma: продавец и покупатель в двух колонках ------------------------
r0 = S.row(14)
r_lbl = S.row(16)
S.cell(r_lbl, (0, 330), f_lbl_p, 'ПодписьСтороны1')
S.cell(r_lbl, (330, 342), f_rule)
S.cell(r_lbl, (342, WIDTH), f_lbl_p, 'ПодписьСтороны2')
r_name = S.row(18)
S.cell(r_name, (0, 330), f_party, 'Сторона1Наименование')
S.cell(r_name, (342, WIDTH), f_party, 'Сторона2Наименование')
r_det = S.row(None)
S.cell(r_det, (0, 330), f_det, 'Сторона1Реквизиты')
S.cell(r_det, (342, WIDTH), f_det, 'Сторона2Реквизиты')
S.area('СтороныФактуры', r0, r_det)

# Сведения документа: основание, договор, комментарий - одной строкой с переносом.
r0 = S.row(6)
r_info = S.row(None)
S.cell(r_info, (0, WIDTH), fmt(font=font(8), verticalAlignment='Top', textPlacement='Wrap', fillType='Parameter'),
       'Сведения')
S.area('СведенияДокумента', r0, r_info)

# --- Таблица КП ------------------------------------------------------------------------------
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
params = ['НомерСтроки', 'Наименование', 'Количество', 'Единица', 'Цена', 'Скидка', 'Сумма']


def table(suffix, cols, bold_col, photo=None):
    # cols: [(заголовок, выравнивание, параметр, (x0, x1))]; photo - высота ряда под фото строки, пт: область строки -
    # ряд текстов с автоматической высотой и ряд под ним, рисунок фото - на оба ряда (строка не ниже фото и растёт с
    # длинным текстом).
    r0 = S.row(14)
    r_head = S.row(22)
    S.rule(r_head, fmt(font=font(8, True), verticalAlignment='Center', textColor=WHITE, backColor=ACCENT))
    for head, align, _, x in cols:
        S.cell(r_head, x, fmt(font=font(8, True), horizontalAlignment=align, verticalAlignment='Center',
                              textColor=WHITE, backColor=ACCENT, textPlacement='Wrap'), text=head)
    S.area('ШапкаТаблицы' + suffix, r0, r_head)
    # Высота строки товара - автоматическая: длинное наименование и единица переносятся, фиксированная высота
    # их обрезала.
    r_line = S.row(None)
    size = 8 if suffix == 'Фактура' else 9
    for i, (_, align, param, x) in enumerate(cols):
        if param is None:
            # Колонка рисунка (фото строки): ячейка без параметра.
            S.cell(r_line, x, fmt(font=font(size), verticalAlignment='Center'))
            continue
        S.cell(r_line, x, fmt(font=font(size, i == bold_col), horizontalAlignment=align, verticalAlignment='Center',
                              textPlacement='Wrap', fillType='Parameter'), param)
    r_end = r_line
    if photo:
        r_end = S.row(photo)
    S.area('Строка' + suffix, r_line, r_end)
    return r_line, r_end


# Варианты таблицы КП: (суффикс области, [(индекс колонки описания, первая колонка КП, число колонок)]).
VARIANTS = [
    ('', [(c, c, 1) for c in range(7)]),
    ('БезСкидки', [(0, 0, 1), (1, 1, 1), (2, 2, 1), (3, 3, 1), (4, 4, 2), (6, 6, 1)]),
    ('БезЦен', [(0, 0, 1), (1, 1, 4), (2, 5, 1), (3, 6, 1)]),
]
for suffix, layout in VARIANTS:
    table(suffix, [(heads[i], aligns[i], params[i], kp(start, span)) for i, start, span in layout], 1)

r_desc = S.row(None)
S.cell(r_desc, kp(1), fmt(font=font(8), verticalAlignment='Top', textColor=MUTED, textPlacement='Wrap',
                          fillType='Parameter'), 'Описание')
S.area('ОписаниеСтроки', r_desc, r_desc)

# --- Таблица Facture и Proforma: колонки старой Facture (В4) и единица старых Счёта и проформы ----------------
fa_cols = [
    (ml('№', 'No.', 'N°', 'N.º'), 'Center', 'НомерСтроки'),
    (ml('Артикул', 'Ref.', 'Réf.', 'Ref.'), 'Left', 'Артикул'),
    (ml('Наименование', 'Description', 'Désignation', 'Descripción'), 'Left', 'Наименование'),
    (ml('Кол-во', 'Qty', 'Qté', 'Cant.'), 'Right', 'Количество'),
    (ml('Ед.', 'Unit', 'Unité', 'Ud.'), 'Center', 'Единица'),
    (ml('Цена', 'Price', 'Prix', 'Precio'), 'Right', 'Цена'),
    (ml('НДС %', 'VAT %', 'TVA %', 'IVA %'), 'Center', 'СтавкаНДС'),
    (ml('НДС', 'VAT', 'TVA', 'IVA'), 'Right', 'СуммаНДС'),
    (ml('Сумма', 'Amount', 'Montant', 'Importe'), 'Right', 'Сумма'),
]
table('Фактура', [(h, a, p, (FA[i], FA[i + 1])) for i, (h, a, p) in enumerate(fa_cols)], 2)

r_desc = S.row(None)
S.cell(r_desc, (FA[2], FA[7]), fmt(font=font(7), verticalAlignment='Top', textColor=MUTED, textPlacement='Wrap',
                                   fillType='Parameter'), 'Описание')
S.area('ОписаниеСтрокиФактура', r_desc, r_desc)

# --- Таблица BL, Avoir и акта: колонки прежних DevisBL и акта об оказании услуг; вариант без цен ------------------
bl_cols = [fa_cols[0], fa_cols[2], fa_cols[3], fa_cols[4], fa_cols[5], fa_cols[8]]
table('Накладная', [(h, a, p, (BL[i], BL[i + 1])) for i, (h, a, p) in enumerate(bl_cols)], 1)
table('НакладнаяБезЦен', [(h, a, p, (BN[i], BN[i + 1])) for i, (h, a, p) in enumerate(bl_cols[:4])], 1)

r_desc = S.row(None)
S.cell(r_desc, (BL[1], BL[4]), fmt(font=font(8), verticalAlignment='Top', textColor=MUTED, textPlacement='Wrap',
                                   fillType='Parameter'), 'Описание')
S.area('ОписаниеСтрокиНакладная', r_desc, r_desc)

# --- Таблица запроса котировок: колонки прежнего ЗапросКотировок (без цен), вариант с фото номенклатуры в строке ------
# (docs/plans/branded-print.md, 13.4). Фото - рисунок ФотоСтроки строки фиксированной высоты; картинку строки задаёт
# ФирменнаяПечать (пустая - строка без фото).
qt_cols = [
    fa_cols[0], fa_cols[2],
    (ml('Артикул', 'Ref.', 'Réf.', 'Ref.'), 'Left', 'Артикул'),
    (ml('Код поставщика', 'Supplier code', 'Code fournisseur', 'Código del proveedor'), 'Left', 'КодПоставщика'),
    (ml('Код производителя', 'Manufacturer code', 'Code fabricant', 'Código del fabricante'), 'Left', 'КодПроизводителя'),
    fa_cols[4], fa_cols[3],
]
table('Котировка', [(h, a, p, (QT[i], QT[i + 1])) for i, (h, a, p) in enumerate(qt_cols)], 1)
qf_cols = qt_cols + [(ml('Фото', 'Photo', 'Photo', 'Foto'), 'Center', None)]
r_text, r_photo = table('КотировкаФото', [(h, a, p, (QF[i], QF[i + 1])) for i, (h, a, p) in enumerate(qf_cols)], 1,
                        PHOTO_ROW)
# Смещения рисунка внутри строки - в четвертях пункта, как высоты строк mxlx (сверено по прежнему ЗапросКотировок): в
# пунктах рисунок занимал четверть ряда под фото.
S.drawings.append(dict(name='ФотоСтроки', r0=r_text, r0off=2 * PT, r1=r_photo, r1off=(PHOTO_ROW - 2) * PT, x0=QF[7] + 4,
                       x1=WIDTH - 4, size='Proportionally'))

r_desc = S.row(None)
S.cell(r_desc, (QT[1], QT[4]), fmt(font=font(8), verticalAlignment='Top', textColor=MUTED, textPlacement='Wrap',
                                   fillType='Parameter'), 'Описание')
S.area('ОписаниеСтрокиКотировка', r_desc, r_desc)

# --- Таблица письма о платеже: основания прежнего LettreDePaiement - документ, дата и номер BL поставщика, сумма ------
lt_cols = [
    fa_cols[0],
    (ml('Документ', 'Document', 'Numéro', 'Documento'), 'Left', 'Документ'),
    (ml('Дата BL', 'BL date', 'Date de BL', 'Fecha BL'), 'Center', 'ДатаОтгрузки'),
    (ml('№ BL', 'BL No.', 'BL n°', 'BL n.º'), 'Left', 'НомерОтгрузки'),
    fa_cols[8],
]
table('Письмо', [(h, a, p, (LT[i], LT[i + 1])) for i, (h, a, p) in enumerate(lt_cols)], -1)

# --- Таблица акта сверки: колонки прежних АктСверки (с НДС строки) и АктСверкиБезНДС; итоговые строки - сальдо и
# обороты в тех же колонках (docs/plans/branded-print.md, 12.4).
sv_cols = [
    (ml('Дата', 'Date', 'Date', 'Fecha'), 'Center', 'Дата'),
    (ml('Документ', 'Document', 'Document', 'Documento'), 'Left', 'Документ'),
    (ml('Дебет', 'Debit', 'Débit', 'Debe'), 'Right', 'Дебет'),
    (ml('Кредит', 'Credit', 'Crédit', 'Haber'), 'Right', 'Кредит'),
    (ml('в т. ч. НДС', 'incl. VAT', 'dont TVA', 'IVA incluido'), 'Right', 'НДС'),
]
f_sv_lbl = fmt(font=font(9, True), verticalAlignment='Center', textPlacement='Wrap', backColor=SOFT,
               fillType='Parameter')
f_sv_val = fmt(font=font(9, True), horizontalAlignment='Right', verticalAlignment='Center', textPlacement='Wrap',
               backColor=SOFT, fillType='Parameter')
for suffix, grid, cols in (('Сверка', SV, sv_cols), ('СверкаБезНДС', SB, sv_cols[:4])):
    table(suffix, [(h, a, p, (grid[i], grid[i + 1])) for i, (h, a, p) in enumerate(cols)], -1)
    r_sum = S.row(None)
    S.cell(r_sum, (0, grid[2]), f_sv_lbl, 'ПодписьИтога')
    for i, name in enumerate(('ИтогДебет', 'ИтогКредит', 'ИтогНДС')[:len(cols) - 2]):
        S.cell(r_sum, (grid[i + 2], grid[i + 3]), f_sv_val, name)
    S.area('СверкаИтог' + suffix[len('Сверка'):], r_sum, r_sum)

# Группа строк: документ отгрузки (BL), к которому относятся следующие строки.
r_grp = S.row(16)
S.cell(r_grp, (FA[1], WIDTH), fmt(font=font(8, True), verticalAlignment='Center', fillType='Parameter'), 'Группа')
S.area('ГруппаСтрок', r_grp, r_grp)

r_sep = S.row(4)
S.rule(r_sep, f_rule)
S.area('РазделительСтрок', r_sep, r_sep)

# --- Итоги ----------------------------------------------------------------------------------
# Значение итогов - на две колонки (≈ 118 пт): «9 999 999,99 MAD» полужирным 10 пт помещается целиком; в одной колонке
# старшие разряды срезались («TOTAL TTC 9 000,00» у суммы 279 000).
X_LBL = (330, 528)
X_VAL = (528, WIDTH)
f_tv = fmt(font=font(9), horizontalAlignment='Right', verticalAlignment='Center', fillType='Parameter')
f_tl = fmt(font=font(9), horizontalAlignment='Right', verticalAlignment='Center', textColor=MUTED)
r_disc = S.row(17)
S.cell(r_disc, X_LBL, f_tl, text=ml('В том числе скидка', 'Discount included', 'Dont remise', 'Descuento incluido'))
S.cell(r_disc, X_VAL, f_tv, 'СуммаСкидки')
S.area('ИтогСкидки', r_disc, r_disc)

r0 = S.row(10)
for lbl, val in ((ml('Итого без НДС', 'Total excl. VAT', 'Total HT', 'Total sin IVA'), 'СуммаБезНДС'),
                 (ml('НДС', 'VAT', 'TVA', 'IVA'), 'СуммаНДС')):
    r = S.row(17)
    S.cell(r, X_LBL, f_tl, text=lbl)
    S.cell(r, X_VAL, f_tv, val)
r_tot = S.row(24)
S.cell(r_tot, X_LBL, fmt(font=font(10, True), horizontalAlignment='Right', verticalAlignment='Center', textColor=WHITE,
                         backColor=ACCENT), text=ml('ИТОГО', 'TOTAL', 'TOTAL TTC', 'TOTAL'))
S.cell(r_tot, X_VAL, fmt(font=font(10, True), horizontalAlignment='Right', verticalAlignment='Center', textColor=WHITE,
                         backColor=ACCENT, fillType='Parameter'), 'Итого')
r_words = S.row(None)
S.cell(r_words, (0, WIDTH), fmt(font=font(8, False, True), verticalAlignment='Top', textColor=MUTED,
                                textPlacement='Wrap', fillType='Parameter'), 'СуммаПрописью')
S.area('Итоги', r0, r_words)

# --- Условия --------------------------------------------------------------------------------
r0 = S.row(12)
r_lbl = S.row(16)
S.rule(r_lbl, f_rule)
S.cell(r_lbl, (0, WIDTH), f_lbl, text=ml('УСЛОВИЯ', 'TERMS', 'CONDITIONS', 'CONDICIONES'))
r_cond = S.row(None)
f_block = fmt(font=font(9), verticalAlignment='Top', textPlacement='Wrap', fillType='Parameter')
S.cell(r_cond, (0, WIDTH), f_block, 'Условия')
S.area('Условия', r0, r_cond)

# Блок с подписью-параметром: способ оплаты, банковские реквизиты.
r0 = S.row(12)
r_lbl = S.row(16)
S.rule(r_lbl, f_rule)
S.cell(r_lbl, (0, WIDTH), f_lbl_p, 'ПодписьБлока')
r_text = S.row(None)
S.cell(r_text, (0, WIDTH), f_block, 'ТекстБлока')
S.area('БлокТекста', r0, r_text)

# Текст акта сверки: вступление с периодом, НДС по ставкам, долг и результат сверки - абзац на всю ширину.
r0 = S.row(6)
r_text = S.row(None)
S.cell(r_text, (0, WIDTH), fmt(font=font(9), verticalAlignment='Top', textPlacement='Wrap', fillType='Parameter'),
       'ТекстСверки')
S.area('СверкаТекст', r0, r_text)

# Квитанция (Reçu ПКО и РКО): сумма крупно с прописью, затем строки «подпись: значение» (основание, касса, статья).
r0 = S.row(12)
r_sum = S.row(26)
S.cell(r_sum, (0, 170), fmt(font=font(9, True), verticalAlignment='Center', textColor=MUTED, topBorder=L_RULE,
                            bottomBorder=L_RULE, borderColor=RULE),
       text=ml('СУММА', 'AMOUNT', 'MONTANT', 'IMPORTE'))
S.cell(r_sum, (170, WIDTH), fmt(font=font(14, True), verticalAlignment='Center', textColor=ACCENT, topBorder=L_RULE,
                                bottomBorder=L_RULE, borderColor=RULE, fillType='Parameter'), 'СуммаКвитанции')
r_words = S.row(None)
S.cell(r_words, (0, WIDTH), fmt(font=font(8, False, True), verticalAlignment='Top', textColor=MUTED,
                                textPlacement='Wrap', fillType='Parameter'), 'СуммаПрописью')
r_gap = S.row(6)
S.area('КвитанцияСумма', r0, r_gap)
r_line = S.row(None)
S.cell(r_line, (0, 170), fmt(font=font(8, True), verticalAlignment='Top', textColor=MUTED, textPlacement='Wrap',
                             fillType='Parameter'), 'ПодписьСтроки')
S.cell(r_line, (170, WIDTH), fmt(font=font(9), verticalAlignment='Top', textPlacement='Wrap', fillType='Parameter'),
       'ЗначениеСтроки')
S.area('КвитанцияСтрока', r_line, r_line)

# Оплаты по документу и долг клиента до документа (BL, Avoir): четыре вида оплаты по четверти ширины, долг - в колонках
# итогов. Подписи видов оплаты - параметры: это представления элементов справочника видов оплаты.
r0 = S.row(12)
r_lbl = S.row(16)
S.rule(r_lbl, f_rule)
S.cell(r_lbl, (0, WIDTH), f_lbl, text=ml('ОПЛАТЫ ПО ДОКУМЕНТУ', 'PAYMENTS', 'RÈGLEMENTS', 'PAGOS'))
r_pay = S.row(18)
f_pay = fmt(font=font(9), verticalAlignment='Center', textPlacement='Wrap', fillType='Parameter')
for i, name in enumerate(('ОплатаНаличные', 'ОплатаЧеком', 'ОплатаПрочие', 'ОплатаКредит')):
    S.cell(r_pay, (170 * i, 170 * (i + 1)), f_pay, name)
r_debt = S.row(18)
S.cell(r_debt, X_LBL, fmt(font=font(9, True), horizontalAlignment='Right', verticalAlignment='Center'),
       text=ml('Долг клиента', 'Customer balance', 'Solde client', 'Saldo del cliente'))
S.cell(r_debt, X_VAL, fmt(font=font(9, True), horizontalAlignment='Right', verticalAlignment='Center',
                          fillType='Parameter'), 'ДолгКлиента')
S.area('ОплатыДокумента', r0, r_debt)

# Сведения печати (BL, Avoir): дата и время печати и кто выписал документ - строка на языке печати.
r0 = S.row(8)
r_info = S.row(14)
S.cell(r_info, (0, WIDTH), fmt(font=font(8), verticalAlignment='Center', textColor=MUTED, fillType='Parameter'),
       'СведенияПечати')
S.area('СведенияПечати', r0, r_info)

# --- Подписи сторон (BL, Avoir, акт): текст над подписями, две колонки с подписью стороны, наименованием и линией;
# печать организации - в левой колонке (исполнитель-организация акта).
r0 = S.row(10)
r_text = S.row(None)
S.cell(r_text, (0, WIDTH), fmt(font=font(9), verticalAlignment='Top', textPlacement='Wrap', fillType='Parameter'),
       'ТекстПодписей')
r_lbl = S.row(22)
f_sig_lbl = fmt(font=font(8, True), verticalAlignment='Bottom', textColor=MUTED, fillType='Parameter')
S.cell(r_lbl, (0, 330), f_sig_lbl, 'ПодписьЛевая')
S.cell(r_lbl, (342, WIDTH), f_sig_lbl, 'ПодписьПравая')
r_name = S.row(None)
f_sig_name = fmt(font=font(9, True), verticalAlignment='Top', textPlacement='Wrap', fillType='Parameter')
S.cell(r_name, (0, 330), f_sig_name, 'НаименованиеЛевое')
S.cell(r_name, (342, WIDTH), f_sig_name, 'НаименованиеПравое')
r_space = S.row(40)
r_line = S.row(6)
f_sig_line = fmt(font=F_BASE, bottomBorder=L_RULE, borderColor=MUTED)
S.cell(r_line, (0, 250), f_sig_line)
S.cell(r_line, (342, 592), f_sig_line)
S.area('ПодписиСторон', r0, r_line)
S.drawings.append(dict(name='ПечатьПодписей', r0=r_space, r0off=0, r1=r_line, r1off=6, x0=120, x1=320,
                       size='Proportionally'))
# Факсимиле подписи руководителя (акт сверки с печатью) - над линией подписи левой колонки.
S.drawings.append(dict(name='ПодписьПодписей', r0=r_space, r0off=0, r1=r_line, r1off=6, x0=0, x1=150,
                       size='Proportionally'))

# --- Подпись КП -----------------------------------------------------------------------------
r0 = S.row(16)
r_sig_lbl = S.row(14)
S.cell(r_sig_lbl, kp(0, 3), fmt(font=font(8), verticalAlignment='Bottom', textColor=MUTED),
       text=ml('С уважением,', 'Kind regards,', 'Cordialement,', 'Atentamente,'))
r_sig = S.row(18)
S.cell(r_sig, kp(0, 3), fmt(font=font(10, True), verticalAlignment='Center', fillType='Parameter'), 'ПодписьМенеджер')
r_sig2 = S.row(14)
S.cell(r_sig2, kp(0, 3), fmt(font=font(8), verticalAlignment='Top', textColor=MUTED, fillType='Parameter'),
       'ПодписьОрганизация')
r_sig3 = S.row(30)
S.area('Подпись', r0, r_sig3)
S.drawings.append(dict(name='ПечатьДокумента', r0=r0, r0off=0, r1=r_sig3, r1off=30, x0=KP[4] + 10, x1=KP[6] + 90,
                       size='Proportionally'))

# --- Подпись Facture: организация, «печать и подпись» и рисунок печати -----------------------
r0 = S.row(16)
r_sig_lbl = S.row(14)
S.cell(r_sig_lbl, (342, WIDTH), fmt(font=font(8), verticalAlignment='Bottom', textColor=MUTED, fillType='Parameter'),
       'ПодписьПечати')
r_sig = S.row(18)
S.cell(r_sig, (342, WIDTH), fmt(font=font(10, True), verticalAlignment='Center', fillType='Parameter'),
       'ПодписьОрганизация')
r_sig3 = S.row(44)
S.area('ПодписьФактуры', r0, r_sig3)
S.drawings.append(dict(name='ПечатьФактуры', r0=r_sig, r0off=0, r1=r_sig3, r1off=44, x0=400, x1=620,
                       size='Proportionally'))

# --- Подвал реквизитов и пустая строка -----------------------------------------------------
r_foot0 = S.row(8)
S.rule(r_foot0, f_rule)
r_foot = S.row(26)
S.cell(r_foot, (0, WIDTH), fmt(font=font(7), horizontalAlignment='Center', verticalAlignment='Center', textColor=MUTED,
                               textPlacement='Wrap', fillType='Parameter'), 'ПодвалРеквизитов')
S.area('ПодвалРеквизитов', r_foot0, r_foot)

r_empty = S.row(14)
S.area('ПустаяСтрока', r_empty, r_empty)

# Общая сетка: все границы колонок всех областей.
GRID = sorted({0, WIDTH} | set(KP) | set(FA) | set(BL) | set(BN) | set(SV) | set(SB) | set(QT) | set(QF) | set(LT) | {x for _, cells in S.rows for c in cells for x in c[:2] if x is not None})
COLS = [b - a for a, b in zip(GRID, GRID[1:])]
NCOLS = len(COLS)


def col_of(x):
    # Колонка общей сетки и смещение внутри неё для позиции рисунка.
    for i in range(NCOLS):
        if GRID[i] <= x < GRID[i + 1]:
            return i, x - GRID[i]
    return NCOLS - 1, COLS[-1]


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

merges = []
for idx, (height, cells) in enumerate(S.rows):
    out += ['\t<rowsItem>', f'\t\t<index>{idx}</index>', '\t\t<row>']
    if height is not None:
        # Высота строки в модели листа - в пунктах, а <height> в mxlx - в четвертях пункта: прочитанный макет
        # отдаёт ВысотаСтроки = height / 4. Пункты без пересчёта сжимали строки КП вчетверо (2.0.16.67).
        out.append(f'\t\t\t<formatIndex>{fmt(height=height * PT)}</formatIndex>')
    placed = {}
    for x0, x1, f, param, text, vspan in cells:
        if x0 is None:
            for c in range(NCOLS):
                placed.setdefault(c, (f, None, None))
            continue
        c0, c1 = GRID.index(x0), GRID.index(x1)
        placed[c0] = (f, param, text)
        # Остальные ячейки объединения - тот же формат: у них свои границы и заливка.
        for c in range(c0 + 1, c1):
            placed[c] = (f, None, None)
        if c1 - c0 > 1 or vspan > 1:
            merges.append((idx, c0, c1 - c0 - 1, vspan - 1))
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

for n, d in enumerate(S.drawings, start=1):
    d['c0'], d['c0off'] = col_of(d['x0'])
    d['c1'], d['c1off'] = col_of(d['x1'])
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
for r, c, w, h in merges:
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
