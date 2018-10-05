from django.contrib import admin

# Register your models here.
from .models import Student, Events

admin.site.register(Student)
admin.site.register(Events)