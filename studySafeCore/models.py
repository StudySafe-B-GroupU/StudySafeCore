from datetime import datetime
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Venues(models.Model):
    venueCode = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    type = models.CharField(max_length=2)
    capacity = models.SmallIntegerField()
    def __str__(self):
        return self.venueCode

class HKUMembers(models.Model):
    hku_id = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.hku_id

class Records(models.Model):
    hku_id = models.ForeignKey(HKUMembers, on_delete=models.CASCADE)
    venueCode = models.ForeignKey(Venues, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)

class TaskForceMembers(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.username

class DeviceUsers(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    def __str__(self):
        return self.username
