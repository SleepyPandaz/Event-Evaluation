from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.

class GroupsPageView(TemplateView):
    template_name = "group.html"
   # def view(self,request, **kwargs):
       # return render(request,'group.html',context=None)

    #for x in range(0,10):
    def group(request):
        return HttpResponse("Hello, world. You're at the polls X2 index.")

#def groups(request):
   # return render(request, 'Groups/group.html', {})


#def sort(gender:String,age:Numbers,major:String):
   # student = gender,age,major
   # return student