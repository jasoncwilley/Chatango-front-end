"""Chatango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from chats import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^chats/', include('chats.urls', namespace='chats')),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^users/(?P<username>\w{0,30})/$', 'chats.views.users'),
    url(r'^$', 'chats.views.index'),

]
if settings.DEBUG:
    urlpatterns +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
