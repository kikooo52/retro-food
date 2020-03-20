from django.contrib import admin
from .models import Order


@admin.register(Order)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    list_filter = ('name', 'phone', 'email',)
    date_hierarchy = 'created_at'
    search_fields = ('name', )