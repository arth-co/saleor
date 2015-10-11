# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import saleor.product.models.fields
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20150825_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedproductdiscount',
            name='discount',
            field=django_prices.models.PriceField(verbose_name='discount value', currency='INR', decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=django_prices.models.PriceField(verbose_name='price', currency='INR', decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=saleor.product.models.fields.WeightField(verbose_name='weight', unit='KG', decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='price_override',
            field=django_prices.models.PriceField(verbose_name='price override', null=True, currency='INR', max_digits=12, blank=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='weight_override',
            field=saleor.product.models.fields.WeightField(verbose_name='weight override', null=True, max_digits=6, unit='KG', blank=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cost_price',
            field=django_prices.models.PriceField(verbose_name='cost price', null=True, currency='INR', max_digits=12, blank=True, decimal_places=2),
        ),
    ]
