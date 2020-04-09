from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.models.pluginmodel import CMSPlugin

class CategoryFood(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category food')
        verbose_name_plural = _('Categories food')


# Create your models here.
class Food(models.Model):
    title = models.CharField(u'Заглавие', max_length=200)
    text = models.TextField(u'Текст')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    category_food = models.ForeignKey(CategoryFood, on_delete=models.SET_NULL, related_name='food', null=True)

    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Foods')
        ordering = ('-created_at',)


    def __str__(self):
        return self.title