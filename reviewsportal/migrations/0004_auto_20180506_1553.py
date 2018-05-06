# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-06 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsportal', '0003_auto_20180503_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='mentorship_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='personal_growth_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='work_life_balance_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
