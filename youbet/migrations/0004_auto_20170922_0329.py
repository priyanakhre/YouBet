# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-22 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youbet', '0003_auto_20170922_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='bet',
        ),
        migrations.RemoveField(
            model_name='response',
            name='user',
        ),
        migrations.AddField(
            model_name='response',
            name='bet_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
