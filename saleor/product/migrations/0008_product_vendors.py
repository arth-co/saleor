# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20151004_0243'),
        ('product', '0007_product_is_subscribable'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendors',
            field=models.ManyToManyField(to='userprofile.Vendor'),
        ),
    ]
