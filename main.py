import modules.fork_texttoimage as fork_texttoimage
from generate_ngrams import generate_poem
from unsplash import generate_bg_image
import os


def read_poem(filename):
    with open(filename, "r") as file:
        return file.read()


def write_poem_txt(title, lines):
    with open("generated_poems_txt/" + title + ".txt", "w") as file:
        for line in lines:
            file.write(line + "\n")


def write_poem_png(title):
    poem = read_poem("generated_poems_txt/" + title + ".txt")
    bg_filename = "generated_poems_png/" + title + "_bg.png"
    fork_texttoimage.convert(poem, bg_filename)


def main():
    lines, significant_nouns = generate_poem()
    title = f"{significant_nouns[0]}_{significant_nouns[1]}"
    print(f"title: {title}")
    generate_bg_image(significant_nouns, title)
    write_poem_txt(title, lines)
    write_poem_png(title)

    os.system(f"bash perform_poem.sh {title} --move-bg")


main()
