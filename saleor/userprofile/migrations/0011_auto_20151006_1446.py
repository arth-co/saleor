# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20151004_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=256, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=256, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=False, blank=True, max_length=254),
        ),
    ]
