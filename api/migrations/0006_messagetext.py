# Generated by Django 4.0.4 on 2022-06-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_usertelegram_tg_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=128, null=True, verbose_name='Кратко тема(чтоб не запутаться)')),
                ('man_text', models.TextField(blank=True, null=True, verbose_name='Текст с мужскими окончаниями')),
                ('woman_text', models.TextField(blank=True, null=True, verbose_name='Текст с женскими окончаниями')),
                ('common_text', models.TextField(blank=True, null=True, verbose_name='Общий для всех текст')),
            ],
        ),
    ]
