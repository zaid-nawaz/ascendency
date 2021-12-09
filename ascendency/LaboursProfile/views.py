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
    user_followers_count = len(logged_in_user.user_followers.all())
    user_following_count = len(logged_in_user.user_following.all())
    context = {
        'user_id':logged_in_user.id,
        'user_name':logged_in_user.name,
        'user_followers_count': user_followers_count,
        'user_following_count': user_following_count,
        'show_unfollow_button' : False,
        'logged_in_profile': True 
        
    }
    return render(request, 'LaboursProfile/profile_page.html',context)
    
def search_user(request):
    searched_user_name = request.POST['search_field']
    all_users = Labourinfo.objects.all()
    search_result_users = []
    for people in all_users:
        if searched_user_name.lower() in people.name.lower():
            search_result_users.append(people)

    context = {
        'search_results' : search_result_users
    }

    return render(request, 'LaboursProfile/search_page.html',context)
    
def profile_visit(request):
    user_name = request.GET['username']
    user_id = request.GET['id']
    name = request.session['logged_in_user_name']
    password = request.session['logged_in_user_password']
    logged_in_user = Labourinfo.objects.filter(name=name , password=password)[0]
    particular_user = Labourinfo.objects.filter(name=user_name,id=user_id)[0]
    
    if particular_user in logged_in_user.user_following.all():
        show_unfollow_button = True
    else:
        show_unfollow_button = False
    part_user_followers_count = len(particular_user.user_followers.all())
    part_user_following_count = len(particular_user.user_following.all())
    context = {
        'user_id':particular_user.id,
        'user_name':particular_user.name,
        'user_followers_count': part_user_followers_count,
        'user_following_count': part_user_following_count,
        'show_unfollow_button' : show_unfollow_button,
        
    }
    
    return render(request, 'LaboursProfile/profile_page.html',context)


def follow_view(request):
    user_name = request.GET['username']
    user_id = request.GET['id']
    name = request.session['logged_in_user_name']
    password = request.session['logged_in_user_password']
    logged_in_user = Labourinfo.objects.filter(name=name , password=password)[0]
    particular_user = Labourinfo.objects.filter(name=user_name,id=user_id)[0]
   
    logged_in_user.user_following.add(particular_user)
    particular_user.user_followers.add(logged_in_user)
    part_user_followers_count = len(particular_user.user_followers.all())
    part_user_following_count = len(particular_user.user_following.all())
    context = {
        'user_id':particular_user.id,
        'user_name':particular_user.name,
        'user_followers_count': part_user_followers_count,
        'user_following_count': part_user_following_count,
        'show_unfollow_button' : True,
        
    }
    return render(request, 'LaboursProfile/profile_page.html',context)


def unfollow_view(request):
    user_name = request.GET['username']
    user_id = request.GET['id']
    name = request.session['logged_in_user_name']
    password = request.session['logged_in_user_password']
    logged_in_user = Labourinfo.objects.filter(name=name , password=password)[0]
    particular_user = Labourinfo.objects.filter(name=user_name,id=user_id)[0]
    logged_in_user.user_following.remove(particular_user)
    particular_user.user_followers.remove(logged_in_user)
    part_user_followers_count = len(particular_user.user_followers.all())
    part_user_following_count = len(particular_user.user_following.all())
    context = {
        'user_id':particular_user.id,
        'user_name':particular_user.name,
        'user_followers_count': part_user_followers_count,
        'user_following_count': part_user_following_count,
        'show_unfollow_button' : False,

    }
    return render(request, 'LaboursProfile/profile_page.html',context)