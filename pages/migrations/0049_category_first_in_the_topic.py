# Generated by Django 4.0.6 on 2022-08-02 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0048_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='first_in_the_topic',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
