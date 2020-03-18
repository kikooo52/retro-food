from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import LatestNewPluginModel
from .models import News

@plugin_pool.register_plugin
class LatestNewsPluginPublisher(CMSPluginBase):
    model = LatestNewPluginModel
    module = _('News')
    name = _('Latest News Plugin')
    render_template = 'news/latest_news.html'
    
    def render(self, context, instance, placeholder):
        news = News.objects.filter(author=instance.author)[:instance.number_of_news]
        context.update({
            'news_list': news,
        })
        return super().render(context, instance, placeholder)
