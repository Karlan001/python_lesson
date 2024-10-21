from django.urls import path, include
from .views import myshop, product_list

app_name = 'myshop'
urlpatterns = [
    path('', myshop, name='myshop'),
    path('products/', product_list, name='product_list'),
]