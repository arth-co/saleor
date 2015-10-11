# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20151004_0243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AddField(
            model_name='vendor',
            name='default_warehouse',
            field=models.ForeignKey(null=True, verbose_name='Default Warehouse', related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='userprofile.Address', blank=True),
        ),
    ]
