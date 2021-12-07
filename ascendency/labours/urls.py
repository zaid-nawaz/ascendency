from django.conf.urls import url , include
from django.contrib import admin
from labours import views

app_name = 'labours'
urlpatterns = [

    url(r'^login/', views.login_page, name='login_page'),
    url(r'^signup/', views.signup_page, name='signup_page'),
    url(r'^logout/', views.logout_page, name='logout_page'),
    


]