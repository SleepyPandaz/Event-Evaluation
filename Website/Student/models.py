from django.db import models
from unittest.util import _MAX_LENGTH


class Name(models.Model):
    firstName = models.CharField(max_length=30)
    middleName= models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    studentId = models.CharField(max_length=15)
    year = models.CharField(max_length=15)
    numEvents = models.CharField(max_length=3)
    numSurveys = models.CharField(max_length=3)

    @property
    def __str__(self):
        return '%s' % (self.firstName)
