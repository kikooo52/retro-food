from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.models.pluginmodel import CMSPlugin

class Category(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=200)


# Create your models here.
class News(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    description = models.TextField(_('Description'))
    text = models.TextField(_('Text'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='news', null=True)
    tags = models.ManyToManyField(Tag, related_name='news')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='news', null=True)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-created_at',)


class LatestNewPluginModel(CMSPlugin):
    number_of_news = models.IntegerField(_('Number of News'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='latest_news_plugin', null=True)
