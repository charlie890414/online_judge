# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0009_merge_20171001_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='imgUrl',
            field=models.CharField(default='https://images.unsplash.com/photo-1484788984921-03950022c9ef?dpr=1&auto=compress,format&fit=crop&w=2004&h=&q=80&cs=tinysrgb&crop=', max_length=1000),
        ),
    ]
