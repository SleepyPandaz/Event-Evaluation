from django.db import models
from unittest.util import _MAX_LENGTH

    
class Name(models.Model):   
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.first_Name)
   
    
