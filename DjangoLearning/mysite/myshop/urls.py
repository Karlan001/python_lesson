from django.urls import path, include
from .views import myshop, product_list, order_list, create_products

app_name = 'myshop'
urlpatterns = [
    path('', myshop, name='myshop'),
    path('products/', product_list, name='product_list'),
    path('products/create/', create_products, name='product_create'),
    path('orders/', order_list, name='order_list'),
]
