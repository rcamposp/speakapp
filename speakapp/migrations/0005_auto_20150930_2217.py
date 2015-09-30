# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('speakapp', '0004_auto_20150928_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='backers',
            field=models.ManyToManyField(related_name='backers', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='opposers',
            field=models.ManyToManyField(related_name='opposers', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
