# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-29 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0007_user_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Headgear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_aura',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_background',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_head',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_weapon',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='weapon',
            name='owner',
            field=models.ManyToManyField(related_name='weapons', to='one.User'),
        ),
        migrations.AddField(
            model_name='headgear',
            name='owner',
            field=models.ManyToManyField(related_name='headgears', to='one.User'),
        ),
        migrations.AddField(
            model_name='background',
            name='owner',
            field=models.ManyToManyField(related_name='backgrounds', to='one.User'),
        ),
        migrations.AddField(
            model_name='aura',
            name='owner',
            field=models.ManyToManyField(related_name='auras', to='one.User'),
        ),
    ]