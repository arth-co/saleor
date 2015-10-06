from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (ProductImage, Category, FixedProductDiscount, Product, ProductVariant)
from .forms import ImageInline


class ImageAdminInline(admin.StackedInline):
    model = ProductImage
    formset = ImageInline


class ProductCollectionAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(FixedProductDiscount)
admin.site.register(Product)
admin.site.register(ProductVariant)