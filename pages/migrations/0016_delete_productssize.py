# Generated by Django 4.0.6 on 2022-07-16 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_remove_products_color_remove_products_product_type_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductsSize',
        ),
    ]
