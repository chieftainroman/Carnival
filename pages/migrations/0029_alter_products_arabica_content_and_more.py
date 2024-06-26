# Generated by Django 4.0.6 on 2022-07-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_products_producting_technology_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='arabica_content',
            field=models.IntegerField(blank=True, null=True, verbose_name='Содержание арабики в %'),
        ),
        migrations.AlterField(
            model_name='products',
            name='composition_of_coffee',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Состав кофе'),
        ),
        migrations.AlterField(
            model_name='products',
            name='producting_technology',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Технология производства'),
        ),
    ]
