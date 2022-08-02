from unicodedata import category
from django.db import models
from django.db.models.fields import FloatField
from django.forms import IntegerField
from tinymce import models as tinymce_models
#from django.template.defaultfilters import slugify
from django.urls import reverse
from django.dispatch import receiver
from django.db.models import signals
from django.db.models.signals import pre_save
from django.utils.text import slugify
import string  # for string constants
import random  # for generating random strings
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название категории")
    slug = models.SlugField(
        max_length=160, verbose_name="(Это поле создасться автоматически.Ее заполнять не нужно!)", null=True,unique=True,blank = True)
    first_in_the_topic = models.BooleanField(null=True,blank= True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        title = self.title
        # allow_unicode=True for support utf-8 languages
        self.slug = self.generate_slug()
        super(Category, self).save(*args, **kwargs)
        
    def generate_slug(self, save_to_obj=False, add_random_suffix=True):
        """
        Generates and returns slug for this obj.
        If `save_to_obj` is True, then saves to current obj.
        Warning: setting `save_to_obj` to True
              when called from `.save()` method
              can lead to recursion error!

        `add_random_suffix ` is to make sure that slug field has unique value.
        """

        # We rely on django's slugify function here. But if
        # it is not sufficient for you needs, you can implement
        # you own way of generating slugs.
        generated_slug = slugify(self.title)

        # Generate random suffix here.
        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            generated_slug += '-%s' % random_suffix

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])
        
        return generated_slug

    

PRODUCT_TYPE_CHOICES = (
    ('Чай в пакетиках','Чай в пакетиках'),
    ('Чай листовый','Чай листовый'),
    ('Кофе растворимый','Кофе растворимый'),
    ('Кофе в зернах','Кофе в зернах'),
    
)

TEA_SHAPES_CHOICES = (
    ('Рассыпной','Рассыпной'),
    ('Комковой','Комковой'),
    ('Гранулированный','Гранулированный'),
    ('Прессованный','Прессованный'),
    ('Экстрагированный','Экстрагированный'),
    ('Связанный','Связанный'),

)

TEA_LEAF_SIZE = (
    ('Крупный','Крупный'),
    ('Средний','Средний'),
    ('Мелкий','Мелкий'),
    ('Прессованный','Прессованный'),
)

COFFEE_ROASTING = (
    ('Слабообжаренный кофе','Слабообжаренный кофе'),
    ('Среднеобжаренный кофе','Среднеобжаренный кофе'),
    ('Сильнообжаренный кофе','Сильнообжаренный кофе'),
    ('Высшая степень обжарки кофе','Высшая степень обжарки кофе'),
)

TASTE_INTENSITY = (
    ('Крепкий','Крепкий'),
    ('Средний','Средний'),
    ('Мягкий','Мягкий'),

)

KIND_OF_TEA = (
    ('Черный','Черный'),
    ('Зеленый','Зеленый'),
    ('Белый','Белый'),
    ('Желтый','Желтый'),
    ('Улун','Улун'),
    ('Пуэр','Пуэр'),
    
)

