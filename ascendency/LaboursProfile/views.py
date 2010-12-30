# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django import http


from django.shortcuts import render, HttpResponseRedirect , redirect
import datetime
from django.http import HttpResponse

from labours.models import Labourinfo , Labourpost
from django.urls import reverse
from django.utils import timezone
import threading

# Create your views here.
def index_page(request):
    logged_in_user_name = request.session['logged_in_user_name']
    logged_in_user_password = request.session['logged_in_user_password']
    logged_in_user = Labourinfo.objects.filter(name=logged_in_user_name, password=logged_in_user_password)
    if logged_in_user.exists():
        return render(request, 'LaboursProfile/index_page.html')
    else:
        return render(request,'labours/login_page.html')

def updation(followers_count):
    if followers_count >= 1000 and followers_count < 10000:
        return 2
    elif followers_count >= 10000 and followers_count < 100000:
        return 4
    elif followers_count >= 100000 and followers_count< 1000000:
        return 10
    elif followers_count > 1000000:
        return 'infinity'
    else:
        return 1

def post_count_renewal():
    allobj = Labourinfo.objects.all()
    while True:
        for i in allobj:
            i.user_post_count = i.max_post_count
            i.save()
            if updation(len(i.user_followers.all())) == 1:
                i.user_post_count = 1
                i.max_post_count = 1
                i.save()
            elif updation(len(i.user_followers.all())) == 2:
                i.user_post_count = 2
                i.max_post_count = 2
                i.save()
            elif updation(len(i.user_followers.all())) == 4:
                i.user_post_count = 4
                i.max_post_count = 4
                i.save()
            elif updation(len(i.user_followers.all())) == 10:
                i.user_post_count = 10
                i.max_post_count = 10
                i.save()
            elif updation(len(i.user_followers.all())) == 'infinity':
                i.user_post_count = 1000000
                i.max_post_count = 1000000
                i.save()
        print('zaid')
        time.sleep(86400)
   



def profile_page(request):
    logged_in_user_name = request.session['logged_in_user_name']
    logged_in_user_password = request.session['logged_in_user_password']
    logged_in_user = Labourinfo.objects.filter(name=logged_in_user_name, password=logged_in_user_password)[0]
    user_followers_count = len(logged_in_user.user_followers.all())
    user_following_count = len(logged_in_user.user_following.all())
    user_profile_picture = logged_in_user.profile_picture

    user_post_images = Labourpost.objects.filter(labourer=logged_in_user).order_by('-published_date')
    context = {
        'user_id':logged_in_user.id,
        'user_name':logged_in_user.name,
        'user_followers_count': user_followers_count,
        'user_following_count': user_following_count,
        'show_unfollow_button' : False,
        'logged_in_profile': True,
        'user_post_images' : user_post_images,
        'user_profile_picture':user_profile_picture,
        
    }
    
    return render(request, 'LaboursProfile/profile_page.html',context)
    
def search_user(request):
    searched_user_name = request.POST['search_field']
    all_users = Labourinfo.objects.all()
    search_result_users = []
    for people in all_users:
        if searched_user_name.lower() in people.name.lower():
            search_result_users.append(people)

    name = request.session['logged_in_user_name']
    password = request.session['logged_in_user_password']
    logged_in_user = Labourinfo.objects.filter(name=name , password=password)[0]

    if logged_in_user in search_result_users:
        search_result_users.remove(logged_in_user)

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
    user_profile_picture = particular_user.profile_picture
    
    if particular_user in logged_in_user.user_following.all():
        show_unfollow_button = True
    else:
        show_unfollow_button = False
    part_user_followers_count = len(particular_user.user_followers.all())
    part_user_following_count = len(particular_user.user_following.all())
    particular_user_posts = Labourpost.objects.filter(labourer=particular_user).order_by('-published_date')

    context = {
        'user_id':particular_user.id,
        'user_name':particular_user.name,
        'user_followers_count': part_user_followers_count,
        'user_following_count': part_user_following_count,
        'show_unfollow_button' : show_unfollow_button,
        'particular_user_posts' : particular_user_posts,
        'user_profile_picture': user_profile_picture,
        
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
    particular_user_posts = Labourpost.objects.filter(labourer=particular_user).order_by('-published_date')
    user_profile_picture = particular_user.profile_picture
    context = {
        'user_id':particular_user.id,
        'user_name':particular_user.name,
        'user_followers_count': part_user_followers_count,
        'user_following_count': part_user_following_count,
        'show_unfollow_button' : True,
        'particular_user_posts' : particular_user_posts,
        'user_profile_picture': user_profile_picture,
        
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
    particular_user_posts = Labourpost.objects.filter(labourer=particular_user).order_by('-published_date')
    user_profile_picture = particular_user.profile_picture
    context = {
        'user_id':particular_user.id,
        'user_name':particular_user.name,
        'user_followers_count': part_user_followers_count,
        'user_following_count': part_user_following_count,
        'show_unfollow_button' : False,
        'particular_user_posts' : particular_user_posts,
        'user_profile_picture': user_profile_picture,

    }
    return render(request, 'LaboursProfile/profile_page.html',context)

def less_than_thousand_followers(logged_in_user):
    if len(logged_in_user.user_followers.all()) < 1000:
        return True
    else:
        return False
    

def post_page(request):
    if request.method == 'POST':
        
        name = request.session['logged_in_user_name']
        password = request.session['logged_in_user_password']
        logged_in_user = Labourinfo.objects.filter(name=name , password=password)[0]
        post_image = request.FILES['labour_post']

        # i am taking the latest post of the user and by writing this code
        user_post_images = Labourpost.objects.filter(labourer=logged_in_user).order_by('-published_date')
        if user_post_images.exists():

            latest_post = user_post_images[0]

            # i am converting the today's date and published date of the latest post in certain string format to subtract it later

            # strftime helps me to achieve that 

            s1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            s2 = latest_post.published_date.strftime("%Y-%m-%d %H:%M:%S")

            timeformat  = "%Y-%m-%d %H:%M:%S"

            # now i am converting it back to datetime object to subtract it and get the time difference with the help of strptime function 

            delta = datetime.datetime.strptime(s1, timeformat) - datetime.datetime.strptime(s2, timeformat)

            # i am checking if the last post in the span of a day , then i wont let the user upload another post.
        
            if delta.total_seconds() < 86400 and less_than_thousand_followers(logged_in_user):
        
            
                print('cant let you post.')
            else:
                if logged_in_user.user_post_count > 0:
                    Labourpost.objects.create(labourer=logged_in_user, labour_image=post_image)
                    logged_in_user.user_post_count = logged_in_user.user_post_count - 1 
                    logged_in_user.save()
                else:
                    print('sorry cant let you post')

        else:
            Labourpost.objects.create(labourer=logged_in_user, labour_image=post_image)
            logged_in_user.user_post_count = logged_in_user.user_post_count - 1 
            logged_in_user.save()
 
        return HttpResponseRedirect(reverse('LaboursProfile:profile_page'))

t = threading.Thread(target=post_count_renewal)
t.start()
   
    