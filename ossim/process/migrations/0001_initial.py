# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-22 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessSchedAlg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('demourl', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='adv',
            name='alg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.ProcessSchedAlg'),
        ),
    ]
