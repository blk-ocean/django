# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloceanapp', '0003_lounge_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lounge',
            name='location',
            field=models.CharField(default=b'null', max_length=256),
        ),
    ]
