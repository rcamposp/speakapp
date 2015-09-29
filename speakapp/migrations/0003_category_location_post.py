# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('speakapp', '0002_auto_20150928_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('parent', models.OneToOneField(blank=True, to='speakapp.Location', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('message', models.TextField()),
                ('twitter_accounts', models.CharField(max_length=200)),
                ('author', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('backers', models.ManyToManyField(related_name='backers', to=settings.AUTH_USER_MODEL)),
                ('category', models.OneToOneField(to='speakapp.Category')),
                ('location', models.OneToOneField(to='speakapp.Location')),
                ('opposers', models.ManyToManyField(related_name='opposers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
