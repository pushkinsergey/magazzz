# Generated by Django 3.1 on 2021-03-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210313_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]
