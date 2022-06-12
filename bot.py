import asyncio
import sys
import logging
import os
from pathlib import Path
import json

import django

# Загружаем настройки Джанго
sys.path.append(str(Path(__file__).resolve().parent))
os.environ['DJANGO_SETTINGS_MODULE'] = 'telega.settings'
django.setup()

from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater, messagequeue)

from bot_utils.handlers import user_profile, creating_settings, smart, planning
from bot_utils.user_profile import greet_user
from bot_utils.utils import test
from report_make import graphs
from api.models import HappinessStore, UserTelegram

logging.basicConfig(filename='bot.log', level=logging.INFO)

API_TOKEN = os.environ.get('API_TOKEN')



# def test(update,env):
#     pass
# with open('file.json') as file:
#     data = json.load(file).get("res")
#     for mess in data:
#         m=MessageText()
#         m.title=mess.get("title")
#         m.man_text=mess.get("man") if mess.get("man") else None
#         m.woman_text=mess.get("woman") if mess.get("woman") else None
#         m.common_text = mess.get("common") if mess.get("common") else None
#         m.save()

# with open("DB.txt") as DB:
#     while True:
#         line = DB.readline().split(" ")
#         if not line[0]:
#             break
# update.message.reply_text('Тест пройден',
#                           reply_markup=ReplyKeyboardMarkup([['/test']]))
def report(update, env):
    def make_report():
        happy = HappinessStore.objects.order_by('id').last()
        user = happy.user
        stat = [
            f"{happy.course_name}@{happy.thema_now}@{happy.learn}@{happy.remember}@{happy.task}@{user.education_start}@{user.percent_complete}",
            happy.regularity_week, happy.emotional_week, happy.motivation_week]
        return graphs(stat)

    time = make_report()

    env.bot.send_document(chat_id=update.message.chat_id, document=open(f"stat/{time}/generated_doc.docx", 'rb'))
    # with open(f"stat/{time}/generated_doc.docx") as doc:
    #     env.bot.send_document(chat_id=update.message.chat_id, document=doc)




def main():
    my_bot = Updater(API_TOKEN, use_context=True)
    dp = my_bot.dispatcher
    dp.add_handler(creating_settings)
    dp.add_handler(user_profile)
    dp.add_handler(smart)
    dp.add_handler(planning)

    dp.add_handler(CommandHandler('start', greet_user))


    dp.add_handler(CommandHandler('report', report))
    dp.add_handler(MessageHandler(Filters.text, greet_user))


    logging.info('Бот стартовал')
    my_bot.start_polling()
    my_bot.idle()

# asyncio.run(test())

if __name__ == "__main__":
    main()
