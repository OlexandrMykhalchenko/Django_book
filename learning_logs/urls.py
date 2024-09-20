"""Определяет схемы URL для Learning_logs"""

from django.urls import path
from . import views

app_name = 'Learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
]
