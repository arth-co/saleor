# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('iso_number', models.PositiveSmallIntegerField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=3, editable=False)),
                ('verbose_name', models.CharField(max_length='20', editable=False)),
            ],
        ),
    ]
