from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'accounts'


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^profile/(?P<profile_id>\d+)/$', views.profile, name='profile'),
]
