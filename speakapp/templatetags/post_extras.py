from django import template
register = template.Library()
from speakapp.models import Post


@register.filter(name='is_backer')
def is_backer(value, arg):
	return Post.objects.filter(pk=value).filter(backers=arg).exists()
	
@register.filter(name='is_opposer')
def is_opposer(value, arg):
	return Post.objects.filter(pk=value).filter(opposers=arg).exists()

@register.filter(name='percentage_backers')
def percentage_backers(value, arg):
	if value+arg > 0:
		return int(value*100/(value+arg))
	else:
		return 0

@register.filter(name='clean_hashtag')
def clean_hashtag(value):
	return value.replace("#", "")