#!/usr/bin/env python3
# Заставка maERP (Configuration/Splash.jpg): карандашный эскиз склада, грузовиков и щита с графиком, как у типовых
# конфигураций 1С. Использование: scripts/splash.py 610 460 src/cf/src/Configuration/Splash.jpg
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(7)
W, H = int(sys.argv[1]), int(sys.argv[2])
S = 3  # суперсэмплинг
OUT = sys.argv[3]
img = Image.new('L', (W * S, H * S), 255)
d = ImageDraw.Draw(img)


def P(x, y):
    # координаты сцены заданы в долях 1000x450, вписываются по ширине
    k = W * S / 1000
    return (x * k, (y + (H * 1000 / W - 450) / 2) * k)


def stroke(a, b, w=1.6, tone=60, passes=2, jit=1.2):
    """Карандашная линия: несколько проходов с дрожанием и разным нажимом."""
    k = W * S / 1000
    for p in range(passes):
        (x1, y1), (x2, y2) = P(*a), P(*b)
        n = max(2, int(math.hypot(x2 - x1, y2 - y1) / (18 * k)))
        pts = []
        ox1, oy1 = random.uniform(-jit, jit) * k, random.uniform(-jit, jit) * k
        ox2, oy2 = random.uniform(-jit, jit) * k, random.uniform(-jit, jit) * k
        for i in range(n + 1):
            t = i / n
            pts.append((x1 + (x2 - x1) * t + ox1 * (1 - t) + ox2 * t + random.uniform(-.35, .35) * k,
                        y1 + (y2 - y1) * t + oy1 * (1 - t) + oy2 * t + random.uniform(-.35, .35) * k))
        c = min(235, tone + random.randint(0, 45) + p * 30)
        d.line(pts, fill=c, width=max(1, int(w * k * (1 - .25 * p))))


def poly(pts, close=True, **kw):
    for i in range(len(pts) - (0 if close else 1)):
        stroke(pts[i], pts[(i + 1) % len(pts)], **kw)


def hatch(pts, step=6, angle=60, tone=150, w=.8):
    """Штриховка многоугольника параллельными линиями."""
    k = W * S / 1000
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    a = math.radians(angle)
    dx, dy = math.cos(a), math.sin(a)
    cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
    R = max(max(xs) - min(xs), max(ys) - min(ys))
    t = -R
    while t <= R:
        # прямая через точку смещения по нормали
        px, py = cx - dy * t, cy + dx * t
        hits = []
        for i in range(len(pts)):
            (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % len(pts)]
            den = dx * (y2 - y1) - dy * (x2 - x1)
            if abs(den) < 1e-9:
                continue
            u = ((x1 - px) * (y2 - y1) - (y1 - py) * (x2 - x1)) / den
            v = ((x1 - px) * dy - (y1 - py) * dx) / den
            if 0 <= v <= 1:
                hits.append(u)
        hits.sort()
        for j in range(0, len(hits) - 1, 2):
            a1 = (px + dx * hits[j], py + dy * hits[j]); a2 = (px + dx * hits[j + 1], py + dy * hits[j + 1])
            if random.random() < .9:
                stroke(a1, a2, w=w, tone=tone, passes=1, jit=.6)
        t += step * random.uniform(.8, 1.2)


def rect(x, y, ww, hh, **kw):
    poly([(x, y), (x + ww, y), (x + ww, y + hh), (x, y + hh)], **kw)


# --- горизонт и земля ---------------------------------------------------------
stroke((0, 330), (1000, 318), w=1, tone=170)
for i in range(40):
    x = random.uniform(0, 1000); y = random.uniform(345, 445)
    stroke((x, y), (x + random.uniform(15, 50), y - random.uniform(0, 3)), w=.6, tone=200, passes=1)

# --- щит с графиком справа (перспектива) ------------------------------------
board = [(690, 30), (985, 12), (985, 262), (690, 240)]
poly(board, w=2, tone=40)
poly([(700, 40), (975, 23), (975, 250), (700, 230)], w=1, tone=120)
for i in range(1, 7):  # сетка
    y1 = 30 + i * 27; y2 = 12 + i * 33
    stroke((700, y1), (980, y2), w=.6, tone=190, passes=1)
