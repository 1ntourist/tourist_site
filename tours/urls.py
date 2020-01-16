from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('', ArticleListView.as_view(), name='tour_list'),
    # path('detail/<int:pk>/', TourDetailView.as_view(), name='detail'),
    path('category/', list_category, name='list_category'),
    path('category/<int:category__id>/', list_of_tours, name='list_tours'),
    path('category/<int:category>/<int:id>/', detail_of_tour, name='detail'),

]


