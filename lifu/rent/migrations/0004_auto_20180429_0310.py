# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_auto_20180429_0205'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'', max_length=50)),
                ('password', models.CharField(default=b'', max_length=20)),
                ('email', models.EmailField(default=b'', max_length=20)),
                ('name', models.CharField(default=b'', max_length=10)),
                ('sex', models.CharField(default=b'', max_length=10)),
                ('address', models.CharField(default=b'', max_length=50)),
                ('phone', models.CharField(default=b'', max_length=20)),
                ('sign', models.CharField(default=b'', max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
