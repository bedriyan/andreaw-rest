from django.urls import path
from . import views

urlpatterns = [
    path('single_tweet/',views.SingleTweetView.as_view()),
]