# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0002_auto_20180722_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='ip_address',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
