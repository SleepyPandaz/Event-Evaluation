from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.list, name='list'),
    #path('<varChar:eventName>/', views.view, name='view'),
]