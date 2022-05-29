import logging

from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keyboard


def start_profile(update, context):
    update.message.reply_text(
        "Привет, как тебя зовут?\nВведи свои фамилию, имя и отчество:",
        reply_markup=ReplyKeyboardRemove()
    )
    return 'name'


def name(update, context):
    user_name = update.message.text
    logging.info(f'name: "{update.message.text}"')
    if len(user_name.split()) < 3:
        update.message.reply_text(
            'Необходимо, введите фамилию, имя и отчество.')
        return 'name'
    else:
        context.user_data['user_profile'] = {'name': user_name}
        reply_keyboard = [['Мужской','Женский']]
        update.message.reply_text(
            'Пожалуйста, укажите Ваш пол:',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                             one_time_keyboard=True)
            )
    return 'gender'


def gender(update, context):
    logging.info(f'gender: "{update.message.text}"')
    context.user_data['user_profile']['gender'] = update.message.text
    update.message.reply_text('Пожалуйста, введите Ваш возраст:',
                              reply_markup=ReplyKeyboardRemove())
    return 'age'


def age(update, context):
    user_age = update.message.text
    logging.info(f'age: "{update.message.text}"')
    if user_age.isdigit():
        context.user_data['user_profile']['age'] = int(update.message.text)
        user_profile = f'''<b>ФИО</b>: {
            context.user_data['user_profile']['name']}
<b>Пол</b>: {context.user_data['user_profile']['gender']}
<b>Возраст</b>: {context.user_data['user_profile']['age']}'''
        update.message.reply_text(user_profile, reply_markup=main_keyboard(),
                                  parse_mode=ParseMode.HTML)
        return ConversationHandler.END
    else:
        update.message.reply_text(
            'Возраст должен состоять только из цифр.\nПовторите ввод!')
        return 'age'


def wrong_answer(update, context):
    update.message.reply_text('Некорректный ответ. Повторите ввод.')
