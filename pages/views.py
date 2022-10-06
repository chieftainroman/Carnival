from .models import OrderItem, Cart
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from urllib import parse
from .forms import OrderCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import hashlib
from itertools import product
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from . models import Offers, Slider, Products, SaleOffers, ProductsImage, Category
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django import template
from django.contrib import messages
import decimal
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail as sm
from django.db.models import Q
register = template.Library()


def index(request):
    slider = Slider.objects.all()
    offers = Offers.objects.all()
    saleOffers = SaleOffers.objects.all()
    products = Products.objects.all()
    data = Products.objects.filter(is_featured=True).order_by('-id')
    exclusive = Products.objects.filter(is_exclusive=True).order_by('-id')
    categories = Category.objects.all()
    first_topic_categories = Category.objects.filter(first_in_the_topic=True)
    context = {
        "slider": slider,
        "offers": offers,
        "saleOffers": saleOffers,
        "products": products,
        "data": data,
        "exclusive": exclusive,
        "categories": categories,
        "first_topic_categories": first_topic_categories,

    }

    return render(request, "index.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, 'authentication/signup.html', {'form': form})


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form, 'title': 'log in'})


def logout_view(request):
    logout(request)
    return redirect("home")


def search(request):
    categories = Category.objects.all()
    search_post = request.GET.get('search')
    if search_post:
        products = Products.objects.filter(Q(product_name__icontains=search_post) & Q(
            product_description__icontains=search_post))
    else:
        # If not searched, return default posts
        products = Products.objects.all()
    context = {
        "products": products,
        "categories": categories,
    }
    return render(request, "products.html", context)


def products(request):
    products = Products.objects.all()
    first_topic_categories = Category.objects.filter(first_in_the_topic=True)
    categories = Category.objects.all()
    context = {
        "products": products,
        "first_topic_categories": first_topic_categories,
        "categories": categories,
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


@login_required(login_url="https://www.carnival-shop.info/login/")
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Products, id=product_id)

    # Check whether the Product is alread in Cart or Not
    item_already_in_cart = Cart.objects.filter(product=product_id, user=user)
    if item_already_in_cart:
        cp = get_object_or_404(Cart, product=product_id, user=user)
        cp.quantity += 1
        cp.save()
    else:
        Cart(user=user, product=product).save()

    return redirect('cart')


@login_required(login_url="/login/")
def cart(request):
    user = request.user
    cart_products = Cart.objects.filter(user=user)
    # Display Total on Cart Page
    amount = decimal.Decimal(0)
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in Cart.objects.all() if p.user == user]
    if cp:
        for p in cp:
            if p.product.discount_percent == None or p.product.discount_percent == 0:
                temp_amount = (p.quantity * p.product.product_price)
                amount += temp_amount
            else:
                temp_amount = round((p.quantity * p.product.product_price -
                                    (p.product.product_price * p.product.discount_percent/100)))
                amount += temp_amount
    else:
        title = "Cart is empty"
    context = {
        'cart_products': cart_products,
        'amount': amount,
        'total_amount': amount,
    }
    return render(request, 'cart/index.html', context)


@login_required(login_url="/login/")
def remove_cart(request, cart_id):
    if request.method == 'GET':
        c = get_object_or_404(Cart, id=cart_id)
        c.delete()
        messages.success(request, "Product removed from Cart.")
    return redirect('cart')


@login_required(login_url="/login/")
def plus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        cp.quantity += 1
        cp.save()
    return redirect('cart')


@login_required(login_url="/login/")
def minus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        # Remove the Product if the quantity is already 1
        if cp.quantity == 1:
            cp.delete()
        else:
            cp.quantity -= 1
            cp.save()
    return redirect('cart')


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Products.objects.filter(category=category)
    first_topic_categories = Category.objects.filter(first_in_the_topic=True)
    categories = Category.objects.filter()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        "first_topic_categories": first_topic_categories,

    }
    return render(request, 'category_products.html', context)


def terms(request):
    return render(request, "terms/index.html")


def order_create(request):
    cp = Cart.objects.filter(user=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for p in cp:
                sellprice = p.product.product_price - \
                    (p.product.product_price * p.product.discount_percent / 100)
                OrderItem.objects.create(order=order,
                                         product=p.product,
                                         price=sellprice,
                                         quantity=p.quantity,
                                         user=request.user,
                                         )
            # очистка корзины
            cp.delete()
            return render(request, 'checkout.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'checkout.html', {'cart': cp, 'form': form})


def calculate_signature(*args) -> str:
    """Create signature MD5.
    """
    return hashlib.md5(':'.join(str(arg) for arg in args).encode()).hexdigest()


def generate_payment_link(
    request,
    merchant_login="carnivalshopru",
    merchant_password_1='10520126Roman',
    cost=10.0,  # Cost of goods, RU
    number=12,  # Invoice number
    description="salam",  # Description of the purchase
    is_test=1,
    robokassa_payment_url='https://auth.robokassa.ru/Merchant/Index.aspx',
) -> str:
    signature = calculate_signature(
        merchant_login,
        cost,
        number,
        merchant_password_1
    )

    data = {
        'MerchantLogin': merchant_login,
        'OutSum': cost,
        'InvId': number,
        'Description': description,
        'SignatureValue': signature,
        'IsTest': is_test
    }
    return f'{robokassa_payment_url}?{parse.urlencode(data)}'

print(generate_payment_link())