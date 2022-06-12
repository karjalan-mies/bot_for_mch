# Generated by Django 4.0.4 on 2022-06-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usertelegram_age_alter_usertelegram_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertelegram',
            name='education_end',
            field=models.TextField(blank=True, null=True, verbose_name='Предполагаемы конец обучения'),
        ),
        migrations.AlterField(
            model_name='usertelegram',
            name='education_start',
            field=models.TextField(blank=True, null=True, verbose_name='Время начала обучения'),
        ),
        migrations.AlterField(
            model_name='usertelegram',
            name='remind_next',
            field=models.TextField(blank=True, null=True, verbose_name='Следующее напоминание'),
        ),
    ]
