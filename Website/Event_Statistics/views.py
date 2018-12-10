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
    ESList = Event_Statistics.objects.all()
    data = request.session['data_set']
    year=[]
    campus=[]
    data=data.split("\n")
 
    for lines in data:
        line=lines.split(',');
        print(len(line));
        if(len(line)>=35):
            campus.append(line[33]);
            if(line[34]!=""):
                year.append(line[34].strip('\r'));
            else:
                year.append("no year");
        
    context = {
        'ESList': ESList,
        'data':data,
        'year':year,
        'campus':campus
    }
    
    
    
    
    return render(request,'Event_Statistics/index2.html',context)