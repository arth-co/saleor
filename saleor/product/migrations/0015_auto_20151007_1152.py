# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0014_user_email'),
        ('product', '0014_auto_20151007_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='location',
            field=models.ForeignKey(related_name='+', null=True, to='userprofile.Address', verbose_name='location'),
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together=set([('variant', 'location')]),
        ),
    ]
