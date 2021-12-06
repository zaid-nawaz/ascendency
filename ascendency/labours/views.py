# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
import random
import string
from labours.models import Labourinfo
# Create your views here.
def random_code_generator():
    length = 10
    code = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(length))
    return code


def login_page(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        authenticated_user = Labourinfo.objects.filter(name=user_name,password=user_password)
        if authenticated_user.exists():
            return HttpResponseRedirect(reverse('index_page'))
        else:
            context = {'logged_in':False}
        return render(request,'labours/login_page.html',context)
    return render(request,'labours/login_page.html')
        
    

def signup_page(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        invite_code = request.POST['invitation_code']
        user_invitation_code = Labourinfo.objects.filter(user_invitation_code=invite_code)
        if user_invitation_code.exists():
            Labourinfo.objects.create(name=user_name,password=user_password,user_invitation_code=random_code_generator())
            return HttpResponseRedirect(reverse('login_page'))
        else:
            context = {'signed_up':False}
            return render(request, 'labours/signup_page.html',context)
    return render(request, 'labours/signup_page.html')

def temp_index(request):
    return HttpResponse('this is the temporary index page.')