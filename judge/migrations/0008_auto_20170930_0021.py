# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import judge.models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0007_auto_20170930_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='test',
            field=models.FileField(blank=True, null=True, upload_to=judge.models.generate_questionfiletest),
        ),
    ]