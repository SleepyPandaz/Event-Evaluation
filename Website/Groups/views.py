from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
import datetime
from django.shortcuts import HttpResponse
from .models import Student,Events
# Create your views here

def index(request):
  html = "<H1>Groups</H1><HR>"
  #template = loader.get_template('Events/index.html')
  #template = loader.get_template('Events/general_template.html')
  return render(request,'Groups/group.html')
  #return render(request,'Events/general_template.html')

def list(request):
    student_name = Student.objects.all()
    event_name = Events.objects.all()
    context= {
        'student_name' : student_name,
        'event_name': event_name
        } 
    return render(request,'Groups/group.html',context)