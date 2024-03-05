from django.contrib import admin
from carpartsapi.models.product_model import Product
from carpartsapi.models.cart_model import Cart
from carpartsapi.models.order_model import Order

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
