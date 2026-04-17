from django.urls import path
from . import views

urlpatterns = [
    path('', views.deal_list, name='deal_list'),
    path('add/', views.deal_create, name='deal_create'),
    path('view/<int:pk>/', views.deal_detail, name='deal_detail'),
    path('edit/<int:pk>/', views.deal_edit, name='deal_edit'),
    path('delete/<int:pk>/', views.deal_delete, name='deal_delete'),
    path('pipeline/', views.deal_pipeline, name='deal_pipeline'),
    path('update-stage/', views.update_deal_stage, name='update_deal_stage'),
]