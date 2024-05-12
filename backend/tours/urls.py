from django.urls import path
from .api import tour_list, tour_detail


urlpatterns = [
    path('', tour_list, name='api_tour_list'),
    path('<slug:slug>/', tour_detail , name='api_tour_detail')
]

