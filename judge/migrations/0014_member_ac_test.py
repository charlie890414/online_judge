# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 14:03
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0013_auto_20171015_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='AC_test',
            field=jsonfield.fields.JSONField(blank=True),
        ),
    ]
