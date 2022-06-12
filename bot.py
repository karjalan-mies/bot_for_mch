import asyncio
import sys
import time
import logging
import os
from pathlib import Path

from telegram import ReplyKeyboardMarkup

import django

# Загружаем настройки Джанго
sys.path.append(str(Path(__file__).resolve().parent))
os.environ['DJANGO_SETTINGS_MODULE'] = 'telega.settings'
django.setup()

from asgiref.sync import sync_to_async
from api.models import UserTelegram

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from bot_utils.handlers import user_profile, creating_settings, smart, planning
from bot_utils.user_profile import greet_user

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = os.environ.get('API_TOKEN')
# my_bot = Updater(API_TOKEN, use_context=True)
# dp = my_bot.dispatcher


def test(update,env):
#     logging.info('ВТЕСТЕ')
    update.message.reply_text('Тест пройден',
                              reply_markup=ReplyKeyboardMarkup([['/test']]))
    # time.sleep(5)
    # test=PeriodicTask.objects.create(
    #     name="TESTTASK",
    #     task='repeat_test',
    #     interval=IntervalSchedule.objects.get(every=10, period='seconds'),
    #     args=json.dumps([update.__dict__]),
    #     start_time=timezone.now(),
    # )


def main():
    my_bot = Updater(API_TOKEN, use_context=True)
    dp = my_bot.dispatcher

    #dp.add_handler(CommandHandler('test', test))
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
#         logging.info('ВТЕСТЕ')
#         await asyncio.sleep(1)
#         print('... World!')

# asyncio.run(test())


if __name__ == "__main__":
    main()
