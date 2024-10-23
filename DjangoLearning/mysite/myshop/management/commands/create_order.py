from django.core.management import BaseCommand
from django.contrib.auth.models import User

from myshop.models import Order, Product


class Command(BaseCommand):
    """
    Creates order in DB
    """

    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            delivery_address='ul Pushkina dom Kolotushkina',
            promocode='qwerty123',
            user=user,
        )
        self.stdout.write(f"Created order {order} done")
