from django.db import models
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	
	def __str__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=200,null=False, blank=False)
	parent = models.OneToOneField('self', null=True, blank=True)
	
	def __str__(self):
		return self.name

class Post(models.Model):
	message 	= models.TextField(null=False, blank=False)
	author 		= models.ForeignKey(User)
	category 	= models.ForeignKey(Category, null=False, blank=False)
	location 	= models.ForeignKey(Location, null=False, blank=False)	
	backers 	= models.ManyToManyField(User, related_name="backers",null=True, blank=True)
	opposers 	= models.ManyToManyField(User, related_name="opposers", null=True, blank=True)
	twitter_accounts = models.CharField(max_length=200)	
	
	def __str__(self):
		return self.message

