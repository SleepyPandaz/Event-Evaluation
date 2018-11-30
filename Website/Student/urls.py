from django.urls import path
from . import views

urlpatterns = [
    path('Index/', views.index, name= 'index'),
    path('', views.studentList, name = 'studentList'),
    path('upload-csv/',views.student_upload, name= 'student_upload'),
    
    #path('^student/(?P<post_id>\d+)/$',views.objectDelete, name='delete_object'),
    path('deletion', views.objectDelete, name='delete_object')
]

