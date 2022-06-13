# Проект bot-for-mch

bot-for-mch - это бот для Telegram, который способствует осознанному прохождению обучения.

Перейти к боту: https://t.me/netology_helper_bot

## Дополнительные материалы
[Описание методологии](https://miro.com/app/board/uXjVOysa1fo=/?share_link_id=557079550908 )
Проект запущен на Heroku, используется база данные PostgreSQL

## Установка

1. Клонируйте репозиторий с git_hub
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Добавьте в файл `activate` виртуального окружения переменную:
```
API_TOKEN="API-ключ бота"
```
5. Запустите бота командой `python3 bot.py`