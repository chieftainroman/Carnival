# Generated by Django 4.0.6 on 2022-07-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='discount_percent',
            field=models.IntegerField(null=True),
        ),
    ]
