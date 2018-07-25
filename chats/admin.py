from django.contrib import admin
from . models import Profile, Spam, PrivateSpam
admin.site.register(Profile)
admin.site.register(Spam)
admin.site.register(PrivateSpam)
