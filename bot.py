import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

API_TOKEN = os.environ.get('API_TOKEN')


def greet_user(update, context):
    update.message.reply_text(
        'Привет!\nЯ бот-помощник. Давай начнем общение!',
    )


def main():
    my_bot = Updater(API_TOKEN, use_context=True)
    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
