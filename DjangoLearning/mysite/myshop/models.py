from django.contrib.auth.models import User
from django.db import models, migrations


class Product(models.Model):
    class Meta:
        ordering = ['product_name', 'price']

    product_name = models.CharField(max_length=100)
    product_description = models.TextField(null=False, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    # @property
    # def product_description_short(self) -> str:
    #     if len(self.product_description) > 50:
    #         return self.product_description[:51] + '...'
    #     else:
    #         return self.product_description

    def __str__(self) -> str:
        return f'Product(id={self.id}, name={self.product_name!r})'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    delivery_address = models.TextField(null=False, blank=True)
    promocode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='order') #Создаем связь многие ко многим

