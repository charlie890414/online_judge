# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_auto_20170915_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='lang',
            field=models.CharField(default='', max_length=15),
        ),
    ]
