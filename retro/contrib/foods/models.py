from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from ..orders.utils import adminfield
from cms.models.pluginmodel import CMSPlugin

class CategoryFood(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Категирия'
        verbose_name_plural = u'Категории'


class Food(models.Model):
    title = models.CharField(u'Заглавие', max_length=200)
    text = models.TextField(u'Текст')
    price = models.DecimalField(u'Цена', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(u'Създадено на', auto_now_add=True)
    updated_at = models.DateTimeField(u'Променено на', auto_now=True)
    image = models.ImageField()
    category_food = models.ForeignKey(CategoryFood, on_delete=models.SET_NULL, related_name='food', null=True)

    class Meta:
        verbose_name = u'Храна'
        verbose_name_plural = u'Храни'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    @adminfield(u'Текст')
    def short_text(self):
        return self.text if len(self.text) < 30 else (self.text[:30] + ' ...')

class DailyFood(models.Model):
    title = models.CharField(u'Заглавие', max_length=200)
    price = models.DecimalField(u'Цена', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(u'Създадено на', auto_now_add=True)
    updated_at = models.DateTimeField(u'Променено на', auto_now=True)
    category_food = models.ForeignKey(CategoryFood, on_delete=models.SET_NULL, related_name='dailyfood', null=True)

    class Meta:
        verbose_name = u'Храна'
        verbose_name_plural = _('Обедно меню')
        ordering = ('-created_at',)


    def __str__(self):
        return self.title        