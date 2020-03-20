from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

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
        else:
            form = OrderForm()
        context.update({
            'instance': instance,
            'form': form,
        })
        return context
