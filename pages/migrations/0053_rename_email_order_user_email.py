# Generated by Django 4.0.6 on 2022-09-29 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0052_rename_first_name_order_full_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='user_email',
        ),
    ]
