# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-03 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compost_bin', '0003_auto_20161203_2217'),
        ('compost_sensor', '0002_auto_20161203_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compostsensor',
            old_name='name',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='compostsensor',
            name='description',
        ),
        migrations.RemoveField(
            model_name='compostsensor',
            name='sensor_values',
        ),
        migrations.AddField(
            model_name='compostsensor',
            name='bin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compost_bin.CompostBin', verbose_name='the compost bin this sensor is in'),
        ),
    ]
