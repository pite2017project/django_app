# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_auto_20180109_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='user',
        ),
    ]
