from django.urls import path, include
from . import views
from Home.views import HomeView
#from django.contrib.auth.views import L

urlpatterns = [
    #path('', views.home, name='Home'),
    path('', HomeView.as_view(), name='Home'), 
    #path('login/', login, {'template_name': 'Website/Home/login.html'}) 
    path('', include('django.contrib.auth.urls')),
    
]   