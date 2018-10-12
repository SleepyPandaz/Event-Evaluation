from django.urls import path
from . import views
from Home.views import HomeView

urlpatterns = [
    #path('', views.home, name='Home'),
    path('', HomeView.as_view(), name='Home'),  
]