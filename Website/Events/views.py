from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Event

def index(request):
  html = "<H1>Events</H1><HR>"
  #template = loader.get_template('Events/index.html')
  #template = loader.get_template('Events/general_template.html')
  return render(request,'Events/index.html')
  #return render(request,'Events/general_template.html')
  
def list(request):
    latest_event_list = Event.objects.all()
    context = {
        'latest_event_list': latest_event_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request,'Events/event_list_template.html',context)