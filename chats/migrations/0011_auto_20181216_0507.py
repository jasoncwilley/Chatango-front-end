# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0010_auto_20181215_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='datecreated',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='profile',
            name='address1',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='address2',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(verbose_name='Bio', max_length=500, default=datetime.datetime(2018, 12, 16, 5, 7, 1, 349427, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=25, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(null=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone1',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone2',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone3',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=2, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='zipcode',
            field=models.IntegerField(null=True),
        ),
    ]
