from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
import datetime
from django.shortcuts import HttpResponse
from .models import Name

def index(request):
   html = "<H1>Students</H1><HR>"
   return render(request,'Student/index.html')
    
def list(request):
    name_list = Name.objects.all()
    context = {
        'name_list': name_list,
    }
    return render(request,'Student/index.html',context)

