from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import News


class NewsListView(ListView):
    model = News


class NewsDetailView(DetailView):
    model = News
