# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
                ('state_name', models.CharField(max_length=30)),
            ],
        ),
    ]
