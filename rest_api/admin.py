from django.contrib import admin
from .models import *


# for displaying your models (db tables) at the admin panel you have to register them here for basic registiration
# you can use just -> admin.site.register(Tweet). It only shows one field of the tweets with that.


# you can specify the fields that you want see at the admin panel with this
class TweetAdmin(admin.ModelAdmin):
    list_display = ("user", "tweet_text", "image", "date")


admin.site.register(Tweet, TweetAdmin)
