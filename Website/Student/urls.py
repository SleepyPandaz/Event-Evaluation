from django.urls import path
from . import views

urlpatterns = [
    path('Index/', views.index, name= 'index'),
    path('', views.list, name = 'list'),
    path('upload-csv/',views.student_upload, name= 'student_upload'),
]
