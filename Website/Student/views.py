from django.template import loader
from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Name

def index(request):
    html = "<H1>Students</H1><HR>"
    return render(request,'Student/index.html')
    
        

def list(request):
    name_list = Name.objects.order_by('-firstName')[:5]
    template = loader.get_template('Student/index.html')
    context = {
        'name_list': name_list,
    }
    return render(request, 'Student/index.html', context)

