# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-09 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0002_auto_20170208_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Historico')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.Dentist', verbose_name='Dentista')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consulta',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='patient',
            name='dentist',
        ),
        migrations.AddField(
            model_name='consultation',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.Patient', verbose_name='Nome'),
        ),
    ]
