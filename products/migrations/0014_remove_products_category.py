# Generated by Django 3.1 on 2021-03-13 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20210314_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
    ]
