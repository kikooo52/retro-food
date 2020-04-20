from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^terms_site/$', views.terms_site, name='terms_site'),
    url(r'^terms_gdpr/$', views.terms_gdpr, name='terms_gdpr')
]