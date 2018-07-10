from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'accounts'


urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login_view),
    url(r'^logout$', views.logout_view)
]
