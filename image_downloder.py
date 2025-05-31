from dotenv import load_dotenv

import os
import argparse

from spacex_images import fetch_spacex_images
from nasa_apod import fetch_nasa_apod_images
from earth_photos import download_earth_photos
from images_utils import download_image


def setup_argparse():
    parser = argparse.ArgumentParser(description='Загружайте космические снимки из разных источников')
    parser.add_argument('--spacex', action='store_true', help='Загрузить фотографии запуска SpaceX')
    parser.add_argument('--apod', action='store_true', help='Загрузить фотографии NASA APOD')
    parser.add_argument('--earth', action='store_true', help='Загрузить фотографии Земли из NASA EPIC')
    parser.add_argument('--all', action='store_true', help='Скачать из всех источников')
    parser.add_argument('--count', type=int, default=1, help='Количество изображений для загрузки (по умолчанию: 1)')
    return parser.parse_args()


def main():

    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    args = setup_argparse()

    if not any([args.spacex, args.apod, args.earth, args.all]):
        print("Пожалуйста, укажите хотя бы один источник для загрузки")
        return

    if args.all or args.spacex:
        print("Загрузка изображений SpaceX.")
        spacex_images = fetch_spacex_images(count=args.count)
        for index, image_url in enumerate(spacex_images[:args.count], start=1):
            filename = f'spacex_{index}'
            download_image(image_url, filename)

    if args.all or args.apod:
        print("Загрузка изображений NASA APOD")
        apod_images = fetch_nasa_apod_images(api_key, count=args.count)
        for index, image_url in enumerate(apod_images, start=1):
            filename = f'nasa_apod_{index}'
            download_image(image_url, filename)

    if args.all or args.earth:
        print("Загрузка фотографий Земли.")
        download_earth_photos(api_key, num_photos=args.count)


if __name__ == "__main__":
    main()
