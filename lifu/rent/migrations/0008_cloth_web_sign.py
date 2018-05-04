# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_auto_20180502_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='web_sign',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
