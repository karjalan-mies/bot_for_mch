from django.contrib import admin
from .models import UserTelegram,MessageText,Imagestore,HappinessStore
# Register your models here.
admin.site.register(UserTelegram)
admin.site.register(MessageText)
admin.site.register(Imagestore)
admin.site.register(HappinessStore)
