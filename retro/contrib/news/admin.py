from django.contrib import admin
from .models import Category, News, Tag


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'created_at', 'updated_at', 'category')
    list_filter = ('author', 'created_at', 'updated_at', 'tags', 'category')
    date_hierarchy = 'created_at'
    search_fields = ('title', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
