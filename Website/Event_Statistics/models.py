from django.db import models
from unittest.util import _MAX_LENGTH
from django.template.defaultfilters import default

# Create your models here.

class Event_Statistics(models.Model):
    eventName = models.CharField(max_length=200 )
    numberOfParticipants= models.PositiveIntegerField(default=1)
    numberOfJonnies=models.PositiveIntegerField(default=1)
    numberOfBennies=models.PositiveIntegerField(default=1)
    numberOfFreshman=models.PositiveIntegerField(default=1)
    numberOfSophomore=models.PositiveIntegerField(default=1)
    numberOfJunior=models.PositiveIntegerField(default=1)
    numberOfSenior=models.PositiveIntegerField(default=1)
    numberOfOutOfState=models.PositiveIntegerField(default=1)
    numberOfLocal=models.PositiveIntegerField(default=1)
    
   
  
        
        
        
        
        
        
        
    def __str__(self):
        
        return '%s' % (self.eventName)
        
    