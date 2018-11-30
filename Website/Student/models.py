from django.db import models
from unittest.util import _MAX_LENGTH
from django.urls import reverse,reverse_lazy 

class Name(models.Model):
    firstName = models.CharField(max_length=30)
    middleName= models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    studentId = models.IntegerField()
    year = models.CharField(max_length=15)
    numEvents = models.IntegerField(default=0)
    numSurveys = models.IntegerField(default=0)
    def __str__(self):
        return '%s' % (self.firstName)
    
    def get_absolute_url(self):
        #return reverse('Student:objectDelete', kwargs={'post_id': self.id})
        return ""