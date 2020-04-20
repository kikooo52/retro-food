from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ..cart.forms import CartAddProductForm

from .models import Food


class FoodsListView(ListView):
    model = Food

    def get_context_data(self, **kwargs):
        cart_product_form = CartAddProductForm()
        context = super().get_context_data(**kwargs)                     
        context["cart_product_form"] = cart_product_form
        return context


class FoodsDetailView(DetailView):
    model = Food

    def get_context_data(self, **kwargs):
        cart_product_form = CartAddProductForm()
        context = super().get_context_data(**kwargs)                     
        context["cart_product_form"] = cart_product_form
        return context
