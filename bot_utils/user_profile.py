import logging

from django.core.exceptions import ObjectDoesNotExist
from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from .utils import main_keyboard
from api.models import UserTelegram


def greet_user(update, context):
    try:
        user = UserTelegram.objects.get(tg_id=update.message.chat_id)
        logging.info(f'В БД уже есть user tg_id={user.tg_id}')
        update.message.reply_text(
            f'Привет, {user.name}!\n' +
            'Мы уже знакомы. Давай теперь настроим твой профиль',
            reply_markup=ReplyKeyboardMarkup([['Настроить',
                                               'Не сейчас']])
        )
    except ObjectDoesNotExist:
        logging.info('Объект в базе не найден. Будет создан новый.')
        user = UserTelegram(tg_id=update.message.chat_id)
        user.save()
        logging.info(f'Добавлен user с id={user.id}')
        update.message.reply_text(
            'Привет!\nЯ Степан - бот-помощник от компании "Нетология".\n' +
            'Моя задача способствовать повышению осознанности и ' +
            'эффективности твоего обучения. '
            'Давай знакомиться',
            reply_markup=ReplyKeyboardMarkup([['Познакомиться']]))


def start_profile(update, context):
    update.message.reply_text('Как я могу к тебе обращаться?',
                              reply_markup=ReplyKeyboardRemove())
    return 'name'


def name(update, context):
    user_name = update.message.text
    logging.info(f'name: "{update.message.text}"')
    if len(user_name.strip()) == 0:
        update.message.reply_text(
            'Имя не может быть пустым.')
        return 'name'
    else:
        context.user_data['user_profile'] = {'name': user_name}
        """"""
        user = UserTelegram.objects.get(tg_id=update.message.chat_id)
        user.name = user_name
        user.save()
        """"""
        reply_keyboard = [['Мужской', 'Женский']]
        update.message.reply_text(
            'Укажи свой пол, чтобы мне было проще строить диалог.',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                             one_time_keyboard=True)
        )
    return 'gender'


def gender(update, context):
    logging.info(f'gender: "{update.message.text}"')
    context.user_data['user_profile']['gender'] = update.message.text

    """"""
    user = UserTelegram.objects.get(tg_id=update.message.chat_id)
    user.sex = (True if context.user_data['user_profile']
                ['gender'] == "Мужской" else False)
    user.save()
    """"""

    keyboard_markup = [['Настроить', 'Не сейчас']]
    update.message.reply_text('Отлично! Теперь можем приступить к настройке' +
                              ' твоего профиля',
                              reply_markup=ReplyKeyboardMarkup(keyboard_markup)
                              )
    return ConversationHandler.END


def wrong_answer(update, context):
    update.message.reply_text('Некорректный ответ. Повторите ввод.')
