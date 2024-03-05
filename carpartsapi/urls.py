from django.urls import path
from carpartsapi.views.cart_view import CartListApiView, CartDetailApiView
from carpartsapi.views.order_view import OrderListApiView, OrderDetailApiView
from carpartsapi.views.product_view import ProductListApiView, ProductDetailApiView

urlpatterns = [
    path('product', ProductListApiView.as_view()),
    path('product/<str:product_code>/', ProductDetailApiView.as_view()),
    path('cart', CartListApiView.as_view()),
    path('cart/<int:cart_id>/', CartDetailApiView.as_view()),
    path('order', OrderListApiView.as_view()),
    path('order/<int:order_id>/', OrderDetailApiView.as_view()),
]