for i in range(1, 9):
    x = 700 + i * 31
    stroke((x, 30 - (x - 700) * .064), (x, 220 + (x - 700) * .082), w=.6, tone=190, passes=1)
chart = [(712, 190), (760, 170), (805, 178), (850, 130), (895, 140), (940, 80), (968, 55)]
for i in range(len(chart) - 1):
    stroke(chart[i], chart[i + 1], w=2.4, tone=30, passes=3)
k = W * S / 1000
for p in chart[1:-1]:
    x, y = P(*p); r = 5 * k
    d.ellipse((x - r, y - r, x + r, y + r), outline=40, width=int(1.6 * k), fill=230)
ax, ay = chart[-1]  # стрелка
stroke((ax, ay), (ax - 16, ay + 2), w=2.2, tone=30); stroke((ax, ay), (ax - 6, ay + 15), w=2.2, tone=30)
# опоры щита
stroke((740, 236), (735, 330), w=2, tone=60); stroke((950, 257), (955, 322), w=2, tone=60)

# --- склад: фасад и боковая стена ---------------------------------------------
front = [(140, 150), (470, 150), (470, 330), (140, 330)]
side = [(470, 150), (610, 175), (610, 318), (470, 330)]
roof = [(120, 150), (155, 105), (455, 105), (490, 150)]
roof_side = [(455, 105), (490, 150), (630, 175), (600, 132)]
poly(front, w=2.2, tone=40); poly(side, w=2, tone=50)
poly(roof, w=2, tone=40); poly(roof_side, w=1.8, tone=50)
hatch(side, step=7, angle=75, tone=170)
hatch(roof_side, step=6, angle=20, tone=140)
for i in range(1, 14):  # профнастил крыши
    x = 155 + i * 23
    stroke((x - 35 * (1 - (x - 155) / 300) * 0 , 106), (x - 2, 149), w=.6, tone=170, passes=1)
# окна ленточные
for row in (175, 205):
    for i in range(9):
        rect(160 + i * 33, row, 22, 14, w=1.1, tone=70)
        hatch([(160 + i * 33, row), (182 + i * 33, row), (182 + i * 33, row + 14), (160 + i * 33, row + 14)],
              step=4, angle=45, tone=120, w=.6)
# ворота с навесами
for i in range(4):
    x = 165 + i * 75
    rect(x, 250, 52, 80, w=1.6, tone=50)
    for j in range(1, 8):
        stroke((x + 2, 250 + j * 10), (x + 50, 250 + j * 10), w=.6, tone=150, passes=1)
    stroke((x - 6, 244), (x + 58, 244), w=1.6, tone=50)
hatch([(480, 338), (610, 318), (680, 330), (560, 352)], step=4, angle=10, tone=175)
hatch([(140, 338), (480, 338), (470, 352), (130, 352)], step=3, angle=0, tone=185)
# рампа
poly([(150, 330), (470, 330), (480, 338), (140, 338)], w=1.2, tone=90)
# боковые окна
for i in range(4):
    x = 488 + i * 30
    poly([(x, 210 + i * 5.3), (x + 18, 213 + i * 5.3), (x + 18, 228 + i * 5.3), (x, 225 + i * 5.3)], w=1, tone=80)

# --- деревья слева ------------------------------------------------------------
def tree(cx, base, h, r):
    stroke((cx, base), (cx + 1, base - h * .45), w=2, tone=60)
    for _ in range(int(r * 9)):
        a = random.uniform(0, 2 * math.pi); rr = r * math.sqrt(random.random())
        x = cx + math.cos(a) * rr; y = base - h * .62 + math.sin(a) * rr * 1.05
        b = random.uniform(0, 2 * math.pi); L = random.uniform(4, 9)
        stroke((x, y), (x + math.cos(b) * L, y + math.sin(b) * L), w=.9, tone=random.randint(40, 150) + (25 if math.sin(a) < -.3 else 0), passes=1, jit=.4)


