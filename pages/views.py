from itertools import product
from django.shortcuts import render, redirect
from . models import Offers, Slider, Products, SaleOffers, ProductsImage, Category, Cart
from django.shortcuts import get_object_or_404
from . forms import ContactForm
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
import hashlib
from django.contrib.auth import login, authenticate  
from .forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

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
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('authentication/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  
    else:  
        form = SignupForm()  
    return render(request, 'authentication/signup.html', {'form': form})  

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect("login")
    else:  
        return HttpResponse('Activation link is invalid!')  

def Login(request):
    if request.method == 'POST':
      
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form':form, 'title':'log in'})

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

@login_required(login_url="https://www.carnival-shop.info/login/")
def cart(request):

    user = request.user
    cart_products = Cart.objects.filter(user=user)
    # Display Total on Cart Page
    amount = decimal.Decimal(0)
    shipping_amount = decimal.Decimal(10)
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in Cart.objects.all() if p.user==user]
    if cp:
        for p in cp:
            temp_amount = (p.quantity * p.product.product_price)
            amount += temp_amount

    context = {
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount,
    }
    return render(request, 'cart/index.html', context)


def remove_cart(request, cart_id):
    if request.method == 'GET':
        c = get_object_or_404(Cart, id=cart_id)
        c.delete()
        messages.success(request, "Product removed from Cart.")
    return redirect('cart')



def plus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        cp.quantity += 1
        cp.save()
    return redirect('cart')


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
