from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponse
from .models import Name
from tablib import Dataset
import csv,io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


def index(request):
   html = "<H1>Students</H1><HR>"
   return render(request,'Student/index2.html')
    
def list(request):
    storage = messages.get_messages(request)
    name_list = Name.objects.all()
    context = {
        'name_list': name_list,
        'messages': storage,
    }
    return render(request,'Student/student_list_template.html',context)

@permission_required('admin.can_add_log_entry')
def student_upload(request):
    storage = messages.get_messages(request)
    if request.method == "GET":
        return render(request, 'Student/import.html')
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'That is not a csv file')
        return redirect('student_upload')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar='|'):
        _, created = Name.objects.update_or_create(
            firstName= column[4],
            middleName = column[5],
            lastName = column[3],
            studentId = column[2],
            year = column[6],
            email = column[1],
            
            
        )
    return redirect('list')
        
    
    
    