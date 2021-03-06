from django.db import models


class UserTelegram(models.Model):
    """Модель для хранения пользователей"""
    name = models.TextField(max_length=128, blank=True, null=True, verbose_name="Никнейм пользователя")
    sex = models.BooleanField(blank=True, null=True, verbose_name="Пол (Мужской-1, Женский-0) пользователя")
    tg_id = models.IntegerField(verbose_name="Уникальный ИД телеграмма")  # unique=True
    age = models.IntegerField(blank=True, null=True, verbose_name="Возраст пользователя")

    course_name = models.TextField(max_length=128, blank=True, null=True, verbose_name="Название курса")
    education_start = models.TextField(blank=True, null=True, verbose_name="Время начала обучения")
    education_end = models.TextField(blank=True, null=True, verbose_name="Предполагаемы конец обучения")
    remind_next = models.TextField(blank=True, null=True, verbose_name="Следующее напоминание")
    remind_interval_in_day = models.IntegerField(blank=True, null=True, verbose_name="В какой день напоминать?")

    percent_complete = models.IntegerField(default=0, verbose_name="% выполнения цели")
    education_rate = models.TextField(blank=True, null=True, verbose_name="Оценка уровня обучения")
    hapiness_level = models.TextField(blank=True, null=True, verbose_name="Оценка удовольствия от обучения")

    what_for = models.TextField(blank=True, null=True, verbose_name="Зачем тебе этому учиться")
    what_you_want = models.TextField(blank=True, null=True, verbose_name="Что ты хочешь от обучения")
    what_changed = models.TextField(blank=True, null=True, verbose_name="Что в твоей жизни изменится после обучения?")
    main_target = models.TextField(blank=True, null=True, verbose_name="Основная цель -задача")
    smart = models.TextField(blank=True, null=True, verbose_name="SMART критерии через @!")

    period = models.DateField(blank=True, null=True, verbose_name="Cколько времени готов потратить на подцель")

    def __str__(self):
        return self.name


# Create your models here.

class MessageText(models.Model):
    """ Хранилище текстов для бота """
    title = models.TextField(max_length=128, blank=True, null=True, verbose_name="Кратко тема(чтоб не запутаться)")
    man_text = models.TextField(blank=True, null=True, verbose_name="Текст с мужскими окончаниями")
    woman_text = models.TextField(blank=True, null=True, verbose_name="Текст с женскими окончаниями")
    common_text = models.TextField(blank=True, null=True, verbose_name="Общий для всех текст")

    def __str__(self):
        return self.title


class Imagestore(models.Model):
    """ Хранилище картинок для бота """
    title = models.TextField(max_length=128, blank=True, null=True, verbose_name="Название картинки")
    image = models.ImageField(blank=True, upload_to="img")

    def __str__(self):
        return self.title


class HappinessStore(models.Model):
    user = models.ForeignKey(UserTelegram, on_delete=models.CASCADE)
    course_name = models.TextField(max_length=128, blank=True, null=True, verbose_name="Название курса")
    thema_now = models.TextField(blank=True, null=True, verbose_name="тема курса")
    learn = models.TextField(blank=True, null=True, verbose_name="что выучить")
    remember = models.TextField(blank=True, null=True, verbose_name="что вспомнить")
    task = models.TextField(blank=True, null=True, verbose_name="текущая задача")
    emotional_week = models.TextField(blank=True, null=True, verbose_name="Эмоции на неделю")
    regularity_week = models.TextField(blank=True, null=True, verbose_name="Регулярность на неделю")
    motivation_week = models.TextField(blank=True, null=True, verbose_name="уровень понимания темы")
    emotional_month = models.TextField(blank=True, null=True, verbose_name="Эмоции на месяц")
    regularity_month = models.TextField(blank=True, null=True, verbose_name="Регулярность на месяц")
    motivation_month = models.TextField(blank=True, null=True, verbose_name="уровень понимания темы на месяц")
