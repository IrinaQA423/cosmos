import requests

from datetime import datetime, timedelta


def fetch_nasa_apod_images(api_key, count):
    url = "https://api.nasa.gov/planetary/apod"
    images = []
    current_date = datetime.now()-timedelta(days=1)

    while len(images) < count:
        date_str = current_date.strftime('%Y-%m-%d')
        params = {
            'api_key': api_key,
            'date': date_str
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get('media_type') == 'image':
                images.append(data['url'])
        except requests.exceptions.HTTPError as e:
            print(f"Ошибка при запросе {date_str}: {e}")

        current_date -= timedelta(days=1)

    return images[:count]
