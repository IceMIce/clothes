# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clothNo', models.CharField(max_length=20)),
                ('generNo', models.CharField(max_length=20)),
                ('clothName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cusNo', models.AutoField(serialize=False, primary_key=True)),
                ('cusName', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
                ('sign', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gener',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('generNo', models.CharField(max_length=20)),
                ('generName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('managerNo', models.AutoField(serialize=False, primary_key=True)),
                ('managerName', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderNo', models.CharField(max_length=20)),
            ],
        ),
    ]
