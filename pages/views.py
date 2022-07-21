from itertools import product
from django.shortcuts import render, redirect
from . models import Offers, Slider, Products, SaleOffers, ProductsImage, Category
from django.shortcuts import get_object_or_404
from . forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings


def index(request):
    slider = Slider.objects.all()
    offers = Offers.objects.all()
    saleOffers = SaleOffers.objects.all()
    products = Products.objects.all()
    data=Products.objects.filter(is_featured=True).order_by('-id')
    exclusive = Products.objects.filter(is_exclusive=True).order_by('-id')
    categories = Category.objects.all()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['romanmammadov872@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('products')
    context = {
        "slider": slider,
        "offers": offers,
        "saleOffers": saleOffers,
        "products": products,
        "form": form,
        "data":data,
        "exclusive":exclusive,
        "categories":categories,
    }

    return render(request, "index.html", context)


def products(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context = {
        "products": products,
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
    categories = Category.objects.filter()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'category_products.html', context)
