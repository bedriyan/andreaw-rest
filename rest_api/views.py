from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from django.shortcuts import get_object_or_404
import json
from django.http import FileResponse

ip_adress = "http://127.0.0.1:8000/"

# You can think that each class is an endpoint. And you can write different logics for the same endpoint with
# using different methods like post, get, delete etc.
class SingleTweetView(APIView):

    # this setting handles the token-based auth. if you remove them you can use the endpoint without a token.
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # get method of this endpoint reads a single tweet with given tweet id
    def get(self, request):
        # checks if the request has tweet_id param or not
        tweet_id = request.GET.get('tweet_id')
        if not tweet_id:
            HttpResponse(json.dumps({'error':'tweet_id is required'}), content_type='application/json')

        # checks the database for if there is a tweet with given tweet_id or not.
        tweet = get_object_or_404(Tweet, id = tweet_id)

        # I added also an extra ImageField to the tweet model. I didn't use it but wanted to show you
        # that how you can serve an image url.
        tweet_image = None
        if tweet.image is not None:
            tweet_image = ip_adress + "media/" + tweet.image.name

        # prepares the response with tweets properties
        response_data = {
            'tweet_id': tweet.id,
            'tweet_text': tweet.tweet_text,
            'tweet_user': tweet.user.username,
            'tweet_image': tweet_image,
            'tweet_date': str(tweet.date),
        }

        # turns the dict into a json and returns the response
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    # post method of this endpoint creates a new tweet with given tweet_text
    def post(self, request):

        # checks if the request has tweet_text param or not
        if request.POST.get('tweet_text'):
            # creates a new tweet and saves it into the database
            new_tweet = Tweet()
            new_tweet.user = request.user
            new_tweet.tweet_text = request.POST.get('tweet_text')
            new_tweet.save()

            # prepares a response dictionary with tweet information.
            response = {'tweet_id': new_tweet.id,
                        'tweet_text': new_tweet.tweet_text,
                        'status': 'Saved!'}
        else:
            response = {'error': 'tweet_text is empty!'}

        # returns the response in a different way.
        return Response(response, status=status.HTTP_201_CREATED)

    # delete method of this endpoint deletes the tweet with given tweet_id
    def delete(self, request):
        # checks if the request has tweet_id param or not
        tweet_id = request.GET.get('tweet_id')
        if not tweet_id:
            HttpResponse(json.dumps({'error': 'tweet_id is required'}), content_type='application/json')

        # checks the database for if there is a tweet with given tweet_id or not.
        tweet = get_object_or_404(Tweet, id = tweet_id)
        tweet.delete()

        response_data = {
            'tweet_id': tweet_id,
            'status':'Deleted',
        }

        # turns the dict into a json and returns the response
        return HttpResponse(json.dumps(response_data), content_type='application/json')



# homepage endpoint
class HomePageView(APIView):

    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # this endpoint reads all tweets
    def get(self, request):

        all_tweets = Tweet.objects.all()
        all_tweet_list = []

        # reads all tweets and adds them into a list.
        for tweet in all_tweets:
            tweet_informations = {
                'tweet_id': tweet.id,
                'tweet_text': tweet.tweet,
                'tweet_user': tweet.user.username,
                'tweet_date': str(tweet.date),
            }
            all_tweet_list.append(tweet_informations)

        # turns the dict into a json and returns the response
        return HttpResponse(json.dumps(all_tweet_list), content_type='application/json')

# profile page endpoint
class ProfilePageView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # this endpoint reads all tweets of the auth user.
    def get(self, request):

        # the difference from the homepage endpoint: there is a filter for user field.
        all_tweets = Tweet.objects.filter(user=request.user)
        all_tweet_list = []

        # reads all tweets and adds them into a list.
        for tweet in all_tweets:
            tweet_informations = {
                'tweet_id': tweet.id,
                'tweet_text': tweet.tweet,
                'tweet_user': tweet.user.username,
                'tweet_date': str(tweet.date),
            }
            all_tweet_list.append(tweet_informations)

        # turns the dict into a json and returns the response
        return HttpResponse(json.dumps(all_tweet_list), content_type='application/json')


