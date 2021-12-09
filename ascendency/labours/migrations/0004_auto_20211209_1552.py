# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-09 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labours', '0003_auto_20101231_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfollowing',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='userfollowing',
            name='following',
        ),
        migrations.AddField(
            model_name='labourinfo',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_followers', to='labours.Labourinfo'),
        ),
        migrations.AddField(
            model_name='labourinfo',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_following', to='labours.Labourinfo'),
        ),
        migrations.DeleteModel(
            name='userfollowing',
        ),
    ]
