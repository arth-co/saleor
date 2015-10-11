# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20150921_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{5,5}$', message="Phone number must be entered in the format: '+999999999' and is ")], max_length=10, unique=True),
        ),
    ]
