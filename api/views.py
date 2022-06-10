from celery import shared_task
from celery.schedules import crontab
from django.shortcuts import render
from django.http import HttpResponse


def periodic_task(run_every):
    pass


@periodic_task(run_every=crontab(minute="*"))
def do_something_with_form_data(data):
    print("CELERY TIME!")


def test(request):
    do_something_with_form_data.delay()
    return HttpResponse()

# tasks.py
# Create your views here.
