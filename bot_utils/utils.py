import asyncio
import datetime
import logging
import os
import requests
from django.core.exceptions import ObjectDoesNotExist
from telegram import ReplyKeyboardMarkup
from telegram.ext import messagequeue as mq
from api.models import MessageText, UserTelegram,HappinessStore
from asgiref.sync import sync_to_async
import matplotlib as mpl


def main_keyboard():
    return ReplyKeyboardMarkup([['Меню']], resize_keyboard=True)


def get_user_gender(update):
    user_id = update.message.chat_id
    try:
        user = UserTelegram.objects.get(tg_id=user_id)
        return user.sex
    except ObjectDoesNotExist:
        logging.info(f'Пользователь с id:{user_id} не содержится в БД')


def get_message_text(code, update):
    user_gender = get_user_gender(update)
    try:
        message_text = MessageText.objects.get(title=code)
        if message_text.common_text != '':
            return message_text.common_text
        else:
            if user_gender:
                return message_text.man_text
            else:
                return message_text.woman_text
    except ObjectDoesNotExist:
        logging.info(f'Сообщение с кодом {code} не найдено!')
        return 'Технические проблемы с БД. Сообщите администратору.'


def wrong_answer(update, context):
    message_text = get_message_text('wrong_answer', update)
    update.message.reply_text(message_text)


def save_in_DB(row, value, chat_id):
    try:
        user = UserTelegram.objects.get(tg_id=chat_id)
        setattr(user, row, value)
        user.save()
    except ObjectDoesNotExist:
        logging.info(f'Пользователь с кодом {chat_id} не найден!')
        return 'Технические проблемы с БД. Сообщите администратору.'


def save_SMART_in_DB(value,chat_id):
    try:
        user = UserTelegram.objects.get(tg_id=chat_id)
        user.smart=f"{user.smart}{value}@!"
        user.save()
        return user.smart
    except:
        logging.info(f'Пользователь с кодом {chat_id} не найден!')
        return 'Технические проблемы с БД. Сообщите администратору.'

async def test():

    @sync_to_async
    def get_today_users():
        usr = UserTelegram.objects.get(name="example")
