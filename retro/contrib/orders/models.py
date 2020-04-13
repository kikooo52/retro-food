from django.db import models
from django.utils.translation import ugettext_lazy as _
from .utils import adminfield

from cms.models.pluginmodel import CMSPlugin
from ..foods.models import Food

class Order(models.Model):
    name = models.CharField(u'Име и Фамилия', max_length=150)
    phone = models.CharField(u'Телефон', max_length=150)
    email = models.EmailField(u'E-mail', blank=True)
    address = models.EmailField(u'Адрес', max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)    

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    @adminfield(u'Сума')
    def get_total_cost(self):
        return '{} лв.'.format(sum(item.get_cost() for item in self.items.all()))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    foods = models.ForeignKey(Food, related_name='order_foods', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.foods.title)

    def get_cost(self):
        return self.price * self.quantity
