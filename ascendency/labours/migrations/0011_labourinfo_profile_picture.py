# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-13 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labours', '0010_labourinfo_max_post_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourinfo',
            name='profile_picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]