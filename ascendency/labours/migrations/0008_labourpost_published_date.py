# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-11 13:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labours', '0007_auto_20211211_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourpost',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
