from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Order
        fields = ('name', 'phone', 'email',)
