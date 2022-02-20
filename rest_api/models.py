# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# our main table which stores the tweet informations.
class Tweet(models.Model):
    user = models.ForeignKey(User, verbose_name='Account', on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=140, null=True, blank=True)
    image = models.ImageField(verbose_name="Tweet Picture", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def _str_(self):
        return str(self.tweet_text)


# you can extend the User model like this example. It is just for an example.
class UserProfilePicture:
    user = models.ForeignKey(User, verbose_name='Account', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Profile Picture", null=True, blank=True)

    def _str_(self):
        return str(self.user)
