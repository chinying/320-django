# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-03 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
    ]
