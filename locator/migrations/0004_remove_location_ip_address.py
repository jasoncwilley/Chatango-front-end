# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0003_auto_20181215_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='ip_address',
        ),
    ]
