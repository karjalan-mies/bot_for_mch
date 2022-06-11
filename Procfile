worker: python3 bot.py
web: gunicorn telega.wsgi
worker2: celery -A telega worker -l info
