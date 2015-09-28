# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitteruser',
            name='user',
        ),
        migrations.DeleteModel(
            name='twitterUser',
        ),
    ]
