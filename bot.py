import asyncio
import sys
import logging
import os
from pathlib import Path
import json

import django

# Загружаем настройки Джанго
sys.path.append(str(Path(__file__).resolve().parent))
os.environ['DJANGO_SETTINGS_MODULE'] = 'telega.settings'
django.setup()

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater,messagequeue)

from bot_utils.handlers import user_profile, creating_settings, smart, planning
from bot_utils.user_profile import greet_user
from bot_utils.utils import make_report,test

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = os.environ.get('API_TOKEN')


def report():
    make_report()


def main():
    my_bot = Updater(API_TOKEN, use_context=True)
    dp = my_bot.dispatcher
    dp.add_handler(creating_settings)
    dp.add_handler(user_profile)
    dp.add_handler(smart)
    dp.add_handler(planning)

    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('report', test))
    dp.add_handler(MessageHandler(Filters.text, greet_user))

    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()

# asyncio.run(test())


if __name__ == "__main__":
    main()
