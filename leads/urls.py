from django.urls import path
from .views import lead_list, lead_create, lead_edit

urlpatterns = [
    path('', lead_list, name='lead_list'),
    path('add/', lead_create, name='lead_create'),
    path('edit/<int:pk>/', lead_edit, name='lead_edit'),
]