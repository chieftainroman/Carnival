from django import template

register = template.Library()

@register.simple_tag
def call_sellprice(product_price,discount_percent ):
    if discount_percent == None or discount_percent == 0:
        return product_price
    sellprice = product_price
    sellprice = product_price - (product_price * discount_percent /100)
    return sellprice