# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0029_remove_sensor_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawdata',
            name='parsed',
        ),
    ]
