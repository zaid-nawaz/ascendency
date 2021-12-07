# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from labours.models import Labourinfo
# Create your views here.
def index_page(request):
    return render(request, 'LaboursProfile/index_page.html')


def profile_page(request):
    logged_in_user_name = request.session['logged_in_user_name']
    logged_in_user_password = request.session['logged_in_user_password']
    logged_in_user = Labourinfo.objects.filter(name=logged_in_user_name, password=logged_in_user_password)[0]
    user_followers_count = len(logged_in_user.followers.all())
    user_following_count = len(logged_in_user.following.all())
    context = {
        'user_name':logged_in_user.name,
        'user_followers_count': user_followers_count,
        'user_following_count': user_following_count,
    }
    return render(request, 'LaboursProfile/profile_page.html',context)
    
