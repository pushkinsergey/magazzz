from rest_framework import serializers
from django.contrib.auth.models import User
from products.models import Currency
from products.models import Brand
from products.models import Vendor
from products.models import Сategory
from products.models import SubСategory
from products.models import Unit
from products.models import Сountry
from products.models import Products
from products.models import Properties
from products.models import PropertiesProducts
from products.models import Orders
from products.models import OrderDetails
from products.forms import ProductSearch
from products.forms import Add2Order


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'short_currency_name', 'currency_name')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'brand_name', 'img_url')


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'vendor_name')


class СategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Сategory
        fields = ('id', 'category_name')


class SubСategorySerializer(serializers.ModelSerializer):
    category = СategorySerializer()

    class Meta:
        model = SubСategory
        fields = ('id', 'sub_category_name', 'category')


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'unit_name')


class СountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Сountry
        fields = ('id', 'country_name')


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ('id', 'properties_name', 'category')


class PropertiesProductsSerializer(serializers.ModelSerializer):
    properties = PropertiesSerializer()
    class Meta:
        model = PropertiesProducts
        fields = ('id', 'product', 'properties', 'properties_value')


class ProductsSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    vendor = VendorSerializer()
    currency = CurrencySerializer()
    country_of_origin = СountrySerializer()
    unit = UnitSerializer()
    sub_category = SubСategorySerializer()

    properties = PropertiesProductsSerializer(many=True, read_only=True)


    class Meta:
        model = Products
        fields = (
            'id',
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
            'sub_category',
            'properties'
        )
