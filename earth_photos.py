import requests

from datetime import datetime

from images_utils import download_image


def download_earth_photos(api_key, num_photos, save_dir='images'):
    earth_url = "https://api.nasa.gov/EPIC/api/natural"
    params = {'api_key': api_key}

    response = requests.get(earth_url, params=params)
    response.raise_for_status()
    nasa_earth_photos = response.json()

    for i, image_info in enumerate(images_info[:num_photos]):

        image_date = datetime.strptime(image_info['date'], "%Y-%m-%d %H:%M:%S")
        date_str = image_date.strftime("%Y/%m/%d")
        image_filename = image_info['image']
        photo_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date_str}/png/{image_filename}.png"
        download_image(photo_url, f'earth_photo_{i + 1}', save_dir)
