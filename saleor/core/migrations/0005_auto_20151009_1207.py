# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151009_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryslot',
            name='length',
        ),
        migrations.RemoveField(
            model_name='deliveryslot',
            name='timing',
        ),
        migrations.AddField(
            model_name='deliveryslot',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='deliveryslot',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
