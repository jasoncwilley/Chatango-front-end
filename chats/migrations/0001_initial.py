# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Spam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='sender')),
                ('content', models.TextField(max_length=140, verbose_name='Content')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='SpamTimeStamp')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='FirstName')),
                ('lname', models.CharField(max_length=50, verbose_name='LastName')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('phone', models.CharField(default=None, blank=True, null=True, max_length=20, verbose_name='Phone number')),
                ('dateofbirth', models.DateField(default=None, blank=True, null=True, verbose_name='DateofBirth')),
                ('last_connection', models.DateTimeField(default=None, blank=True, null=True, verbose_name='DateofLastConnection')),
                ('email', models.EmailField(null=True, max_length=254, verbose_name='Email')),
                ('datecreated', models.DateTimeField(auto_now_add=True, verbose_name='datecreated')),
                ('image', models.FileField(upload_to='', default=None, blank=True, null=True)),
                ('follows', models.ManyToManyField(to='chats.UserProfile', blank=True, null=True, related_name='followed_by')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
