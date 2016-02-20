# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weatherSentiment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('sentiment', models.FloatField()),
                ('datetime', models.DateTimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='weatherSentiment.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wind', models.CharField(max_length=200)),
                ('precipitation', models.CharField(max_length=200)),
                ('temperature', models.FloatField()),
                ('weather', models.CharField(max_length=200)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='weatherSentiment.Location')),
            ],
        ),
    ]
