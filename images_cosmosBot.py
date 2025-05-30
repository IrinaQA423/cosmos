import os
import random
import time

from dotenv import load_dotenv
from telegram import Bot, InputFile

def load_config()
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    channel_id = os.getenv('CHANNEL_ID')
    return tg_token, channel_id


def get_image_files(folder):
    return [f for f in os.listdir(folder)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]


def publish_image(bot, channel_id, image_path):
    try:
        with open(image_path, 'rb') as photo_file:
            bot.send_photo(
                chat_id=channel_id,
                photo=InputFile(photo_file),
                caption=f"{os.path.basename(image_path)}"
            )
    except FileNotFoundError:
        print(f"Файл не найден: {image_path}")
    except Exception as e:
        print(f"Произошла ошибка при публикации изображения {image_path}: {e}")


def main():
    try:
    	bot = Bot(token=tg_token)
        image_folder = "C:/python_scripts/cosmos/images"
        tg_token, channel_id = load_config()

        images = get_image_files(image_folder)
        if not images:
            print("Нет изображений для публикации.")
            return

        for image in images.copy():
            publish_image(os.path.join(image_folder, image))
            time.sleep(4 * 60 * 60)

        while True:
            try:
                random.shuffle(images)
                for image in images:
                    publish_image(os.path.join(image_folder, image))
                    time.sleep(4 * 60 * 60)

            except KeyboardInterrupt:
                print("Публикация остановлена пользователем")
                break

    except Exception as e:
        print(f"Ошибка в основном цикле: {e}")


if __name__ == "__main__":
    main()
