# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-27 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0008_auto_20180629_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headgear',
            name='owner',
        ),
        migrations.AddField(
            model_name='aura',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='background',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='weapon',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Headgear',
        ),
    ]
