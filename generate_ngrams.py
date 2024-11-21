import pandas as pd
from collections import defaultdict


MIN_CHARACTERS = 1000


def import_and_clean_data():

    df = pd.read_csv("PoetryFoundationData.csv")

    # Drop index
    df = df.drop("Unnamed: 0", axis=1)

    # Drop poet
    df = df.drop("Poet", axis=1)

    # Drop rows with missing tags
    df = df.dropna(subset=["Tags"])

    # Mitigate data sparsity for higher n-grams
    df = df[df["Poem"].str.len() >= MIN_CHARACTERS]

    # Remove \r, \n and extra spacing from titles and poems
    df["Title"] = df["Title"].str.replace(r"[\r\n]", "", regex=True)
    df["Poem"] = df["Poem"].str.replace(r"[\r\n]", " ", regex=True)
    df["Poem"] = df["Poem"].str.replace(r"\s+", " ", regex=True)

    return df


import_and_clean_data()
