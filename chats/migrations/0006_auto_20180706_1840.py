# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0005_auto_20180706_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spam',
            name='username',
        ),
        migrations.AddField(
            model_name='spam',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=None),
        ),
    ]
