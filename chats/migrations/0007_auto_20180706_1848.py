# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_auto_20180706_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spam',
            old_name='sender',
            new_name='subject',
        ),
    ]
