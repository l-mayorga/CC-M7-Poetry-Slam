"""
Author: Leonard Mayorga

Using a dataset of poems from Kaggle, create n-grams and generate a poem.
Present the poem with a relevant background image and read it aloud.
"""

import modules.fork_texttoimage as texttoimage
from generate_ngrams import generate_poem
from unsplash import generate_bg_image
import os


def read_poem(filename):
    """Read a poem from a text file and return it as a string."""
    with open(filename, "r") as file:
        return file.read()


def write_poem_txt(title, lines):
    """Write a poem to a text file."""
    with open("generated_poems_txt/" + title + ".txt", "w") as file:
        for line in lines:
            file.write(line + "\n")


def write_poem_png(title):
    """Use a background image to create a PNG of a poem with the background."""
    poem = read_poem("generated_poems_txt/" + title + ".txt")
    bg_filename = "generated_poems_png/" + title + "_bg.png"
    texttoimage.convert(poem, bg_filename)


def main():
    """Generate a poem and perform it."""
    lines, significant_nouns = generate_poem()
    title = f"{significant_nouns[0]}_{significant_nouns[1]}"
    print(f"title: {title}")
    generate_bg_image(significant_nouns, title)
    write_poem_txt(title, lines)
    write_poem_png(title)

    os.system(f"bash perform_poem.sh {title} --move-bg")


main()
