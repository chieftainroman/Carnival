# Generated by Django 4.0.6 on 2022-10-26 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, max_length=160, null=True, unique=True, verbose_name='(Это поле создасться автоматически.Ее заполнять не нужно!)')),
                ('first_in_the_topic', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(default='Object', max_length=255)),
                ('offer_title', models.CharField(blank=True, max_length=255, null=True)),
                ('offer_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('offer_image', models.FileField(null=True, upload_to='offer_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название продукта')),
                ('product_price', models.IntegerField(blank=True, null=True, verbose_name='Цена продукта')),
                ('product_description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание товара')),
                ('product_image', models.FileField(blank=True, null=True, upload_to='product_images/', verbose_name='Основное изображение товара(Обложка)')),
                ('discount_percent', models.IntegerField(null=True, verbose_name='Скидка')),
                ('slug', models.SlugField(blank=True, max_length=160, null=True, unique=True, verbose_name='Ссылка продукта')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Это один из лучших товаров?')),
                ('is_exclusive', models.BooleanField(default=False, verbose_name='Это один из эксклюзивных товаров?')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('available', models.CharField(choices=[('В наличии', 'В наличии'), ('Нет в наличии', 'Нет в наличии')], max_length=255, null=True, verbose_name='Товар в наличии?')),
                ('type_of_product', models.CharField(blank=True, choices=[('Чай в пакетиках', 'Чай в пакетиках'), ('Чай листовый', 'Чай листовый'), ('Кофе растворимый', 'Кофе растворимый'), ('Кофе в зернах', 'Кофе в зернах')], max_length=255, null=True, verbose_name='Тип товара')),
                ('kind_of_tea', models.CharField(blank=True, choices=[('Черный', 'Черный'), ('Зеленый', 'Зеленый'), ('Белый', 'Белый'), ('Желтый', 'Желтый'), ('Улун', 'Улун'), ('Пуэр', 'Пуэр')], max_length=255, null=True, verbose_name='Вид чая')),
                ('sort_of_tea', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сорт чая')),
                ('number_of_suchets', models.IntegerField(blank=True, null=True, verbose_name='Количество пакетиков внутри')),
                ('tea_shapes', models.CharField(blank=True, choices=[('Рассыпной', 'Рассыпной'), ('Комковой', 'Комковой'), ('Гранулированный', 'Гранулированный'), ('Прессованный', 'Прессованный'), ('Экстрагированный', 'Экстрагированный'), ('Связанный', 'Связанный')], max_length=255, null=True, verbose_name='Форма чая')),
                ('tea_leaf_size', models.CharField(blank=True, choices=[('Крупный', 'Крупный'), ('Средний', 'Средний'), ('Мелкий', 'Мелкий'), ('Прессованный', 'Прессованный')], max_length=255, null=True, verbose_name='Размер чайного листа')),
                ('weight_of_product', models.IntegerField(blank=True, null=True, verbose_name='Вес продукта в граммах')),
                ('composition_of_coffee', models.CharField(blank=True, max_length=255, null=True, verbose_name='Состав кофе')),
                ('coffe_roasting', models.CharField(blank=True, choices=[('Слабообжаренный кофе', 'Слабообжаренный кофе'), ('Среднеобжаренный кофе', 'Среднеобжаренный кофе'), ('Сильнообжаренный кофе', 'Сильнообжаренный кофе'), ('Высшая степень обжарки кофе', 'Высшая степень обжарки кофе')], max_length=255, null=True, verbose_name='Степень обжарки зерен')),
                ('taste_intensity', models.CharField(blank=True, choices=[('Крепкий', 'Крепкий'), ('Средний', 'Средний'), ('Мягкий', 'Мягкий')], max_length=255, null=True, verbose_name='Интенсивность вкуса')),
                ('arabica_content', models.IntegerField(blank=True, null=True, verbose_name='Содержание арабики в %')),
                ('producting_technology', models.CharField(blank=True, max_length=255, null=True, verbose_name='Технология производства')),
                ('category', models.ManyToManyField(blank=True, to='pages.category', verbose_name='Категория товара')),
            ],
        ),
        migrations.CreateModel(
            name='SaleOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_red_title', models.CharField(blank=True, max_length=255, null=True)),
                ('sale_title', models.CharField(blank=True, max_length=255, null=True)),
                ('sale_sale_words', models.CharField(blank=True, max_length=255, null=True)),
                ('sale_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('sale_image', models.FileField(null=True, upload_to='sale_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_name', models.CharField(max_length=255)),
                ('slider_sale', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_tittle', models.CharField(blank=True, max_length=255, null=True)),
                ('slider_image', models.FileField(blank=True, null=True, upload_to='slider_images/')),
                ('slider_slug', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeaDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_of_tea', models.CharField(max_length=255, null=True)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.products')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='product_images/', verbose_name='Дополнительные снимки продукта')),
                ('place', models.IntegerField(null=True, verbose_name='Какая фотка по очереди?')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.products')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pages.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='pages.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.products', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
