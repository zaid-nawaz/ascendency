from django.conf.urls import url , include
from django.contrib import admin
from LaboursProfile import views
app_name = 'LaboursProfile'

urlpatterns = [
   
    url(r'^$',views.index_page , name='index_page'),
    url(r'^profile/', views.profile_page, name='profile_page' ),
    url(r'^search/', views.search_user, name='search_page' ),
    url(r'^profileVisit/',views.profile_visit,name='profile_visit'),
    url(r'^followView/',views.follow_view,name='follow_view'),
    url(r'^unfollowView/',views.unfollow_view,name='unfollow_view'),
    url(r'^postPage/',views.post_page, name='post_page'),
    
    
]