from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^users/(?P<username>\w{0,30})/$', 'chats.views.users'),
    url(r'^$', 'chats.views.index'),
    url(r'^users/$', 'chats.views.users'),
    url(r'^profiles$', 'chats.views.profiles', name='profiles'),
    url(r'^follow$', 'chats.views.follow'),
    url(r'^public$', 'chats.views.public'),
    url(r'^submit$', 'chats.views.submit'),
    url(r'^follow$', 'chats.views.follow'),
    url(r'^friends$', 'chats.views.friends'),
]
