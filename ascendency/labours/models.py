# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Labourinfo(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_invitation_code = models.CharField(max_length=100)
    followers = models.ManyToManyField('self',symmetrical=False, blank=True, null=True,related_name='user_followers')
    following = models.ManyToManyField('self',symmetrical=False, blank=True, null=True,related_name='user_following')
    
    def __str__(self):
        return self.name
    