from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from .models import Event
from .forms import AddEventForm

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

#def addEvent(request):
    
    #return render(request,'Events/add_events.html')

def addEvent(request):
    if request.method == "GET":
        return render(request, 'Events/add_events.html')
    form = AddEventForm(request.POST)
    created = Event.objects.update_or_create(
            eventDate=  request.session['date_of_event'],
            eventName = request.session(event_name),
            eventCategory = request.session(event_category),
            eventYears = request.session(years_at_csbsju),
            eventParticipants = request.session(no_of_participants),
            eventResponseRate = request.session(response_rate),
        )


    return redirect('eventList')
    