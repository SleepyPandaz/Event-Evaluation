from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.

class Event_Statistics(models.Model):
    eventName = models.CharField(max_length=200 )
    pub_date = models.DateTimeField('Date published')
    def __str__(self):
        return '%s' % (self.eventName)
        