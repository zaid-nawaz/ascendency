# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2010-12-30 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labourinfo',
            name='followers',
        ),
        migrations.AddField(
            model_name='labourinfo',
            name='followers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_followers', to='labours.Labourinfo'),
        ),
        migrations.RemoveField(
            model_name='labourinfo',
            name='following',
        ),
        migrations.AddField(
            model_name='labourinfo',
            name='following',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to='labours.Labourinfo'),
        ),
    ]