# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151009_1207'),
        ('product', '0019_auto_20151009_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slots_available',
            field=models.ManyToManyField(default=0, to='core.DeliverySlot'),
        ),
    ]
