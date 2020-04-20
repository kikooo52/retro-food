from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = 'foods', 'price', 'quantity',
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'address', 'paid', 'get_total_cost', 'created_at')
    list_filter = ['paid', 'created_at', 'updated', 'name']
    readonly_fields = ('get_total_cost', 'created_at', 'updated', )
    date_hierarchy = 'created_at'
    search_fields = ('name', )

    inlines = [OrderItemInline]    