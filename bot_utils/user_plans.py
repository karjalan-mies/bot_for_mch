import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from .utils import get_message_text, main_keyboard


def start_planning(update, context):
    logging.info('Вызов функции "start_planning"')
    message_text = get_message_text(219, update)
    keyboard_markup = [['По темам', 'За период']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(
                                keyboard_markup,
                                resize_keyboard=True))
    return 'which_planning'


def which_planning(update, context):
    logging.info('Вызов функции "which_planning"')
    user_answer = update.message.text
    if user_answer == 'По темам':
        logging.info('Вызов функции "which_themes_week"')
        message_text = get_message_text(219, update)
        keyboard_markup = [['Добавить еще тему', 'Ввел все необходимые темы']]
        update.message.reply_text(message_text,
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard_markup,
                                    resize_keyboard=True))
        return 'adding_themes'
    elif user_answer == 'За период':
        message_text = get_message_text(221, update)
        keyboard_markup = [['На месяц и на неделю', 'Только на неделю']]
        update.message.reply_text(message_text,
                                  reply_markup=ReplyKeyboardMarkup(
                                    keyboard_markup,
                                    resize_keyboard=True))
        return 'which_themes_period'


def adding_themes(update, context):
    logging.info('Вызов функции "adding_themes"')
    user_answer = update.message.text
    if user_answer == 'Добавить еще тему':
        logging.info('Вызов функции "which_themes_week"')
        message_text = get_message_text(219, update)
        keyboard_markup = [['Добавить еще тему', 'Ввел все необходимые темы']]
        update.message.reply_text(message_text,
                                  reply_markup=ReplyKeyboardMarkup(
                                    keyboard_markup,
                                    resize_keyboard=True))
        return 'adding_themes'
    elif user_answer == 'Ввел все необходимые темы':
        message_text = get_message_text(221, update)
        update.message.reply_text(message_text,
                                  reply_markup=main_keyboard())
        return ConversationHandler.END


def which_themes_period(update, context):
    logging.info('Вызов функции "which_themes_period"')
    message_text = get_message_text(219, update)
    keyboard_markup = [['Одна тема', 'Несколько тем']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(
                                keyboard_markup,
                                resize_keyboard=True))
    return
