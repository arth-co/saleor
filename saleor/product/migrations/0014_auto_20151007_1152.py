# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20151007_1112'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='stock',
            name='location',
        ),
    ]
