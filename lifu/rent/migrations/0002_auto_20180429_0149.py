# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(default=b'', max_length=20)),
                ('name', models.CharField(default=b'', max_length=20)),
                ('password', models.CharField(default=b'', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(default=b'', max_length=20)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cloth',
        ),
        migrations.DeleteModel(
            name='Gener',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='code',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cusName',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cusNo',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='sign',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.CharField(default=b'', max_length=50, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='sex',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
