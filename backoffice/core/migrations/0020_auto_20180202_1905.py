# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-02 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20171220_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]