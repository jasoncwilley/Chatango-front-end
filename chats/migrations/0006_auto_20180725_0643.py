# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0005_auto_20180713_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateSpam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('reciever', models.ForeignKey(related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', verbose_name=b'User', to=settings.AUTH_USER_MODEL),
        ),
    ]
