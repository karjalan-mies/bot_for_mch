import logging

from telegram import ReplyKeyboardRemove

from api.models import Target, UserTelegram
from .utils import get_message_text


def set_up_profile(update, context):
    logging.info('Вызов функции "set_up_profile"')
    message_text = get_message_text(201, update)
    update.message.reply_text(message_text, reply_markup=ReplyKeyboardRemove())
    return 'course_name'


def course_name(update, context):
    logging.info('Вызов функции "course_name"')
    course_name = update.message.text
    if len(course_name.strip()) == 0:
        update.message.reply_text(
            'Название курса не может быть пустым.')
        return 'name'
    else:
        # Сохраняем название курса
        user = UserTelegram.objects.get(tg_id=update.message.chat_id)
        target = Target.objects.get(user)
        target.course_name = course_name
        target.save()
        logging.info(f'course_name: "{update.message.text}"')
    message_text = get_message_text(202, update)
    update.message.reply_text(message_text, reply_markup=ReplyKeyboardRemove())
    return 'which_dates'


def which_dates(update, context):
    logging.info('Вызов функции "which_dates"')
    dates = update.message.text.split()
    user = UserTelegram.objects.get(tg_id=update.message.chat_id)
    user.education_start = '-'.join(dates[0].split('.')[::-1])
    user.education_start = '-'.join(dates[1].split('.')[::-1])
    user.save()
    logging.info(f'Добавлены даты обучения с {dates[0]} по {dates[1]}')
    message_text = get_message_text(203, update)
    update.message.reply_text(message_text, reply_markup=ReplyKeyboardRemove())
    return 
