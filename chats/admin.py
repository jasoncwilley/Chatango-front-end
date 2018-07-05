from django.contrib import admin
from . models import UserProfile, Spam
admin.site.register(UserProfile)
admin.site.register(Spam)
