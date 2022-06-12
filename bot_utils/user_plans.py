import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from .utils import get_message_text


def start_planning(update, context):
    logging.info('Вызов функции "start_planning"')
    message_text = get_message_text(219, update)
    keyboard_markup = [['По темам', 'За период']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(
                                keyboard_markup,
                                resize_keyboard=True))
    return ConversationHandler.END


def which_planning(update, context):
    logging.info('Вызов функции "which_planning"')
    user_answer = update.message.text
    if user_answer == 'По темам':
        message_text = get_message_text(220, update)
        keyboard_markup = [['По темам', 'За период']]
        update.message.reply_text(message_text,
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard_markup,
                                    resize_keyboard=True))
        return ConversationHandler.END
    elif user_answer == 'За период':
        message_text = get_message_text(221, update)
        keyboard_markup = [['По темам', 'За период']]
        update.message.reply_text(message_text,
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard_markup,
                                    resize_keyboard=True))
        return ConversationHandler.END