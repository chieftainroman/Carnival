# Generated by Django 4.0.6 on 2022-07-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_alter_products_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=160, null=True, unique=True, verbose_name='Ссылка продукта'),
        ),
    ]
