# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('number_of_pets', models.IntegerField()),
            ],
        ),
    ]