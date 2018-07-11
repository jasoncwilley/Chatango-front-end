from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [

    #url(r'^update/$', views.update, name='update'),
    url(r'profiles', views.profiles, name='profiles'),
    url(r'^public$', views.public, name='public'),
    url(r'^register$', views.register, name='register'),
    url(r'^home$', views.home, name='home'),
    url(r'^buddies$', views.users, name='buddies'),
    url(r'^viewprofile/(?P<profile_id>\d+)/$', views.viewprofile, name='viewprofile'),
    url(r'^profileform$', views.update),
    url(r'^follow$', views.follow),

]
