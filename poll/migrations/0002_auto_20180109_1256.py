# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='publication_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='publication_date'),
        ),
    ]
