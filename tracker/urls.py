from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('habits/add/', views.add_habit, name='add_habit'),
    path('habits/log/', views.log_habit, name='log_habit'),
]
