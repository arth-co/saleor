# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151006_1416'),
        ('product', '0016_auto_20151007_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='days_available',
            field=models.ManyToManyField(default=[1, 2, 3, 4, 5, 6, 7], to='core.Weekday'),
        ),
    ]
