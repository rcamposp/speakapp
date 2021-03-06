"""speakapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from . import views 


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'), 
    url(r'^list', views.list, name='list'),
    url(r'^campaing/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^add', views.add, name='add'),
    url(r'^agree', views.agree, name='agree'),
    url(r'^disagree', views.disagree, name='disagree'),
    url(r'^parseJson', views.parseJson, name='parseJson'),    
    #url(r'^auth', views.twitterAuthenticate),
    url(r'^register/', include('twitter_registration.urls', namespace="twitter_registration")),    
]
