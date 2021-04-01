from django.db import models
from django.conf import settings


class Currency(models.Model):
    short_currency_name = models.CharField(
        max_length=3, db_index=True, verbose_name='Сокращенно')
    currency_name = models.CharField(
        max_length=25, db_index=True, verbose_name='Валюта')

    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name_plural = 'Валюты'
        verbose_name = 'Валюта'
        ordering = ['currency_name']


class Brand(models.Model):
    brand_name = models.CharField(
        max_length=30, db_index=True, unique=True, verbose_name='Бренд')
    img_url = models.URLField(max_length=200, null=True, blank=True,)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name_plural = 'Бренды'
        verbose_name = 'Бренд'
        ordering = ['brand_name']


class Vendor(models.Model):
    vendor_name = models.CharField(
        max_length=90, db_index=True, verbose_name='Производитель')

    def __str__(self):
        return self.vendor_name

    class Meta:
        verbose_name_plural = 'Производители'
        verbose_name = 'Производитель'
        ordering = ['vendor_name']


class Сategory(models.Model):
    category_name = models.CharField(
        max_length=90, db_index=True, unique=True, verbose_name='Группы товара')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Группы товара'
        verbose_name = 'Группа товара'
        ordering = ['category_name']


class SubСategory(models.Model):
    sub_category_name = models.CharField(
        max_length=90, db_index=True, default='',
        null=True, blank=True, unique=True,
        verbose_name='Подгруппы товара')
    category = models.ForeignKey(
        'Сategory', on_delete=models.CASCADE, default=719,
        verbose_name='Группы товара')

    def __str__(self):
        return self.sub_category_name

    class Meta:
        verbose_name_plural = 'Подгруппы товара'
        verbose_name = 'Подгруппа товара'
        ordering = ['sub_category_name']


class Unit(models.Model):
    unit_name = models.CharField(
        max_length=15, db_index=True, verbose_name='Единица измерения')

    def __str__(self):
        return self.unit_name

    class Meta:
        verbose_name_plural = 'Единицы измерения'
        verbose_name = 'Единица измерения'
        ordering = ['unit_name']


class Сountry(models.Model):
    country_name = models.CharField(
        max_length=15, db_index=True, verbose_name='Страна производства')

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = 'Страны производства'
        verbose_name = 'Страна производства'
        ordering = ['country_name']


class Products(models.Model):
    artno = models.CharField(
        max_length=25, db_index=True, verbose_name='Артикул')
    name = models.CharField(max_length=200, db_index=True,
                            verbose_name='Наименование')
    price = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Цена')
    currency = models.ForeignKey(
        'Currency', on_delete=models.PROTECT, verbose_name='Валюта')
    img_url = models.URLField(max_length=200, null=True, blank=True,)
    quantity = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Количество складе')
    description = models.TextField(
        null=True, blank=True, verbose_name='Подробное описание')
    tizer = models.TextField(null=True, blank=True,
                             verbose_name='Краткое описание')
    rating = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Ретинг')
    brand = models.ForeignKey(
        'Brand', on_delete=models.PROTECT, verbose_name='Бренд')
    vendor = models.ForeignKey(
        'Vendor', on_delete=models.PROTECT, verbose_name='Производитель')
    country_of_origin = models.ForeignKey(
        'Сountry', on_delete=models.PROTECT,
        verbose_name='Страна производства')
    unit = models.ForeignKey(
        'Unit', on_delete=models.PROTECT, verbose_name='Единица измерения')
    sub_category = models.ForeignKey(
        'SubСategory', on_delete=models.PROTECT, verbose_name='Группы товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['name']


class Properties(models.Model):
    properties_name = models.CharField(
        max_length=25, db_index=True, verbose_name='Характеристика')
    category = models.ForeignKey(
        'Сategory', on_delete=models.PROTECT, verbose_name='Группы товара')

    def __str__(self):
        return self.properties_name

    class Meta:
        verbose_name_plural = 'Характеристики'
        verbose_name = 'Характеристика'
        ordering = ['properties_name']


class PropertiesProducts(models.Model):
    product = models.ForeignKey(
        'Products', on_delete=models.CASCADE, related_name='properties', verbose_name='Товар')
    properties = models.ForeignKey(
        'Properties', on_delete=models.CASCADE, verbose_name='Характеристика')
    properties_value = models.CharField(
        max_length=25, db_index=True, verbose_name='Значение характеристики')

    class Meta:
        verbose_name_plural = 'Характеристики товаров'
        verbose_name = 'Характеристика товара'


class Orders(models.Model):
    date = models.DateField(null=False, blank=False,
                            verbose_name='Дата заказа')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    status = models.SmallIntegerField(choices=(
        (1, 'Новый'), (2, 'В работе'), (3, 'Отменен'), (4, 'Завершен')),
        default=1)
    delivery = models.SmallIntegerField(
        choices=((1, 'Самовывоз'), (2, 'Доставка'),), default=1)
    paid = models.SmallIntegerField(
        choices=((1, 'Не оплачен'), (2, 'Оплачен'),), default=1)
    summa = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Сумма заказа')
    description = models.TextField(
        null=True, blank=True, verbose_name='Комментарий')


class OrderDetails(models.Model):
    order = models.ForeignKey(
        'Orders', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(
        'Products', on_delete=models.PROTECT, verbose_name='Товар')
    amount = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Количество')
