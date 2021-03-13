from django.contrib import admin
from products.models import Currency
from products.models import Brand
from products.models import Vendor
from products.models import Сategory
from products.models import Unit
from products.models import Сountry
from products.models import Products
from products.models import Properties
from products.models import PropertiesProducts
from products.models import Orders
from products.models import OrderDetails


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('short_currency_name', 'currency_name')
    list_display_link = ('short_currency_name', 'currency_name')
    search_fields = ('short_currency_name', 'currency_name')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'img_url')
    list_display_link = ('brand_name', 'img_url')
    search_fields = ('brand_name',)


class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name',)
    list_display_link = ('vendor_name',)
    search_fields = ('vendor_name',)


class СategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_display_link = ('category_name',)
    search_fields = ('category_name',)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_name',)
    list_display_link = ('unit_name',)
    search_fields = ('unit_name',)


class СountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)
    list_display_link = ('country_name',)
    search_fields = ('country_name',)


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'artno',
        'name',
        'price',
        'currency',
        'img_url',
        'quantity',
        'description',
        'tizer',
        'rating',
        'brand',
        'vendor',
        'country_of_origin',
        'unit',
        'category',)
    list_display_link = (
        'artno',
        'name',
        'price',
        'currency',
        'img_url',
        'quantity',
        'description',
        'tizer',
        'rating',
        'brand',
        'vendor',
        'country_of_origin',
        'unit',
        'category',)
    search_fields = ('artno', 'name',)


class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('properties_name', 'category')
    list_display_link = ('properties_name', 'category')
    search_fields = ('properties_name', 'category')


class PropertiesProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'properties', 'properties_value')
    list_display_link = ('product', 'properties', 'properties_value')
    search_fields = ('product', 'properties', 'properties_value')


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'status',
        'delivery',
        'paid',
        'summa',
        'description')
    list_display_link = (
        'date',
        'status',
        'delivery',
        'paid',
        'summa',
        'description')
    search_fields = ('date',)


class PropertiesProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'properties', 'properties_value')
    list_display_link = ('product', 'properties', 'properties_value')
    search_fields = ('product', 'properties', 'properties_value')


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'amount')
    list_display_link = ('order', 'product', 'amount')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Сategory, СategoryAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Сountry, СountryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Properties, PropertiesAdmin)
admin.site.register(PropertiesProducts, PropertiesProductsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
