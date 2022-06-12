import asyncio
import sys
import time
import logging
import os
from pathlib import Path
import json
from telegram import ReplyKeyboardMarkup

import django

# Загружаем настройки Джанго
sys.path.append(str(Path(__file__).resolve().parent))
os.environ['DJANGO_SETTINGS_MODULE'] = 'telega.settings'
django.setup()
from api.models import MessageText
from asgiref.sync import sync_to_async
from api.models import UserTelegram

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from bot_utils.handlers import user_profile, creating_settings, smart, planning
from bot_utils.user_profile import greet_user

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = os.environ.get('API_TOKEN')

def test(update,env):
    pass
    # with open('file.json') as file:
    #     data = json.load(file).get("res")
    #     for mess in data:
    #         m=MessageText()
    #         m.title=mess.get("title")
    #         m.man_text=mess.get("man") if mess.get("man") else None
    #         m.woman_text=mess.get("woman") if mess.get("woman") else None
    #         m.common_text = mess.get("common") if mess.get("common") else None
    #         m.save()

    # with open("DB.txt") as DB:
    #     while True:
    #         line = DB.readline().split(" ")
    #         if not line[0]:
    #             break
    # update.message.reply_text('Тест пройден',
    #                           reply_markup=ReplyKeyboardMarkup([['/test']]))


def main():
    my_bot = Updater(API_TOKEN, use_context=True)
    dp = my_bot.dispatcher

    #dp.add_handler(CommandHandler('test', test))
    dp.add_handler(creating_settings)
    dp.add_handler(user_profile)
    dp.add_handler(smart)
    dp.add_handler(planning)

    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('test', test))
    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()

# async def test():
#     @sync_to_async
#     def get_all_users():
#         return list(UserTelegram.objects.all())
#
#     while True:
#         users=await get_all_users()
#         print(users)
#         await asyncio.sleep(1)

# asyncio.run(test())


if __name__ == "__main__":
    main()
