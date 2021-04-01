from django.contrib import admin
from django.urls import path
from products.views import index
from products.views import catalog
from products.views import product
from api.views import ProductList
from api.views import Product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('catalog', catalog, name='catalog'),
    path('product/<int:idprotucts>/', product, name='product'),
    path('api/products/', ProductList.as_view()),
    path('api/products/<int:idprotuct>/', Product.as_view()),
]
