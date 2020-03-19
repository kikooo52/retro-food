from django.db import models
from django.utils.translation import ugettext_lazy as _



class Order(models.Model):
    name = models.CharField(_('Order'), max_length=200)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')