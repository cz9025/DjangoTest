# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopp',
            name='ctime',
            field=models.DateTimeField(auto_now=True, max_length=30),
        ),
    ]