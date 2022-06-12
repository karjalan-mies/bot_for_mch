import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from .utils import get_message_text,save_in_DB,save_SMART_in_DB


def send_image(chat_id: str, context):
    with open('bot_utils/image.png', 'rb') as img:
        context.bot.send_photo(chat_id=chat_id,
                               photo=img)


def about_SMART(update, context):
    logging.info('Вызов функции "about_SMART"')
    chat_id = update.message.chat_id
    send_image(chat_id, context)
    message_text = get_message_text(211, update)
    reply_keyboard = [['Дальше']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(
                                reply_keyboard,
                                resize_keyboard=True))
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
    save_SMART_in_DB(update.message.text, update.message.chat_id)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'achievable'


def achievable(update, context):
    logging.info('Вызов функции "achievable"')
    message_text = get_message_text(214, update)
    save_SMART_in_DB(update.message.text, update.message.chat_id)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'relevant'


def relevant(update, context):
    logging.info('Вызов функции "relevant"')
    message_text = get_message_text(215, update)
    save_SMART_in_DB(update.message.text, update.message.chat_id)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'time_bound'


def time_bound(update, context):
    logging.info('Вызов функции "time_bound"')
    message_text = get_message_text(216, update)
    save_SMART_in_DB(update.message.text, update.message.chat_id)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'show_SMART'


def show_SMART(update, context):
    logging.info('Вызов функции "show_SMART"')
    smart=save_SMART_in_DB(update.message.text, update.message.chat_id)
    splitsmart=smart.split("@!")
    message_text = f'''Давай посмотрим, что у тебя получилось:\n
- specific: {splitsmart[0]}\n
- measurable: {splitsmart[1]}\n
- achievable: {splitsmart[2]}\n
- relevant: {splitsmart[3]}\n
- time_bound: {splitsmart[4]}\n
'''
    reply_keyboard = [['Супер!']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(
                                reply_keyboard,
                                resize_keyboard=True))
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
    save_in_DB("main_target", update.message.text, update.message.chat_id)
    reply_keyboard = [['Да, все верно', 'Изменить цели']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(
                                reply_keyboard,
                                resize_keyboard=True))
    return ConversationHandler.END

