from django.contrib import admin
from .models import *
# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    list_display = ("user","tweet_text","image","date")

admin.site.register(Tweet,TweetAdmin)