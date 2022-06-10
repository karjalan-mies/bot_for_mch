from django.db import models


class UserTelegram(models.Model):
    name = models.TextField(max_length=128, blank=True, null=True)
    first_name = models.TextField(max_length=70, blank=True, null=True)
    last_name = models.TextField(max_length=70, blank=True, null=True)
    patronymic = models.TextField(max_length=70, blank=True, null=True)
    sex = models.BooleanField(blank=True, null=True)
    tg_id = models.IntegerField()#unique=True
    age = models.IntegerField(default=0)
# Create your models here.

class MessageText(models.Model):
    """
    Хранилище текстов для бота
    """
    title=models.TextField(max_length=128, blank=True, null=True,verbose_name="Кратко тема(чтоб не запутаться)")
    man_text=models.TextField(blank=True, null=True,verbose_name="Текст с мужскими окончаниями")
    woman_text=models.TextField(blank=True, null=True,verbose_name="Текст с женскими окончаниями")
    common_text=models.TextField(blank=True, null=True,verbose_name="Общий для всех текст")
