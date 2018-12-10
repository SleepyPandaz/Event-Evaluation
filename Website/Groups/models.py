from django.db import models
import datetime
from unittest.util import _MAX_LENGTH
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=400)
    major = models.CharField(max_length=200)
    year = models.IntegerField()
   # race_Ethnicity = models.CharField(max_length=800)
    #international= models.CharField(max_length=100)
   # campus = models.CharField(max_length=300)
    def __str__(self):
        return '%s' % (self.name)
class Events(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField("Date of Event")
    def __str__(self):
        return '%s' % (self.name)
