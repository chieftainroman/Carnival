# Generated by Django 4.0.6 on 2022-07-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_products_weight_of_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='kind_of_tea',
            field=models.CharField(blank=True, choices=[('Черный', 'Черный'), ('Зеленый', 'Зеленый'), ('Белый', 'Белый'), ('Желтый', 'Желтый'), ('Улун', 'Улун'), ('Пуэр', 'Пуэр')], max_length=255, null=True, verbose_name='Вид чая'),
        ),
        migrations.AlterField(
            model_name='products',
            name='number_of_suchets',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество пакетиков внутри'),
        ),
        migrations.AlterField(
            model_name='products',
            name='sort_of_tea',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Сорт чая'),
        ),
        migrations.AlterField(
            model_name='products',
            name='tea_leaf_size',
            field=models.CharField(blank=True, choices=[('Крупный', 'Крупный'), ('Средний', 'Средний'), ('Мелкий', 'Мелкий'), ('Прессованный', 'Прессованный')], max_length=255, null=True, verbose_name='Размер чайного листа'),
        ),
        migrations.AlterField(
            model_name='products',
            name='tea_shapes',
            field=models.CharField(blank=True, choices=[('Рассыпной', 'Рассыпной'), ('Комковой', 'Комковой'), ('Гранулированный', 'Гранулированный'), ('Прессованный', 'Прессованный'), ('Экстрагированный', 'Экстрагированный'), ('Связанный', 'Связанный')], max_length=255, null=True, verbose_name='Вид чая'),
        ),
        migrations.AlterField(
            model_name='products',
            name='type_of_tea',
            field=models.CharField(blank=True, choices=[('Чай в пакетиках', 'Чай в пакетиках'), ('Чай листовый', 'Чай листовый')], max_length=255, null=True, verbose_name='Тип чая'),
        ),
        migrations.AlterField(
            model_name='products',
            name='weight_of_product',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
