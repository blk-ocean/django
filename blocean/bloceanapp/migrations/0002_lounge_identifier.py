# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloceanapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lounge',
            name='identifier',
            field=models.CharField(default=b'null', unique=True, max_length=256),
            preserve_default=True,
        ),
    ]
