from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class Event(models.Model):
    eventName = models.CharField(max_length=200 )
    eventDate = models.CharField(max_length=200 )
    eventCategory = models.CharField(max_length=30)
    eventYears = models.CharField(max_length=30)
    eventParticpants = models.CharField(max_length=200)
    eventResponseRate = models.CharField(max_length = 200)
    def __str__(self):
        return '%s' % (self.eventName)
        