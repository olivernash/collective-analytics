# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_analysis_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='included_in_analysis',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]