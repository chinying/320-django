# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-06 16:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsportal', '0004_auto_20180506_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 5, 6, 16, 7, 4, 234527, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
