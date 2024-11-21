from fonts.ttf import Roboto
from PIL import Image, ImageFont, ImageDraw
import random


RGB_TO_COLOR_NAMES = {
    (0, 0, 0): ["Black"],
    (0, 0, 128): ["Navy", "NavyBlue"],
    (0, 0, 139): ["DarkBlue"],
    (0, 0, 205): ["MediumBlue"],
    (0, 0, 255): ["Blue"],
    (0, 100, 0): ["DarkGreen"],
    (0, 128, 0): ["Green"],
    (0, 139, 139): ["DarkCyan"],
    (0, 191, 255): ["DeepSkyBlue"],
    (0, 206, 209): ["DarkTurquoise"],
    (0, 250, 154): ["MediumSpringGreen"],
    (0, 255, 0): ["Lime"],
    (0, 255, 127): ["SpringGreen"],
    (0, 255, 255): ["Cyan", "Aqua"],
    (25, 25, 112): ["MidnightBlue"],
    (30, 144, 255): ["DodgerBlue"],
    (32, 178, 170): ["LightSeaGreen"],
    (34, 139, 34): ["ForestGreen"],
    (46, 139, 87): ["SeaGreen"],
    (47, 79, 79): ["DarkSlateGray", "DarkSlateGrey"],
    (50, 205, 50): ["LimeGreen"],
    (60, 179, 113): ["MediumSeaGreen"],
    (64, 224, 208): ["Turquoise"],
    (65, 105, 225): ["RoyalBlue"],
    (70, 130, 180): ["SteelBlue"],
    (72, 61, 139): ["DarkSlateBlue"],
    (72, 209, 204): ["MediumTurquoise"],
    (75, 0, 130): ["Indigo"],
    (85, 107, 47): ["DarkOliveGreen"],
    (95, 158, 160): ["CadetBlue"],
    (100, 149, 237): ["CornflowerBlue"],
    (102, 205, 170): ["MediumAquamarine"],
    (105, 105, 105): ["DimGray", "DimGrey"],
    (106, 90, 205): ["SlateBlue"],
    (107, 142, 35): ["OliveDrab"],
    (112, 128, 144): ["SlateGray", "SlateGrey"],
    (119, 136, 153): ["LightSlateGray", "LightSlateGrey"],
    (123, 104, 238): ["MediumSlateBlue"],
    (124, 252, 0): ["LawnGreen"],
    (127, 255, 0): ["Chartreuse"],
    (127, 255, 212): ["Aquamarine"],
    (128, 0, 0): ["Maroon"],
    (128, 0, 128): ["Purple"],
    (128, 128, 0): ["Olive"],
    (128, 128, 128): ["Gray", "Grey"],
    (132, 112, 255): ["LightSlateBlue"],
    (135, 206, 235): ["SkyBlue"],
    (135, 206, 250): ["LightSkyBlue"],
    (138, 43, 226): ["BlueViolet"],
    (139, 0, 0): ["DarkRed"],
    (139, 0, 139): ["DarkMagenta"],
    (139, 69, 19): ["SaddleBrown"],
    (143, 188, 143): ["DarkSeaGreen"],
    (144, 238, 144): ["LightGreen"],
    (147, 112, 219): ["MediumPurple"],
    (148, 0, 211): ["DarkViolet"],
    (152, 251, 152): ["PaleGreen"],
    (153, 50, 204): ["DarkOrchid"],
    (154, 205, 50): ["YellowGreen"],
    (160, 82, 45): ["Sienna"],
    (165, 42, 42): ["Brown"],
    (169, 169, 169): ["DarkGray", "DarkGrey"],
    (173, 216, 230): ["LightBlue"],
    (173, 255, 47): ["GreenYellow"],
    (175, 238, 238): ["PaleTurquoise"],
    (176, 196, 222): ["LightSteelBlue"],
    (176, 224, 230): ["PowderBlue"],
    (178, 34, 34): ["Firebrick"],
    (184, 134, 11): ["DarkGoldenrod"],
    (186, 85, 211): ["MediumOrchid"],
    (188, 143, 143): ["RosyBrown"],
    (189, 183, 107): ["DarkKhaki"],
    (192, 192, 192): ["Silver"],
    (199, 21, 133): ["MediumVioletRed"],
    (205, 92, 92): ["IndianRed"],
    (205, 133, 63): ["Peru"],
    (208, 32, 144): ["VioletRed"],
    (210, 105, 30): ["Chocolate"],
    (210, 180, 140): ["Tan"],
    (211, 211, 211): ["LightGray", "LightGrey"],
    (216, 191, 216): ["Thistle"],
    (218, 112, 214): ["Orchid"],
    (218, 165, 32): ["Goldenrod"],
    (219, 112, 147): ["PaleVioletRed"],
    (220, 20, 60): ["Crimson"],
    (220, 220, 220): ["Gainsboro"],
    (221, 160, 221): ["Plum"],
    (222, 184, 135): ["Burlywood"],
    (224, 255, 255): ["LightCyan"],
    (230, 230, 250): ["Lavender"],
    (233, 150, 122): ["DarkSalmon"],
    (238, 130, 238): ["Violet"],
    (238, 221, 130): ["LightGoldenrod"],
    (238, 232, 170): ["PaleGoldenrod"],
    (240, 128, 128): ["LightCoral"],
    (240, 230, 140): ["Khaki"],
    (240, 248, 255): ["AliceBlue"],
    (240, 255, 240): ["Honeydew"],
    (240, 255, 255): ["Azure"],
    (244, 164, 96): ["SandyBrown"],
    (245, 222, 179): ["Wheat"],
    (245, 245, 220): ["Beige"],
    (245, 245, 245): ["WhiteSmoke"],
    (245, 255, 250): ["MintCream"],
    (248, 248, 255): ["GhostWhite"],
    (250, 128, 114): ["Salmon"],
    (250, 235, 215): ["AntiqueWhite"],
    (250, 240, 230): ["Linen"],
    (250, 250, 210): ["LightGoldenrodYellow"],
    (253, 245, 230): ["OldLace"],
    (255, 0, 0): ["Red"],
    (255, 0, 255): ["Magenta", "Fuchsia"],
    (255, 20, 147): ["DeepPink"],
    (255, 69, 0): ["OrangeRed"],
    (255, 99, 71): ["Tomato"],
    (255, 105, 180): ["HotPink"],
    (255, 127, 80): ["Coral"],
    (255, 140, 0): ["DarkOrange"],
    (255, 160, 122): ["LightSalmon"],
    (255, 165, 0): ["Orange"],
    (255, 182, 193): ["LightPink"],
    (255, 192, 203): ["Pink"],
    (255, 215, 0): ["Gold"],
    (255, 218, 185): ["PeachPuff"],
    (255, 222, 173): ["NavajoWhite"],
    (255, 228, 181): ["Moccasin"],
    (255, 228, 196): ["Bisque"],
    (255, 228, 225): ["MistyRose"],
    (255, 235, 205): ["BlanchedAlmond"],
    (255, 239, 213): ["PapayaWhip"],
    (255, 240, 245): ["LavenderBlush"],
    (255, 245, 238): ["Seashell"],
    (255, 248, 220): ["Cornsilk"],
    (255, 250, 205): ["LemonChiffon"],
    (255, 250, 240): ["FloralWhite"],
    (255, 250, 250): ["Snow"],
    (255, 255, 0): ["Yellow"],
    (255, 255, 224): ["LightYellow"],
    (255, 255, 240): ["Ivory"],
    (255, 255, 255): ["White"],
}

