from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
    fname = models.CharField(max_length=50, verbose_name="FirstName")
    lname = models.CharField(max_length=50, verbose_name="LastName")
    username = models.CharField(max_length=50, verbose_name="Username")
    password = models.CharField(max_length=100, verbose_name="Password")
    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
    dateofbirth = models.DateField(verbose_name="DateofBirth" , null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="DateofLastConnection", null=True, default=None, blank=True)
    email = models.EmailField(verbose_name="Email")
    datecreated = models.DateTimeField(verbose_name="datecreated",auto_now_add=True)
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', null=True, related_name='followed_by', blank=True, symmetrical=False)




class Spam(models.Model):
    username = models.ForeignKey(UserProfile, null=True, blank=True)
    sender = models.CharField(max_length=50, verbose_name="sender")
    content = models.TextField(max_length=140, verbose_name="Content")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="SpamTimeStamp")
