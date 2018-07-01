# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='\u8bf7\u8f93\u5165\u540d\u5b57')),
                ('content', models.CharField(max_length=200)),
                ('kind', models.CharField(choices=[('python', 'python'), ('java', 'java'), ('script', 'script'), ('android', 'android'), ('else', 'else')], default=('python', 'python'), max_length=20)),
            ],
            options={
                'db_table': 'Moment',
            },
        ),
    ]
