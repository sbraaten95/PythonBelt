# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_poked'),
        ('poke', '0003_auto_20160925_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Poker', to='login.User'),
            preserve_default=False,
        ),
    ]
