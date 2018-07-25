from django.conf.urls import include, url
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^userloc$', 'locator.views.userloc'),
    url(r'^savelocation$', 'locator.views.savelocation'),
    url(r'^usermap$', 'locator.views.usermap'),

]
