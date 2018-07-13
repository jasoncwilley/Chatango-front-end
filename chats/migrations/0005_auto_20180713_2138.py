# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20180711_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', verbose_name=b'user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='spam',
            name='content',
            field=models.CharField(max_length=140, verbose_name=b'Message'),
        ),
        migrations.AlterField(
            model_name='spam',
            name='subject',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='spam',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
