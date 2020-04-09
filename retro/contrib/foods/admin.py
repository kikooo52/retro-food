from django.contrib import admin
from .models import CategoryFood, Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'updated_at', 'category_food', 'text')
    list_filter = ('title', 'created_at', 'updated_at', 'category_food')
    date_hierarchy = 'created_at'
    search_fields = ('title', )

@admin.register(CategoryFood)
class CategoryFoodAdmin(admin.ModelAdmin):
    pass
