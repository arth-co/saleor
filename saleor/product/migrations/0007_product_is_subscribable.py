# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20150923_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_subscribable',
            field=models.BooleanField(default=False, verbose_name='is subscribable'),
        ),
    ]
