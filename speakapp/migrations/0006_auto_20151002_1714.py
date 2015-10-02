# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakapp', '0005_auto_20150930_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(to='speakapp.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(to='speakapp.Location'),
        ),
    ]
