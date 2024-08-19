from django.urls import path
from .views import get_data, get_info

urlpatterns = [
    path('data/', get_data),
    path('info/', get_info),
]
