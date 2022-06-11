worker.1: python3 bot.py
web: gunicorn telega.wsgi
worker.2: celery -A telega worker -l info
