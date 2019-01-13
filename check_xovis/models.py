from django.db import models
from django.utils import timezone

# Create your models here.

class Xovis(models.Model):
    ip = models.CharField(max_length=15)
    serial = models.CharField(max_length=23)
    name = models.CharField(max_length=150)
    used = models.BooleanField(default=True)
    group = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)

class Check_xovis(models.Model):
    ip = models.ForeignKey(Xovis, on_delete=models.CASCADE)
    time = models.DateTimeField('time to check')
    result = models.BooleanField()
