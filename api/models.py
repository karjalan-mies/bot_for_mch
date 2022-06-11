from django.db import models


class UserTelegram(models.Model):
    """Модель для хранения пользователей"""
    name = models.TextField(max_length=128, blank=True, null=True,verbose_name="Никнейм пользователя")
    sex = models.BooleanField(blank=True, null=True,verbose_name="Пол (Мужской-1, Женский-0) пользователя")
    tg_id = models.IntegerField(verbose_name="Уникальный ИД телеграмма")#unique=True
    age = models.IntegerField(default=0,verbose_name="Возраст пользователя")
    education_start = models.DateField(auto_now_add=True,blank=True, null=True)
    education_end = models.DateField(blank=True, null=True)
    remind_interval = models.IntegerField(default=86400)
# Create your models here.

class MessageText(models.Model):
    """ Хранилище текстов для бота """
    title = models.TextField(max_length=128, blank=True, null=True, verbose_name="Кратко тема(чтоб не запутаться)")
    man_text = models.TextField(blank=True, null=True, verbose_name="Текст с мужскими окончаниями")
    woman_text = models.TextField(blank=True, null=True, verbose_name="Текст с женскими окончаниями")
    common_text = models.TextField(blank=True, null=True, verbose_name="Общий для всех текст")
    def __str__(self):
        return self.title


class Target(models.Model):
    user = models.ForeignKey(UserTelegram, on_delete=models.CASCADE)

    course_name = models.TextField(max_length=128, blank=True, null=True,verbose_name="Название курса")
    education_start = models.DateField(auto_now_add=True, verbose_name="Время начала обучения")
    education_end = models.DateField(blank=True, null=True, verbose_name="Предполагаемы конец обучения")
    remind_next = models.DateField(default=86400, verbose_name="Следующее напоминание")
    remind_interval_in_day = models.IntegerField(default=0, verbose_name="Частота напоминаний")

    percent_complete = models.IntegerField(default=0, verbose_name="% выполнения цели")
    education_rate = models.TextField(blank=True, null=True, verbose_name="Оценка уровня обучения")
    hapiness_level = models.TextField(blank=True, null=True, verbose_name="Оценка удовольствия от обучения")

    what_for = models.TextField(blank=True, null=True, verbose_name="Зачем тебе этому учиться")
    what_you_want = models.TextField(blank=True, null=True, verbose_name="Что ты хочешь от обучения")
    what_changed = models.TextField(blank=True, null=True, verbose_name="Что в твоей жизни изменится после обучения?")
    main_target = models.TextField(blank=True, null=True, verbose_name="Основная цель -задача")
    smart = models.TextField(blank=True, null=True, verbose_name="SMART критерии через запятую")

    period = models.DateField(default=86400, verbose_name="Cколько времени готов потратить на подцель")
    def __str__(self):
        return self.course_name
