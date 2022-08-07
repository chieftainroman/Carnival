from django.urls import path, include
from . import views
from django.conf import settings
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

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
