# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20170210_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ldap_password_hash',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]