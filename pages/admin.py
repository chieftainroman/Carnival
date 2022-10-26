from django.contrib import admin
from . models import Products, Slider, Offers, SaleOffers, ProductsImage, Category , TeaDetail, Cart, Order,OrderItem

admin.site.register(Slider)
admin.site.register(Offers)
admin.site.register(SaleOffers)
admin.site.register(Category)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    list_per_page = 20
    search_fields = ('user', 'product')


class PostImageAdmin(admin.StackedInline):
    model = ProductsImage


@admin.register(Products)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    fieldsets = (
        (None, {
            'fields': ('product_name','product_price','product_description',
                       'product_image','weight_of_product','discount_percent','slug','is_featured','is_exclusive','category','available','type_of_product')
        }),
        ('Если добавляемый вами продукт является чаем,то заполните эти поля', {
            'classes': (),
            'fields': ('kind_of_tea',),
        }),
        ('Если добавляемый вами чай является рассыпным чаем,то добавьте также эти поля', {
            'classes': (),
            'fields': ('tea_shapes','tea_leaf_size',),
        }),
        ('Если же добавляемый вами чай является чаем в пакетиках,то заполните эти данные', {
            'classes': (),
            'fields': ('sort_of_tea','number_of_suchets',),
        }),
        ('Если добавляемый вами продукт является кофе,то заполните эти данные', {
            'classes': (),
            'fields': ('composition_of_coffee','coffe_roasting','taste_intensity','arabica_content','producting_technology',),
        }),
    )

@admin.register(ProductsImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cart, CartAdmin)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
