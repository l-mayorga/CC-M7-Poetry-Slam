import texttoimage

text = """I need a front door for my hall,
The replacement I bought was too tall.
So I hacked it and chopped it,
And carefully lopped it,
And now the dumb thing is too small."""


def read_poem(filename):
    with open(filename, "r") as file:
        return file.read()


texttoimage.convert(
    read_poem("generated_poems/short_example.txt"), "test_unsplash_image.png"
)
