# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20180705_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spam',
            name='sender',
            field=models.CharField(max_length=50, verbose_name='sender'),
        ),
    ]
