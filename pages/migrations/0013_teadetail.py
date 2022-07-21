# Generated by Django 4.0.6 on 2022-07-16 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_remove_type_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeaDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_of_tea', models.CharField(max_length=255, null=True)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.products')),
            ],
        ),
    ]
