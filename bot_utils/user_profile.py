import logging

from django.core.exceptions import ObjectDoesNotExist
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from .utils import save_in_DB
from api.models import UserTelegram


def greet_user(update, context):
    """Приветствие при команде /start"""
    try:
        #Проверка зарегистрирован ли пользователь. Если да, перенаправление в "Личный кабинет"
        user = UserTelegram.objects.get(tg_id=update.message.chat_id)
        if user.main_target:
            update.message.reply_text(
                'Твои цели определены и сохранены',
                reply_markup=ReplyKeyboardMarkup([['Посмотреть',
                                                   'Изменить',
                                                   'Отчет']],
                                                 resize_keyboard=True))
        else:
            update.message.reply_text(
                f'Привет, {user.name}!\n' +
                'Мы уже знакомы. Давай теперь настроим твой профиль',
                reply_markup=ReplyKeyboardMarkup([['Настроить',
                                                   'Не сейчас']],
                                                 resize_keyboard=True))
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
            reply_markup=ReplyKeyboardMarkup([['Познакомиться']],
                                             resize_keyboard=True))


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
        save_in_DB("name", user_name, update.message.chat_id)
        logging.info(f'name: "{update.message.text}"')

        # Спрашиваем пол пользователя
        reply_keyboard = [['Мужской', 'Женский']]
        update.message.reply_text(
            'Укажи свой пол, чтобы мне было проще строить диалог.',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                             one_time_keyboard=True,
                                             resize_keyboard=True))
    return 'gender'


def gender(update, context):
    """Заносим пол пользователя в Базу Данных"""
    # Сохраняем пол пользователя по его телеграмм ИД
    sex = update.message.text
    save_in_DB("sex", True if sex == "Мужской" else False, update.message.chat_id)
    logging.info(f'gender: "{update.message.text}"')

    # Спрашиваем , хочет ли пользователь сейчас настроить профиль или позже?
    keyboard_markup = [['Настроить', 'Не сейчас']]
    update.message.reply_text('Отлично! Теперь можем приступить к настройке' +
                              ' твоего профиля',
                              reply_markup=ReplyKeyboardMarkup(
                                keyboard_markup,
                                resize_keyboard=True))
    return ConversationHandler.END
