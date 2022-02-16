from django.urls import path
from . import views

urlpatterns = [
    path('single_tweet/',views.SingleTweetView.as_view()),
    path('homepage/',views.HomePageView.as_view()),
    path('profile/',views.ProfilePageView.as_view()),
]