from django import template
register = template.Library()
from speakapp.models import Post


@register.filter(name='is_backer')
def is_backer(value, arg):
	return Post.objects.filter(pk=value).filter(backers=arg).exists()
	
@register.filter(name='is_opposer')
def is_opposer(value, arg):
	return Post.objects.filter(pk=value).filter(opposers=arg).exists()