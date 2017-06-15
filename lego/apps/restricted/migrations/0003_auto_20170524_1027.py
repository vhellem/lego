# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 10:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restricted', '0002_restrictedmail_hide_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restrictedmail',
            name='events',
            field=models.ManyToManyField(blank=True, to='events.Event'),
        ),
        migrations.AlterField(
            model_name='restrictedmail',
            name='groups',
            field=models.ManyToManyField(blank=True, to='users.AbakusGroup'),
        ),
        migrations.AlterField(
            model_name='restrictedmail',
            name='meetings',
            field=models.ManyToManyField(blank=True, to='meetings.Meeting'),
        ),
        migrations.AlterField(
            model_name='restrictedmail',
            name='token',
            field=models.CharField(db_index=True, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='restrictedmail',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]