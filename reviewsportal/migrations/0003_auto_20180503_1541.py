# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-03 15:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsportal', '0002_auto_20180503_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviewsportal.Company'),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]