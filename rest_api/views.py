from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from django.shortcuts import get_object_or_404
import json
from django.http import FileResponse

ip_adress = "http://127.0.0.1:8000/"

# Create your views here.


class SingleTweetView(APIView):

    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # Get a single tweet with tweet id param
    def get(self, request,format=None):
        tweet_id = request.GET.get('tweet_id')
        if not tweet_id:
            HttpResponse(json.dumps({'error':'tweet_id is required'}), content_type='application/json')

        tweet = get_object_or_404(Tweet, id = tweet_id)
        tweet_image = None
        if tweet.image is not None:
            tweet_image = ip_adress + "/media/" + tweet.image.name

        listResponse = {
            'tweet_id': tweet.id,
            'tweet_text': tweet.tweet_text,
            'tweet_user': tweet.user.username,
            'tweet_image': tweet_image,
            'tweet_date': str(tweet.date),

        }
        return HttpResponse(json.dumps(listResponse), content_type='application/json')

    # Create a new tweet
    def post(self, request, format = None):
        data = json.loads(request.body)
        print(data.get("tweet_text"))
        if data.get('tweet_text'):
            new_tweet = Tweet()
            new_tweet.user = request.user
            new_tweet.tweet_text = data.get('tweet_text')
            new_tweet.save()

            response = {'tweet_id': new_tweet.id,
                        'tweet_text': new_tweet.tweet_text,
                        'status': 'Saved!'}
        else:
            response = {'error': 'tweet_text is empty!'}

        return Response(response, status=status.HTTP_201_CREATED)

    # Delete a tweet with tweet_id
    def delete(self,request,format=None):
        tweet_id = request.GET.get('tweet_id')
        if not tweet_id:
            HttpResponse(json.dumps({'error': 'tweet_id is required'}), content_type='application/json')

        tweet = get_object_or_404(Tweet, id = tweet_id)
        tweet.delete()
        responseData = {'tweet_id': tweet_id}
        responseData['status'] = 'Deleted'

        return HttpResponse(json.dumps(responseData), content_type='application/json')


class HomePageView(APIView):

    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # Get a single tweet with tweet id param
    def get(self, request,format=None):

        all_tweets = Tweet.objects.all()
        all_tweet_list = []

        for tweet in all_tweets:
            tweet_informations = {
                'tweet_id': tweet.id,
                'tweet_text': tweet.tweet_text,
                'tweet_user': tweet.user.username,
                'tweet_date': str(tweet.date),
            }
            all_tweet_list.append(tweet_informations)

        return HttpResponse(json.dumps(all_tweet_list), content_type='application/json')


class ProfilePageView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # Get a single tweet with tweet id param
    def get(self, request, format=None):
        all_tweets = Tweet.objects.filter(user=request.user)
        all_tweet_list = []

        for tweet in all_tweets:
            tweet_informations = {
                'tweet_id': tweet.id,
                'tweet_text': tweet.tweet_text,
                'tweet_user': tweet.user.username,
                'tweet_date': str(tweet.date),
            }
            all_tweet_list.append(tweet_informations)

        return HttpResponse(json.dumps(all_tweet_list), content_type='application/json')


