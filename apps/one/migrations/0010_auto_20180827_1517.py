# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-27 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0009_auto_20180827_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aura',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='background',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]