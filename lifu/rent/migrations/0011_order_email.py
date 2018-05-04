# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0010_auto_20180503_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
