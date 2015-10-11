# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('order', '0005_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_days',
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_days',
            field=models.ManyToManyField(to='core.Weekday'),
        ),
    ]
