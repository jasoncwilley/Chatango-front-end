# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20180705_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spam',
            name='timestamp',
            field=models.DateTimeField(verbose_name='SpamTimeStamp', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='datecreated',
            field=models.DateTimeField(verbose_name='datecreated', auto_now_add=True),
        ),
    ]
