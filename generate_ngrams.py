import string
import pandas as pd
import random
from collections import defaultdict


MIN_CHARACTERS = 1000


def import_and_clean_data():

    df = pd.read_csv("PoetryFoundationData.csv")

    # Drop index
    df = df.drop("Unnamed: 0", axis=1)

    # Drop poet
    df = df.drop("Poet", axis=1)

    # Drop rows with missing tags
    # df = df.dropna(subset=["Tags"])

    # Mitigate data sparsity for higher n-grams
    # df = df[df["Poem"].str.len() >= MIN_CHARACTERS]

    # Remove \r, \n and extra spacing from titles and poems
    df["Title"] = df["Title"].str.replace(r"[\r\n]", "", regex=True)
    df["Poem"] = df["Poem"].str.replace(r"[\r\n]", " ", regex=True)
    df["Poem"] = df["Poem"].str.replace(r"\s+", " ", regex=True)

    return df


def generate_ngrams(df, n=2):

    n_grams = defaultdict(list)

    for poem in df["Poem"]:

        poem = poem.translate(str.maketrans("", "", string.punctuation))
        poem = poem.lower().strip()

        words = poem.split(" ")

        for i in range(len(words) - n + 1):
            n_gram = tuple(words[i : i + n])
            # Map all but the last word to the last word
            n_grams[n_gram[:-1]].append(n_gram[-1])

    return n_grams


def generate_output_poem(n_grams, start, length=5):

    n_gram_len = len(list(n_grams.keys())[0])

    if len(start) < n_gram_len:
        raise ValueError(
            f"Start sequence must be at least {n_gram_len} words long"
        )
        return

    # Generate a poem from n_grams
    current_sequence = tuple(start[-n_gram_len:])
    generated_text = list(start)

    for _ in range(length - len(generated_text)):
        next_words = n_grams.get(current_sequence, [])
        # print(f"Next words for {current_sequence}: {next_words}")

        if not next_words:
            print(f"Sequence: {current_sequence} not found in n-grams")
            break

        next_word = random.choice(next_words)
        generated_text.append(next_word)

        # Shift forward one word
        current_sequence = current_sequence[1:] + (next_word,)

    return " ".join(generated_text)


df = import_and_clean_data()
print(df.size)

# shorted_df = df.iloc[:10000]

# shorted_df["Poem"] = shorted_df["Poem"].str[:100]

n_grams = generate_ngrams(df, 4)

print(generate_output_poem(n_grams, ["a", "tree", "and"], 100))
