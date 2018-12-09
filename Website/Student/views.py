from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponse
from .models import Name
from Events.models import Event
import csv,io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required



def index(request):
   html = "<H1>Students</H1><HR>"
   return render(request,'Student/index2.html')
    
def studentList(request):
    storage = messages.get_messages(request)
    name_list = Name.objects.all()
    context = {
        'name_list': name_list,
        'messages': storage,
    }
    return render(request,'Student/student_list_template.html',context)

@permission_required('admin.can_add_log_entry')
def student_upload(request):
    
    if request.method == "GET":
        return render(request, 'Student/import.html')
    
    csv_file = request.FILES['file']
    fileName = csv_file.name.replace('_',' ').replace('.csv','')
    'if statement'
    _, created = Event.objects.update_or_create(
        eventName = fileName,
        eventDate = '',
        eventCategory = '',
        eventYears = '',
        eventParticpants = '',
        eventResponseRate = '',
        )
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file'+'\n'+csv_file.name)
        return redirect('student_upload')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    request.session['data_set'] = data_set
    next(io_string)
    for column in csv.reader(io_string,delimiter=',',quotechar='|'):
        if (''.join(column) == ''):
            continue
        _, created = Name.objects.update_or_create(
            firstName= column[4].strip('"'),
            middleName = column[5].strip('"'),
            lastName = column[3].strip('"'),
            studentId = column[2].strip('"'),
            year = column[6].strip('"'),
            email = column[1].strip('"'),
            
            
        )
    return redirect('studentList')

def objectDelete(request):
    post_id = request.GET['post_id']
    object = get_object_or_404(Name, pk=post_id)
    object.delete()
    return redirect('studentList')