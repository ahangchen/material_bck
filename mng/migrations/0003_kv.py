# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng', '0002_remove_applytime_part'),
    ]

    operations = [
        migrations.CreateModel(
            name='KV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_key', models.CharField(max_length=100)),
                ('set_value', models.CharField(max_length=200)),
            ],
        ),
    ]