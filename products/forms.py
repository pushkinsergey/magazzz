from django import forms

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


class ProductSearch(forms.Form):
    product = forms.CharField(required=False)
    price_min = forms.IntegerField(required=False, widget=forms.NumberInput)
    price_max = forms.IntegerField(required=False, widget=forms.NumberInput)
    brand = forms.ModelMultipleChoiceField(
        required=False, queryset=Brand.objects.all())
    vendor = forms.ModelMultipleChoiceField(
        required=False, queryset=Vendor.objects.all())


class Add2Order(forms.Form):
    amount = forms.IntegerField(label='Количество',
                                widget=forms.NumberInput)
