from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from .models import Event

def index(request):
  html = "<H1>Events</H1><HR>"
  #template = loader.get_template('Events/index.html')
  #template = loader.get_template('Events/general_template.html')
  return render(request,'Events/index.html')
  #return render(request,'Events/general_template.html')
  
def eventList(request):
    latest_event_list = Event.objects.all()
    context = {
        'latest_event_list': latest_event_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request,'Events/event_list_template.html',context)

def objectDelete(request):
    post_id = request.GET['post_id']
    object = get_object_or_404(Event, pk=post_id)
    object.delete()
    return redirect('eventList')