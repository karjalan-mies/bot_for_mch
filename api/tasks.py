import datetime
import os

from celery import shared_task
from django_celery_beat.models import PeriodicTask

@shared_task(name="repeat_test")
def repeat_test():
    os.mkdir(f"folder{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}")