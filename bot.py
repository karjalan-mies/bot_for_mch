import asyncio
import sys
import time
import logging
import os
from pathlib import Path
import json

import django

# Загружаем настройки Джанго
sys.path.append(str(Path(__file__).resolve().parent))
os.environ['DJANGO_SETTINGS_MODULE'] = 'telega.settings'
django.setup()

from asgiref.sync import sync_to_async

from telegram.ext import CommandHandler, Updater

from bot_utils.handlers import user_profile, creating_settings, smart, planning
from bot_utils.user_profile import greet_user

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = os.environ.get('API_TOKEN')


def main():
    my_bot = Updater(API_TOKEN, use_context=True)
    dp = my_bot.dispatcher
    dp.add_handler(creating_settings)
    dp.add_handler(user_profile)
    dp.add_handler(smart)
    dp.add_handler(planning)

    dp.add_handler(CommandHandler('start', greet_user))
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
