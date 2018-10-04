from django.db import models
import datetime
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    year = models.IntegerField()
    
class Events(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField("Date of Event")
    