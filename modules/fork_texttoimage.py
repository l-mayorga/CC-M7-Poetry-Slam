"""
Author: zhiwehu, github.com/zhiwehu/texttoimage
Contributor: Leonard Mayorga

This module is a fork of the texttoimage module found on GitHub. My changes
add a background box to the text to make it more readable, and use an write on
an existing png instead of creating a new one. The rest of the code is
unmodified.
"""

from fonts.ttf import Roboto
from PIL import Image, ImageFont, ImageDraw
import random


# Color palette from coolors.co
BG_COLORS = [
    (254, 197, 187),
    (252, 213, 206),
    (250, 225, 221),
    (248, 237, 235),
    (232, 232, 228),
    (254, 200, 154),
    (255, 215, 186),
    (255, 229, 217),
    (236, 228, 219),
    (216, 226, 220),
]


def convert(
    text,
    bg_image_file,
    font_size=24,
    color="Black",
    font_name=None,
    box_padding=10,
):
    if font_name is None:
        font_name = Roboto
    font = ImageFont.truetype(font_name, font_size, encoding="utf-8")

    if bg_image_file:
        image = Image.open(bg_image_file)
    else:
        raise ValueError("An valid bg image file must be provided.")

    draw = ImageDraw.Draw(image)

    # Get size of the text to adjust its position
    w, h = draw.textsize(text, font=font)

    x = (image.width - w) / 2  # Center the text horizontally
    y = (image.height - h) / 2  # Center the text vertically

    box_x0 = x - box_padding  # Left padding
    box_y0 = y - box_padding  # Top padding
    box_x1 = x + w + box_padding  # Right padding
    box_y1 = y + h + box_padding  # Bottom padding

    # Draw bg box
    draw.rectangle(
        [box_x0, box_y0, box_x1, box_y1], fill=random.choice(BG_COLORS)
    )

    # Draw the text
    draw.text((x, y), text, fill=color, font=font)

    image.save(bg_image_file.replace("_bg.png", ".png"), "PNG")
