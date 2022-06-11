worker: python3 bot.py
web: gunicorn telega.wsgi
worker: celery -A telega worker -l info
