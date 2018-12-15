# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('ip_address', models.GenericIPAddressField(null=True, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=16, decimal_places=10, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=10, decimal_places=10, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
