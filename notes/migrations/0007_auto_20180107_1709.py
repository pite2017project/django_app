# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20180107_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='classes',
            new_name='course',
        ),
    ]