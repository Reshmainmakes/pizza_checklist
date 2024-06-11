# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('terminal/', views.terminal, name='terminal'),
    path('driver/', views.driver, name='driver'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('save_task/', views.save_task, name='save_task'),

]
