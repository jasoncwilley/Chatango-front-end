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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('content', models.TextField(max_length=140, verbose_name='Content')),
                ('timestamp', models.DateTimeField(verbose_name='SpamTimeStamp')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fname', models.CharField(max_length=50, verbose_name='FirstName')),
                ('lname', models.CharField(max_length=50, verbose_name='LastName')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('phone', models.CharField(max_length=20, blank=True, verbose_name='Phone number', default=None, null=True)),
                ('dateofbirth', models.DateField(blank=True, verbose_name='DateofBirth', default=None, null=True)),
                ('last_connection', models.DateTimeField(blank=True, verbose_name='DateofLastConnection', default=None, null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('datecreated', models.DateField(auto_now_add=True, verbose_name='datecreated')),
                ('follows', models.ManyToManyField(related_name='followed_by', blank=True, to='chats.UserProfile', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='spam',
            name='username',
            field=models.ForeignKey(to='chats.UserProfile'),
        ),
    ]
