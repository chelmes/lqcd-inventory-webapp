# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lqcd_inventory', '0002_auto_20161108_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eigensystem',
            name='comment',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='perambulator',
            name='comment',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='storage',
            name='account',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
