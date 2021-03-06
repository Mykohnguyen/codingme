# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-24 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0003_auto_20180523_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('correct', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('difficult', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='one.Question'),
        ),
    ]
