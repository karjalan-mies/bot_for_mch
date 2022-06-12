import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from .utils import get_message_text


def start_planning(update, context):
    logging.info('Вызов функции "start_planning"')
    message_text = get_message_text(219, update)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
