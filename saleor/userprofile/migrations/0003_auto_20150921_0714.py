# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20150907_0602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999' and is ", regex='^\\+?1?\\d{5,5}$')], default='1234567890', max_length=10, unique=True),
        ),
    ]
