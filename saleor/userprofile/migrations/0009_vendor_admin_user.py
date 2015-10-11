# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20151004_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='admin_user',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='Default User'),
        ),
    ]
