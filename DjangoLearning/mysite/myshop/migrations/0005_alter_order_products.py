# Generated by Django 5.1.2 on 2024-10-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='order', to='myshop.product'),
        ),
    ]