from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (Category, Product, ProductImage)

admin.site.register(Category, MPTTModelAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
