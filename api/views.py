import random
from datetime import datetime
from datetime import timedelta
from django.http import Http404
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
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
from api.serializers import ProductsSerializer
from api.serializers import BrandSerializer
from api.serializers import VendorSerializer
from api.serializers import CurrencySerializer

class ProductList(APIView):

    def get(self, request, format=None):

        products = Products.objects.filter(id__in=PropertiesProducts.objects.filter(properties_value).distinct())[:10]
        #products = Products.objects.all()[:50]
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

class Product(APIView):

    def get(self, request, idprotuct, format=None):

        products = Products.objects.filter(pk=idprotuct)
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)        