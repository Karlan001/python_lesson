from django.contrib import admin
from .models import Product, Order
from django.http import HttpRequest
from django.db.models import QuerySet
from .admin_mixins import ExportAsCSVMixin



# Register your models here.

class ProductInLine(admin.StackedInline):
    model = Order.products.through


class OrderdInline(admin.TabularInline):
    model = Product.order.through


@admin.register(Order)
class Order_admin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
    ]
    list_display = 'delivery_address', 'promocode', 'created_at', 'name_verbose'

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    def name_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username

@admin.action(description='Archived products')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.action(description='Unarchived products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)
class Product_admin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv',

    ]
    inlines = [
        OrderdInline,
    ]
    list_display = 'id', 'product_name', 'product_description_short', 'price', 'discount', 'archived'
    list_display_links = 'id', 'product_name'
    ordering = 'id',
    search_fields = 'product_name', 'product_description', 'price'
    fieldsets = [
        (None, {'fields': ('product_name', 'product_description')}
         ),
        ('Price options', {'fields': ('price', 'discount'),
                           'classes': ('collapse',)
                           }
         ),
        ('Extra options', {
            'fields': ('archived',),
            'classes': ('collapse',),
            'description': 'Extra options. Field "archived" is for soft delete',
        })
    ]

    def product_description_short(self, obj: Product) -> str:
        if len(obj.product_description) > 50:
            return obj.product_description[:51] + '...'
        else:
            return obj.product_description

# admin.site.register(Product, Product_admin)
