import ast
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from ..news.models import News
from .models import OrderFormPlugin
from .forms import OrderForm


@plugin_pool.register_plugin
class OrdersPluginPublisher(CMSPluginBase):
    model = OrderFormPlugin
    module = _('Orders')
    name = _('Latest Orders')
    render_template = 'orders/latest_orders.html'
    
    def render(self, context, instance, placeholder):
        request = context['request']
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                self.render_template = 'orders/complete.html'
        else:
            form = OrderForm()
        

        context.update({
            'instance': instance,
            'form': form,
        })
        ids = request.COOKIES.get('ordersId')
        if ids:
            dd = ast.literal_eval(ids)
            selected_food = News.objects.filter(id__in=dd)
            ddss = dict((i, dd.count(i.id)) for i in set(selected_food))
            context.update({
                'foods': ddss.items()
            })
        return context

