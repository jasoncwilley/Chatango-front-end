# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_auto_20180725_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatespam',
            name='reciever',
        ),
        migrations.AddField(
            model_name='privatespam',
            name='follows',
            field=models.ForeignKey(related_name='reciever', to='chats.Profile', null=True),
        ),
    ]
