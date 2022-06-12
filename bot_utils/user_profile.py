import logging

from django.core.exceptions import ObjectDoesNotExist
from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from .utils import main_keyboard
from api.models import UserTelegram


def greet_user(update, context):
    """Приветствие при команде /start"""
    try:
        #Проверка зарегистрирован ли пользователь. Если да, перенаправление в "Личный кабинет"
        user = UserTelegram.objects.get(tg_id=update.message.chat_id)
        update.message.reply_text(
            f'Привет, {user.name}!\n' +
            'Мы уже знакомы. Давай теперь настроим твой профиль',
            reply_markup=ReplyKeyboardMarkup([['Настроить',
                                               'Не сейчас']]
                                             )
        )
    except ObjectDoesNotExist:
        logging.info('Объект в базе не найден. Будет создан новый.')

        # Создание уникального юзера по Телеграмм ИД
        user = UserTelegram(tg_id=update.message.chat_id)
        user.save()

        logging.info(f'Добавлен user с id={user.id}')

        # Текст для знакомства
        update.message.reply_text(
            'Привет!\nЯ Степан - бот-помощник от компании "Нетология".\n' +
            'Моя задача способствовать повышению осознанности и ' +
            'эффективности твоего обучения. '
            'Давай знакомиться',
            reply_markup=ReplyKeyboardMarkup([['Познакомиться']]))


def start_profile(update, context):
    """Спрашиваем имя пользователя"""
    update.message.reply_text('Как я могу к тебе обращаться?',
                              reply_markup=ReplyKeyboardRemove())
    return 'name'


def name(update, context):
    """Заносим имя пользователя в Базу Данных"""
    user_name = update.message.text

    if len(user_name.strip()) == 0:
        update.message.reply_text(
            'Имя не может быть пустым.')
        return 'name'
    else:
        context.user_data['user_profile'] = {'name': user_name}#Нужно ли это уже убрать??????????????7
        # Сохраняем имя пользователя по его телеграмм ИД
        user = UserTelegram.objects.get(tg_id=update.message.chat_id)
        user.name = user_name
        user.save()
        logging.info(f'name: "{update.message.text}"')

        # Спрашиваем пол пользователя
        reply_keyboard = [['Мужской', 'Женский']]
        update.message.reply_text(
            'Укажи свой пол, чтобы мне было проще строить диалог.',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                             one_time_keyboard=True)
        )
    return 'gender'


def gender(update, context):
    """Заносим пол пользователя в Базу Данных"""
    context.user_data['user_profile']['gender'] = update.message.text#Нужно ли это уже убрать??????????????7

    # Сохраняем пол пользователя по его телеграмм ИД
    sex = context.user_data['user_profile']['gender']
    user = UserTelegram.objects.get(tg_id=update.message.chat_id)
    user.sex = (True if sex == "Мужской" else False)
    user.save()
    logging.info(f'gender: "{update.message.text}"')

    # Спрашиваем , хочет ли пользователь сейчас настроить профиль или позже?
    keyboard_markup = [['Настроить', 'Не сейчас']]
    update.message.reply_text('Отлично! Теперь можем приступить к настройке' +
                              ' твоего профиля',
                              reply_markup=ReplyKeyboardMarkup(keyboard_markup)
                              )
    return ConversationHandler.END
