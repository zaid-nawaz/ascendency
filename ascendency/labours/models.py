# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime
# Create your models here.
class Labourinfo(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_invitation_code = models.CharField(max_length=100)
    followers = models.ManyToManyField('self',symmetrical=False, blank=True, null=True,related_name='user_followers')
    following = models.ManyToManyField('self',symmetrical=False, blank=True, null=True,related_name='user_following')
    user_post_count = models.IntegerField(default=1)
    max_post_count = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

class Labourpost(models.Model):
    labourer = models.ForeignKey(Labourinfo,on_delete=models.CASCADE)
    labour_image = models.ImageField(upload_to='')
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    
