import asyncio
import sys
import time
import logging
import os
from pathlib import Path
import schedule

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

from bot_utils.profile_settings import set_up_profile
from bot_utils.user_profile import (start_profile, name, gender,
                                    wrong_answer, greet_user)

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = "5304608341:AAGF6us_q8qso_KDV_QxIqsrblQdfBPOQUw"
my_bot = Updater(API_TOKEN, use_context=True)
dp = my_bot.dispatcher

# def test():
#     logging.info('ВТЕСТЕ')
    # update.message.reply_text('Тест пройден',
    #                               reply_markup=ReplyKeyboardMarkup([['/test']]))
    # time.sleep(5)
    # test=PeriodicTask.objects.create(
    #     name="TESTTASK",
    #     task='repeat_test',
    #     interval=IntervalSchedule.objects.get(every=10, period='seconds'),
    #     args=json.dumps([update.__dict__]),
    #     start_time=timezone.now(),
    # )



def get_user_data(update):#Можно ли уже это убрать?????????????????
    print(dir(update.message.from_user))
    user_data = {}
    user_data['full_name'] = update.message.chat.full_name
    user_data['first_name'] = update.message.chat.first_name
    user_data['last_name'] = update.message.chat.last_name
    user_data['username'] = update.message.chat.username
    user_data['user_id'] = update.message.chat.id
    return user_data


def main():
    # my_bot = Updater(API_TOKEN, use_context=True)
    # dp = my_bot.dispatcher

    user_profile = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Познакомиться)$'),
                           start_profile)
        ],
        states={
            'name': [MessageHandler(Filters.text, name)],
            'gender': [MessageHandler(Filters.regex('^(Мужской|Женский)$'),
                       gender)],
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.photo | Filters.video |
                           Filters.document | Filters.location, wrong_answer)
        ]
    )
    creating_settings = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Настроить)$'), set_up_profile)
        ],
        states={},
        fallbacks=[]
    )


    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(creating_settings)
    dp.add_handler(user_profile)

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

