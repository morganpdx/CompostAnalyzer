# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-03 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compost_bin', '0002_auto_20161203_2133'),
        ('compost_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compostuser',
            name='compost_bins',
            field=models.ManyToManyField(to='compost_bin.CompostBin'),
        ),
    ]