import sys
from email.message import Message
from importlib.metadata import entry_points
import json
import logging
import os
from pathlib import Path

from telegram import ReplyKeyboardMarkup
from celery import shared_task
import django

# Загружаем настройки Джанго
sys.path.append(str(Path(__file__).resolve().parent))
os.environ['DJANGO_SETTINGS_MODULE'] = 'telega.settings'
django.setup()

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from bot_utils.profile_settings import set_up_profile, course_name, which_dates
from bot_utils.user_profile import start_profile, name, gender, greet_user

from bot_utils.utils import wrong_answer

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = os.environ.get('API_TOKEN')
my_bot = Updater(API_TOKEN, use_context=True)
dp = my_bot.dispatcher


def test(update, context):
    update.message.reply_text('Тест пройден',
                              reply_markup=ReplyKeyboardMarkup([['/test']]))


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
        states={
            'course_name': [MessageHandler(Filters.text, course_name)],
            'which_dates': [MessageHandler(
                Filters.regex('^\d{2}\.\d{2}\.\d{4} \d{2}\.\d{2}\.\d{4}$'),
                which_dates)]
            },
        fallbacks=[MessageHandler(Filters.text | Filters.photo | Filters.video |
                           Filters.document | Filters.location, wrong_answer)]
    )
    dp.add_handler(CommandHandler('test', test))
    dp.add_handler(creating_settings)
    dp.add_handler(user_profile)

    dp.add_handler(CommandHandler('start', greet_user))

    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
