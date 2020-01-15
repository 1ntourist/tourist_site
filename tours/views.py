from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *
from .forms import *


# class TestTemplateView(TemplateView):
#     template_name = 'test_index.html'


class ArticleListView(LoginRequiredMixin, ListView):
    model = Tour
    template_name = 'tour_list.html'
    login_url = 'login'
    paginate_by = 5
    context_object_name = 'tours'


class TourDetailView(DetailView):
    model = Tour
    template_name = 'tour_detail.html'
    context_object_name = 'tour'
