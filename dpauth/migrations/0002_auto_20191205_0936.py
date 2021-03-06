# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-05 09:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dpauth.utils


class Migration(migrations.Migration):

    dependencies = [
        ('dpauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='username',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=dpauth.utils.UploadNameFromContent('avatar/', 'avatar'), validators=[dpauth.utils.AvatarValidator(max_dims=(64, 64))]),
        ),
        migrations.AlterField(
            model_name='username',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawpilename_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
