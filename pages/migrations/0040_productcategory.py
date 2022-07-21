# Generated by Django 4.0.6 on 2022-07-20 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0039_remove_products_brand_delete_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.category', verbose_name='Категория товара')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.products')),
            ],
        ),
    ]
