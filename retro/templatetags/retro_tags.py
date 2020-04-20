from django import template
from django.db.models import Count

from ..contrib.foods.models import DailyFood, CategoryFood

register = template.Library()


@register.inclusion_tag('daily_foods.html')
def get_daily_foods(category_list=None):
    return { 'category_list' : CategoryFood.objects.all() }
