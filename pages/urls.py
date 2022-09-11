from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views 
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name = "home"),
    path("products/", views.products, name = "products"),
    path('product/<slug:slug>/', views.detail, name="product-detail"),
    path('products/category/<slug:slug>/', views.category_products, name="category-products"),
    path('search',views.search,name = "search"),
    path('payment_error',views.payment_error,name = "payment_error"),
    path('payment_success',views.payment_success,name = "payment_success"),
    path('payment_alerts',views.payment_alerts,name = "payment_alerts"),
    path('payment',views.balance,name = "balance"),
    path('cart/',views.cart,name = "cart"),
    path('add-to-cart/', views.add_to_cart, name="add-to-cart"),
    path('remove-cart/<int:cart_id>/', views.remove_cart, name="remove-cart"),
    path('plus-cart/<int:cart_id>/', views.plus_cart, name="plus-cart"),
    path('minus-cart/<int:cart_id>/', views.minus_cart, name="minus-cart"),
    path('signup',views.signup,name = "signup"),
    path('accounts/login',views.Login,name = "login"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  views.activate, name='activate'),
    
    #path("reset_password/", auth_views.PasswordResetView.as_view(),name="reset_password"),
    #path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    #path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"), 



    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
