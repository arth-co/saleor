# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20151004_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='location',
            field=models.ForeignKey(null=True, to='userprofile.Address', related_name='+', verbose_name='location'),
        ),
    ]
