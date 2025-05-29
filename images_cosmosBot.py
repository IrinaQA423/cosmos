import requests
from telegram import Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
import os


load_dotenv()
tg_token = os.getenv('TG_TOKEN')
channel_id = os.getenv('CHANNEL_ID')
message = 'Привет, мир!'

bot = Bot(token=tg_token)

bot.send_message(chat_id=channel_id, text=message)
        

#bot = Bot(tg_token)
#info = bot.get_me()
#filtered_info = {
    #"id": info.id,
    #"first_name": info.first_name,
    #"is_bot": info.is_bot,
    #"username": info.username
#}
#print(filtered_info)
