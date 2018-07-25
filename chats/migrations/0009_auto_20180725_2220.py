# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0008_auto_20180725_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatespam',
            name='user',
            field=models.ForeignKey(related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
