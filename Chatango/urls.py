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
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'accounts.views.login_view'),
    url(r'^chats', include('chats.urls', namespace='chats')),
    url(r'^accounts', include("accounts.urls")),
    url(r'^users/(?P<username>\w{0,30})/$', 'chats.views.users'),
    url(r'^$', 'chats.views.index'),
    url(r'^users/$', 'chats.views.users'),
    url(r'^logout$', 'accounts.views.logout_view'),
    url(r'^register$', 'accounts.views.register'),
    url(r'^profiles$', 'chats.views.profiles', name='profiles'),
    url(r'^follow$', 'chats.views.follow'),
    url(r'^public$', 'chats.views.public'),
    url(r'^submit$', 'chats.views.submit'),
    url(r'^follow$', 'chats.views.follow'),
    url(r'^userloc$', 'locator.views.userloc'),
    url(r'^savelocation$', 'locator.views.savelocation'),
    url(r'^usermap$', 'locator.views.usermap'),
    url(r'^friends$', 'chats.views.friends'),
    url(r'^private$', 'chats.views.private'),
    url(r'^send$', 'chats.views.send_private'),
    url(r'^check$', 'chats.views.check_private'),
    url(r'^following$', 'chats.views.following'),
    url(r'^followers$', 'chats.views.followers'),
]
if settings.DEBUG:
   urlpatterns +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += patterns('django.contrib.staticfiles.views',
#        url(r'^static/(?P<path>.*)$', 'serve'),
#    )
