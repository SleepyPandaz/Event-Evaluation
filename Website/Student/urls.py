from django.urls import path
from . import views

urlpatterns = [
    path('Index/', views.index, name= 'index'),
    path('', views.list, name = 'list')
]
