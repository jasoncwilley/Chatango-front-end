from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import hashlib
class UserProfile(models.Model):
    fname = models.CharField(max_length=50, verbose_name="FirstName")
    lname = models.CharField(max_length=50, verbose_name="LastName")
    username = models.CharField(max_length=50, verbose_name="Username")
    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
    dateofbirth = models.DateField(null=True, verbose_name="DateofBirth", default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="DateofLastConnection", null=True, default=None, blank=True)
    email = models.EmailField(null=True, verbose_name="Email")
    datecreated = models.DateTimeField(verbose_name="datecreated",auto_now_add=True)
    follows = models.ManyToManyField('self', null=True, related_name='followed_by', blank=True, symmetrical=False)
    user = models.ForeignKey(User)
    image = models.FileField(null=True, blank=True, default=None)

    def __unicode__(self):
       return self.user.username

class Spam(models.Model):
    user = models.ForeignKey(User)
    subject = models.CharField(max_length=50, verbose_name="sender")
    content = models.TextField(max_length=140, verbose_name="Content")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="SpamTimeStamp")

    class Meta:
        ordering = ['-timestamp']

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
