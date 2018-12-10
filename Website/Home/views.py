from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from Student.models import Name
from Student.views import studentList

# Create your views here.
def home(request):
    return HttpResponse("It works")

class HomeView(TemplateView):
    template_name = 'Home.html'
    name_list = Name.objects.all()

   

        