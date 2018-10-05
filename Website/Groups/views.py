from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
import datetime
from django.shortcuts import HttpResponse
from .models import Student,Events
# Create your views here

#class GroupsPageView(TemplateView):
   # template_name = "group.html"
   # def view(self,request, **kwargs):
       # return render(request,'group.html',context=None)

    #for x in range(0,10):
#    def group(request):
  #      return HttpResponse("Hello, world. You're at the polls X2 index.")

#def groups(request):
   # return render(request, 'Groups/group.html', {})


#def sort(gender:String,age:Numbers,major:String):
   # student = gender,age,major
   # return student
   
   
def index(request):
  html = "<H1>Groups</H1><HR>"
  #template = loader.get_template('Events/index.html')
  #template = loader.get_template('Events/general_template.html')
  return render(request,'Groups/group.html')
  #return render(request,'Events/general_template.html')
  
