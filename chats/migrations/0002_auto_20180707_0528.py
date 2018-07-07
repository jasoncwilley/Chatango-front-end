# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('fname', models.CharField(verbose_name='FirstName', max_length=50)),
                ('lname', models.CharField(verbose_name='LastName', max_length=50)),
                ('username', models.CharField(verbose_name='Username', max_length=50)),
                ('phone', models.CharField(default=None, blank=True, null=True, max_length=20, verbose_name='Phone number')),
                ('dateofbirth', models.DateField(default=None, blank=True, null=True, verbose_name='DateofBirth')),
                ('last_connection', models.DateTimeField(default=None, blank=True, null=True, verbose_name='DateofLastConnection')),
                ('email', models.EmailField(null=True, max_length=254, verbose_name='Email')),
                ('datecreated', models.DateTimeField(verbose_name='datecreated', auto_now_add=True)),
                ('image', models.FileField(default=None, blank=True, null=True, upload_to='')),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', null=True, to='chats.Profile')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='follows',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