for cx, h, r in [(30, 150, 34), (75, 170, 40), (115, 140, 30)]:
    tree(cx, 330, h, r)

# --- грузовики ----------------------------------------------------------------
def truck(x, y, s=1.0, flip=False):
    def q(px, py):
        return (x + (-px if flip else px) * s, y + py * s)
    body = [q(0, -42), q(62, -42), q(62, 0), q(0, 0)]
    cab = [q(62, -28), q(80, -28), q(88, -14), q(88, 0), q(62, 0)]
    poly(body, w=1.6, tone=40); poly(cab, w=1.6, tone=40)
    hatch(body, step=5, angle=80, tone=200, w=.6)
    poly([q(66, -25), q(78, -25), q(84, -15), q(66, -15)], w=.9, tone=80)
    for wx in (16, 72):
        cx, cy = P(*q(wx, 2)); rr = 7 * s * k
        d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=30, width=int(1.8 * k), fill=110)


truck(200, 372, .8)
truck(330, 405, 1.0)
truck(490, 392, .9)
truck(690, 362, .75, flip=True)

# --- навесы/киоски справа -----------------------------------------------------
for x0 in (790, 880):
    poly([(x0, 300), (x0 + 75, 296), (x0 + 75, 335), (x0, 340)], w=1.5, tone=50)
    poly([(x0 - 6, 300), (x0 + 81, 295), (x0 + 75, 286), (x0, 290)], w=1.3, tone=60)
    hatch([(x0 - 6, 300), (x0 + 81, 295), (x0 + 75, 286), (x0, 290)], step=3, angle=0, tone=120)
    rect(x0 + 10, 308, 20, 16, w=.9, tone=90)

# --- люди ---------------------------------------------------------------------
def person(x, y, s=1.0):
    cx, cy = P(x, y - 22 * s); rr = 2.6 * s * k
    d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), fill=60)
    stroke((x, y - 19 * s), (x, y - 9 * s), w=1.6 * s, tone=50, passes=1)
    stroke((x, y - 9 * s), (x - 3 * s, y), w=1.2 * s, tone=50, passes=1)
    stroke((x, y - 9 * s), (x + 3 * s, y), w=1.2 * s, tone=50, passes=1)
    stroke((x, y - 17 * s), (x + random.choice((-4, 4)) * s, y - 11 * s), w=1 * s, tone=60, passes=1)


for x, y, s in [(660, 380, 1), (700, 405, 1.1), (740, 360, .9), (840, 395, 1), (905, 370, .9), (520, 420, 1.1),
                (620, 430, 1.1), (960, 410, 1)]:
    person(x, y, s)

# --- дорога: колеи ------------------------------------------------------------
stroke((180, 445), (640, 340), w=.9, tone=180)
stroke((300, 450), (720, 345), w=.9, tone=180)

# --- сборка: лёгкая бумага и виньетка, заголовок -----------------------------
img = img.filter(ImageFilter.GaussianBlur(.6 * S / 3))
img = img.resize((W, H), Image.LANCZOS)
rgb = Image.merge('RGB', (img, img, img))
# тёплая бумага
paper = Image.new('RGB', (W, H), (250, 249, 246))
rgb = Image.composite(rgb, paper, img.point(lambda v: 255 - v).convert('L').point(lambda v: 255))
rgb = Image.blend(Image.new('RGB', (W, H), (250, 249, 246)), rgb, 1.0)
px = rgb.load()
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        m = min(r, 250)
        px[x, y] = (min(r, 250), min(g, 249), min(b, 246)) if m > 240 else (r, g, b)

dd = ImageDraw.Draw(rgb)
# белая подложка под заголовок слева сверху, как у КА
title = 'maERP'
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', int(H * .085))
sub = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', int(H * .036))
tx, ty = int(W * .022), int(H * .03)
dd.text((tx, ty), title, font=font, fill=(25, 28, 32))
tb = dd.textbbox((tx, ty), title, font=font)
dd.text((tx + 2, tb[3] + int(H * .012)), 'Commerce · Production · Finance', font=sub, fill=(90, 98, 108))
rgb.save(OUT, quality=95)
print(OUT, rgb.size)
