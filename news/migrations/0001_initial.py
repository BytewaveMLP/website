# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 12:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[-.\\w]+$')])),
                ('publish', models.DateTimeField()),
                ('is_visible', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('intro', models.TextField()),
                ('readmore', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]