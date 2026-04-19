from django.urls import path
from .views import lead_list, lead_create, lead_detail, lead_edit, lead_delete

urlpatterns = [
    path('', lead_list, name='lead_list'),
    path('add/', lead_create, name='lead_create'),
    path('view/<int:pk>/', lead_detail, name='lead_detail'),
    path('edit/<int:pk>/', lead_edit, name='lead_edit'),
    path('delete/<int:pk>/', lead_delete, name='lead_delete'),
]