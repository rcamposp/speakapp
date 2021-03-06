from django.db import models
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class TwitterUser(models.Model):
	user = models.OneToOneField(User, related_name='twitter_user')
	twitter_id = models.BigIntegerField()
	access_token = models.CharField(max_length=200)
	access_token_secret = models.CharField(max_length=200)
	