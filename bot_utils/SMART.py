import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from .utils import get_message_text


def send_image(chat_id: str, context):
    context.bot.send_photo(chat_id=chat_id,
                           photo=open('bot_utils/image.png', 'rb'))


def about_SMART(update, context):
    logging.info('Вызов функции "about_SMART"')
    chat_id = update.message.chat_id
    send_image(chat_id, context)
    message_text = get_message_text(211, update)
    reply_keyboard = [['Дальше']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return 'specific'


def specific(update, context):
    logging.info('Вызов функции "specific"')
    message_text = get_message_text(212, update)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'measurable'


def measurable(update, context):
    logging.info('Вызов функции "measurable"')
    message_text = get_message_text(213, update)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'achievable'


def achievable(update, context):
    logging.info('Вызов функции "achievable"')
    message_text = get_message_text(214, update)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'relevant'


def relevant(update, context):
    logging.info('Вызов функции "relevant"')
    message_text = get_message_text(215, update)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'time_bound'


def time_bound(update, context):
    logging.info('Вызов функции "time_bound"')
    message_text = get_message_text(216, update)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'show_SMART'


def show_SMART(update, context):
    logging.info('Вызов функции "show_SMART"')
    message_text = '''Давай посмотрим, что у тебя получилось:\n
- specific: ответ\n
- measurable: ответ\n
- achievable: ответ\n
- relevant: ответ\n
- time_bound: ответ\n
'''
    reply_keyboard = [['Супер!']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return 'set_total_target'


def set_total_target(update, context):
    logging.info('Вызов функции "set_total_target"')
    message_text = get_message_text(217, update)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'targets_right'


def targets_right(update, context):
    logging.info('Вызов функции "targets_right"')
    message_text = get_message_text(218, update)
    reply_keyboard = [['Да, все верно', 'Изменить цели']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return ConversationHandler.END