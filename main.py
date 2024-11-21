# import texttoimage

# text = """I need a front door for my hall,
# The replacement I bought was too tall.
# So I hacked it and chopped it,
# And carefully lopped it,
# And now the dumb thing is too small."""


# def read_poem(filename):
#     with open(filename, "r") as file:
#         return file.read()


# texttoimage.convert(
#     read_poem("generated_poems_txt/short_example.txt"),
#     "test_unsplash_image.png",
# )

# import spacy

# nlp = spacy.load("en_core_web_sm")

# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# for token in doc:
#     print(token.text, token.pos_, token.dep_)

# import spacy

# nlp = spacy.load("en_core_web_md")  # make sure to use larger package!
# doc1 = nlp("I like salty fries and hamburgers.")
# doc2 = nlp("Fast food tastes very good.")

# # Similarity of two documents
# print(doc1, "<->", doc2, doc1.similarity(doc2))
