from django import forms
from .models import Contact,Order
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from . models import Order,OrderItem
class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')  

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким username уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует")
        return email

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Ваш Username'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Ваш Email'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Повторите пароль'
        })


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'user_email', 'address', 'postal_code', 'city']
