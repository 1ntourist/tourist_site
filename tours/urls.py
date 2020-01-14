from django.urls import path
from .views import *


urlpatterns = [
    path('', ArticleListView.as_view(), name='test'),
    path('detail/<int:pk>/', TourDetailView.as_view(), name='detail'),

]