# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('volume', models.IntegerField(default=0)),
                ('site', models.CharField(max_length=50)),
                ('listUrl', models.CharField(max_length=150)),
                ('watchUrl', models.CharField(max_length=150)),
                ('imgUrl', models.CharField(max_length=150)),
                ('imgSrc', models.CharField(max_length=150)),
                ('subscribe', models.BooleanField()),
                ('ended', models.BooleanField()),
            ],
        ),
    ]
