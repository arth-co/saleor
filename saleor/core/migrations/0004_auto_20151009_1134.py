# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_deliveryslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryslot',
            name='length',
            field=models.DurationField(editable=False),
        ),
        migrations.AlterField(
            model_name='deliveryslot',
            name='timing',
            field=models.TimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='weekday',
            name='iso_number',
            field=models.PositiveSmallIntegerField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weekday',
            name='name',
            field=models.CharField(max_length=3, editable=False),
        ),
        migrations.AlterField(
            model_name='weekday',
            name='verbose_name',
            field=models.CharField(max_length='20', editable=False),
        ),
    ]
