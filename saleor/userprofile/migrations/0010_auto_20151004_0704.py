# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_vendor_admin_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='admin_user',
            field=models.ForeignKey(null=True, related_name='+', blank=True, verbose_name='Admin User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Vendor Name'),
        ),
    ]
