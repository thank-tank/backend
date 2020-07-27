from django.db import models

# Create your models here.

class Sensor(models.Model):
    sensor = models.CharField(max_length=200)
    data = models.FloatField()
