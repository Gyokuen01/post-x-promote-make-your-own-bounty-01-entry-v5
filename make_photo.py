#!/usr/bin/env python3
"""Draw photo.png for the post-x-promote entry.

A flat illustration, 1080x1080: a light-blue robot sits behind a wooden
desk with a laptop, a big screen behind it shows a pixel platformer game,
a gold trophy stands on the desk, and the background is dark green with
stars and confetti. Run: python3 make_photo.py
"""

import os
import random

from PIL import Image, ImageDraw, ImageFont

W = H = 1080
random.seed(7)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "photo.png")

# --- palette ------------------------------------------------------------
DARK_GREEN = (14, 59, 46)
SCREEN_BLUE = (16, 42, 92)
SCREEN_EDGE = (210, 225, 255)
SKY_MOON = (240, 238, 210)
CLOUD = (235, 242, 255)
PLATFORM = (146, 96, 48)
PLATFORM_TOP = (198, 142, 66)
COIN = (255, 210, 63)
COIN_EDGE = (176, 124, 8)
HERO = (220, 60, 60)
SLIME = (74, 180, 92)
WOOD = (139, 90, 43)
WOOD_DARK = (104, 64, 28)
GOLD = (255, 196, 0)
GOLD_DARK = (176, 124, 8)
ROBOT = (147, 197, 253)
ROBOT_DARK = (96, 140, 200)
ROBOT_PANEL = (38, 78, 130)
LAPTOP = (30, 34, 44)
LAPTOP_SCREEN = (18, 24, 40)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

img = Image.new("RGB", (W, H), DARK_GREEN)
d = ImageDraw.Draw(img)


def font(size):
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


# --- stars and confetti in the dark-green background --------------------
for _ in range(90):
    x = random.randint(10, W - 10)
    y = random.randint(10, 420)
    r = random.randint(1, 3)
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 244, 180))

confetti_colors = [(255, 99, 99), (255, 210, 63), (96, 165, 250), (244, 114, 182)]
for _ in range(46):
    x = random.randint(10, W - 10)
    y = random.randint(10, H - 10)
    w = random.randint(6, 12)
    h = random.randint(4, 8)
    d.rectangle([x, y, x + w, y + h], fill=random.choice(confetti_colors))

# --- big screen: pixel platformer game ----------------------------------
d.rounded_rectangle([70, 60, 1010, 560], radius=28,
                    fill=SCREEN_BLUE, outline=SCREEN_EDGE, width=6)

# moon
d.ellipse([880, 95, 950, 165], fill=SKY_MOON)
d.ellipse([900, 110, 920, 130], fill=(214, 212, 186))
d.ellipse([925, 135, 940, 150], fill=(214, 212, 186))

# clouds
for cx, cy in ((140, 130), (330, 100), (620, 140)):
    d.ellipse([cx, cy, cx + 90, cy + 34], fill=CLOUD)
    d.ellipse([cx + 22, cy - 16, cx + 72, cy + 18], fill=CLOUD)

# ground strip inside the screen
d.rectangle([82, 470, 998, 548], fill=(52, 110, 62))
for gx in range(90, 990, 30):
    d.rectangle([gx, 470, gx + 16, 478], fill=(76, 150, 84))

# block platforms
def platform(x, y, n):
    for i in range(n):
        bx = x + i * 52
        d.rectangle([bx, y, bx + 52, y + 52], fill=PLATFORM,
                    outline=PLATFORM_TOP, width=3)
        d.rectangle([bx + 8, y + 8, bx + 20, y + 20], fill=PLATFORM_TOP)
        d.rectangle([bx + 30, y + 26, bx + 44, y + 40], fill=PLATFORM_TOP)

platform(120, 380, 3)
platform(700, 340, 3)
platform(420, 250, 2)

# gold coins
for cx, cy in ((300, 330), (360, 330), (520, 200), (580, 200), (840, 300)):
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=COIN,
              outline=COIN_EDGE, width=3)
    d.ellipse([cx - 6, cy - 8, cx + 6, cy + 8], outline=COIN_EDGE, width=2)

