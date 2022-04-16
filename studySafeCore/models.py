from tkinter import CASCADE
from django.db import models

# Create your models here.
class Venues(models.Model):
    venueCode = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    type = models.CharField(max_length=2)
    capacity = models.IntegerField()

class Members(models.Model):
    hku_id = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

class Records(models.Model):
    hku_id = models.ForeignKey(Members, on_delete=models.CASCADE)
    venueCode = models.ForeignKey(Venues, on_delete=models.CASCADE)
    entry_time = models.TimeField(auto_now=False, auto_now_add=False)
    exit_time = models.TimeField(auto_now=False, auto_now_add=False)