# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2010-12-31 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labours', '0008_labourpost_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourinfo',
            name='user_post_count',
            field=models.IntegerField(default=1),
        ),
    ]
