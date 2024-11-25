"""
Author: Leonard Mayorga

Using a dataset of poems from Kaggle, generate n-grams based on word
frequencies. Also generate a poem based on the n-grams and evaluate the poem
based on internal similarity. Finally, format the poem into lines and extract
important nouns based on frequency.
"""

import pandas as pd
import spacy
import random
from collections import defaultdict
from collections import Counter

nlp = spacy.load("en_core_web_md")


def import_and_clean_data():
    """
    Import the poetry dataset and clean it by removing unnecessary columns.
    Return the cleaned dataset.
    """
    df = pd.read_csv("PoetryFoundationData.csv")

    df = df.drop("Unnamed: 0", axis=1)
    df = df.drop("Poet", axis=1)

    # Remove spacing from titles and poems
    df["Title"] = df["Title"].str.replace(r"[\r\n]", "", regex=True)
    df["Poem"] = df["Poem"].str.replace(r"[\r\n]", " ", regex=True)
    df["Poem"] = df["Poem"].str.replace(r"\s+", " ", regex=True)

    return df


def generate_ngrams(df, n=2):
    """
    Generate n-grams from a dataset of poems and return it.
    """

    print(f"Using {df.shape[0]} poems to generate {n}-grams")
    n_grams = defaultdict(list)

    for poem in df["Poem"]:
        poem = poem.lower().strip()

        words = poem.split(" ")

        for i in range(len(words) - n + 1):
            n_gram = tuple(words[i : i + n])
            # Map all but the last word to the last word
            n_grams[n_gram[:-1]].append(n_gram[-1])

    return n_grams


def generate_output_poem(n_grams, start, length=5, special_word=None):
    """
    Generate a poem based on n-grams and a starting sequence of words. If a
    special word is specified, it will be included if found at all in the
    n-grams.
    """
    n_gram_len = len(list(n_grams.keys())[0])

    if len(start) < n_gram_len:
        raise ValueError(
            f"Start sequence must be at least {n_gram_len} words long"
        )

    # Generate a poem from n_grams
    current_sequence = tuple(start[-n_gram_len:])
    generated_text = list(start)

    for _ in range(length - len(generated_text)):
        next_words = n_grams.get(current_sequence, [])

        if not next_words:  # No next words
            return None

        if special_word and special_word in next_words:
            next_word = special_word
            print("\nSpecial word found!\n")
            special_word = None  # Only use special word once

        else:
            next_word = random.choice(next_words)

        generated_text.append(next_word)

        # Shift forward one word
        current_sequence = current_sequence[1:] + (next_word,)

    return " ".join(generated_text), special_word


def split_into_sentences_and_trim(poem):
    """
    Use spaCy to split poem into sentences and cut malformed sentences.
    """
    if not poem:
        return None
    poem_doc = nlp(poem)
    # Remove last sentence (likely incomplete)
    sentences = list(poem_doc.sents)[:-1]

    # Remove sentences with only one word
    sentences = [
        sentence for sentence in sentences if len(sentence.text.split(" ")) > 1
    ]
    return sentences


def evaluate_internal_similarity(poem_sentences):
    """Compare each sentence in a poem to every other sentence and return the
    average similarity.
    """
    if not poem_sentences:
        return 0

    scores = []

    for i in range(len(poem_sentences)):
        for j in range(i + 1, len(poem_sentences)):
            scores.append(poem_sentences[i].similarity(poem_sentences[j]))

    avg_scores = sum(scores) / len(scores) if scores else 0

    return avg_scores


def format_poem(poem_sentences, max_len=45):
    """Split a poem into lines based on length and capitalize the first word of
    each sentence.
    """
    lines = []
    current_line = ""

    for sentence in poem_sentences:
        words = sentence.text.capitalize().split(" ")
        for word in words:
            if len(current_line) + len(word) < max_len:
                current_line += word + " "
            else:  # Start a new line
                lines.append(current_line[:-1])
                current_line = word + " "

    if current_line:
        lines.append(current_line[:-1])

    return lines


def find_significant_nouns(poem_sentences):
    """Find the two most common nouns in a poem. Used for title and bg image."""
    nouns = []
    for sentence in poem_sentences:
        for token in sentence:
            if token.pos_ == "NOUN":
                nouns.append(token.text)

    noun_counts = Counter(nouns)
    sorted_nouns = sorted(
        noun_counts.items(), key=lambda x: x[1], reverse=True
    )
    return [noun for noun, _ in sorted_nouns[:2]]


def generate_poem(min_similarity=0.95):
    """
    Generate a poem surpassing an internal similarity threshold and couple with
    the two most frequent nouns.
    """
    df = import_and_clean_data()
    n_grams = generate_ngrams(df, 4)

    curr_similarity = 0
    while curr_similarity < min_similarity:
        generated_poem = generate_output_poem(
            n_grams, ["i", "am", "like"], 100
        )
        if not generated_poem:  # No next n-gram
            continue

        generated_poem = generated_poem[0]
        split = split_into_sentences_and_trim(generated_poem)
        curr_similarity = evaluate_internal_similarity(split)
    print(f"Intra poem similarity: {curr_similarity}")

    lines = format_poem(split)
    significant_nouns = find_significant_nouns(split)

    return lines, significant_nouns
