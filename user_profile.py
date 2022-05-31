import logging

from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keyboard


def start_profile(update, context):
    update.message.reply_text(
        "Как к Вам обращаться?",
        reply_markup=ReplyKeyboardRemove()
    )
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
    try:
        user_age = int(update.message.text)
    except:
        update.message.reply_text(
            'Возраст должен состоять только из цифр.\nПовторите ввод!')
        
    logging.info(f'age: "{update.message.text}"')
    
    context.user_data['user_profile']['age'] = int(update.message.text)
    user_profile = f'''<b>Имя</b>: {
            context.user_data['user_profile']['name']}
    <b>Пол</b>: {context.user_data['user_profile']['gender']}
    <b>Возраст</b>: {context.user_data['user_profile']['age']}'''
    update.message.reply_text(user_profile, reply_markup=main_keyboard(),
                                  parse_mode=ParseMode.HTML)

    return ConversationHandler.END


def wrong_answer(update, context):
    update.message.reply_text('Некорректный ответ. Повторите ввод.')
