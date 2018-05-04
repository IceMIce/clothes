# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0006_auto_20180430_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clothName', models.CharField(max_length=20)),
                ('count', models.CharField(max_length=20)),
                ('money', models.CharField(max_length=20)),
                ('daytime', models.CharField(max_length=20)),
                ('orderState', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('cusName', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='orderState',
        ),
    ]
