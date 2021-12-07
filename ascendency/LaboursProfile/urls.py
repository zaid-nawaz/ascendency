from django.conf.urls import url , include
from django.contrib import admin
from LaboursProfile import views
app_name = 'LaboursProfile'

urlpatterns = [
   
    url(r'^$',views.index_page , name='index_page'),
    url(r'^profile/', views.profile_page, name='profile_page' ),
    
    
    
]