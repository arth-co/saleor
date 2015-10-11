# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekday',
            name='iso_number',
            field=models.PositiveSmallIntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='weekday',
            name='name',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='weekday',
            name='verbose_name',
            field=models.CharField(max_length='20'),
        ),
    ]
