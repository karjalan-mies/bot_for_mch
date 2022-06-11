from django.db import models


class UserTelegram(models.Model):
    """Модель для хранения пользователей"""
    name = models.TextField(max_length=128, blank=True, null=True,verbose_name="Никнейм пользователя")
    sex = models.BooleanField(blank=True, null=True,verbose_name="Пол (Мужской-1, Женский-0) пользователя")
    tg_id = models.IntegerField(verbose_name="Уникальный ИД телеграмма")#unique=True
    age = models.IntegerField(default=0,verbose_name="Возраст пользователя")
    course_name = models.TextField(max_length=128, blank=True, null=True,verbose_name="Название курса")
    education_start = models.DateField(auto_now_add=True)
    education_end = models.DateField(blank=True, null=True)
    remind_interval = models.IntegerField(default=86400)
# Create your models here.

class MessageText(models.Model):
    """ Хранилище текстов для бота """
    title = models.TextField(max_length=128, blank=True, null=True,verbose_name="Кратко тема(чтоб не запутаться)")
    man_text = models.TextField(blank=True, null=True,verbose_name="Текст с мужскими окончаниями")
    woman_text = models.TextField(blank=True, null=True,verbose_name="Текст с женскими окончаниями")
    common_text = models.TextField(blank=True, null=True,verbose_name="Общий для всех текст")
