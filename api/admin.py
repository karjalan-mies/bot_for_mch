from django.contrib import admin
from .models import UserTelegram,MessageText
# Register your models here.
admin.site.register(UserTelegram)
admin.site.register(MessageText)