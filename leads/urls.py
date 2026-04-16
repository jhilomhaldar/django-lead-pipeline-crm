from django.urls import path
from .views import lead_list

urlpatterns = [
    path('', lead_list, name='lead_list'),
]