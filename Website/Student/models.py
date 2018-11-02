from django.db import models
from unittest.util import _MAX_LENGTH

    
class Name(models.Model):   
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.firstName)
   
    
