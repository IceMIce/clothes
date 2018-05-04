# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0011_order_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='count',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='count',
            field=models.IntegerField(max_length=20),
        ),
    ]
