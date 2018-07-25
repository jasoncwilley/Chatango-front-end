from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'accounts'


urlpatterns = [
    url(r'^login$', 'accounts.views.login_view'),
    url(r'^logout$', 'accounts.views.logout_view'),
    url(r'^register$', 'accounts.views.register'),
]
