# Generated by Django 4.0.6 on 2022-07-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_products_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
