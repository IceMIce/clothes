# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_cloth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloth',
            name='color',
        ),
        migrations.RemoveField(
            model_name='cloth',
            name='size',
        ),
        migrations.AddField(
            model_name='cloth',
            name='picture',
            field=models.ImageField(default=b'picture/no-img.jpg', upload_to=b'picture/'),
        ),
    ]
