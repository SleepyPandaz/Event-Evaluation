from django.urls import path
from .models import Event_Statistics
from . import views

urlpatterns = [
    path('Index/', views.index, name='index'),
    path('', views.list, name='list'),
]