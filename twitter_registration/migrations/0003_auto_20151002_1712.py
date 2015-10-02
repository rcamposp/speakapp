# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_registration', '0002_auto_20150930_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='twitter_id',
            field=models.BigIntegerField(),
        ),
    ]
