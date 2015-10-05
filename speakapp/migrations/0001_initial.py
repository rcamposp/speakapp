# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('parent', models.OneToOneField(null=True, to='speakapp.Location', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('message', models.TextField()),
                ('twitter_accounts', models.CharField(max_length=200)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('backers', models.ManyToManyField(related_name='backers', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('category', models.ForeignKey(to='speakapp.Category')),
                ('location', models.ForeignKey(to='speakapp.Location')),
                ('opposers', models.ManyToManyField(related_name='opposers', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
    ]