COLOR_NAME_TO_RGB = dict(
    (name.lower(), rgb)
    for rgb, names in RGB_TO_COLOR_NAMES.items()
    for name in names
)

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
    image_file,
    font_size=24,
    color="Black",
    font_name=None,
    bg_color=None,
    box_padding=10,
):
    if font_name is None:
        font_name = Roboto
    font = ImageFont.truetype(font_name, font_size, encoding="utf-8")

    # Open the existing image
    print(image_file)
    if image_file:
        image = Image.open(image_file)
    else:
        raise ValueError("An valid bg image file must be provided.")

    # image = image.convert('RGBA')

    # blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))

    draw = ImageDraw.Draw(image)

    # Check if color is valid
    if bg_color not in COLOR_NAME_TO_RGB.keys():
        bg_color = random.choice(BG_COLORS)

    # Get size of the text to adjust its position
    w, h = draw.textsize(text, font=font)

    # You can modify this to choose where to position the text on the image
    x = (image.width - w) / 2  # Center the text horizontally
    y = (image.height - h) / 2  # Center the text vertically

    # Draw a rectangle (background box) behind the text to make it more readable
    # Adding padding around the text for better readability
    box_x0 = x - box_padding  # Left padding
    box_y0 = y - box_padding  # Top padding
    box_x1 = x + w + box_padding  # Right padding
    box_y1 = y + h + box_padding  # Bottom padding

    # Draw the background box with the given background color (can be opaque)
    draw.rectangle([box_x0, box_y0, box_x1, box_y1], fill=bg_color)

    # Draw the text on the existing image
    draw.text((x, y), text, fill=color, font=font)

    # filename = "generated_poems_png/" + image_file.replace("_bg", "")
    # Save the image with the text added
    image.save(image_file.replace("_bg.png", ".png"), "PNG")
