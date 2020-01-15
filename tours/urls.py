from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('', ArticleListView.as_view(), name='tour_list'),
    path('detail/<int:pk>/', TourDetailView.as_view(), name='detail'),

]