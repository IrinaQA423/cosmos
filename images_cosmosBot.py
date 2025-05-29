import requests
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os


load_dotenv()
tg_token = os.getenv('TG_TOKEN')
channel_id = os.getenv('CHANNEL_ID')
message = 'Привет, мир!'

url = f'https://api.telegram.org/bot{tg_token}/sendMessage'
payload = {
    'chat_id': channel_id,
    'text': message
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print('Сообщение отправлено успешно!')
else:
    print('Ошибка при отправке сообщения:', response.text)

#bot = Bot(tg_token)
#info = bot.get_me()
#filtered_info = {
    #"id": info.id,
    #"first_name": info.first_name,
    #"is_bot": info.is_bot,
    #"username": info.username
#}
#print(filtered_info)
#update.message.reply_text("I'm sorry Dave I'm afraid I can't do that.")