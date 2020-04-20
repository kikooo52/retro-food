from django.contrib import admin
from .models import CategoryFood, Food, DailyFood


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'updated_at', 'category_food', 'short_text')
    list_filter = ('title', 'created_at', 'updated_at', 'category_food')
    readonly_fields = ('short_text', 'created_at', 'updated_at', )
    date_hierarchy = 'created_at'
    search_fields = ('title', )


@admin.register(DailyFood)
class DailyFoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'updated_at')
    list_filter = ('title', 'created_at')
    readonly_fields = ('created_at', 'updated_at', )
    date_hierarchy = 'created_at'
    search_fields = ('title', )


@admin.register(CategoryFood)
class CategoryFoodAdmin(admin.ModelAdmin):
    pass
