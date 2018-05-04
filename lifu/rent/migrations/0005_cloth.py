# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_auto_20180429_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clothName', models.CharField(max_length=50)),
                ('price', models.CharField(default=b'', max_length=50)),
                ('color', models.CharField(default=b'', max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('count', models.CharField(max_length=50)),
                ('orderState', models.CharField(max_length=20)),
            ],
        ),
    ]
