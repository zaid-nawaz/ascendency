from django.conf.urls import url , include
from django.contrib import admin
from labours import views
urlpatterns = [

    url(r'^login/', views.login_page, name='login_page'),
    url(r'^signup/', views.signup_page, name='signup_page'),
    url(r'tempindexpage/',views.temp_index, name='index_page'),


]