from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from ..foods.models import Food
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object 
    food = get_object_or_404(Food, id=product_id) 
    form = CartAddProductForm(request.POST)
    response_data = {}
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(food=food, quantity=cd['quantity'], update_quantity=cd['update'])
        if request.is_ajax():
            response_data = {
                'quantity': cd['quantity'],
                'product_id': product_id,
                'status': '200',
            }
            response_data['quantity'] = cd['quantity']
            response_data['product_id'] = product_id
            response_data['food_name'] = food.title
            return JsonResponse({'result':response_data}, status=200, safe=False)
    elif request.is_ajax():
        return JsonResponse({'error': form.errors}, status=400, safe=False)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Food, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
