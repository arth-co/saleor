# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20151004_0704'),
        ('product', '0008_product_vendors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_subscribable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vendors',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='is_subscribable',
            field=models.BooleanField(default=False, verbose_name='Is Subscribable'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='vendors',
            field=models.ManyToManyField(to='userprofile.Vendor'),
        ),
    ]
