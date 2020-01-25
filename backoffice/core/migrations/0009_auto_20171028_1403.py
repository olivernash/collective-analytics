# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_attribute_included_in_analysis'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Algorithm',
            new_name='AnalysisType',
        ),
        migrations.RenameField(
            model_name='analysis',
            old_name='algorithm',
            new_name='analysis_type',
        ),
        migrations.RenameField(
            model_name='analysistype',
            old_name='algorithm_name',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='attribute',
            old_name='attribute_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='dataset',
            old_name='dataset_file',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='dataset',
            old_name='dataset_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='analysis',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]