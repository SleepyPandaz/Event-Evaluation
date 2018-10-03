from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls X2 index.")

#def groups(request):
   # return render(request, 'Groups/group.html', {})


#def sort(gender:String,age:Numbers,major:String):
   # student = gender,age,major
   # return student