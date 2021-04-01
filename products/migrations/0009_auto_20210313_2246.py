# Generated by Django 3.1 on 2021-03-13 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210313_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubСategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(db_index=True, max_length=90, unique=True, verbose_name='Подгруппы товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.сategory', verbose_name='Группы товара')),
            ],
            options={
                'verbose_name': 'Подгруппа товара',
                'verbose_name_plural': 'Подгруппы товара',
                'ordering': ['sub_category_name'],
            },
        ),
        migrations.AddField(
            model_name='products',
            name='sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.subсategory', verbose_name='Группы товара'),
            preserve_default=False,
        ),
    ]