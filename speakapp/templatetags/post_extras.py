from django import template
register = template.Library()
from speakapp.models import Post


@register.filter(name='is_backer')
def is_backer(value, arg):
	return Post.objects.filter(pk=value).filter(backers=arg).exists()
	