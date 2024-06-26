# Generated by Django 4.0.6 on 2022-07-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_products_tea_shapes_alter_products_type_of_tea'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='tea_leaf_size',
            field=models.CharField(choices=[('Крупный', 'Крупный'), ('Средний', 'Средний'), ('Мелкий', 'Мелкий'), ('Прессованный', 'Прессованный')], max_length=255, null=True, verbose_name='Размер чайного листа'),
        ),
        migrations.AlterField(
            model_name='products',
            name='tea_shapes',
            field=models.CharField(choices=[('Рассыпной', 'Рассыпной'), ('Комковой', 'Комковой'), ('Гранулированный', 'Гранулированный'), ('Прессованный', 'Прессованный'), ('Экстрагированный', 'Экстрагированный'), ('Связанный', 'Связанный')], max_length=255, null=True, verbose_name='Вид чая'),
        ),
    ]
