from datetime import datetime
from tkinter import CASCADE
from django.db import models

# Create your models here.
class HKUMembers(models.Model):
    hku_id = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.hku_id

class Venues(models.Model):
    venueCode = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    type = models.CharField(max_length=2)
    capacity = models.SmallIntegerField()
    members = models.ManyToManyField(HKUMembers, through='Records')
    def __str__(self):
        return self.venueCode

class Records(models.Model):
    hku_id = models.ForeignKey(HKUMembers, on_delete=models.CASCADE, default = 1)
    venueCode = models.ForeignKey(Venues, on_delete=models.CASCADE)
    event = models.CharField(max_length=5, default="Entry")
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return f'{self.hku_id}'

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
