# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0007_auto_20170925_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='sphone',
        ),
        migrations.AlterField(
            model_name='member',
            name='pphone',
            field=models.CharField(blank=True, default=' ', max_length=10),
        ),
    ]