from django.urls import path
from .models import Event
from . import views

urlpatterns = [
    path('Index/', views.index, name='index'),
    path('', views.eventList, name='eventList'),
    path('add_events/', views.addEvent, name='addEvent'),
    path('deletion2', views.objectDelete, name='delete_object')
]