# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20171210_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notefileimage',
            old_name='image',
            new_name='content',
        ),
    ]
