from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_location_for_new_user(sender, created, instance, **kwargs):
        if created:
            location = Location(user=instance)
            location.save()



    User.location = property(lambda u: Location.objects.get_or_create(user=u)[0])
