from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class Order(models.Model):
    name = models.CharField(u'Име и Фамилия', max_length=150)
    phone = models.CharField(u'Телефон', max_length=150)
    email = models.EmailField(u'E-mail', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderFormPlugin(CMSPlugin):
    title = models.CharField(_('Title'), max_length=100)
    success_message = models.CharField(_('Success Message after form is submitted'), max_length=300, default='')

    def __str__(self):
        return self.title
