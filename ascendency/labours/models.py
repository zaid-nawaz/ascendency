# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Labourinfo(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_invitation_code = models.CharField(max_length=100)
    followers = models.ManyToManyField('self',blank=True, null=True)
    following = models.ManyToManyField('self', blank=True, null=True)

    def __str__(self):
        return self.name
    