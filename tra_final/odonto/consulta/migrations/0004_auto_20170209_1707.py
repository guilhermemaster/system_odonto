# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-09 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_auto_20170209_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultation',
            options={'ordering': ['dentist'], 'verbose_name': 'Consulta', 'verbose_name_plural': 'Consulta'},
        ),
        migrations.AddField(
            model_name='consultation',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
