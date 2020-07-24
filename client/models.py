from django.db import models

# Create your models here.
class Device(models.Model):
    device_id = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    data_label = models.CharField(max_length=20)
    data_value = models.IntegerField(default=0)
