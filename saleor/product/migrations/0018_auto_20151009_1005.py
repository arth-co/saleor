# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_product_days_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='days_available',
            field=models.ManyToManyField(to='core.Weekday', default=1),
        ),
    ]
