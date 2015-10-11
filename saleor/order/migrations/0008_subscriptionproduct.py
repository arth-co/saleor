# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151006_1416'),
        ('product', '0010_auto_20151004_0840'),
        ('order', '0007_auto_20151006_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('quantity', models.IntegerField(verbose_name='quantity', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('days', models.ManyToManyField(to='core.Weekday')),
                ('product', models.ForeignKey(verbose_name='product', related_name='subscriptions', blank=True, to='product.Product', null=True)),
                ('subscription', models.ForeignKey(verbose_name='subscription', related_name='products', blank=True, to='order.Subscription', null=True)),
            ],
        ),
    ]
