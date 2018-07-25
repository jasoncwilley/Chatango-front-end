# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0007_auto_20180725_0804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatespam',
            name='follows',
        ),
        migrations.AddField(
            model_name='privatespam',
            name='username',
            field=models.ForeignKey(related_name='reciever', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
