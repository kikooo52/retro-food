from django.views.generic import ListView
from django.https import JsonResponse

from .models import Order


class Stuff(ListView):
    model = Order

    def get(self, request, item_id):
        import ipdb; ipdb.set_trace()
        stuff_item = Order.objects.get(id=item_id)
        return JsonResponse({'item': stuff_item})

    def post(self, request, item_id):
        import ipdb; ipdb.set_trace()
        if request.is_ajax():
            new_stuff = Order(item_id=item_id)
            new_stuff.save()
            return JsonResponse({'message': 'OK'})
        else:
            return JsonResponse({'message': 'Failed'})
