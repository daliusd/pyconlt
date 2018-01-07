# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 20:44
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presenters', '0002_auto_20171210_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenter',
            name='expertise',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, null=True), blank=True, help_text="Speaker's skills and areas of expertise", null=True, size=None),
        ),
    ]
