# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 23:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fridge_app', '0003_auto_20160630_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fridge',
            old_name='user',
            new_name='user_id',
        ),
    ]
