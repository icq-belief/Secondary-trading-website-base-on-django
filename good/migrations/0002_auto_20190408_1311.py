# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-08 05:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_time',
        ),
    ]