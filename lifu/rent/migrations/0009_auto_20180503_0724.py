# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0008_cloth_web_sign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cloth',
            old_name='price',
            new_name='cloth_price',
        ),
        migrations.RenameField(
            model_name='cloth',
            old_name='web_sign',
            new_name='rent_price',
        ),
        migrations.AddField(
            model_name='cloth',
            name='type',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
