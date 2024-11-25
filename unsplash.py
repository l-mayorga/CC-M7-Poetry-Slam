"""
Author: Leonard Mayorga

This module sources a background image for the poem based on two queries. If no
image is found for either query, a default image of a banana is used. The use of
this module requires an API key from Unsplash.
"""

import requests
import os

# Insert your Unsplash API key here
API_KEY = os.getenv("UNSPLASH_API_KEY")


def generate_bg_image(queries, title):
    """
    Sources a background image for the poem based on two queries. If no image
    is found, use an image of a banana. The image is saved in the
    generated_bgs_png directory.

    """
    url = "https://api.unsplash.com/photos/random"
    headers = {"Authorization": f"Client-ID {API_KEY}"}

    for query in queries:
        params = {"query": query, "orientation": "landscape"}

        response = requests.get(url, headers=headers, params=params)

        try:
            response.raise_for_status()  # If error, raise exception
            print(f"Image found for {query}")
            break
        except requests.exceptions.HTTPError as e:
            response = None
            continue

    if not response:
        params = {"query": "banana", "orientation": "landscape"}
        print("\nNo image found for queries, using default banana\n")
        response = requests.get(url, headers=headers, params=params)

    image_url = response.json()["urls"]["regular"]
    image_response = requests.get(image_url)
    image_response.raise_for_status()

    filename = "generated_poems_png/" + title + "_bg.png"
    with open(filename, "wb") as file:
        file.write(image_response.content)
