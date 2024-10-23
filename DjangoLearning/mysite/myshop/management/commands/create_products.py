from django.core.management import BaseCommand

from myshop.models import Product


class Command(BaseCommand):
    """
    Creates products in DB
    """

    def handle(self, *args, **options):
        self.stdout.write("Create products")
        products_name = [
            'Laptop',
            'Smartphone',
            'Desktop',
        ]
        for product_name in products_name:
            product, created = Product.objects.get_or_create(product_name=product_name)
            self.stdout.write(f'Created product {product.product_name}')

        self.stdout.write(self.style.SUCCESS("Created done"))