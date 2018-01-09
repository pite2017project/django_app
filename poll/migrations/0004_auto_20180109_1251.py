# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 11:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_poll_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
