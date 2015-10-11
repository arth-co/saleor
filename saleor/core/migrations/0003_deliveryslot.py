# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151006_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliverySlot',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('timing', models.TimeField()),
                ('length', models.DurationField()),
            ],
        ),
    ]
