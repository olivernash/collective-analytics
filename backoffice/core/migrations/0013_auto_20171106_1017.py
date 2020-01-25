# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20171103_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParameterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='parameter',
            name='default_value',
            field=models.CharField(default='null', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='parameter_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.ParameterType'),
            preserve_default=False,
        ),
    ]
