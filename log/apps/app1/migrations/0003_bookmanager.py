# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-22 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20191022_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
