# Generated by Django 4.0.6 on 2022-07-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0045_remove_products_category_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='tea_shapes',
            field=models.CharField(blank=True, choices=[('Рассыпной', 'Рассыпной'), ('Комковой', 'Комковой'), ('Гранулированный', 'Гранулированный'), ('Прессованный', 'Прессованный'), ('Экстрагированный', 'Экстрагированный'), ('Связанный', 'Связанный')], max_length=255, null=True, verbose_name='Форма чая'),
        ),
        migrations.AlterField(
            model_name='products',
            name='weight_of_product',
            field=models.IntegerField(blank=True, null=True, verbose_name='Вес продукта в граммах'),
        ),
    ]