AVAILABLE_CHOICES = (
    ('В наличии','В наличии'),
    ('Нет в наличии','Нет в наличии'), 
)
class Products(models.Model):
    product_name = models.CharField(max_length=255, null=True, blank=True,verbose_name="Название продукта")
    product_price = models.IntegerField(null=True, blank=True,verbose_name="Цена продукта")
    product_description = tinymce_models.HTMLField(null=True, blank=True,verbose_name="Описание товара")
    product_image = models.FileField(upload_to="product_images/", null=True,verbose_name="Основное изображение товара(Обложка)",blank=True)
    discount_percent = models.IntegerField(null=True,verbose_name="Скидка")
    slug = models.SlugField(
        max_length=160, verbose_name="Ссылка продукта", null=True,unique=True,blank = True)
    is_featured = models.BooleanField(verbose_name="Это один из лучших товаров?",default=False)
    is_exclusive= models.BooleanField(verbose_name="Это один из эксклюзивных товаров?",default=False)

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created Date", null=True)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Updated Date")
    category = models.ManyToManyField(
        Category, verbose_name="Категория товара", blank=True)
    available = models.CharField(max_length=255,choices=AVAILABLE_CHOICES,null=True,verbose_name="Товар в наличии?")
    type_of_product= models.CharField(max_length=255,choices=PRODUCT_TYPE_CHOICES ,null=True,blank=True,verbose_name="Тип товара") 

    #чай
    kind_of_tea = models.CharField(max_length=255,choices=KIND_OF_TEA ,null=True,blank=True,verbose_name="Вид чая")
      
    #чай в пакетиках
    sort_of_tea = models.CharField(max_length=255,null=True,blank=True,verbose_name="Сорт чая")
    number_of_suchets = models.IntegerField(null=True,blank=True, verbose_name="Количество пакетиков внутри")
    
    #рассыпной чай
    tea_shapes = models.CharField(max_length=255, choices=TEA_SHAPES_CHOICES,null=True, blank=True,verbose_name="Форма чая")
    tea_leaf_size = models.CharField(max_length=255,choices = TEA_LEAF_SIZE,null=True,blank=True, verbose_name="Размер чайного листа")
    weight_of_product = models.IntegerField(null=True,blank=True,verbose_name="Вес продукта в граммах")
    
    #кофе
    composition_of_coffee = models.CharField(max_length=255,null=True,blank=True,verbose_name="Состав кофе")
    coffe_roasting = models.CharField(max_length=255,choices=COFFEE_ROASTING,null=True,blank=True,verbose_name="Степень обжарки зерен")
    taste_intensity = models.CharField(max_length=255,choices=TASTE_INTENSITY,null=True,blank=True,verbose_name="Интенсивность вкуса")
    arabica_content = models.IntegerField(null=True,blank=True,verbose_name="Содержание арабики в %")
    
    producting_technology = models.CharField(max_length=255,null=True,blank=True,verbose_name="Технология производства")
    def __str__(self):
        return self.product_name
    
    def save(self, *args, **kwargs):
        product_name = self.product_name
        # allow_unicode=True for support utf-8 languages
        self.slug = self.generate_slug()
        super(Products, self).save(*args, **kwargs)
        
    def generate_slug(self, save_to_obj=False, add_random_suffix=True):

        # We rely on django's slugify function here. But if
        # it is not sufficient for you needs, you can implement
        # you own way of generating slugs.
        generated_slug = slugify(self.product_name)

        # Generate random suffix here.
        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            generated_slug += '-%s' % random_suffix

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])
        
        return generated_slug
    





class TeaDetail(models.Model):
    post = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    kind_of_tea = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.post.product_name


class ProductsImage(models.Model):
    post = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='product_images/',verbose_name='Дополнительные снимки продукта')
    place = models.IntegerField(null=True,verbose_name='Какая фотка по очереди?')

    def __str__(self):
        return self.post.product_name


class Slider(models.Model):
    slider_name = models.CharField(max_length=255)
    slider_sale = models.CharField(max_length=255, null=True, blank=True)
    slider_tittle = models.CharField(max_length=255, null=True, blank=True)
    slider_image = models.FileField(
        upload_to="slider_images/", null=True, blank=True)
    slider_slug = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.slider_name


class Offers(models.Model):
    offer_name = models.CharField(max_length=255, default="Object")
    offer_title = models.CharField(max_length=255, null=True, blank=True)
    offer_slug = models.CharField(max_length=255, null=True, blank=True)
    offer_image = models.FileField(upload_to="offer_images/", null=True)

    def __str__(self):
        return self.offer_name


class SaleOffers(models.Model):
    sale_red_title = models.CharField(max_length=255, null=True, blank=True)
    sale_title = models.CharField(max_length=255, null=True, blank=True)
    sale_sale_words = models.CharField(max_length=255, null=True, blank=True)
    sale_slug = models.CharField(max_length=255, null=True, blank=True)
    sale_image = models.FileField(upload_to="sale_images/", null=True)

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email