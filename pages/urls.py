from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name = "home"),
    path("products/", views.products, name = "products"),
    path('product/<slug:slug>/', views.detail, name="product-detail"),
    path('products/category/<slug:slug>/', views.category_products, name="category-products"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
