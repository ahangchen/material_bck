# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng', '0005_auto_20160222_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='assistant',
            field=models.CharField(default='no_name', max_length=50),
        ),
        migrations.AddField(
            model_name='apply',
            name='record_day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apply',
            name='record_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apply',
            name='record_year',
            field=models.IntegerField(default=0),
        ),
    ]