# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='poked',
            field=models.BooleanField(default=0),
        ),
    ]