# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examv3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]
