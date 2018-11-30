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
    file=open("Event_Statistics\dataFiles\Alphabet_Soup_Evaluation.csv",'r')
    data=file.read().split("\n")
    context = {
        'ESList': ESList,
        'data':data,
    }
    
    
    
    
    return render(request,'Event_Statistics/index2.html',context)