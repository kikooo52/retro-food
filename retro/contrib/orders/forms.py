from django import forms
from captcha.fields import CaptchaField

from .models import Order


class OrderForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': '0XXXXXXXXX'}))
    declaration_site = forms.BooleanField(label=u'Съгласен съм с <a href="/bg/orders/terms_site/" target="_blank">Условията на сайта</a>', required=True)
    declaration_gdpr = forms.BooleanField(label=u'Съгласен съм с <a href="/bg/orders/terms_gdpr/" target="_blank">Политиката за лични данни</a>', required=True)

    captcha = CaptchaField(label=u'Не съм робот')

    class Meta:
        model = Order
        fields = ('name', 'phone', 'address', 'email', 'declaration_site', 'declaration_gdpr')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
