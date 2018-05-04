# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0009_auto_20180503_0724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cusName',
            new_name='cus_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='order_time',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='daytime',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='telephone',
            new_name='rent_time',
        ),
    ]