# red hero standing on the left platform
d.rounded_rectangle([185, 318, 235, 380], radius=8, fill=HERO,
                    outline=(140, 30, 30), width=3)
d.ellipse([198, 332, 212, 346], fill=WHITE)
d.ellipse([216, 332, 230, 346], fill=WHITE)
d.ellipse([202, 336, 208, 342], fill=BLACK)
d.ellipse([220, 336, 226, 342], fill=BLACK)

# green slime on the ground
d.ellipse([640, 420, 730, 470], fill=SLIME, outline=(40, 120, 56), width=3)
d.ellipse([665, 432, 683, 450], fill=WHITE)
d.ellipse([695, 432, 713, 450], fill=WHITE)
d.ellipse([671, 438, 677, 444], fill=BLACK)
d.ellipse([701, 438, 707, 444], fill=BLACK)

# --- wooden desk ---------------------------------------------------------
d.rectangle([40, 760, 1040, 940], fill=WOOD)
for gy in (800, 840, 880):
    d.line([40, gy, 1040, gy], fill=WOOD_DARK, width=3)
d.rectangle([40, 760, 1040, 772], fill=PLATFORM_TOP)

# --- gold trophy on the desk, left ---------------------------------------
d.polygon([(150, 640), (260, 640), (245, 700), (165, 700)], fill=GOLD,
          outline=GOLD_DARK)
d.ellipse([140, 625, 175, 665], outline=GOLD, width=8)
d.ellipse([235, 625, 270, 665], outline=GOLD, width=8)
d.rectangle([196, 700, 214, 735], fill=GOLD_DARK)
d.rectangle([165, 735, 245, 760], fill=GOLD, outline=GOLD_DARK, width=2)

# --- robot behind the desk, centre ---------------------------------------
# antenna
d.line([540, 540, 540, 488], fill=ROBOT_DARK, width=8)
d.ellipse([522, 468, 558, 504], fill=COIN, outline=COIN_EDGE, width=3)
# body
d.rounded_rectangle([400, 540, 680, 800], radius=46, fill=ROBOT,
                    outline=ROBOT_DARK, width=5)
# ears
d.ellipse([382, 610, 410, 650], fill=ROBOT_DARK)
d.ellipse([670, 610, 698, 650], fill=ROBOT_DARK)
# eyes
d.ellipse([452, 600, 506, 654], fill=WHITE, outline=ROBOT_DARK, width=3)
d.ellipse([574, 600, 628, 654], fill=WHITE, outline=ROBOT_DARK, width=3)
d.ellipse([472, 620, 490, 638], fill=BLACK)
d.ellipse([594, 620, 612, 638], fill=BLACK)
# smile
d.arc([490, 660, 590, 730], start=15, end=165, fill=BLACK, width=6)
# chest panel with buttons
d.rounded_rectangle([480, 712, 600, 782], radius=10, fill=ROBOT_PANEL)
for i, col in enumerate(((255, 99, 99), (255, 210, 63), (74, 180, 92))):
    cx = 508 + i * 32
    d.ellipse([cx - 9, 738, cx + 9, 756], fill=col)

# --- laptop on the desk, right -------------------------------------------
d.polygon([(800, 770), (980, 770), (1000, 800), (780, 800)], fill=(52, 58, 72))
d.rounded_rectangle([805, 648, 975, 772], radius=10, fill=LAPTOP,
                    outline=(12, 14, 22), width=3)
d.rectangle([820, 662, 960, 758], fill=LAPTOP_SCREEN)
for i, col in enumerate(((96, 165, 250), (74, 180, 92), (255, 210, 63),
                         (244, 114, 182), (255, 255, 255))):
    y = 676 + i * 16
    d.line([832, y, 832 + 90 - i * 12, y], fill=col, width=6)

# --- bottom caption --------------------------------------------------------
text = "make.fun - build a tiny game, get paid"
f = font(44)
tw = d.textlength(text, font=f)
d.text(((W - tw) / 2, 985), text, font=f, fill=WHITE)

img.save(OUT, "PNG")
print(f"wrote {OUT} ({W}x{H})")
