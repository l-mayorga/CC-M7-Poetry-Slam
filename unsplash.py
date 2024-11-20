import requests
import os

# Store API key in environment
API_KEY = os.getenv("UNSPLASH_API_KEY")


def get_image_from_unsplash(query, filename):
    url = "https://api.unsplash.com/photos/random"
    headers = {"Authorization": f"Client-ID {API_KEY}"}
    params = {"query": query, "orientation": "landscape"}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # If error, raise exception

    image_url = response.json()["urls"]["regular"]
    image_response = requests.get(image_url)
    image_response.raise_for_status()

    with open(filename, "wb") as file:
        file.write(image_response.content)


if __name__ == "__main__":
    query = "pie"
    filename = "test_unsplash_image.png"
    get_image_from_unsplash(query, filename)
