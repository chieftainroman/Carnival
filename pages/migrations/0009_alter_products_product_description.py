# Generated by Django 4.0.6 on 2022-07-09 13:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
