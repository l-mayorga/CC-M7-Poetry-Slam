import requests
import os

# Store API key in environment
API_KEY = os.getenv("UNSPLASH_API_KEY")


def generate_bg_image(queries, title):
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
        params = {"query": "dog", "orientation": "landscape"}
        print("\nNo image found for queries, using default dog\n")
        response = requests.get(url, headers=headers, params=params)

    image_url = response.json()["urls"]["regular"]
    image_response = requests.get(image_url)
    image_response.raise_for_status()

    filename = "generated_poems_png/" + title + "_bg.png"
    with open(filename, "wb") as file:
        file.write(image_response.content)


if __name__ == "__main__":
    queries = ["piano", "boat"]
    filename = "test_unsplash_image.png"
    generate_bg_image(queries, filename)
