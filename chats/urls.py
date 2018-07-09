from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [

    url(r'^update/$', views.update, name='update'),
    url(r'profiles', views.profiles, name='profiles'),
    #url(r'^chats$' include('chats.urls'))
    url(r'profile/(?P<pk>\d+)$', views.get_user_profile),
    url(r'^register$', views.register, name='register'),
    url(r'^latestspam$', views.latestspam, name='latestspam'),
    url(r'^home$', views.home, name='home'),
    url(r'^buddies$', views.users, name='buddies'),
    url(r'^users/$', views.users),
    url(r'^users/(?P<username>\w{0,30})/$', views.get_user_profile,name='user_url' ),


]
