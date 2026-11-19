#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261119.

One 1024x1024 poster summing up Thursday 19 November 2026 in four panels:
1. Grand Theft Auto VI rolls out worldwide (Vice City).
2. Hakeem Jeffries to become the first Black Speaker of the U.S. House.
3. Floods deepen the Gaza crisis; four nations urge Israel to let aid in.
4. Anthropic raises $81.3B at $83 a share, the biggest IPO ever.

All artwork is drawn from scratch with PIL primitives (no photos, no logos,
no copyrighted assets). Text is rendered with DejaVu fonts so it stays sharp.
Deterministic: fixed seed, no timestamps, no network.
"""
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
random.seed(19)

img = Image.new("RGB", (W, H), (11, 22, 38))
d = ImageDraw.Draw(img)


def font(path, size):
    return ImageFont.truetype(path, size)


def vgrad(box, top, bottom):
    x0, y0, x1, y1 = box
    for y in range(y0, y1):
        t = (y - y0) / max(1, y1 - y0 - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(x0, y), (x1, y)], fill=c)


def fit_font(text, path, start, max_w):
    size = start
    while size > 12 and font(path, size).getlength(text) > max_w:
        size -= 1
    return font(path, size), size


def wrap(text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- header
vgrad((0, 0, W, 118), (18, 35, 61), (11, 22, 38))
f_date = font(BOLD, 58)
d.text((28, 16), "19 NOVEMBER 2026", fill=(255, 255, 255), font=f_date)
f_sub = font(BOLD, 27)
d.text((30, 80), "THE WORLD IN ONE DAY", fill=(232, 184, 75), font=f_sub)
d.rectangle((0, 116, W, 118), fill=(232, 184, 75))

PANELS = [
    # (x, y, tag, tag_color, headline, caption, draw_fn)
    (14, 126, "GAMING", (201, 75, 124), "VICE CITY OPENS",
     "Grand Theft Auto VI rolls out worldwide after a 13-year wait.", "vice"),
    (518, 126, "POLITICS", (58, 110, 200), "A FIRST FOR THE HOUSE",
     "Hakeem Jeffries to become the first Black Speaker of the U.S. House.", "capitol"),
    (14, 565, "MIDDLE EAST", (46, 130, 140), "FLOODS DEEPEN GAZA CRISIS",
     "Australia, Canada, Italy and the UK urge Israel to let aid reach flooded Gaza.", "gaza"),
    (518, 565, "BUSINESS", (42, 160, 90), "THE BIGGEST IPO EVER",
     "Anthropic raises $81.3 billion at $83 a share — the largest IPO ever.", "ipo"),
]
PW, PH = 492, 427
BAND = 150


def panel_frame(x, y):
    d.rounded_rectangle((x, y, x + PW, y + PH), radius=12, outline=(70, 95, 130), width=2)


def text_band(x, y, tag, tag_color, headline, caption):
    # translucent dark band at the bottom of the panel
    ov = Image.new("RGBA", (PW, BAND), (5, 10, 20, 178))
    img.paste(ov, (x, y + PH - BAND), ov)
    f_h, _ = fit_font(headline, BOLD, 33, PW - 36)
    d.text((x + 18, y + PH - BAND + 12), headline, fill=(255, 255, 255), font=f_h)
    f_c = font(REG, 20)
    lines = wrap(caption, f_c, PW - 36)[:2]
    yy = y + PH - BAND + 56
    for ln in lines:
        d.text((x + 18, yy), ln, fill=(216, 226, 236), font=f_c)
        yy += 26


def tag_pill(x, y, tag, color):
    f_t = font(BOLD, 16)
    tw = f_t.getlength(tag)
    d.rounded_rectangle((x + 12, y + 12, x + 12 + tw + 20, y + 12 + 28), radius=14, fill=color)
    d.text((x + 22, y + 16), tag, fill=(255, 255, 255), font=f_t)


# ---------------------------------------------------------------- panel 1: Vice City dusk
def draw_vice(x, y):
    vgrad((x, y, x + PW, y + PH), (43, 27, 78), (245, 158, 75))
    # sun with glow
    cx, cy = x + PW - 120, y + 150
    for r, a in ((86, 40), (70, 60), (54, 90)):
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        od.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 209, 102, a))
        img.paste(ov, (0, 0), ov)
    d.ellipse((cx - 46, cy - 46, cx + 46, cy + 46), fill=(255, 209, 102))
    # skyline silhouettes
    bx = x + 8
    while bx < x + PW - 20:
        bw = random.randint(34, 62)
        bh = random.randint(90, 210)
        by = y + PH - BAND - bh + 40
        d.rectangle((bx, by, bx + bw, y + PH - BAND + 40), fill=(26, 16, 51))
        # lit windows
        for wy in range(by + 12, y + PH - BAND + 28, 18):
            for wx in range(bx + 7, bx + bw - 6, 14):
                if random.random() < 0.4:
                    d.rectangle((wx, wy, wx + 5, wy + 7),
                                fill=random.choice([(255, 209, 102), (255, 120, 180), (120, 230, 255)]))
        # neon bar on some roofs
        if random.random() < 0.5:
            d.rectangle((bx + 4, by - 4, bx + bw - 4, by),
                        fill=random.choice([(255, 80, 160), (60, 220, 255)]))
        bx += bw + 6
    # palm silhouettes (long drooping fronds)
    for px, ph in ((x + 52, 120), (x + PW - 70, 96)):
        top_x, top_y = px + 8, y + PH - BAND + 40 - ph
        d.line((px, y + PH - BAND + 40, top_x, top_y), fill=(20, 12, 38), width=7)
        for ang in (-75, -45, -15, 15, 45, 75):
            import math
            r = math.radians(ang)
            ex = top_x + 48 * math.sin(r)
            ey = top_y - 14 + 34 * abs(math.sin(r))
            d.line([(top_x, top_y), (ex, ey)], fill=(20, 12, 38), width=5)
    # water reflection
    for i in range(6):
        yy = y + PH - BAND + 52 + i * 9
        d.line((x + 20 + i * 7, yy, x + PW - 20 - i * 5, yy),
               fill=(255, 150, 110), width=3)


def draw_capitol(x, y):
    vgrad((x, y, x + PW, y + PH), (22, 48, 94), (12, 24, 48))
    # stars
    for _ in range(40):
        sx = x + random.randint(10, PW - 10)
        sy = y + random.randint(10, 150)
        r = random.randint(1, 3)
        d.ellipse((sx - r, sy - r, sx + r, sy + r), fill=(255, 255, 255))
    # capitol dome, stylised, light silhouette
    cx = x + PW // 2
    base_y = y + PH - BAND + 30
    col = (226, 232, 240)
    d.rectangle((cx - 150, base_y - 26, cx + 150, base_y), fill=col)          # base
    d.rectangle((cx - 120, base_y - 52, cx + 120, base_y - 26), fill=col)      # terrace
    for i in range(-4, 5):                                                      # columns
        ccx = cx + i * 26
        d.rectangle((ccx - 6, base_y - 108, ccx + 6, base_y - 52), fill=col)
    d.rectangle((cx - 122, base_y - 118, cx + 122, base_y - 108), fill=col)    # entablature
    d.pieslice((cx - 62, base_y - 190, cx + 62, base_y - 66), 180, 360, fill=col)  # dome
    d.rectangle((cx - 62, base_y - 128, cx + 62, base_y - 116), fill=col)      # drum
    d.line((cx, base_y - 190, cx, base_y - 214), fill=col, width=5)            # spire
    d.ellipse((cx - 6, base_y - 220, cx + 6, base_y - 208), fill=col)
    # flag poles flanking
    for fx in (x + 52, x + PW - 52):
        d.line((fx, base_y - 150, fx, base_y), fill=(200, 210, 220), width=4)
        d.polygon([(fx, base_y - 150), (fx + 34, base_y - 141), (fx, base_y - 132)], fill=(200, 60, 70))


def draw_gaza(x, y):
    vgrad((x, y, x + PW, y + PH), (30, 42, 51), (58, 74, 85))
    # storm clouds
    for cx, cy, r in ((x + 90, y + 46, 66), (x + 210, y + 30, 84), (x + 350, y + 52, 74),
                      (x + 430, y + 30, 60), (x + 150, y + 70, 60)):
        d.ellipse((cx - r, cy - r // 2, cx + r, cy + r // 2), fill=(24, 34, 44))
    # rain
    for _ in range(90):
        rx = x + random.randint(6, PW - 6)
        ry = y + random.randint(60, PH - BAND - 60)
        d.line((rx, ry, rx - 7, ry + 20), fill=(170, 200, 220), width=2)
    # flood water
    wy = y + PH - BAND - 66
    d.rectangle((x, wy, x + PW, y + PH), fill=(38, 84, 106))
    for i, yy in enumerate((wy + 18, wy + 40, wy + 62)):
        for k in range(0, PW, 46):
            d.arc((x + k, yy - 8, x + k + 44, yy + 10), 200, 340, fill=(150, 205, 230), width=3)
    # half-submerged houses
    for hx, hw, hh in ((x + 40, 92, 64), (x + 180, 110, 78), (x + 330, 96, 58)):
        d.rectangle((hx, wy - hh + 34, hx + hw, wy + 26), fill=(16, 26, 34))
        d.polygon([(hx - 8, wy - hh + 34), (hx + hw // 2, wy - hh - 6), (hx + hw + 8, wy - hh + 34)],
                  fill=(12, 20, 28))
        d.rectangle((hx + hw // 2 - 9, wy + 2, hx + hw // 2 + 9, wy + 26), fill=(120, 150, 170))
    # aid crate with cross, on a small dry patch
    ax, ay = x + PW - 96, wy - 34
    d.rectangle((ax, ay, ax + 52, ay + 40), fill=(214, 178, 110))
    d.rectangle((ax, ay, ax + 52, ay + 40), outline=(120, 88, 40), width=3)
    d.rectangle((ax + 21, ay + 8, ax + 31, ay + 32), fill=(255, 255, 255))
    d.rectangle((ax + 10, ay + 15, ax + 42, ay + 25), fill=(255, 255, 255))


def draw_ipo(x, y):
    vgrad((x, y, x + PW, y + PH), (14, 36, 31), (18, 59, 47))
    # circuit nodes
    for _ in range(16):
        nx = x + random.randint(16, PW - 16)
        ny = y + random.randint(16, 130)
        d.ellipse((nx - 3, ny - 3, nx + 3, ny + 3), outline=(90, 180, 140), width=2)
    # rising bars
    base_y = y + PH - BAND - 8
    bars = [52, 84, 118, 158, 205]
    bw, gap = 56, 22
    bx = x + 34
    for h in bars:
        d.rectangle((bx, base_y - h, bx + bw, base_y), fill=(42, 160, 90))
        d.rectangle((bx, base_y - h, bx + bw, base_y - h + 8), fill=(120, 230, 160))
        bx += bw + gap
    # gold trend arrow
    pts = [(x + 40, base_y - 40), (x + 130, base_y - 96), (x + 210, base_y - 74),
           (x + 300, base_y - 150), (x + 400, base_y - 196), (x + 452, base_y - 232)]
    d.line(pts, fill=(232, 184, 75), width=6, joint="curve")
    hx, hy = pts[-1]
    d.polygon([(hx - 4, hy + 16), (hx + 20, hy + 2), (hx - 16, hy - 6)], fill=(232, 184, 75))
    # price tag (top-right, clear of the BUSINESS pill)
    f_p = font(BOLD, 30)
    d.text((x + PW - 208, y + 20), "$83 / share", fill=(255, 255, 255), font=f_p)


DRAW = {"vice": draw_vice, "capitol": draw_capitol, "gaza": draw_gaza, "ipo": draw_ipo}

for (px, py, tag, color, headline, caption, kind) in PANELS:
    # clip illustration to the panel rect via a mask
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((px, py, px + PW, py + PH), radius=12, fill=255)
    layer = Image.new("RGB", (W, H), (11, 22, 38))
    old_img, old_d = img, d
    img, d = layer, ImageDraw.Draw(layer)
    DRAW[kind](px, py)
    img, d = old_img, old_d
    img.paste(layer, (0, 0), mask)
    panel_frame(px, py)
    tag_pill(px, py, tag, color)
    text_band(px, py, tag, color, headline, caption)

# ---------------------------------------------------------------- footer
f_f = font(REG, 16)
foot = "Original artwork  •  Headlines as reported on 19 November 2026"
d.text(((W - f_f.getlength(foot)) // 2, 998), foot, fill=(140, 160, 180), font=f_f)

img.save("/home/hatch/workspace/makefun/builds/news-image-20261119/entry.png", optimize=True)
print("saved")
