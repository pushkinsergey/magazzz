from django.shortcuts import render
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
from django.db.models import Q


def index(request):
    info = ''

    return render(request, 'test.html', {'test': info})


def catalog(request):
    info = ''
    if request.method == 'POST':
        form = ProductSearch(request.POST or None)
        # int(form.price_min)
        if form.is_valid():
            #info = form.cleaned_data.get("brand")['Brand']
            product = form.cleaned_data.get("product")
            if form.cleaned_data.get("price_min"):
                price_min = int(form.cleaned_data.get("price_min"))
            else:
                price_min = 0
            if form.cleaned_data.get("price_max"):
                price_max = int(form.cleaned_data.get("price_max"))
            else:
                price_max = 999999999
            brand = form.cleaned_data.get("brand")
            if brand:
                pass
            else:
                brand = Brand.objects.all()
            vendor = form.cleaned_data.get("vendor")
            if vendor:
                pass
            else:
                vendor = Vendor.objects.all()

        products = Products.objects.all().filter(
            Q(name__icontains=product) or
            Q(description__icontains=product) or
            Q(artno__icontains=product)).filter(
            price__gte=price_min).filter(
            price__lte=price_max).filter(
            brand__in=brand).filter(
            vendor__in=vendor)
    else:
        form = ProductSearch()
        products = Products.objects.all()
    return render(request, 'catalog.html', {'form': form, 'products': products, 'test': info})


def product(request, idprotucts: int):
    form = Add2Order()
    product = Products.objects.get(id=idprotucts)
    propertiesproducts = PropertiesProducts.objects.filter(product__id=idprotucts)
    return render(request, 'cardproduct.html', {
        'form': form,
        'product': product,
        'properties': propertiesproducts
        })
