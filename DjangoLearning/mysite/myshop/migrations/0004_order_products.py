# Generated by Django 5.1.2 on 2024-10-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', to='myshop.product'),
        ),
    ]
