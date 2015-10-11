# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20151007_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available_on',
        ),
        migrations.AddField(
            model_name='product',
            name='lead_time',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='lead time'),
        ),
    ]
