import requests
from common_utils import download_images_batch, load_env
import os


def fetch_nasa_apod_photos():
    api_key = os.getenv("NASA_API_KEY")

    api_url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "count": 30}

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Ошибка при получении данных NASA APOD: {e}")
        return

    photo_urls = []
    if isinstance(data, list):
        for item in data:
            url = item.get("url")
            if url:
                photo_urls.append(url)
    else:
        url = data.get("url")
        if url:
            photo_urls.append(url)

    if photo_urls:
        download_images_batch(photo_urls, "nasa_images", "nasa")


if __name__ == "__main__":
    load_env()
    fetch_nasa_apod_photos()
