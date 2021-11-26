from django.db import models

from django.conf import settings

class Queue(models.Model):
    arrival_time1 = models.CharField(max_length=50)
    arrival_time2 = models.CharField(max_length=50)
    arrival_time3 = models.CharField(max_length=50)
    arrival_time4 = models.CharField(max_length=50)
    average_time = models.CharField(max_length=50)
    waiting_time = models.CharField(max_length=50)
    hospital    =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 