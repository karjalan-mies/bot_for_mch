from email.message import Message
from importlib.metadata import entry_points
import logging
import os

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from user_profile import start_profile, name, gender, age, wrong_answer
from utils import main_keyboard

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = os.environ.get('API_TOKEN')


def get_user_data(update):
    print(dir(update.message.from_user))
    user_data = {}
    user_data['full_name'] = update.message.chat.full_name
    user_data['first_name'] = update.message.chat.first_name
    user_data['last_name'] = update.message.chat.last_name
    user_data['username'] = update.message.chat.username
    user_data['user_id'] = update.message.chat.id
    return user_data


def greet_user(update, context):
    # get_user_data(update)
    update.message.reply_text(
        'Привет!\nЯ бот-помощник. Давай начнем общение!',
        reply_markup=main_keyboard()
    )


def main():
    my_bot = Updater(API_TOKEN, use_context=True)
    dp = my_bot.dispatcher

    user_profile = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Заполнить профиль)$'),
                           start_profile)
        ],
        states={
            'name': [MessageHandler(Filters.text, name)],
            'gender': [MessageHandler(Filters.regex('^(Мужской|Женский)$'),
                       gender)],
            'age': [MessageHandler(Filters.regex('^(\d+)$'), age)]
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.photo | Filters.video |
                           Filters.document | Filters.location, wrong_answer)
        ]
    )
    dp.add_handler(user_profile)
    dp.add_handler(CommandHandler('start', greet_user))

    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
