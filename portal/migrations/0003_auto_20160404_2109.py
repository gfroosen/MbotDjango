# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-04 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20160404_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='task_direction',
            field=models.CharField(max_length=200),
        ),
    ]
