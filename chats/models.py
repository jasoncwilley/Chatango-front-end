from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import hashlib
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import datetime
class Profile(models.Model):
    bio = models.TextField(max_length=500, verbose_name="Bio")
    fname = models.CharField(max_length=50, verbose_name="FirstName")
    lname = models.CharField(max_length=50, verbose_name="LastName")
    username = models.CharField(max_length=50, verbose_name="Username")
    address1 = models.CharField(blank=True, null=True, max_length=50)
    address2 = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.IntegerField(null=True)
    phone1 = models.CharField(max_length=15, null=True, blank=True)
    phone2 = models.CharField(max_length=15, null=True, blank=True)
    phone3 = models.CharField(max_length=15, null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.datetime.now, null=True)
    dateofbirth = models.DateField(null=True, verbose_name="DateofBirth", default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="DateofLastConnection", null=True, default=None, blank=True)
    email = models.EmailField(null=True, verbose_name="Email")
    follows = models.ManyToManyField('self', blank=True, related_name='followed_by', symmetrical=False)
    user = models.OneToOneField(User,related_name="profile", verbose_name="User", on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username
    @receiver(post_save, sender=User)
    def create_profile_for_new_user(sender, created, instance, **kwargs):
        if created:
            profile = Profile(user=instance)
            profile.save()

class Spam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    content = models.CharField(verbose_name="Message")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['-timestamp']



User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


class PrivateSpam(models.Model):
     user = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
     username = models.ForeignKey(User, null=True, related_name="reciever", on_delete=models.CASCADE)
     subject = models.CharField(max_length=50)
     content = content = models.CharField(max_length=140)
     timestamp = models.DateTimeField(auto_now_add=True)
     class Meta:
        ordering = ['-timestamp']
