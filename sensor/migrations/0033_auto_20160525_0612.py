# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0032_auto_20160524_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawdata',
            name='status',
            field=models.IntegerField(choices=[(0, b'Valid'), (1, b'Invalid key'), (2, b'Format error in value'), (3, b'Value out of range'), (4, b'Invalid sensor ID'), (5, b'Sensor offline')], default=0),
        ),
    ]
