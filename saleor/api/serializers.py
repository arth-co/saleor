__author__ = 'hkalra'

from rest_framework import serializers
from django_prices.models import PriceField
from saleor.product.models.base import Product, Category, ProductVariant


from rest_framework import permissions

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ProductSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='product-highlight', format='html')
    categories = CategorySerializer(many=True)
    price = serializers.DecimalField(source='price.gross',decimal_places=2,max_digits=10)

    class Meta:
        model = Product
        fields = ('name','description','categories','price','weight')
        depth = 1


class ProductVariantSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')
    price_override= serializers.DecimalField(source='price_override.gross',label='price',decimal_places=2,max_digits=10)
    weight_override = serializers.DecimalField(label='weight',decimal_places=2,max_digits=10)
    class Meta:
        model = ProductVariant
        fields = ['sku','product','name','price_override','weight_override']