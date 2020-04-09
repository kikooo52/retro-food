from django.urls import path
from .views import FoodsDetailView, FoodsListView


urlpatterns = [
    path("", FoodsListView.as_view(), name="food-list"),
    path("<int:pk>", FoodsDetailView.as_view(), name="food-detail"),
]
