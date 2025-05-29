import requests


def fetch_spacex_images(count):

    url = "https://api.spacexdata.com/v4/launches"

    response = requests.get(url)
    response.raise_for_status()
    launches = response.json()
    images = []

    for launch in launches:
        if len(images) >= count:
            break
        if launch['links']['flickr']['original']:
            images.extend(launch['links']['flickr']['original'])

    return images[:count]
