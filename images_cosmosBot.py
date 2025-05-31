import os
import random
import time

from dotenv import load_dotenv
from telegram import Bot, InputFile
from telegram.error import BadRequest


def load_config():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    tg_channel_id = os.getenv('TG_CHANNEL_ID')
    return tg_token, tg_channel_id


def get_image_files(folder):
    return [f for f in os.listdir(folder)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

def handle_errors(image_path, error):
    if isinstance(error, BadRequest):
        print(f"Произошла ошибка при публикации изображения {image_path}: {error}")
    

def publish_image(bot, tg_channel_id, image_path):
    try:
        with open(image_path, 'rb') as photo_file:
            bot.send_photo(
                chat_id=tg_channel_id,
                photo=InputFile(photo_file),
                caption=f"{os.path.basename(image_path)}"
            )
    
    except BadRequest as e:
        handle_errors(image_path, e)
    

def send_images(bot, tg_channel_id, images, image_folder, delay=14400):
    for image in images:
        image_path = os.path.join(image_folder, image)
        publish_image(bot, tg_channel_id, image_path)
        time.sleep(delay)
    

def main():
    tg_token, tg_channel_id = load_config()
    bot = Bot(token=tg_token)
    image_folder = "./images"
        
    images = get_image_files(image_folder)
    if not images:
        print("Нет изображений для публикации.")
        return

    send_images(bot, tg_channel_id, images.copy(), image_folder)
                
    while True:
        try:
            random.shuffle(images)
            send_images(bot, tg_channel_id, images.copy(), image_folder)

        except KeyboardInterrupt:
            print("Публикация остановлена пользователем")
            break
    

if __name__ == "__main__":
    main()
