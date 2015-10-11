# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0008_subscriptionproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
        migrations.RenameField(
            model_name='subscriptionproduct',
            old_name='days',
            new_name='delivery_days',
        ),
        migrations.RemoveField(
            model_name='subscriptionproduct',
            name='subscription',
        ),
        migrations.AddField(
            model_name='subscriptionproduct',
            name='user',
            field=models.ForeignKey(null=True, related_name='products', verbose_name='subscription', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
