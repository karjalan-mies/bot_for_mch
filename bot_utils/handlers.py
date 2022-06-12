from re import I
from telegram.ext import ConversationHandler, Filters, MessageHandler


from bot_utils.profile_settings import (set_up_profile, course_name,
                                        which_dates,
                                        which_days, set_targets, why_study,
                                        what_do_you_want, how_life_will_change,
                                        what_is_the_SMART)
from bot_utils.SMART import (about_SMART, specific, measurable, achievable,
                             relevant, time_bound, show_SMART,
                             set_total_target, targets_right,
                             )
from bot_utils.user_profile import start_profile, name, gender
from bot_utils.user_plans import (start_planning, which_planning,
                                  adding_themes)
from bot_utils.utils import wrong_answer

user_profile = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^(Познакомиться)$'),
                       start_profile)
    ],
    states={
        'name': [MessageHandler(Filters.text, name)],
        'gender': [MessageHandler(Filters.regex('^(Мужской|Женский)$'),
                   gender)],
    },
    fallbacks=[
        MessageHandler(Filters.text | Filters.photo | Filters.video |
                       Filters.document | Filters.location, wrong_answer)
    ]
)
creating_settings = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^(Настроить)$'), set_up_profile)
    ],
    states={
        'course_name': [MessageHandler(Filters.text, course_name)],
        'which_dates': [MessageHandler(Filters.text, which_dates)],
        'which_days': [MessageHandler(Filters.text, which_days)],
        'set_targets': [MessageHandler(Filters.text, set_targets)],
        'why_study': [MessageHandler(Filters.text, why_study)],
        'what_do_you_want': [MessageHandler(Filters.text,
                             what_do_you_want)],
        'how_life_will_change': [MessageHandler(Filters.text,
                                 how_life_will_change)],
        'what_is_the_SMART': [MessageHandler(Filters.text,
                              what_is_the_SMART)],
        },
    fallbacks=[MessageHandler(Filters.text | Filters.photo |
               Filters.video | Filters.document | Filters.location,
               wrong_answer)]
)
smart = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^(Нет. Расскажи)$'),
                       about_SMART)
    ],
    states={
        'specific': [MessageHandler(Filters.text, specific)],
        'measurable': [MessageHandler(Filters.text, measurable)],
        'achievable': [MessageHandler(Filters.text, achievable)],
        'relevant': [MessageHandler(Filters.text, relevant)],
        'time_bound': [MessageHandler(Filters.text, time_bound)],
        'show_SMART': [MessageHandler(Filters.text, show_SMART)],
        'set_total_target': [MessageHandler(Filters.text,
                             set_total_target)],
        'targets_right': [MessageHandler(Filters.text, targets_right)],
    },
    fallbacks=[MessageHandler(Filters.text | Filters.photo |
               Filters.video | Filters.document | Filters.location,
               wrong_answer)])

planning = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^(Начать планирование)$'),
                       start_planning)
    ],
    states={
        'which_planning': [MessageHandler(Filters.text, which_planning)],
        'adding_themes': [MessageHandler(Filters.text, adding_themes)],
    },
    fallbacks=[MessageHandler(Filters.text | Filters.photo |
               Filters.video | Filters.document | Filters.location,
               wrong_answer)]
)
