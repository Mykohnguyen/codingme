# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-30 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0012_auto_20180829_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='gold',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
