from django.urls import path
from .models import Event
from . import views

urlpatterns = [
    path('Index/', views.index, name='index'),
    path('', views.list, name='list'),
    path('deletion2', views.objectDelete, name='delete_object')
]