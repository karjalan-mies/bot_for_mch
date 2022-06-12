import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from api.models import Target, UserTelegram
from .utils import get_message_text


def set_up_profile(update, context):
    logging.info('Вызов функции "set_up_profile"')
    message_text = get_message_text(201, update)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardRemove())
    return 'course_name'


def course_name(update, context):
    logging.info('Вызов функции "course_name"')
    course_name = update.message.text
    if len(course_name.strip()) == 0:
        update.message.reply_text(
            'Название курса не может быть пустым.')
        return 'name'
    else:
        user = UserTelegram.objects.get(tg_id=update.message.chat_id)
        user.course_name = course_name
        user.save()

        logging.info(f'course_name: "{update.message.text}"')
    message_text = get_message_text(202, update)
    update.message.reply_text(message_text, reply_markup=ReplyKeyboardRemove())
    return 'which_dates'


def which_dates(update, context):
    logging.info('Вызов функции "which_dates"')
    try:
        dates = update.message.text.split()
        user = UserTelegram.objects.get(tg_id=update.message.chat_id)
        user.education_start = '-'.join(dates[0].split('.')[::-1])
        user.education_start = '-'.join(dates[1].split('.')[::-1])
        user.save()
        logging.info(f'Добавлены даты обучения с {dates[0]} по {dates[1]}')
    except:

    message_text = get_message_text(203, update)
    reply_keyboard = [['Ok!']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return 'which_progress'


def which_progress(update, context):
    logging.info('Вызов функции "which_progress"')
    message_text = get_message_text(204, update)
    reply_keyboard = [['По каждой теме', 'Общий прогресс']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return 'which_days'


def which_days(update, context):
    logging.info('Вызов функции "which_days"')
    message_text = get_message_text(205, update)
    reply_keyboard = [['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return 'set_targets'


def set_targets(update, context):
    logging.info('Вызов функции "set_targets"')
    reply_keyboard = [['Ok!']]
    message_text = get_message_text(206, update)
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return 'why_study'


def why_study(update, context):
    logging.info('Вызов функции "why_study"')
    message_text = get_message_text(207, update)
    update.message.reply_text(message_text, reply_markup=ReplyKeyboardRemove())
    return 'what_do_you_want'


def what_do_you_want(update, context):
    logging.info('Вызов функции "what_do_you_want"')
    message_text = get_message_text(208, update)
    update.message.reply_text(message_text, reply_markup=ReplyKeyboardRemove())
    return 'how_life_will_change'


def how_life_will_change(update, context):
    logging.info('Вызов функции "what_do_you_want"')
    message_text = get_message_text(209, update)
    update.message.reply_text(message_text, reply_markup=ReplyKeyboardRemove())
    return 'what_is_the_SMART'


def what_is_the_SMART(update, context):
    logging.info('Вызов функции "what_do_you_want"')
    message_text = get_message_text(210, update)
    reply_keyboard = [['Начать планирование', 'Что такое S.M.A.R.T']]
    update.message.reply_text(message_text,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return ConversationHandler.END
