# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-03 21:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compost_bin', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompostType',
            new_name='CompostBin',
        ),
    ]
