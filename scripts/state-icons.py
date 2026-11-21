#!/usr/bin/env python3
"""Рисует общую картинку СостоянияОбъекта - значки строк списков в одноцветной стилистике интерфейса 8.5.

Коллекция из семи значков 16x16 (индексы заданы платформой и СтрокиТоваровСписков.КартинкаСостояния):
0 - документ проведён, 1 - помечен на удаление, 2 - записан, 3 - элемент, 4 - элемент помечен на удаление,
5 - бизнес-процесс, 6 - бизнес-процесс помечен на удаление.
Результат - Picture.zip с вариантами под плотности экрана 85-400 % (как у общей картинки «Сумма»).

Использование: scripts/state-icons.py [--preview файл.png]
"""
import io
import os
import sys
import zipfile

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'src/cf/src/CommonPictures/СостоянияОбъекта/Picture.zip')
COLOR = (64, 64, 64, 255)   # #404040 - цвет значков разделов 8.5
SS = 8                      # сглаживание: рисуем в 8 раз крупнее и уменьшаем
DENSITIES = [('85.png', 'bldpi', 14), ('100.png', 'ldpi', 16), ('125.png', 'aldpi', 20), ('150.png', 'mdpi', 24),
             ('175.png', 'amdpi', 28), ('200.png', 'hdpi', 32), ('300.png', 'xdpi', 48), ('400.png', 'udpi', 64)]


class Glyph:
    """Холст одного значка в координатах сетки 16x16."""

    def __init__(self, size):
        self.k = size * SS / 16.0
        self.im = Image.new('RGBA', (size * SS, size * SS), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.im)

    def p(self, v):
        return v * self.k

    def line(self, pts, w=1.1, color=COLOR):
        pts = [(self.p(x), self.p(y)) for x, y in pts]
        self.d.line(pts, fill=color, width=max(1, round(self.p(w))), joint='curve')
        r = self.p(w) / 2
        for x, y in pts:
            self.d.ellipse([x - r, y - r, x + r, y + r], fill=color)

    def rect(self, x0, y0, x1, y1, r=1.2, w=1.1, fill=None):
        self.d.rounded_rectangle([self.p(x0), self.p(y0), self.p(x1), self.p(y1)], radius=self.p(r),
                                 outline=COLOR, width=max(1, round(self.p(w))), fill=fill)

    def erase(self, x0, y0, x1, y1):
        self.d.rectangle([self.p(x0), self.p(y0), self.p(x1), self.p(y1)], fill=(0, 0, 0, 0))

    def result(self, size):
        return self.im.resize((size, size), Image.LANCZOS)


def sheet(g, lines=3):
    g.rect(2.5, 1.5, 12.5, 14.5)
    for i in range(lines):
        g.line([(5, 5 + i * 2.6), (10, 5 + i * 2.6)], w=0.9)


def check(g):
    g.erase(7.6, 8.4, 16, 16)
    g.line([(9.2, 12.2), (11.2, 14.2), (15, 9.8)], w=1.5)


def cross(g):
    g.erase(8.6, 8.6, 16, 16)
    g.line([(10, 10), (14.8, 14.8)], w=1.5)
    g.line([(14.8, 10), (10, 14.8)], w=1.5)


def element(g):
    g.rect(2.5, 6, 13.5, 10, r=2, fill=None)


def process(g):
    g.rect(6.5, 1.5, 13.5, 5.5, r=1)
    g.line([(10, 5.5), (10, 8), (4.5, 8), (4.5, 10)], w=0.9)
    g.line([(10, 8), (10, 10)], w=0.9)
    g.rect(2.5, 10, 6.5, 14, r=1)
    g.rect(8, 10, 12, 14, r=1)


def draw(index, size):
    g = Glyph(size)
    if index in (0, 1, 2):
        sheet(g)
    elif index in (3, 4):
        element(g)
    else:
        process(g)
    if index == 0:
        check(g)
    if index in (1, 4, 6):
        cross(g)
    return g.result(size)


def strip(size):
    im = Image.new('RGBA', (size * 7, size), (0, 0, 0, 0))
    for i in range(7):
        im.paste(draw(i, size), (i * size, 0))
    return im


def png(im):
    buf = io.BytesIO()
    im.save(buf, 'PNG')
    return buf.getvalue()


if len(sys.argv) > 2 and sys.argv[1] == '--preview':
    big = strip(64)
    canvas = Image.new('RGBA', (big.width + 40, big.height * 2 + 60), (255, 255, 255, 255))
    canvas.alpha_composite(big, (20, 20))
    canvas.alpha_composite(strip(32), (20, 100))
    canvas.alpha_composite(strip(16), (20, 150))
    canvas.save(sys.argv[2])
    sys.exit(0)

manifest = ['﻿<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', '<Picture>']
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for name, density, size in DENSITIES:
        z.writestr(zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0)), png(strip(size)))
        manifest.append('\t<PictureVariant name="%s" screenDensity="%s" glyphWidth="%d" glyphHeight="%d"/>'
                        % (name, density, size, size))
    z.writestr(zipfile.ZipInfo('Picture.png', (2026, 1, 1, 0, 0, 0)), png(strip(16)))
    for variant in ('version8_2', 'version8_2_OrdinaryApp'):
        manifest.append('\t<PictureVariant name="Picture.png" interfaceVariant="%s" screenDensity="ldpi" '
                        'glyphWidth="16" glyphHeight="16"/>' % variant)
    manifest.append('</Picture>')
    z.writestr(zipfile.ZipInfo('manifest.xml', (2026, 1, 1, 0, 0, 0)), '\r\n'.join(manifest))
print('Записано: ' + OUT)
