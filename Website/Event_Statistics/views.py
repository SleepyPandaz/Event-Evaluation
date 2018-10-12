from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Event_Statistics

def index(request):
  html = "<H1>Event_Statistics</H1><HR>"
  return render(request,'Event_Statistics/index.html')
  
def list(request):
    latest_event_list = Event_Statistics.objects.all()
    context = {
        'latest_event_list': latest_event_list,
    }
    return render(request,'Event_Statistics/index2.html',context)