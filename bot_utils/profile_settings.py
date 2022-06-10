import logging


def set_up_profile(update, context):
    logging.info('Вызов функции "set_up_profile"')
    logging.info(update.message.message_id)
    from bot import my_bot
    my_bot.delete_message(update.message.chat.id,
                          update.message.message_id)
