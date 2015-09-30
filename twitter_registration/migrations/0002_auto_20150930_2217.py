# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='user',
            field=models.OneToOneField(related_name='twitter_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
