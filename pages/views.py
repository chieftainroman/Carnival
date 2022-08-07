from itertools import product
from django.shortcuts import render, redirect
from . models import Offers, Slider, Products, SaleOffers, ProductsImage, Category
from django.shortcuts import get_object_or_404
from . forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django import template
from django.db.models import Q  
register = template.Library()
import hashlib
def index(request):
    slider = Slider.objects.all()
    offers = Offers.objects.all()
    saleOffers = SaleOffers.objects.all()
    products = Products.objects.all()
    data=Products.objects.filter(is_featured=True).order_by('-id')
    exclusive = Products.objects.filter(is_exclusive=True).order_by('-id')
    categories = Category.objects.all()
    first_topic_categories = Category.objects.filter(first_in_the_topic=True)
    context = {
        "slider": slider,
        "offers": offers,
        "saleOffers": saleOffers,
        "products": products,
        "data":data,
        "exclusive":exclusive,
        "categories":categories,
        "first_topic_categories":first_topic_categories,

    }

    return render(request, "index.html", context)

def search(request):
    categories = Category.objects.all()
    search_post = request.GET.get('search')
    if search_post:
        products = Products.objects.filter (Q(product_name__icontains=search_post) & Q(product_description__icontains=search_post) )
    else:
        # If not searched, return default posts
        products = Products.objects.all()
    context = {
            "products":products,
            "categories" : categories,
    }
    return render(request,"products.html",context)


def products(request):
    products = Products.objects.all()
    first_topic_categories = Category.objects.filter(first_in_the_topic=True)
    categories = Category.objects.all()
    context = {
        "products": products,
        "first_topic_categories":first_topic_categories,
        "categories":categories,
    }

    return render(request, "products.html", context)



def detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    photos = ProductsImage.objects.filter(post=product)
    #related_products = Products.objects.exclude(id=product.id).filter(is_active=True, category=product.category)
    context = {
        'product': product,
        'photos': photos,
        #  'related_products': related_products,

    }
    return render(request, 'detail.html', context)


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Products.objects.filter(category=category)
    first_topic_categories = Category.objects.filter(first_in_the_topic=True)
    categories = Category.objects.filter()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        "first_topic_categories":first_topic_categories,

    }
    return render(request, 'category_products.html', context)

def payment_alerts(request):
    return render(request, 'payment_alerts.html')

        
 
#При успешной оплате
def payment_success(request):
    return render(request, 'success_payment.html')
 
 
#При ошибке в оплате
def payment_error(request):
    return render(request, 'error_payment.html')

def balance(request):
    merchant_id = '20856'
    secret_word = ',?>GmGGS(?&UEBx'
    order_id = '154'
    order_amount = '10.11'
    currency = 'RUB'
    sign = hashlib.md5(f'{merchant_id}:{order_amount}:{secret_word}:{currency}:{order_id}'.encode('utf-8')).hexdigest()
 
    context = {
        'm': merchant_id,
        'oa': order_amount,
        'o': order_id,
        's': sign,
        'currency': currency
    }
 
    return render(request, 'balance.html', context)
