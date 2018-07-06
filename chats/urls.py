from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [

    #url(r'^$' views.index name='index'),
    url(r'profiles', views.profiles, name='profiles'),
    #url(r'^chats$' include('chats.urls'))
    url(r'profile-(?P<pk>\d+)$', 'chats.views.profile', name="profile"),
    url(r'^register$', views.register, name='register'),
    
]
