# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0006_auto_20151006_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_days',
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='subscriptions', blank=True, verbose_name='user'),
        ),
    ]
