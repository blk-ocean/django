# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloceanapp', '0002_lounge_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='lounge',
            name='location',
            field=models.CharField(default=b'null', unique=True, max_length=256),
            preserve_default=True,
        ),
    ]
